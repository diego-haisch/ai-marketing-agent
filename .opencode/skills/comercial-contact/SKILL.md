---
name: comercial-contact
description: Use when the user wants to craft a commercial outreach message (email/LinkedIn) for ApplyChain. Covers writing first-contact messages to potential clients in fashion/retail, using the validated Surkana-style approach. Emphasizes AI sales forecasting as primary value prop, with PowerBI as secondary visibility layer.
---

# Comercial Contact – ApplyChain Outreach

Use this skill when the user asks you to write or revise a commercial contact message for ApplyChain.

## Tone & structure

- **Language**: Spanish (default for all work and commercial outreach)
- **Length**: ~150-170 words
- **Style**: Conversational, not salesy. Direct and brief. No markdown formatting in the final message body.
- **Target**: CEO, COO, Supply Chain Manager, Demand Planning Manager, Director/a de compras of fashion/retail SMEs

## Positioning strategy

Prioritize the message based on the target's profile:

- **Operations/buying profiles** (Supply Chain Manager, Demand Planner, Head of Buying): lead with **AI sales forecasting**. PowerBI is secondary — "it provides visibility, but the core is the ability to predict, not just measure".
- **CEO/General Management profiles**: balance forecasting with business impact (buy better, less capital tied up, higher turnover).
- **Cross-cutting key message**: AI forecasting is no longer exclusive to large corporations. SMBs in fashion/retail can access it and get immediate ROI.

Choose language: Spanish (default for all work and commercial outreach).

## Message structure (template)

Use Spanish as the default language. The structure below:

1. **Brief intro of Diego**: "He pasado mi carrera optimizando operaciones, y evolucioné hacia la creación de herramientas de software para la gestión diaria. Eso me llevó a crear ApplyChain."
   - Keep very short (2-3 lines max)
   - Emphasize: operations background → software tools evolution

2. **What ApplyChain does**: Consultoría especializada en supply chain e IA para moda y retail.

3. **Reference mention** (when applicable): "[Nombre] me sugirió que te contactara — pensé que podría interesarte."
   - Place naturally, not as the opening line

4. **Core value prop — AI forecasting** (primary):
   - AI-powered sales forecasting by SKU and store enables precision buying
   - Avoids overstock in some locations and stockouts in others
   - Smart redistribution across channels (retail, franchise, wholesale)
   - **Key phrase**: "comprar mejor, vender más con menos capital atado"
   - Emphasize: this is now accessible to SMBs, not just enterprise

5. **Power BI** (secondary/enabling):
   - Power BI provides visibility, but the real value is the ability to predict
   - For operations-focused targets: mention Power BI briefly, keep focus on forecasting
   - For CEO-level: can give Power BI slightly more weight as a management tool

6. **Approach**: Practical, no bureaucracy. Diagnose, implement custom predictive models, train teams for autonomy.

7. **Specific problems** (bullet list, tailored to target's profile):
   - Inaccurate initial buys due to lack of reliable forecast
   - Difficulty redistributing stock across channels
   - No visibility into profitability by SKU, store, or channel
   - Reactive discount planning instead of proactive pricing
   - (Adjust bullets based on company specifics)

8. **CTA**: Open invitation for a brief conversation to understand their reality and share similar cases.

## Supporting materials

- **Website**: www.applychain.es — SIEMPRE consultar antes de redactar mensajes para tener info actualizada de servicios, casos y propuesta de valor
- Commercial presentations (PPTX) in `producto/presentaciones/` — use for case studies, examples, client data
- Commercial intelligence playbook in `.opencode/skills/comercial-intelligence/` — check for evolving strategy, hooks, and target priorities
- Weekly plans in `comercial/planes_semanales/` — see what was done and what's coming

## WhatsApp-specific approach

WhatsApp is a valid channel for re-contacts and warm leads. Rules differ from email/LinkedIn:

- **First message on WhatsApp**: Max 2-3 lines. No pitch. Just establish connection and open conversation.
- **Re-contact after redirect**: Reference the previous conversation briefly, then hook with a specific pain point or new development. Never send long messages to strangers.
- **Tone**: Casual, like writing to a friend of a friend. No formal greetings, no "Estimado".
- **Pain point hook**: Use specific operational language the target would recognize ("modelo one shot", "clusterización manual", "stock dormido"). Avoid generic terms like "forecasting con IA".
- **Rule of thumb**: If the message is longer than 5 lines on WhatsApp, it's too long.

### Re-contact message structure (WhatsApp)
1. Brief reminder of connection ("te escribí hace unas semanas", "hablé con [nombre]")
2. Specific hook based on known pain points (from interviews, intel, or previous conversations)
3. Soft CTA ("me encantaría enseñártelo sin compromiso")

## Using interview pain points

When we have interview data from a company, use the specific pain points identified — they're gold for targeted messaging. Reference the problems in their language, not ours.

Example: Instead of "forecast con IA por SKU", say "lo del modelo one shot y la clusterización manual" — that's how THEY describe it.

## Post-contact workflow (automático)

Después de escribir un mensaje o averiguar info nueva de un contacto, SIEMPRE:

0. **Verificar `id`** en contacts.yaml (`comercial/pipeline.yaml`):
   - Si existe → usarlo como referencia en el fichero de contacto
   - Si no existe → preguntar al usuario y añadirlo
   - Formato en fichero contacto: `id: [ID]` en la primera línea del frontmatter

1. **Actualizar contacts.yaml**:
   - Añadir/modificar campos: nombre, rol, LinkedIn, empresa, sector
   - Actualizar `ultimo_contacto` con la fecha de hoy
   - Actualizar `status` si cambia
   - Añadir entrada en `historial` con fecha, tipo y resumen

2. **NO modificar mensajes anteriores** en el fichero de contacto (`comercial/contactos/`):
   - Mantener el mensaje modelo original
   - Añadir nueva entrada con formato: `## YYYY-MM-DD — [Canal] a [Nombre]`
   - Ejemplo: `## 2026-07-14 — LinkedIn a Paco Sánchez (CEO)`

## Variables to ask for

Before writing, ask the user for:
- Target company name and profile (price segment, channels, product type)
- Contact person name and position (if known)
- Reference / common contact (if any)
- Any specific known challenges of the company
- Whether we have interview data with this company (check `inteligencia/entrevistas/`)
- Preferred channel (email, LinkedIn, WhatsApp)

## Tone notes

- Discovery-oriented: "No intento venderte nada, quiero entender tu realidad"
- Solutions-focused, not feature-dump
- Avoid jargon unless specific to fashion/retail operations
- Maintain same tone across all messages
- On WhatsApp: extra casual, shorter, no markdown
