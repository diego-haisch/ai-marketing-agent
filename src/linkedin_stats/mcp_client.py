"""Cliente MCP mínimo sobre stdio (solo stdlib, sin agente).

Lanza el MCP server de LinkedIn como subproceso (`npx @isteam/linkedin-mcp`),
realiza el handshake del protocolo y permite invocar herramientas
(`tools/call`). El server es quien habla HTTPS con LinkedIn; este cliente
solo habla JSON-RPC con el server por stdin/stdout.
"""

from __future__ import annotations

import json
import queue
import subprocess
import threading


class MCPError(Exception):
    """Fallo de protocolo, de herramienta o de la API de LinkedIn."""


def _coerce_text(result: dict) -> str:
    """Extrae el texto de un resultado tools/call (o lo serializa)."""
    content = result.get("content", [])
    texts = [c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"]
    if texts:
        return "\n".join(texts)
    return json.dumps(result)


class MCPClient:
    def __init__(self, command: list[str], env: dict, timeout: int = 120) -> None:
        self.command = command
        self.env = env
        self.timeout = timeout
        self._proc: subprocess.Popen | None = None
        self._lines: queue.Queue[str] = queue.Queue()
        self._reader: threading.Thread | None = None
        self._next_id = 0

    def __enter__(self) -> "MCPClient":
        self._proc = subprocess.Popen(
            self.command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            bufsize=1,
            env=self.env,
        )
        self._reader = threading.Thread(target=self._drain, daemon=True)
        self._reader.start()
        init = self._request("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "linkedin-stats", "version": "0.1.0"},
        })
        if "error" in init:
            raise MCPError(f"Handshake MCP fallido: {init['error']}")
        self._notify("notifications/initialized")
        return self

    def __exit__(self, *exc) -> None:
        try:
            if self._proc and self._proc.stdin:
                self._proc.stdin.close()
        except BrokenPipeError:
            pass
        if self._proc:
            self._proc.kill()
            try:
                self._proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
        if self._reader:
            self._reader.join(timeout=10)

    def _drain(self) -> None:
        try:
            for line in self._proc.stdout:
                line = line.strip()
                if line:
                    self._lines.put(line)
        except Exception:  # noqa: BLE001 - el lector nunca debe tumbar el proceso
            pass

    def _next(self) -> int:
        self._next_id += 1
        return self._next_id

    def _send(self, payload: dict) -> None:
        try:
            self._proc.stdin.write(json.dumps(payload) + "\n")
            self._proc.stdin.flush()
        except BrokenPipeError as exc:
            raise MCPError("El MCP server cerró stdin (¿falló al arrancar? ¿npx sin red?).") from exc

    def _request(self, method: str, params: dict | None = None) -> dict:
        msg_id = self._next()
        msg = {"jsonrpc": "2.0", "id": msg_id, "method": method}
        if params is not None:
            msg["params"] = params
        self._send(msg)
        while True:
            try:
                data = json.loads(self._lines.get(timeout=self.timeout))
            except queue.Empty as exc:
                raise MCPError(f"Sin respuesta del MCP server a '{method}' en {self.timeout}s.") from exc
            except json.JSONDecodeError:
                continue  # línea de log del server, no es JSON-RPC
            if data.get("id") == msg_id:
                return data

    def _notify(self, method: str) -> None:
        self._send({"jsonrpc": "2.0", "method": method})

    def call_tool(self, name: str, arguments: dict | None = None) -> str:
        """Invoca una herramienta y devuelve su texto. Lanza MCPError si falla."""
        reply = self._request("tools/call", {"name": name, "arguments": arguments or {}})
        if "error" in reply:
            raise MCPError(f"Error de protocolo en '{name}': {reply['error']}")
        result = reply.get("result", {})
        if isinstance(result, dict) and result.get("isError"):
            raise MCPError(f"LinkedIn/MCP en '{name}': {_coerce_text(result)[:400]}")
        return _coerce_text(result)
