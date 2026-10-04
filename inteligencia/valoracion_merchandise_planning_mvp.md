# Valoración de procesos de Merchandise Planning para el MVP

**Fecha:** 2026-10-04  
**Estado:** Replanteamiento de la priorización de producto  
**Ámbito:** SaaS de planning multicanal para pymes de moda, calzado y accesorios

## Objetivo

Este documento sustituye la valoración anterior. La unidad de análisis ya no son módulos genéricos de Merchandise Planning, sino procesos operativos completos y su aplicación a cada canal.

El objetivo es decidir qué MVP puede generar más oportunidad comercial, demostrar valor en pocas semanas y servir de base para evolucionar hacia un producto multicanal.

La propuesta parte de cuatro canales con lógicas diferentes:

- **Retail:** surtido y allocation por tienda, ventas por tienda y talla, reposición y traspasos.
- **Wholesale:** pre-orders, make-to-order, extrapolación por cliente o clúster y entregas por olas.
- **E-commerce:** stock en almacén y demanda sin restricción física de surtido.
- **Department stores:** canal con lógica de retail o wholesale según el acuerdo operativo y la disponibilidad del dato.

La multicanalidad debe estar presente en el modelo de datos y en la arquitectura, pero no implica desarrollar desde el primer día todos los algoritmos para todos los canales.

## Evidencia de las entrevistas

### Retail y modelos híbridos

- **Etnia / entrevistas de demand planning:** el seguimiento de ventas y stock mediante Power BI aparece como una necesidad trasladable a un producto SaaS. El forecast por tienda y talla es un nivel de granularidad útil.
- **Boboli, Eva Robles:** no existe un forecasting formal por empresa, canal o tienda. Las decisiones se apoyan en históricos, experiencia y reglas estáticas. El stock tiene impacto directo en liquidez y tesorería. El wholesale también se usa como señal para anticipar el retail.
- **Castañer, Rubén Egea:** existe sobrestock en productos no básicos, falta de forecast global y reposición poco optimizada. La empresa valora modelos simples y robustos, con una implantación rápida.
- **EseOese / SOS, Alfonso Palomares:** forecasts artesanales, allocation y clusterización manual. La gestión de clusters y la distribución inicial son problemas reales, pero requieren una configuración comercial considerable.
- **Nextail y Splio:** el valor operativo se concentra en replenishment, traspasos y soluciones ligeras, no necesariamente en una suite completa de assortment.
- **Crocs:** falta de stock y forecasts de precisión limitada; preferencia por soluciones ligeras e integrables.
- **Billabong, Marie Azam:** collection flow, recomendación de compra, allocation inicial y simulación de escenarios se realizan con mucha intervención manual. Los planners dedican demasiado tiempo a tareas operativas.

### Wholesale

- **Puig, Maite Muñoz:** modelo principalmente make-to-order. Se presenta la colección, se capturan pedidos, se planifica la producción y se entrega según disponibilidad. El forecast de producto terminado es limitado; el forecast de materiales sí tiene relevancia.
- **Castañer:** la venta wholesale está concentrada en una ventana corta y la reposición wholesale se gestiona mediante un sistema utilizado por agentes. Hay una necesidad de anticipar señales antes de que lleguen los datos fiables de marzo o abril.
- **Domingo Barrachina:** baja madurez digital, dependencia de personas, Excel y escasa automatización en clientes wholesale. Aparecen oportunidades en seguimiento de muestras, pedidos, reposición y reporting, aunque la supply chain de algunas empresas se considera relativamente controlada.
- **Eva Robles:** los pedidos wholesale se utilizan para interpretar tendencias futuras del retail.

### Conclusión de la evidencia

Las entrevistas no validan con la misma intensidad todos los procesos:

- La validación más repetida y operativa está en **ventas, stock, forecast retail, replenishment y traspasos**.
- La necesidad de **purchase planning y collection flow** es clara, pero suele implicar más decisiones comerciales, más datos y más trabajo de implantación.
- Wholesale tiene una oportunidad diferenciada, pero exige separar sell-in, pre-orders, make-to-order, producción y entregas. No debe modelarse como retail.
- El problema transversal no es solamente la predicción: es convertir datos fragmentados en una acción concreta.

## Criterios de puntuación

Cada proceso se puntúa sobre 100 con los siguientes criterios:

| Criterio | Peso |
|---|---:|
| Dolor observado y frecuencia | 30% |
| Impacto económico | 25% |
| Oportunidad comercial y diferenciación | 20% |
| Encaje con pymes y canales objetivo | 15% |
| Viabilidad de un MVP y velocidad hasta valor | 10% |

La puntuación no representa únicamente la importancia estratégica del proceso. Representa su conveniencia como punto de entrada comercial para ApplyChain.

