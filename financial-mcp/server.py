from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Financial MCP")

@mcp.tool()
def hello(name: str) -> str:
    """Devuelve un saludo."""
    return f"Hola {name}, el MCP está funcionando correctamente."

if __name__ == "__main__":
    mcp.run()