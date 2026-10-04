# Entrevista – Demand Planning en Bayer (Consumer Health)

- Fecha: 25 sep 2026
- Interlocutor: Demand Planner de Bayer Consumer Health (nombre no recogido en la nota)
- Mercados: Europa Central (Polonia, Rumanía, Bulgaria, Adria)
- Origen: nota Granola https://notes.granola.ai/d/0455060e-2778-4fb2-a706-7376895a1d8d
- Tipo: estudio de mercado / benchmark de procesos de demand planning en gran consumo

# Perfil de la Empresa y Proceso

- Bayer centralizó supply chain en Barcelona hace 2 años; planner 100% remoto
- Productos estacionales fuertes (Aspirin, antifríos); farmacias se cubren en agosto-septiembre antes de temporada
- Proceso DRM: antes en excels complejos, ahora en sistema; el planner mantiene un Excel vinculado para detectar desviaciones
- Financial Reconciliation: comparativa de cantidades y valor con finanzas para identificar gaps

# Stack Tecnológico

- Olympus: herramienta principal de forecast, ~20 modelos (seasonal, non-seasonal, moving average…)
  - El sistema propone los 3 modelos con menor MAPE; el planner ajusta manualmente
- Anaplan: gestión de sellout (nuevo proceso PBS), volcado a Olympus con conversión sell-in
- Excel: detección de desviaciones y ajustes manuales

# Áreas de Dolor

- Roturas de stock: se limpian manualmente; si no, el algoritmo las lee como caída de ventas
- Eventos no recurrentes (cambios de precio, lanzamientos): requieren enriquecimiento manual del modelo
- Bias de forecast: objetivo interno 2%, realidad ~5%
- Riesgo de calendario en el nuevo proceso basado en sellout: datos llegan el día 9-10 y el sistema debe estar listo el día 15
- Obsolescencia: objetivo <0,45% de net sales/año (frente a ~2-2,5% en moda/Inditex)

# Contexto de Negocio Propio (ApplyChain)

- Ventajas declaradas del algoritmo propio vs herramientas genéricas:
  - Productos nuevos sin histórico (no requiere enganche por referencia)
  - In-season forecasting por familia con stock y descuentos
  - Auto-limpieza de picos promocionales y canales irregulares (multimarca)
  - En Etnia, incorporar sellout redujo el error ~20 puntos porcentuales
- Enfoque: software de forecast + replenishment para pymes de moda (10-100M€)
  - La consultoría pura no genera tracción; el software sí cubre demand + supply planning

# Insights para la Plataforma de Planning

- Referencia clara de stack enterprise (Olympus + Anaplan + Excel) contra el que posicionar
- Dolor demostrado: limpieza manual de datos y ajuste manual de eventos → oportunidad de automatización
- El Excel persistente junto al sistema es la evidencia de que la herramienta no cierra el ciclo
- Métricas que hablan el idioma del sector: MAPE, bias, obsolescencia
