# ADR-0001: Ingesta e histórico de métricas de LinkedIn

- **Estado:** Implementada
+- **Fecha:** 2026-09-16
+- **Decisores:** ApplyChain
+- **Implementación:** `src/linkedin_stats/`, ejecutable `./linkedin-stats`

## Contexto

Queremos medir la evolución de las publicaciones propias de LinkedIn, no solo
conservar una fotografía de sus contadores actuales. El histórico debe poder
analizarse desde terminal, HTML y Power BI, y no debe depender de que un agente
esté ejecutando una sesión interactiva.

El plan inicial proponía usar el MCP de LinkedIn para obtener todas las
publicaciones, sus estadísticas y comentarios, y después llamar directamente a
la API desde un ejecutable. La documentación existente en
`producto/specs/linkedin-mcp-setup.md` muestra dos restricciones que hacen que
esa propuesta no sea segura como diseño base:

- El permiso `r_member_social`, necesario para leer determinados datos sociales
  de publicaciones, no está disponible actualmente para la aplicación.
- Los servidores MCP disponibles no ofrecen exactamente las mismas
  capacidades. En particular, no se puede asumir que `get_post_stats` o
  `get_comments` estén disponibles ni que devuelvan impresiones, clics o
  compartidos.

Por tanto, no debemos diseñar el almacenamiento ni el CLI suponiendo que una
llamada REST de LinkedIn vaya a devolver todos los campos. La fuente real puede
ser, según el permiso y el tipo de exportación disponible:

1. Un CSV exportado desde LinkedIn Analytics.
2. Member Data Portability API, si se habilita para la aplicación.
3. Un MCP que exponga una capacidad concreta.
4. Una API oficial adicional aprobada por LinkedIn.

No se usará scraping ni una API reverse-engineered: además de ser frágil,
puede incumplir las condiciones de LinkedIn.

## Decisión

Construiremos una ingesta por adaptadores con un modelo de datos común y un
histórico append-only. El adaptador principal es el MCP server
(`@isteam/linkedin-mcp`) lanzado directamente desde terminal por stdio, sin
pasar por ningún agente: el CLI habla JSON-RPC con el server y el server habla
HTTPS con LinkedIn. El adaptador CSV (exportado desde LinkedIn Analytics)
queda como vía alternativa para los datos que LinkedIn no sirva por API.

Verificado el 2026-09-16: el transporte terminal→MCP funciona (handshake,
`tools/list`, `get_me` correctos). La misma prueba mostró que LinkedIn
responde 403 (`ACCESS_DENIED`, `partnerApiPostsExternal.FINDER-author`) al
listar posts propios de esta app: esa denegación es de LinkedIn, no del
diseño, y es el caso que cubre el adaptador CSV.

El sistema tendrá tres capas:

1. **Entrada:** importador que normaliza CSV, MCP o API a un mismo esquema.
2. **Histórico:** registros inmutables de una publicación observada en una
   fecha concreta.
3. **Salidas:** CSV plano para Power BI, YAML legible para metadatos y HTML
   generado a partir del histórico.

El MCP server se usa de dos formas: el agente lo invoca en sesiones
interactivas (consultas puntuales) y el ejecutable de terminal lo lanza como
subproceso stdio para el seguimiento periódico (vía principal, sin trabajo
manual). En ambos casos el server usa la misma cuenta y token
(`LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_PERSON_ID`; este último se resuelve solo
vía `/v2/userinfo` si falta). No se deducen endpoints privados del paquete
npm: el CLI solo usa las herramientas públicas del protocolo MCP
(`tools/list`, `tools/call`).

## Modelo de datos

### Identidad de publicación

Cada publicación tendrá un registro de catálogo identificado, en este orden de
preferencia, por:

- `post_urn`, si la fuente lo proporciona.
- Un `source_post_id` estable de la exportación.
- Un identificador compuesto documentado como último recurso, nunca el texto
  completo de la publicación por sí solo.

El catálogo conservará atributos relativamente estables:

```yaml
post_urn: urn:li:share:123456
published_at: 2026-09-16T09:00:00Z
source: linkedin_analytics_csv
format: video
topic: forecasting
objective: authority
duration_seconds: 75
status: active
```

Los campos editoriales (`topic`, `objective`, `hook_quality`, `has_case` y
`call_to_action`) pueden completarse manualmente. No se presentarán como datos
obtenidos de LinkedIn.

### Observaciones

Cada consulta o importación crea una observación nueva. No se actualiza ni se
borra la observación anterior:

```yaml
post_urn: urn:li:share:123456
measured_at: 2026-09-17T09:00:00Z
published_at: 2026-09-16T09:00:00Z
age_hours: 24
reactions: 20
comments: 5
reposts: 2
impressions: null
clicks: null
followers_gained: null
source: linkedin_analytics_csv
source_file: analytics_2026-09-17.csv
```

Los campos no disponibles se guardan como `null`, no como cero. Cero significa
que LinkedIn informó explícitamente cero; `null` significa desconocido o no
exportado.

La clave lógica de una observación será:

```text
(post_urn, measured_at, source)
```

La ingesta será idempotente: repetir el mismo archivo o snapshot no generará
duplicados. Si dos fuentes informan la misma medición, se conservarán ambas y
la fuente quedará identificada; el proceso de reporting decidirá cuál tiene
precedencia.

## Retención y frecuencia

### Primera carga

Se importará todo el histórico que proporcione el archivo o fuente inicial.
Esta carga no implica que todas las publicaciones deban seguir consultándose
indefinidamente. El resultado queda como línea base histórica.

### Seguimiento habitual

El proceso operativo consultará o importará solo:

- publicaciones de los últimos 90 días;
- publicaciones marcadas manualmente como `evergreen` o seleccionadas para
  seguimiento;
- publicaciones que necesiten una corrección o reconciliación.

La cadencia recomendada es:

- 0-7 días: una observación diaria;
- 8-30 días: dos observaciones semanales;
- 31-90 días: una observación semanal;
- más de 90 días: congeladas salvo `evergreen`.

La cadencia es una política del CLI, no una suposición sobre lo que LinkedIn
permite consultar. Para una exportación manual, la fecha de medición será la
fecha real del proceso de importación y se conservará el nombre del archivo de
origen.

## Formatos y salidas

El almacenamiento de trabajo será un YAML de catálogo y observaciones por su
legibilidad y facilidad de revisión. Para consumo analítico, el formato
principal será un CSV normalizado, una fila por publicación y fecha de medición.
Power BI no deberá depender de estructuras YAML anidadas.

Columnas mínimas del CSV analítico:

```text
post_urn,source_post_id,published_at,measured_at,age_hours,
format,topic,objective,status,source,
reactions,comments,reposts,impressions,clicks,followers_gained,
total_interactions,engagement_rate,comment_rate
```

Reglas de exportación:

- fechas en ISO 8601 y zona horaria explícita;
- números como números o valores vacíos, nunca textos como `N/A`;
- `null` del modelo se exporta como campo vacío;
- `total_interactions` solo se calcula con campos disponibles y documenta su
  fórmula;
- `engagement_rate` solo se calcula si existen impresiones, y no se sustituye
  por una tasa basada en reacciones cuando falten impresiones;
- el CSV es derivado y puede regenerarse desde el histórico;
- el HTML también es derivado y no será fuente de verdad.

Se podrá añadir un SQLite o Parquet si el CSV resulta insuficiente por volumen,
pero no se introduce ahora: el volumen esperado no lo justifica y CSV es la
opción más directa para Power BI.

## CLI y rutas reales

El ejecutable es `./linkedin-stats` (wrapper bash sobre `.venv`, con
`PYTHONPATH=src`, siguiendo la convención de `src/create_presentation`).
Código en `src/linkedin_stats/` (`paths`, `store`, `importer`, `exporter`,
`reporter`, `main`).

```text
linkedin-stats snapshot --days 90 [--count 50]        # vía principal: MCP por terminal
linkedin-stats import --file export.csv [--measured-at FECHA]   # carga inicial / fallback CSV
linkedin-stats snapshot --source linkedin_analytics_csv --file export.csv  # seguimiento por CSV
linkedin-stats export --csv --html
linkedin-stats report --window 7d
linkedin-stats evergreen --add|--remove POST_KEY | --list
```

Datos en `data/social/linkedin/`:

```text
data/social/linkedin/
  raw/                    # CSV originales (ignorado en Git: datos personales)
  curated/
    catalog.yaml          # catálogo de publicaciones (fuente de verdad editorial)
    observations.yaml     # observaciones append-only (fuente de verdad métrica)
  exports/
    measurements.csv      # derivado plano para Power BI (regenerable)
    report.html           # derivado para revisión visual (regenerable)
```

Notas de implementación:

- El importador normaliza cabeceras y alias (ES/EN, con/sin guiones) antes de
  comparar, para no perder campos como `published_at`.
- `--dry-run` es global y va delante del subcomando:
  `./linkedin-stats --dry-run snapshot --days 90 --file export.csv`.