## Nueva valoración de procesos

### Pre-season

| ID | Proceso | Canales principales | Puntuación | Prioridad | Comentario |
|---|---|---|---:|---|---|
| P1 | Budget multicanal | Retail, department stores, wholesale, e-commerce | 68 | Fase 2 | Importante para alinear ventas, unidades, coste y descuentos, pero poco homogéneo y dependiente de una disciplina presupuestaria que no todas las pymes tienen. |
| P2 | Collection Flow: estructura de colección, assortment y allocation inicial | Retail, wholesale, e-commerce | 84 | Fase 1B | Dolor claro en collection flow y allocation manual. Es diferenciador, pero amplio: combina surtido, clusters, mínimos, capacidad del parque y lógicas específicas por canal. |
| P3 | Purchase Planning | Retail, wholesale, e-commerce | 89 | Fase 1B | Conecta forecast con una decisión económica. Muy relevante para sobrestock, caja y disponibilidad. Debe tener reglas diferentes para stock retail, make-to-order wholesale y stock de almacén e-commerce. |
| P4 | Seguimiento de llegadas pre-season | Todos | 82 | MVP ampliado | Es acotable y genera valor rápido. Un reporting de fechas prometidas, retrasos y mercancía no servible puede ser una primera funcionalidad operativa antes de automatizar la planificación de proveedores. |

### In-season

| ID | Proceso | Canales principales | Puntuación | Prioridad | Comentario |
|---|---|---|---:|---|---|
| I1 | Forecast de ventas | Retail, con extensiones a e-commerce y wholesale | 93 | MVP principal | Es el proceso con mejor combinación de dolor, impacto, validación y capacidad de demostrar precisión. La primera versión debe trabajar a nivel tienda y talla, con baseline ajustable manualmente. |
| I2 | Seguimiento de ventas y stock | Retail, e-commerce y modelos híbridos | 91 | MVP principal | Es la capa de decisión que permite conocer salud de stock, tallaje, cobertura y desviaciones. Debe producir excepciones y acciones, no un dashboard generalista. |
| I3 | Reaprovisionamiento por canal | Retail, wholesale, e-commerce | 91 | MVP principal / Fase 1B | Tiene alto valor, pero la lógica no es única: retail repone según ventas y cobertura; wholesale compra lo pedido y entrega por olas; e-commerce depende de la política de stock de almacén. |
| I4 | Reagrupaciones y balance de stock | Retail y modelos híbridos | 85 | Fase 1B | Dolor validado por EseOese/SOS, Nextail y Splio. Puede generar valor sin comprar más, pero necesita stock fiable, reglas de transporte y aceptación operativa. |
| I5 | Reaprovisionamiento de almacén y básicos | Retail, e-commerce y modelos híbridos | 83 | Fase 1B | Relevante para básicos y referencias recurrentes. Conviene separarlo de la reposición de tienda porque la decisión se toma entre almacén, proveedor y canales. |
| I6 | Markdown y descuentos | Retail y e-commerce | 73 | Fase 2 | Tiene impacto sobre el stock sobrante, pero exige histórico de descuentos, margen y respuesta de la demanda. En la primera versión puede limitarse a alertas de riesgo y propuestas simples. |

## Lectura de la puntuación

La puntuación muestra tres grupos distintos:

### Grupo 1: núcleo de entrada

- Forecast de ventas: **93**.
- Seguimiento de ventas y stock: **91**.
- Reaprovisionamiento por canal: **91**.

Estos procesos forman un ciclo operativo completo:

```text
Ventas y stock reales
→ Forecast ajustado
→ Detección de desviaciones
→ Reposición o acción sobre el stock
→ Medición del resultado
```

Es el mejor punto de entrada porque:

- Está validado en más entrevistas que cualquier otro bloque.
- Puede medirse antes de terminar una temporada.
- Tiene impacto directo en roturas, exceso, disponibilidad y ventas recuperadas.
- Permite una promesa comercial concreta.
- Puede empezar con Excel o extracción del ERP.
- Construye la base de datos necesaria para el pre-season posterior.

### Grupo 2: extensión pre-season vendible

- Purchase Planning: **89**.
- Collection Flow: **84**.
- Seguimiento de llegadas: **82**.
- Reagrupaciones: **85**.

Estos procesos son importantes, pero deben acotarse. Collection Flow no debe convertirse en una suite completa de diseño de colección. Purchase Planning no debe empezar como un sistema financiero integral. El seguimiento de llegadas sí puede incorporarse pronto porque es más concreto y menos dependiente de algoritmos avanzados.

### Grupo 3: fases posteriores

- Budget multicanal: **68**.
- Markdown y descuentos: **73**.

