# LinkedIn MCP — Posada en marxa

## 1. Requisits previs

- Node.js (per executar `npx @isteam/linkedin-mcp`)
- API key d'un proveïdor LLM configurat a OpenCode

## 2. Crear una app a LinkedIn Developer Portal

1. Ves a https://www.linkedin.com/developers/apps
2. Fes clic a **Create app**
3. Omple:
   - **App name**: ApplyChain (o el nom que vulguis)
   - **LinkedIn Page**: opcional (si no tens, selecciona "Other")
4. Un cop creada, ves a la pestanya **Auth**
5. Anota el **Client ID** i **Client Secret**
6. A **OAuth 2.0 settings**, afegeix com a **Redirect URL**:
   ```
   https://www.linkedin.com/developers/tools/oauth/redirect
   ```
7. A **Scopes**, marca:
   - `w_member_social` (publicar i interactuar)
   - `r_liteprofile` (llegir perfil bàsic)
   - `r_emailaddress` (opcional, per correu)
   - `r_organization_social` (si uses mode organització)

## 3. Obtenir el token OAuth 2.0

Fes una petició GET al navegador amb aquesta URL (substitueix `CLIENT_ID`):

```
https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=CLIENT_ID&redirect_uri=https://www.linkedin.com/developers/tools/oauth/redirect&scope=w_member_social%20r_liteprofile
```

Et redirigirà a una URL amb un `code` com a paràmetre. Copia'l.

Des de terminal, bescanvia el code per un token:

```bash
curl -X POST https://www.linkedin.com/oauth/v2/accessToken \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=CODI_REBUT" \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" \
  -d "redirect_uri=https://www.linkedin.com/developers/tools/oauth/redirect"
```

Obtindràs un `access_token` (caduca als 60 dies, cal renovar-lo).

## 4. Obtenir el teu LinkedIn Person ID

```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" https://api.linkedin.com/v2/userinfo
```

El camp `sub` és el teu `person_id` (format: `urn:li:person:...` o un string).

## 5. Configurar variables d'entorn

```bash
export LINKEDIN_ACCESS_TOKEN="eyJhbG..."
export LINKEDIN_PERSON_ID="urn:li:person:..."
```

Afegeix-ho al teu `.bashrc` o `.zshrc` per persistir-ho:

```bash
echo 'export LINKEDIN_ACCESS_TOKEN="eyJhbG..."' >> ~/.zshrc
echo 'export LINKEDIN_PERSON_ID="urn:li:person:..."' >> ~/.zshrc
```

## 6. Verificar que funciona

Obre OpenCode i executa:

```
utilitza les eines de linkedin per obtenir les meves dades d'usuari
```

O directament:

```
@linkedin-analyzer mostra'm els meus últims 3 posts amb comentaris i stats
```

## 7. Eines disponibles

| Tool | Descripció |
|------|-----------|
| `linkedin_get_me` | Info de l'usuari autenticat |
| `linkedin_get_own_posts` | Llista els teus posts recents |
| `linkedin_get_post` | Detall complet d'un post (text, autor, stats) |
| `linkedin_get_comments` | Comentaris d'un post |
| `linkedin_get_post_stats` | Recompte de reaccions + comentaris |
| `linkedin_create_post` | Crear un post de text |
| `linkedin_create_article_post` | Compartir un article amb comentari |
| `linkedin_comment_on_post` | Comentar en un post |
| `linkedin_like_post` | Reaccionar a un post |
| `linkedin_delete_post` | Esborrar un post |

## 8. Notes

- El token OAuth caduca als **60 dies**. Cal repetir el pas 3 per renovar-lo.
- Rate limits (~100 GETs/hora per usuari). Dissenyat per anàlisi periòdica, no temps real.
- El prefix de les eines és `linkedin_*` (ex: `linkedin_get_comments`).

## 9. Configuració actual del projecte

- `opencode.json` — MCP server configurat amb credencials via env vars
- `.opencode/agents/linkedin-analyzer.md` — subagent per analitzar engagement
- `AGENTS.md` — documentació de les eines disponible per a tots els agents
