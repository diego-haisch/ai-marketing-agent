# Runbook: volcado de métricas de LinkedIn

Procedimiento operativo para registrar la evolución de las publicaciones
propias de LinkedIn. Diseño y decisiones en
`docs/adr/0001-ingesta-historico-linkedin.md`.

## Requisitos

- `.venv` del proyecto con dependencias instaladas (`pip install -r requirements.txt`).
- Paquete instalado en editable una vez por entorno (expone el comando
  `linkedin-stats` dentro del `.venv`):

```text
.venv/bin/python -m pip install -e .
```

- Dos formas de invocarlo (equivalentes):
  - con el `.venv` activado: `linkedin-stats --help`;
  - sin activar nada: `./linkedin-stats --help` (wrapper de la raíz).
- `node`/`npx` disponibles (el CLI lanza el MCP server `@isteam/linkedin-mcp`
  por stdio, sin agente).
- `LINKEDIN_ACCESS_TOKEN` válido en `.env` o entorno. `LINKEDIN_PERSON_ID`
  se resuelve solo vía `/v2/userinfo` si falta.

> Vía principal: terminal → MCP server → LinkedIn, sin agente y sin
> descargas manuales. El agente con MCP queda para consultas puntuales.
> Si LinkedIn deniega un permiso (hoy: listar posts propios devuelve 403),
> el CLI lo indica con mensaje claro y la alternativa es el CSV.

## Seguimiento habitual vía MCP (sin descargas manuales)

El seguimiento solo toca publicaciones de los últimos 90 días y las marcadas
como `evergreen`. Publicaciones más antiguas quedan congeladas. El CLI lanza
el MCP server, pide los posts recientes y sus estadísticas, y añade una
observación fechada por publicación. Nada manual:

```text
./linkedin-stats snapshot --days 90
```

Para previsualizar sin escribir nada, antepón el flag global:

```text
./linkedin-stats --dry-run snapshot --days 90
```

Después de cada volcado, regenera las salidas:

```text
./linkedin-stats export --csv --html
```

Cadencia recomendada (automatizable con cron; ejemplo diario a las 08:00):

```text
0 8 * * * cd /ruta/a/applychain-business && ./.venv/bin/linkedin-stats snapshot --days 90 && ./.venv/bin/linkedin-stats export --csv --html
```

| Antigüedad | Frecuencia sugerida |
|---|---|
| 0-7 días | diaria |
| 8-30 días | 2 veces por semana |
| 31-90 días | semanal |
| +90 días | congelada salvo `evergreen` |

> Si el comando falla con el 403 de LinkedIn al listar posts, es una
> denegación de la API para esta app, no un fallo del CLI (sale con código
> 3). Mientras LinkedIn no conceda el permiso, usa la vía CSV de abajo para
> esas métricas.

## Primera carga completa y fallback CSV (una sola vez / cuando la API deniegue)

1. Exporta el histórico desde LinkedIn Analytics a CSV.
2. Copia el CSV a `data/social/linkedin/raw/` (carpeta ignorada en Git).
3. Ejecuta la carga completa:

```text
./linkedin-stats import --file data/social/linkedin/raw/<export>.csv
```

4. Revisa el resumen (`añadidas`, `duplicadas`, `posts`) y genera las salidas:

```text
./linkedin-stats export --csv --html
./linkedin-stats report --window 30d
```

5. Marca como `evergreen` las publicaciones que quieras seguir siempre:

```text
./linkedin-stats evergreen --add <post_key>
```

Esta carga queda como línea base histórica. Para seguimientos por CSV
(mientras la API deniegue el listado), usa:

```text
./linkedin-stats snapshot --source linkedin_analytics_csv --file data/social/linkedin/raw/<export_reciente>.csv
```

## Reglas del histórico

- Cada volcado añade observaciones con `measured_at`; nunca sobrescribe.
- Repetir el mismo fichero con la misma fecha no duplica (clave lógica:
  `post_key` + `measured_at` + `source`).
- Celda vacía = desconocido (`null`), nunca 0.
- `measurements.csv` y `report.html` son derivados: si algo no cuadra,
  se regeneran con `export` sin volver a importar.

## Campos editoriales (opcional, manual)

`topic`, `objective`, `format` y `status` se completan a mano en
`data/social/linkedin/curated/catalog.yaml`. No se presentan como datos de
LinkedIn. Sirven para segmentar el análisis (qué temas generan negocio).

## Conexión desde Power BI

1. Origen de datos: archivo de texto/CSV →
   `data/social/linkedin/exports/measurements.csv`.
2. Claves del modelo: `post_key` (publicación), `measured_at` (fecha de
   medición). Una fila = una publicación observada en una fecha.
3. Fechas en ISO 8601; numéricos como números o vacío (vacío = `null`).
4. Medidas sugeridas:
   - `total_interactions` ya viene calculada (suma de métricas disponibles);
   - `engagement_rate` solo existe si hay impresiones, no sustituirla por
     otra tasa cuando falten;
   - crecimiento = valor actual − valor de la primera observación comparable
     en edad (`age_hours`), no entre publicaciones de distinta antigüedad.

## Comandos de referencia

```text
./linkedin-stats snapshot --days 90
./linkedin-stats import --file <csv> [--measured-at FECHA]
./linkedin-stats snapshot --source linkedin_analytics_csv --file <csv>
./linkedin-stats evergreen --list
./linkedin-stats evergreen --add <post_key>
./linkedin-stats evergreen --remove <post_key>
./linkedin-stats export --csv --html
./linkedin-stats report --window 7d
```
