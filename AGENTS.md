# ApplyChain – Project Context

## Business
ApplyChain és una consultoria especialitzada en supply chain i intel·ligència artificial per a pimes de moda, calçat, accessoris i retail.

## Commercial Content
- For external commercial content, consult **www.applychain.es** first. It is the source of truth for services, value proposition, case studies and news.
- First-contact messages: conversational, reference-based when possible
- Language: Spanish (default for all work and commercial outreach)
- Length: ~150-170 words
- Diego's background: operations optimization → software tools development
- Always frame around the client's specific problems, not generic features

## Contact data
Commercial files are stored in `comercial/`. Business information is in `estrategia/`. Pipeline is in `comercial/pipeline.yaml`.

## LinkedIn MCP
If the LinkedIn MCP server (`@isteam/linkedin-mcp`) is configured, it provides these `linkedin_*` tools:
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
- Cuando el usuario diga `cierra sesión`, `cerrar sesión`, `cierro la sesión` o utilice `/close`, cargar el skill `session-close` y seguir su procedimiento de cierre.

## Weekly Plan
- Skill available: `.opencode/skills/weekly-plan/SKILL.md`
- Default: 3h/week (2 blocks of 1.5h)
- Priority: 5 contacts + 1 publication + interaction + follow-ups
- Ask for weekly plan when requested

## Style
- Direct, concise, no markdown in message bodies
- Solutions-oriented, not feature-dump
- emojis for non so formal conversations

## Repository Structure
- `src/linkedin_stats/`: Python package and CLI `linkedin-stats` for importing, storing, reporting and exporting LinkedIn metrics.
- `src/create_presentation/`: utilities for generating presentations and rendering DOCX files.
- `financial-mcp/`: separate Python MCP server with its own `requirements.txt` and virtual environment.
- `contenido/linkedin/`: LinkedIn drafts and published content.
- `estrategia/`: business, positioning and founder documents.
- `inteligencia/`: interview notes and commercial insights.
- `comercial/`: contacts, follow-ups, weekly plans and sales pipeline.
- `data/social/linkedin/`: generated LinkedIn datasets and exports.
- `docs/runbooks/`: operational procedures.
- `docs/adr/`: architecture decisions.

## Technology
- Python >= 3.10.
- Python packaging uses `pyproject.toml` and a `src/` layout.
- Main Python dependency: `pyyaml`.
- CLI entry point: `linkedin-stats`.
- Node is only used for the `xlsx` dependency and spreadsheet-related utilities.
- Do not modify generated files, `__pycache__/`, `*.egg-info/`, `.venv/`, `node_modules/` or `.env`.

## Common Commands
- Install Python package: `pip install -e .`
- Run CLI: `linkedin-stats`
- Run module directly: `python -m linkedin_stats`
- Install Node dependencies: `npm install`
- Run tests, when present: `pytest`

## Data and Privacy
- LinkedIn raw exports may contain personal data and must not be committed.
- Never read, print or expose secrets from `.env`.
- Preserve existing historical data formats and directory conventions.
- Prefer small, targeted changes. Do not reorganize directories without an explicit request.
