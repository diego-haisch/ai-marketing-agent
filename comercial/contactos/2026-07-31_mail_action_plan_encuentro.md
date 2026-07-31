id:encuentro

## 2026-07-31 — Email (borrador) a Juli Fabre — propuesta inicial tras la reunión

**Asunto:** Hoja de ruta para sacar más partido a Cortés — dos frentes para arrancar ya

Hola Juli (y equipo),

Gracias por la reunión de ayer a todos; fue muy útil profundizar en las problemáticas que estáis afrontando con Cortés y la propuesta de compra. A mi modo de ver, tiene sentido dividir el trabajo en dos frentes complementarios: acciones a corto plazo (con impacto rápido) y actuaciones a medio/largo plazo (que pongan a Cortés al nivel de lo que necesita vuestro operativo). Juntos pueden componer una hoja de ruta práctica para mejorar la gestión y la toma de decisiones.

**1. Acciones a corto plazo — resultados rápidos y evidencias**

El objetivo de esta primera fase es doble: validar dónde está el mayor potencial de mejora y generar quick wins que podáis ver y tocar. La planteamos en tres frentes:

**1.1. Evaluar la efectividad del algoritmo**
Analizaremos el comportamiento real del algoritmo tal y como está hoy: backtests sobre la campaña pasada para medir la desviación entre compra sugerida y compra real (MAPE y métricas por cluster), revisión de errores de clasificación (exceso de "best seller") y detección de reglas fijas que distorsionan los resultados. Resultado: una página con 3 quick wins accionables y su impacto esperado.

**1.2. POC: Range Plan vs capacidad de tienda (la petición de Borja)**
Montaremos una prueba de concepto visual (Excel/mini-dashboard) que muestre la saturación por tienda. La idea es que podáis ver y tocar la información y comprobar si la visualización responde a vuestras necesidades operativas, antes de invertir en nada más grande. Resultado: POC funcionando + demo práctica de 30 min.

**1.3. Reactivar la visualización de métricas**
Para que nada de lo anterior quede en el aire, es crítico reactivar el reporting (aunque sea en Excel) y poder comparar antes/después: desviación, precisión por cluster y % de entradas correctas en Cortés. Sin métricas activas no podemos validar que las acciones tienen impacto. Resultado: un pequeño cuadro de control que os acompañe de forma permanente.


**2. Acciones a medio/largo plazo — mejoras que deberíais tener en el radar**

Tal como comentamos ayer, la herramienta que tenéis implementada ha evolucionado mucho en mi trabajo con otros clientes, y creo que merece la pena valorar estas mejoras:
- Parametrización de percentiles y reglas editables en interfaz (eliminar valores fijos en código).
- Gestión de aperturas mediante tiendas espejo y factor de expansión.
- Clusterización automática de tiendas y curvas de tallas por canal/geografía.
- Overrides controlados (umbrales de variación y validaciones automáticas).
- Entorno de calidad (sandbox) para pruebas masivas y reclasificación.
- Reporting de precisión in-season y cuadro de mando forecast vs real.
- Integración ordenada con el Data Lake (bronce → silver → gold) para consolidar todas las fuentes.

**3. Siguiente paso**

Si no tenéis vacaciones en agosto, me gustaría proponer una reunión a principios de mes para no dilatar los tiempos y fijar prioridades (30 min). Yo estaré de vacaciones sólo unos días y me podría poner con vosotras a partir del 7/ago.

Quedo atento para fijar la llamada y preparar el extracto de datos necesario.

Un saludo,