No son procesos irrelevantes. Se posponen porque requieren más madurez de datos, definición financiera o histórico de comportamiento. El budget debe actuar inicialmente como restricción de la recomendación de compra, no como el centro del producto.

## Diseño funcional por canal

### Retail

Debe ser el canal de referencia para el MVP:

```text
Forecast por tienda y talla
→ Seguimiento de ventas y stock
→ Reposición por cobertura
→ Reagrupación entre tiendas
→ Reaprovisionamiento de almacén
```

La primera versión debería diferenciar:

- Básicos y continuidades.
- Novedades con poco histórico.
- Productos estacionales one-shot.
- Roturas de stock que ocultan la demanda real.
- Tallas o variantes con desequilibrios.

### Wholesale

No debe reutilizarse sin cambios la lógica retail:

```text
Pre-orders y compras reales
→ Extrapolación por cliente o clúster
→ Forecast sell-in
→ Compra o producción make-to-order
→ Entrega por olas
```

La granularidad inicial debería ser total de campaña o clúster de cliente, no necesariamente cliente y SKU. El producto debe indicar cuánto se ha comprado, cuánto falta respecto al objetivo y qué parte es forecast. La cobertura wholesale no debe expresarse como semanas de stock sin validar primero el modelo de Verner y la lógica real de cada empresa.

Wholesale puede compartir la capa de datos, forecast y seguimiento, pero necesita reglas específicas de:

- Pre-orders.
- Probabilidad de conversión.
- Mínimos de compra.
- Make-to-order.
- Capacidad productiva.
- Entregas parciales o por olas.

### E-commerce

La lógica depende de si existe stock dedicado o un pool común con retail. Antes de construir un algoritmo específico hay que verificarlo con clientes.

La primera versión puede cubrir:

- Ventas y stock de almacén.
- Forecast por referencia y canal.
- Alertas de disponibilidad.
- Interacción con la compra multicanal.

No debe asumirse todavía que el e-commerce necesita replenishment independiente. Esa decisión depende de cómo se protege y asigna el stock.

### Department stores

Debe tratarse como un canal configurable, no como una copia automática de retail o wholesale. El proceso dependerá de:

- Si la empresa controla el stock.
- Si recibe ventas por tienda o solo pedidos.
- Si existe reposición.
- Si la mercancía se entrega a un almacén central.

El primer MVP puede incorporarlo mediante una configuración de canal y reglas, sin desarrollar una lógica específica hasta disponer de casos reales.

## MVP recomendado

### Decisión

El mejor MVP para emprender no es una suite completa de pre-season ni una plataforma multicanal simétrica. Es:

> **Forecast operativo y acciones de stock para retail, con arquitectura multicanal y una primera extensión de purchase planning y llegadas.**

La promesa comercial sería:

> **Cada semana indicamos qué está pasando con las ventas y el stock, qué debes reponer y dónde debes mover producto, con un forecast ajustable por tienda y talla.**

### Alcance de la primera versión

1. Carga de ventas, stock, tiendas, tallas, productos y calendario.
2. Normalización de referencias, familias, tallas y canales.
3. Forecast baseline por tienda y talla.
4. Ajuste manual del baseline y registro de la versión final.
5. Seguimiento de ventas y stock.
6. Salud de stock, cobertura, roturas y exceso.
7. Corrección de forecast cuando existe rotura de stock.
8. Propuesta de reaprovisionamiento retail.
9. Reglas para básicos, novedades y one-shot.
10. Lista priorizada de acciones: reponer, vigilar, no comprar o revisar forecast.
11. Medición de forecast frente a venta real.
12. Carga sencilla de pedidos, mercancía en tránsito y fechas previstas.
13. Alertas básicas de retrasos y mercancía que no llegará a tiempo.
14. Exportación a Excel y trazabilidad de las recomendaciones.

El MVP no necesita sustituir el ERP, el Power BI ni el sistema de pedidos. Debe convertirse en la capa que transforma sus datos en decisiones operativas.

## Fase 1B: pre-season y multicanal

Después de validar el núcleo in-season, la ampliación debería ser:

### 1. Purchase Planning

- Objetivo de ventas por canal y familia.
- Cobertura objetivo para retail.
- Ventas previstas frente a stock disponible.
- Pedidos abiertos y mercancía en tránsito.
- Lead times y mínimos de proveedor.
- Compra recomendada.
- Restricción de presupuesto.
- Impacto en stock final y caja.

Para wholesale:

- Pre-orders.
- Pedidos confirmados.
- Forecast por clúster.
- Compra o producción prevista.
- Diferencia entre venta prevista y compra real.
- Entregas por olas.

### 2. Seguimiento de llegadas

