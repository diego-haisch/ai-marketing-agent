# Serie: Building an AI Forecasting Engine for Fashion Retail
Fecha: 2026-09-15
Estado: Propuesta documentada — pendiente planificación puesta en marcha
Valoración: 8,5/10 como estrategia para ApplyChain

## 1. Idea central
No: "He hecho un modelo de forecasting para una empresa de moda" (genérico).
Sí, historia: "¿Por qué hacer forecasting en moda es bastante más difícil de lo que parece?"

Historia de transformación: forecasting tradicional → forecasting retail → ML/IA → problemas reales → decisiones de modelización → aprendizajes.
Más potente para marca personal que enseñar una pantalla de Power BI.

Demanda en moda condicionada por: ciclo de vida producto, promociones, rebajas, stock disponible, temporada.

## 2. Tres audiencias simultáneas
A. Cliente potencial ApplyChain (Supply, Demand Planning, Planning Manager, Retail Director):
Reconoce problemas, no necesita entender Random Forest: promociones, temporadas, rebajas, stockouts, tiendas, cientos/miles SKUs, diferencias entre canales, cambios comportamiento, necesidad reaccionar rápido.

B. Profesional técnico (Data Scientist, ML Engineer, Demand Planner):
Problemas reales ML aplicado a Supply: feature engineering, variables promocionales, temporalidad, lifecycle, modelos globales vs por SKU, train/test temporal, métricas, backtesting, cold start, stockouts, demanda censurada, forecasting jerárquico, interpretabilidad, automatización pipeline.

C. Marca personal Diego:
"Soy alguien que sabe unir negocio + Supply Chain + datos + IA". No "el chico que programa modelos", sino "Diego entiende Supply Chain y además sabe convertir esos problemas en soluciones tecnológicas".

## 3. Mini-serie propuesta (no un único contenido)
1. El problema — "Forecasting en moda: ¿por qué no es simplemente predecir ventas del próximo mes?" (temporada, lifecycle, promos, rebajas, Black Friday, stockouts, canales, tiendas). Audiencia negocio. LinkedIn.
2. Sales ≠ Demand — "Una venta que no ocurre no siempre significa que no había demanda". Ej: Forecast 10, stock 2, ventas 2 → demanda real 10. Demand ≠ Sales, stockout / censored demand visual. LinkedIn + vídeo.
3. Promociones — "¿Qué ocurre cuando el precio cambia y el modelo no lo sabe?" Precio normal → pico promo → caída. Variables discount/markdown/promotion/price/event. Gráfico anonimizado. LinkedIn.
4. Ciclo de vida — Launch → Growth → Peak → Markdown → End of life. Carrusel.
5. Escala — 20 SKUs vs cientos productos × decenas tiendas × canales. Dilema modelo por SKU vs modelo global, aprendizaje compartido. LinkedIn.
6. ¿ML o estadística? — "La pregunta no es qué algoritmo es más moderno, sino qué información tenemos y qué problema queremos resolver". YouTube.
7. El modelo — Input (SKU, Store, Date, Price, Discount, Season, Lifecycle, Sales, Stock...) → Feature engineering → Model → Forecast → Business decision. Arquitectura. YouTube.
8. Cómo evaluar — "Un forecast con MAE 3, ¿es bueno o malo?" Depende: WMAE, MAPE, WAPE, bias, error por SKU/volumen/promos/lifecycle. LinkedIn + YouTube.
9. El modelo no funcionaba — qué probé, qué esperaba, qué ocurrió, qué descubrí, qué cambié. LinkedIn.
10. Qué aprendí — Todos. LinkedIn.
11. De forecast a replenishment — Negocio. YouTube.
12. Qué significa realmente "AI forecasting" — Todos. LinkedIn.

## 4. Regla confidencialidad
Puedes enseñar: datos artificiales, normalizados, gráficos conceptuales, screenshots sin identificativos, arquitecturas, código simplificado, ejemplos ficticios, métricas agregadas, problemas, decisiones, aprendizajes.
NO enseñar: nombre cliente, logos, cifras/ventas reales, SKUs, tiendas, márgenes, precios reales, calendario comercial identificable, resultados identificables.
Añadir disclaimer: "Por motivos de confidencialidad, datos y ejemplos ficticios o anonimizados." Transmite profesionalidad.