El primer comando será el camino soportado para la carga inicial si no existe
una fuente API autorizada. `snapshot` no debe implicar que existe una API: debe
fallar con un mensaje claro cuando el adaptador no esté configurado. Se añadirá
`--dry-run` antes de cualquier operación remota o modificación del histórico.

El script leerá secretos desde variables de entorno o `.env` sin imprimirlos.
Los tokens no se guardarán en YAML, CSV, HTML ni logs. Las exportaciones brutas
que contengan datos personales o comentarios no se incluirán en Git.

## MCP y autenticación

El MCP server (`@isteam/linkedin-mcp`, configurado en `opencode.json` para el
agente) expone, entre otras, `get_me`, `get_post`, `get_comments`,
`get_own_posts` y `get_post_stats`. El CLI lo reutiliza lanzándolo por stdio
desde terminal, con el mismo token. En ambos usos:

- se requiere autenticación válida (`LINKEDIN_ACCESS_TOKEN`; el
  `LINKEDIN_PERSON_ID` se resuelve solo si falta);
- la disponibilidad de cada herramienta y campo depende de los permisos que
  LinkedIn haya concedido a la app (verificado: el listado de posts propios
  devuelve 403 en esta app; ese error se propaga con mensaje claro y código
  de salida 3);
- una llamada exitosa no garantiza que existan impresiones o métricas de
  negocio.

El agente usa el MCP para consultas puntuales. El seguimiento periódico lo
hace el CLI vía MCP sin agente y sin descargas manuales; la persistencia la
realiza el CLI con fuente (`linkedin_mcp` o `linkedin_analytics_csv`) y fecha
de medición explícitas. El CSV queda como fallback para los datos que la API
deniegue.

## Métricas de negocio

Las métricas de LinkedIn no bastan para medir el objetivo comercial. El modelo
permitirá asociar manualmente, en un fichero separado, eventos como:

- mensajes recibidos;
- contactos relevantes;
- reuniones;
- leads;
- oportunidades comerciales o laborales;
- publicación que originó el contacto;
- tiempo invertido en producirla.

Estos eventos no se atribuirán automáticamente por coincidencia temporal. La
atribución tendrá una fuente y una nota manual para evitar confundir alcance
con generación de negocio.

## Alternativas descartadas

### Consultar todo el histórico en cada ejecución

Se descarta por coste, latencia y bajo valor marginal. La primera carga sí es
completa; las siguientes usan la ventana de 90 días y la lista evergreen.

### Usar el MCP como base de datos

Se descarta porque el MCP es una interfaz de herramientas, no un almacén
histórico, y sus capacidades pueden cambiar con el servidor o los permisos.

### Llamar a endpoints internos o hacer scraping

Se descarta por fragilidad, mantenimiento y riesgo de incumplir las condiciones
de LinkedIn.

### Guardar solo un YAML anidado

Se descarta como formato de consumo analítico. Se mantiene YAML como formato
legible del catálogo, pero el dataset para Power BI será plano y regenerable.

## Consecuencias

### Positivas

- Las mediciones históricas no se pierden al actualizar contadores.
- La primera carga puede hacerse con el mecanismo que realmente esté
  disponible.
- El sistema no confunde ausencia de datos con cero.
- Power BI y HTML consumen salidas estables y planas.
- Se puede cambiar de CSV a API o MCP sin cambiar el modelo analítico.
- Se reducen llamadas innecesarias para publicaciones antiguas.

### Costes y limitaciones

- La primera implementación necesita un importador para el formato exacto que
  exporte LinkedIn.
- Algunas métricas pueden seguir siendo `null` por restricciones de permisos.
- Las exportaciones manuales requieren disciplina y una fecha de importación.
- Se necesita una revisión de deduplicación cuando cambien las columnas o el
  formato de LinkedIn.

## Criterios de aceptación

La implementación se considerará alineada con esta ADR cuando:

1. Una misma observación importada dos veces no produzca duplicados.
2. Una nueva ejecución añada `measured_at` sin sobrescribir observaciones
   anteriores.
3. El seguimiento por defecto limite las publicaciones a 90 días más las
   marcadas como `evergreen`.
4. Los campos no disponibles se conserven como `null`/vacíos, no como cero.
5. El CSV exportado sea plano, tenga fechas y tipos consistentes y pueda
   cargarse en Power BI.
6. Sea posible regenerar CSV y HTML sin volver a consultar LinkedIn.
7. No se escriban tokens ni datos secretos en los artefactos generados.
8. El CLI indique claramente si trabaja con CSV, MCP o una API autorizada.
