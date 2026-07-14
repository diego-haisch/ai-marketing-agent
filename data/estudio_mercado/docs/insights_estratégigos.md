# Insights Estratégicos — Playchain

*Basado en 11 entrevistas cualitativas con empresas de retail, moda y bienes de consumo (Crocs, Castañer, Puig, Boboli, Alain Afflelou, Billabong, SOS, Nextail, o9, Splio, Madrid with Love).*

---

## Resumen de Oportunidades Detectadas

| Oportunidad | Validación | Urgencia |
|---|---|---|
| **Replenishment automatizado** | 8/11 entrevistados lo señalan como proceso crítico y no resuelto | 🔴 Alta |
| **Micro-soluciones ligeras** (vs grandes plataformas) | Validado por Nextail, Crocs, Domingo, Splio — mercado se segmenta | 🔴 Alta |
| **Digitalización B2B/wholesale** | 5 entrevistados: baja madurez digital, poca competencia, dolor agudo | 🔴 Alta |
| **Auto-clustering y redistribución** | Alfonso (SOS): 60 clusters manuales. Dolor estructural enorme | 🟡 Media |
| **Collection Flow / compra inicial** | Billabong: 0 sugerencias automáticas. 70% comprometido con 30% visibilidad | 🟡 Media |
| **Reporting conversacional (IA chat)** | Madrid with Love: caso de éxito probado. Splio: tendencia de mercado | 🟡 Media |
| **Simulación financiera (stock -> cash flow)** | Boboli: crisis de liquidez por sobrecompra. Necesidad crítica no cubierta | 🟡 Media |
| **Forecasting upstream (materiales)** | Puig: make-to-order, previsión de materiales es el cuello de botella | 🟢 Baja |

---

## 3 Prioridades por Área de Actuación (Lean Startup)

### 1. Desarrollo de Software

**Principio Lean:** *Build-Measure-Learn. MVP funcional en < 3 meses. Despliegue continuo.*

| Prioridad | Propuesta | Validación | Métrica Clave |
|---|---|---|---|
| **P1: MVP de Replenishment Inteligente** | Algoritmo básico que optimice reposición por tienda usando reglas configurables (no ML complejo). Integración vía API con ERP existente. | Dolor #1 universal. Nextail validó que "replenishment es donde está el valor, no en assortment". Alain Afflelou, Boboli, Castañer, Billabong lo confirman. | Tiempo desde firma hasta primer valor (target: < 4 semanas). Reducción de rotura de stock en tiendas piloto. |
| **P2: Interfaz Conversacional (Chat IA)** | Chat que permite al planner hacer preguntas en lenguaje natural ("¿qué tiendas tienen rotura de la referencia X?"). Sin dashboards. | Madrid with Love lo usa como interfaz diaria. Splio: "el chat reemplaza al dashboard". o9: "Excel será reemplazado por interacción LLM". | % de consultas resueltas sin intervención humana. Tiempo de adopción por usuario. |
| **P3: Arquitectura Modular + APIs** | Cada funcionalidad es un módulo independiente. Se despliega por piezas, no como plataforma monolítica. Integración con Odoo/SAP/Power BI. | Nextail: el mercado se segmenta. Splio: contratos de 12 a 3 meses. Crocs: "soluciones pequeñas, específicas, ligeras, low cost, quick implementation". | Tiempo de integración con sistema del cliente (target: < 1 semana). Nº de módulos activos por cliente. |

**Lógica Lean:** No construir una plataforma. Construir un micro-producto que resuelva UN dolor concreto. Validar. Iterar. El siguiente módulo solo si el anterior genera tracción.

---

### 2. Reporting

**Principio Lean:** *Innovation Accounting. Una métrica que importa. Reportes que generan decisión, no ruido.*