## 5. Narrativa "lo que pensaba vs lo que encontré"
"Cuando empecé pensaba que el problema era X → apareció Y → tuve que cambiar Z."
Ej: "Mi primera intuición era que el reto sería elegir algoritmo. Me di cuenta de que el algoritmo era casi lo de menos. El problema estaba en cómo representar la realidad del negocio." Transmite madurez. Contenido experiencia, no Wikipedia.

## 6. Tesis posicionamiento
"La IA aplicada a Supply Chain no empieza con el algoritmo. Empieza entendiendo el proceso."
Recorrido Diego: Supply Chain → Demand Planning → Data → BI → ML → producto. Esa es la ventaja.

## 7. LinkedIn vs YouTube
LinkedIn: 500-1000 palabras, gráficos, vídeos cortos, reflexiones, casos, aprendizajes, preguntas. Objetivo: "Quiero que un potencial cliente piense en Diego."
YouTube: 8-15 min profundo, ej "Cómo construir sistema forecasting fashion retail: 7 problemas que tuve que resolver" (arquitectura, datos, features, modelos, evaluación, decisiones). Objetivo: evidencia de que sabe hacerlo.
Se alimentan mutuamente.

## 8. Visual sencillo reutilizable
Esquema FASHION FORECASTING: DEMAND → SEASON/PRICE/STOCK → Lifecycle/Discount/Stockout → ML FORECAST → BUSINESS DECISION.
Reutilizar como carrusel, miniatura, slide, imagen artículo, material comercial. Una pieza → cinco activos.

## 9. Bibliografía con moderación
Cerrar algunos posts con Further reading: Hyndman & Athanasopoulos, Deep Learning for Time Series, intermittent/censored demand, docs XGBoost/LightGBM/sklearn, artículos retail forecasting.
Efecto: "No sólo cuenta experiencia; sabe dónde está el conocimiento." Edelman/LinkedIn: compradores valoran contenido con investigación, problemas concretos y casos accionables.

## 10. Lo que NO hacer
No: "Hoy os explico Random Forest", "5 ventajas IA en Supply", "La IA está revolucionando forecasting", "En ApplyChain tenemos solución innovadora...". Contenido consultora genérica.
Sí: "Estoy haciéndolo ahora. Esto es lo que estoy descubriendo." Más creíble.
No vender ApplyChain en cada post. Solo: "Proyecto que estoy desarrollando desde ApplyChain." Objetivo que lleguen solos a "Este tío sabe". Thought leadership más fiable que material comercial para evaluar proveedor.

## 11. Documentar fracasos
"El modelo no mejoraba. Así que dejé de tocar el modelo." Oro técnico vs miles de "I built amazing AI model 🚀". Pocos cuentan: "El modelo tenía error enorme. Estas fueron las 3 cosas que descubrí." Genera credibilidad.

## 12. Diario técnico (8 semanas)
W1 Understanding problem, W2 stockout, W3 promos y elasticidad, W4 feature engineering, W5 choosing model, W6 backtesting, W7 why first results weren't good enough, W8 from forecast to replenishment.
Ventaja: cada semana da material, no hay que inventar qué publicar.

## 13. Valor comercial
En 6 meses, LinkedIn con 10-15 piezas demuestra resolución problemas reales. Llega a CEO (negocio), Supply Director (operativa), Demand Planner (forecasting), Data/IT (técnica), Data Scientist (ML aplicado). Thought leadership ayuda a reconsiderar problema y evaluar proveedores nuevos aunque no busquen activamente.

## Siguiente paso
Diseñar juntos serie desde cero: concepto/nombre definitivo, 10-12 episodios, reparto LinkedIn vs YouTube, gráficos necesarios, y guion episodio 1 para que no parezca post técnico más.
Relación con estrategia_comunicacion: encaja en "problemas antes que funcionalidades" y método 7 pasos (Big Idea → guion).
