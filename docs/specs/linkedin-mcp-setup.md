# LinkedIn MCP — Setup Guide

## Estado actual (2026-07-14)

El MCP server **no está conectado**. Se intentó migrar de `@isteam/linkedin-mcp` a `@kembec/linkedin-mcp` pero el auth flow falló por problemas con WSL (el callback no llegaba al servidor local).

### Credenciales existentes

- **Client ID**: `78mp17m1wfgdzl`
- **Client Secret**: `[REDACTED — ver .env]`
- Guardadas en `.env`

### Limitación importante: `r_member_social` no está disponible

LinkedIn tiene el permiso `r_member_social` (leer posts propios) como **cerrado** — no aceptan solicitudes. Esto significa que ningún MCP server puede leer tus posts a través de la API oficial.

**Opciones para leer posts:**
1. **Member Data Portability API** (`r_dma_portability_self_serve`) — requiere app separada, datos de exportación (no tiempo real)
2. **Scraping manual** — exportar CSV desde LinkedIn Analytics
3. **API reverse-engineered** (`linkedin-internal-api` / `social-brain`) — funciona pero es frágil y viola ToS

---

## Intentos fallidos (2026-07-14)

### Intento 1: @isteam/linkedin-mcp (MCP server original)

- Configurado en `opencode.json` con `LINKEDIN_ACCESS_TOKEN` y `LINKEDIN_PERSON_ID`
- **Problema**: Las variables de entorno nunca se configuraron
- **Resultado**: No funcionó

### Intento 2: @kembec/linkedin-mcp (migración)

- Actualizado `opencode.json` para usar `@kembec/linkedin-mcp`
- **Problema 1**: El auth flow necesita navegador + callback local
- **Problema 2**: En WSL, el callback a `127.0.0.1` no llega al servidor local
- **Intento con IP de WSL** (`172.25.61.96:5003`): LinkedIn rechazó el redirect URI
- **Intento con LinkedIn OAuth Token Generator Tool**: Error "state parameter was modified"
- **Resultado**: No funcionó

### Causa raíz

El entorno WSL complica el OAuth flow porque:
1. El navegador está en Windows
2. El servidor local está en WSL
3. `127.0.0.1` en Windows ≠ `127.0.0.1` en WSL
4. La IP de WSL (`172.25.61.96`) no es aceptada por LinkedIn como redirect URI

---

## Próximos pasos (cuando se retome)

### Opción A: Solucionar el auth flow con WSL

1. Configurar port forwarding de Windows a WSL:
   ```powershell
   netsh interface portproxy add v4tov4 listenport=5003 listenaddress=127.0.0.1 connectport=5003 connectaddress=172.25.61.96
   ```
2. Usar redirect URI: `http://127.0.0.1:5003/callback`
3. Registrar en LinkedIn Developer Portal
4. Ejecutar `npx -y @kembec/linkedin-mcp auth`

### Opción B: Usar LinkedIn OAuth Token Generator Tool

1. Ir a https://www.linkedin.com/developers/tools/oauth
2. Seleccionar la app
3. Poner redirect URL: `https://www.linkedin.com/developers/tools/oauth/redirect`
4. Marcar scopes: `openid`, `profile`, `w_member_social`
5. Request Access Token
6. Copiar el token
7. Configurar manualmente en el MCP server

### Opción C: Usar @isteam/linkedin-mcp con token manual

1. Obtener token con la opción B
2. Configurar en `.env`:
   ```
   export LINKEDIN_ACCESS_TOKEN="token_aqui"
   export LINKEDIN_PERSON_ID="urn:li:person:..."
   ```
3. Revertir `opencode.json` al MCP server original

---

## Configuración de LinkedIn Developer Portal

### App: ApplyChain

- **Client ID**: `78mp17m1wfgdzl`
- **Client Secret**: `[REDACTED — ver .env]`

### Productos solicitados

| Producto | Status | Notas |
|----------|--------|-------|
| Share on LinkedIn | Aprobado | Otorga `w_member_social` |
| Sign in with LinkedIn using OpenID Connect | **Pendiente** | Necesario para identificación |
| Community Management API | No disponible | Requiere app separada |

### Redirect URLs configurados

- `https://www.linkedin.com/developers/tools/oauth/redirect` (el original)
- `http://172.25.61.96:5003/callback` (agregado durante intento, puede quitar)

---

## Herramientas disponibles (cuando funcione)

| MCP Server | Herramientas | Limitaciones |
|------------|-------------|--------------|
| @kembec/linkedin-mcp | `get-profile`, `get-own-posts`, `create-post`, `delete-post` | No tiene `get_comments` ni `get_post_stats` |
| @isteam/linkedin-mcp | `linkedin_get_me`, `linkedin_get_own_posts`, `linkedin_get_post`, `linkedin_get_comments`, `linkedin_get_post_stats`, `linkedin_create_post`, `linkedin_comment_on_post`, `linkedin_like_post`, `linkedin_delete_post` | Requiere `LINKEDIN_ACCESS_TOKEN` y `LINKEDIN_PERSON_ID` |

### Nota sobre lectura de posts

Ninguno de los dos MCP servers puede leer engagement detallado (comentarios, reacciones) sin `r_member_social`. Para análisis de engagement, las opciones son:
1. Exportar CSV desde LinkedIn Analytics → `data/social_media/linkedin/`
2. Usar Member Data Portability API (app separada)
3. Scraping manual del perfil
