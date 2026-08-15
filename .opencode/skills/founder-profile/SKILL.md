---
name: founder-profile
description: Use when you need to know who Diego Haisch (ApplyChain founder) is, his background and strengths, how he approaches a project, or how he applies AI and AI agents in his work — e.g. to write a CV, cover letter, commercial outreach, LinkedIn post, or any document in his voice. Also use to recall ApplyChain positioning, his micro1 application narrative (Q4–Q7 answers), pricing stance, and the honest-RLHF rule.
---

# Perfil del fundador — Diego Haisch

## Quién es

- Fundador de **ApplyChain** (desde 2025): consultora de supply chain + inteligencia artificial para pymes de moda, calzado, accesorios y retail.
- 10+ años en demand planning, forecasting y analítica en retail de moda: **Mango, Desigual, Inditex/Lefties, Etnia Barcelona**.
- Últimos roles: **Data Science Manager** en Etnia Barcelona (ago 2024 – nov 2025) y **Senior Demand Planner – BI Analyst** (ago 2021 – ago 2024).
- Formación: Ingeniería Industrial (Universidad Católica Boliviana), Master en Supply Chain Management (La Salle – Ramon Llull), Data Science Professional Certificate (IBM/Coursera).
- Idiomas: español (nativo), inglés (avanzado), catalán (intermedio alto), alemán (intermedio).

## Background profesional — hit points

- **Etnia Barcelona**: lideró el equipo de Data Science (SQL, Azure, Power BI); mejoró la precisión del forecast global de reaprovisionamiento hasta el **77%**; definió requirements para proveedores y presentaciones para "vender" proyectos internamente; creó el modelo semántico central de reporting de la empresa.
- **ApplyChain**: construye productos de IA end-to-end — Forecast in-season (Random Forest, nivel SKC), Replenishment Engine multi-SKU/tienda, Collection Flow pre-season, reporting conversacional.
- Roles anteriores: presupuestos y estrategia de merchandising, controlling (Inditex), demand planning (Desigual, Mango).

## Cómo encara un proyecto (metodología)

1. **Entender el problema de negocio del cliente primero** — nunca features genéricas.
2. **Diagnóstico rápido** → implementar un MVP funcional en semanas (time-to-value < 4 semanas).
3. **Documentar las decisiones** en ADR (Architecture Decision Records) y specs antes de implementar.
4. **Iterar con métricas**: MAE, wMAE, RMSE, BIAS, forecast accuracy, rotura de stock.
5. **Entregar con formación** para que el equipo del cliente sea autónomo.

## Cómo aplica IA en los proyectos

- **Full-stack**: backend Python/FastAPI/PostgreSQL, frontend React/TypeScript/Tailwind, capa de reporting Power BI/DAX.
- **Desarrollo agentic**: VS Code + opencode con múltiples agentes, skills reutilizables, MCP servers, versionado en GitHub (branching, review, artefactos reproducibles).
- **Harness engineering**: AGENTS.md, skills, convenciones y contratos de test que convierten la necesidad de negocio en tareas acotadas que los agentes ejecutan y consolidan en un proyecto potente y coherente.
- **Flujo de prompts (Q7)**: revisar si existe una skill que cubra el conocimiento general → escribir el prompt con necesidad + procedimiento + objetivo → pedir al agente specs/ADR → revisar las specs a detalle para detectar desviaciones → validar → implementar.
- **Evaluación de salidas IA**: evalúa código, contenido y modelos contra rúbricas (correctitud, rendimiento, alineación con negocio, claridad) antes de liberar.

## Cómo redactar contenido en su voz

- Directo, conciso, orientado a soluciones, sin humo técnico ni capas burocráticas.
- **Español por defecto**; **inglés** para candidaturas internacionales (micro1).
- Mensajes comerciales de 150–170 palabras.
- Enmarcar siempre en el **problema concreto del cliente**, no en features.
- Tono de "gente de operaciones": alguien que habla el idioma del negocio.

## Posicionamiento comercial (ApplyChain)

- Implementación rápida, sin burocracia; soluciones prácticas que se usan, no sistemas que nadie toca.
- Propuesta principal: **forecasting con IA** (valor primario) + **Power BI** como capa de visibilidad.
- Fuente de verdad de servicios/valor: **www.applychain.es** (consultar siempre antes de redactar contenido comercial).

## Candidatura micro1 (ago 2026)

- Roles: **AI Consulting Domain Expert** y **AI Data Science Domain Expert** (remoto, part-time contractor, $100–200/h).
- **Tarifa objetivo: $150/h (~€138)**; mín. aceptable $120–130; anclar $175–200 si hay negociación.
- **Wording honesto**: NO afirmar experiencia formal en RLHF. Usar "AI output evaluation and feedback loops". Su experiencia real: evalúa salidas de IA, revisa/edita código y documentos, anota y fact-check.
- Respuestas **Q4–Q7**: en `src/create_presentation/cv_data.py` (`APPLICATION_QA`) y como anexo en el CV .docx/.pdf.
- Debilidades a compensar al redactar: sin consultoría estratégica formal estilo big-four; ML práctico (no investigación); sin anotación formal RLHF; perfil "builder" más que "grader" → enfatizar evaluación, edición y QA, y mitigar los gaps de ML/estadística.

## Datos de contacto

- Email: diegohaisch@gmail.com · Tel: +34 650 969 382 · Alella (Barcelona)
- LinkedIn: linkedin.com/in/diego-haisch-32a76136

## Fuentes

- CV maestro: `estrategia/cv_fundador.md`
- CV adaptado micro1 (md/pdf/docx): `comercial/contactos/2026-08-15_micro1_ai_expert_cv.*`
- Productos y specs: `producto/*.md`, `producto/specs/`
- Estrategia: `estrategia/business_plan.md`, `estrategia/descripcion_empresa.md`