| Prioridad | Propuesta | Validación | Métrica Clave |
|---|---|---|---|
| **P1: Single Source of Truth (capa de calidad de datos)** | Antes de cualquier reporte avanzado, auditar y limpiar la calidad del dato. Unificación de fuentes (ERP, POS, Excel). | Alain Afflelou: Power BI fracasó por calidad de datos. Puig: "no confiamos en los datos". Billabook: atributos mal clasificados. El reporting falla SIEMPRE por el dato base. | % de conciliación entre fuentes de datos. Tiempo desde conexión de fuente hasta reporte validado. |
| **P2: Reporte Único de Decisión (One Metric That Matters)** | No 50 dashboards. Un reporte semanal que responde: "¿qué tienda necesita qué acción esta semana?" Basado en la métrica crítica de cada cliente. | SOS: Power BI hecho por consultores que no entendían fashion retail — inservible. Billabong: planners pasan 80% en tareas admin. El reporting actual es ruido, no señal. | Tiempo que el planner ahorra en generación de reportes (target: 80%). Decisiones tomadas directamente desde el reporte. |
| **P3: Reporting Conversacional (chat-based insights)** | El usuario pregunta "¿qué pasó con las ventas de la semana 24?" y recibe respuesta textual + un número. Sin BI tool. | Madrid with Love: éxito probado. Splio: "la interfaz chat reemplaza dashboards". Reduce fricción de adopción. Curva de aprendizaje = 0. | Nº de consultas semanales por usuario. Tasa de retención a los 30 días. |

**Lógica Lean:** No construir un sistema de reporting. Resolver el problema de decisión. Una sola métrica. Un solo reporte. Que funcione perfectamente. Luego escalar. El 80% del valor está en el 20% de los reportes.

---

### 3. Consultoría de Procesos

**Principio Lean:** *Customer Development. Validación en campo. Pequeños ciclos. Pivotar si no funciona.*

| Prioridad | Propuesta | Validación | Métrica Clave |
|---|---|---|---|
| **P1: Diagnostic Express (2-4 semanas)** | Auditoría rápida de procesos: mapear flujo de decisión actual, identificar el cuello de botella único, proponer una intervención mínima. No informes de 200 páginas. | Domingo: "las empresas son pequeñas, recursos limitados, no necesitan plataformas sofisticadas, necesitan soluciones simples a problemas concretos". Boboli: crisis financiera por falta de visibilidad. | Tiempo desde inicio hasta recomendación accionable (target: < 2 semanas). Coste para el cliente (target: < 3.000€). |
| **P2: Simulación Stock -> Cash Flow** | Modelo que conecta decisión de compra con impacto en liquidez a 6 meses. No forecast de demanda, sino simulación financiera de escenarios. | Boboli: el problema de stock se convirtió en problema de supervivencia. Necesidad real: "¿qué impacto tendrá esta compra en mi cash flow?" Nadie lo ofrece. | % de decisiones de compra que incorporan la simulación de cash flow. Reducción de overstock proyectado. |
| **P3: Acompañamiento Lean (sprints quincenales)** | Ciclos de 2 semanas: implementar una mejora concreta, medir resultado, ajustar. No proyectos de 6 meses con entregable único. | Nextail: el mercado se segmenta hacia implementaciones ligeras. Splio: contratos de 3 meses. El cliente quiere ver valor en semanas, no en meses. | Tiempo hasta primer impacto medible. Tasa de renovación de contrato. |

**Lógica Lean:** La consultoría no es el negocio. Es el vehículo de descubrimiento. Cada diagnóstico es una oportunidad de validar producto. Cada sprint es una oportunidad de vender el módulo de software. La consultoría financia el learning, el software escala.

---

## Principios Lean Transversales

1. **MVP por módulo**: No existe "Playchain platform". Existe "Playchain Replenishment", "Playchain Chat", "Playchain Data Quality". Cada uno vive o muere por su propio mérito.
2. **Time-to-value < 4 semanas**: Si en un mes el cliente no ve valor, el producto falla. Esto condiciona TODAS las decisiones de producto.
3. **Pivotar sin dolor**: La arquitectura modular permite matar una funcionalidad sin matar el producto. Si replenishment no funciona, nos quedamos con chat. Si chat no funciona, nos quedamos con data quality.
4. **Vender el learning, no el software**: La consultoría genera ingresos y aprendizaje. El software escala el aprendizaje. El reporting cierra el loop.
5. **Build-Measure-Learn por cliente**: Cada cliente es un experimento. Cada implementación genera datos que alimentan el producto.

---

*Documento generado a partir de 11 entrevistas de descubrimiento de clientes (abril-junio 2026). Próximo paso: definir el primer MVP concreto y seleccionar 2-3 clientes piloto.*
