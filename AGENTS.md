# ApplyChain – Project Context

## Business
ApplyChain és una consultoria especialitzada en supply chain i intel·ligència artificial per a pimes de moda, calçat, accessoris i retail.

## Services
- **Conductor**: Consultoria operativa en supply chain (diagnòstic, millora de processos, Lean, Kanban)
- **Armonía**: Suite de dashboards Power BI amb mòduls d'IA (forecasting, optimització d'estoc, pricing)
- **Maestro**: Formació per a equips interns en BI, IA i Big Data

## Commercial approach
- First-contact messages: conversational, reference-based when possible
- Language: Spanish (default for all work and commercial outreach)
- Length: ~150-170 words
- Diego's background: operations optimization → software tools development
- Always frame around the client's specific problems, not generic features

## Contact data
Commercial messages are stored in `data/comercial_contact/`. Business info in `data/datos_empresa/`.

## LinkedIn MCP
LinkedIn MCP server (`@isteam/linkedin-mcp`) available via `linkedin_*` tools:
- `get_own_posts` — llista els teus posts recents
- `get_post` — detall complet d'un post (text, autor, stats)
- `get_comments` — comentaris d'un post
- `get_post_stats` — recompte de reaccions/comentaris
- `get_me` — informació de l'usuari autenticat
- `create_post` / `create_article_post` — publicar contingut
- `comment_on_post` / `like_post` — interactuar
- `delete_post` — esborrar un post

Configura les variables d'entorn `LINKEDIN_ACCESS_TOKEN` i `LINKEDIN_PERSON_ID` abans d'usar-lo.

## Interaction rules
- Siempre que necesites preguntar algo al usuario, usa la herramienta `question` en lugar de listar preguntas en texto plano. Esto garantiza respuestas estructuradas y evita que las preguntas se pierdan.

## Style
- Direct, concise, no markdown in message bodies
- Solutions-oriented, not feature-dump
- No emojis unless requested