- Fecha prometida.
- Fecha revisada.
- Fecha real de llegada.
- Cantidad esperada y recibida.
- Mercancía servible o no servible para la campaña.
- Impacto sobre allocation, reposición y ventas.
- Alerta de retraso priorizada por impacto económico.

Debe ser inicialmente semi-inteligente: detectar desviaciones y priorizar incidencias, sin prometer todavía una predicción avanzada de retrasos de proveedores.

### 3. Collection Flow acotado

- Clusters editables.
- Assortment por tienda y canal.
- Capacidad del parque de tiendas.
- Mínimos de exposición.
- Propuesta de allocation inicial.
- Propuesta de surtido multicanal.
- Comparación entre surtido previsto y demanda histórica.
- Revisión manual antes de aprobar.

En wholesale, debe permitir que la colección sea amplia inicialmente y que las referencias se marquen como viables, en riesgo o descartadas según pre-orders, mínimos y forecast.

## Fase 2

- Budget multicanal completo por canal y familia.
- Simulación de ventas, unidades, coste y descuentos.
- Extrapolación avanzada entre wholesale, retail y e-commerce.
- Forecast de materiales y capacidad productiva.
- Medición de venta perdida.
- Markdown y descuentos con histórico y propuesta de nuevo descuento.
- Forecast específico de e-commerce una vez validada la política de stock.
- Reglas específicas para department stores.
- Interfaz conversacional para consultar excepciones y recomendaciones.

## Qué no debería formar parte del primer MVP

- Un sistema completo de budgeting corporativo.
- Un CRM wholesale.
- Un diseñador automático de colecciones.
- Una optimización total de assortment para todos los canales.
- Un único algoritmo de forecast para retail, wholesale y e-commerce.
- Una cobertura wholesale expresada como stock retail sin validación del modelo.
- Markdown automático sin histórico fiable.
- Planificación detallada de materiales para clientes sin listas de materiales estructuradas.
- Integraciones complejas con todos los ERPs.
- Un dashboard generalista con decenas de KPIs.

## Métricas de validación del MVP

### Forecast

- MAE o wMAE por tienda y talla.
- BIAS por familia y canal.
- Precisión con y sin rotura de stock.
- Porcentaje de forecasts ajustados y aceptados.
- Diferencia entre baseline y forecast final.

### Stock y acciones

- Reducción de roturas.
- Reducción de exceso.
- Mejora de cobertura.
- Ventas recuperadas.
- Porcentaje de recomendaciones ejecutadas.
- Tiempo ahorrado al planner.
- Tiempo desde la alerta hasta la acción.

### Pre-season

- Diferencia entre compra recomendada y compra final.
- Stock sobrante al final de temporada.
- Porcentaje de allocation modificada manualmente.
- Tiempo de preparación de la compra.
- Porcentaje de mercancía llegada tarde o no servible.
- Valor de ventas afectadas por retrasos.

### Validación comercial

- Tiempo hasta el primer valor: objetivo inferior a cuatro semanas.
- Tiempo de integración con una extracción de ERP o Excel.
- Número de decisiones semanales tomadas desde el producto.
- Número de módulos activos por cliente.
- Conversión de piloto a servicio recurrente.

## Decisión final

La priorización recomendada queda así:

1. **Forecast de ventas retail por tienda y talla.**
2. **Seguimiento de ventas y stock.**
3. **Reaprovisionamiento retail.**
4. **Seguimiento básico de llegadas.**
5. **Reagrupaciones y balance de stock.**
6. **Purchase Planning multicanal.**
7. **Collection Flow, clusters y allocation inicial.**
8. **Reaprovisionamiento de almacén y básicos.**
9. **Budget multicanal.**
10. **Markdown y descuentos.**

Esta secuencia permite entrar por un problema muy concreto y validado, sin cerrar la evolución hacia pre-season ni hacia wholesale y e-commerce.

La decisión no es ignorar wholesale. Es evitar construir una lógica mayorista incompleta antes de validar los procesos retail con mayor frecuencia y capacidad de medición. Wholesale debe estar contemplado desde el diseño como un canal diferente y puede convertirse en una segunda propuesta comercial cuando se haya validado la estructura de forecast, compras, clientes y entregas.

La arquitectura de producto debería quedar orientada a este flujo:

```text
Datos multicanal
→ Forecast específico por canal
→ Salud de ventas y stock
→ Acción operativa
→ Compra y llegadas pre-season
→ Allocation y collection flow
→ Budget y optimización avanzada
```

La oportunidad comercial máxima no está en vender una plataforma completa desde el inicio. Está en demostrar que ApplyChain convierte datos imperfectos en decisiones de stock medibles y, a partir de esa base, ampliar hacia la compra multicanal y el pre-season.
