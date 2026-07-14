---
name: comercial-followup
description: Use when the user needs to craft a follow-up message to a commercial contact — second message after no reply, friendly pressure after a meeting, re-engagement after silence. Covers timing, tone, and tactics to move contacts forward in the pipeline.
---

# Comercial Follow-Up — ApplyChain Pipeline Advancement

Use this skill when the user wants to:
- Follow up after a first message got no reply
- Send friendly pressure after a meeting/entrevista
- Re-engage a contact that went silent
- Advance a contact from one status to the next

---

## 1. Pipeline Status Reference

| Status | Meaning | Typical action |
|---|---|---|
| 0. Prospección | Not yet contacted | First outreach |
| 1. Primer mensaje | First message sent, no reply | Follow-up after 2-3 weeks |
| 2. Segundo mensaje | Second message sent, no reply | Final follow-up or pause |
| 3. Reunión entrevista | Meeting done | Friendly pressure follow-up |
| 4. Precontrato | Proposal sent, negotiating | Close-focused follow-up |
| 5. Contrato | Client | Onboarding & delivery |
| 6. Anulado | Dead | Only re-engage with new angle |
| 7. Bloqueado MV | Blocked by Miguel V. | Respect block |

---

## 2. Language & Tone

- **Language hierarchy**: English (primary) → Spanish (secondary) → Catalan (rare, warm local contacts)
- **Tone**: Warm but direct. Assume good intent ("probably busy, not ignoring").
- **Length**: 100-150 words (shorter than first message)
- **Key principle**: Add value or progress update, don't just say "did you see my message?"

---

## 3. Follow-Up Types & When to Use

### Type A: "No reply to first message" (1→2)
**When**: 2-3 weeks after first message with no response
**Tactic**: Short, assume busy, add a new angle or piece of social proof
**Structure**:
1. Gentle reference to first message
2. New info share (progress, client win, article)
3. Softer CTA

### Type B: "Friendly pressure after meeting" (3→4)
**When**: 2-4 weeks after a good meeting with no next step
**Tactic**: Reference the conversation, share progress on your end, create gentle scarcity
**Structure**:
1. Reference the meeting ("since we spoke on [date]")
2. Share what you've been doing (client wins, product progress)
3. Gentle timeline note (not pushy — honest capacity constraint)
4. Open CTA

### Type C: "Re-engage after silence" (2→3 or revive dead)
**When**: 4-8 weeks since last contact, no response to previous messages
**Tactic**: New context/hook (event, news, case study) — don't reference old messages
**Structure**:
1. New context/hook (not "I wrote you before")
2. Brief intro re-cap (in case they forgot)
3. Fresh CTA

### Type D: "Close the deal" (4→5)
**When**: Proposal sent, waiting for decision
**Tactic**: Social proof + timeline scarcity + direct ask
**Structure**:
1. Reference proposal
2. Share relevant case study or result from another client
3. Timeline note (capacity filling up)
4. Direct but respectful ask

### Type E: "Re-contact after redirect" (redirected → same contact)
**When**: Someone redirected you to another person who doesn't respond, or you need to re-engage the original contact with a new angle
**Tactic**: Acknowledge the redirect briefly, then hook with a specific new development (product update, interview insight, pain point). Don't dwell on the failed redirect.
**Channel**: Usually WhatsApp (shorter, more casual)
**Structure**:
1. Brief reminder ("te escribí hace [X] y me comentaste que hablara con [nombre]")
2. New hook — something concrete and specific (module developed, insight from interview, pain point you can solve)
3. Soft CTA ("me encantaría enseñártelo sin compromiso")
**Length**: Max 5 lines on WhatsApp. Less is more.

**Key rules**:
- Don't blame the person who didn't respond ("German no me contestó")
- Frame it as your initiative, not their problem
- Use their language (pain points from interviews, not your service catalog)
- If no response after this, park for 3+ months

---

## 4. The Scarcity Tactic (validated)

This is the most effective friendly pressure pattern for ApplyChain:

> "I'm working with [X companies] on [similar projects]. Because these are custom developments, my delivery timelines are stretching toward [month]. But if we define the scope quickly, I could fit you in before then."

**Key rules**:
- Be honest — only use if real capacity constraints exist
- Name real companies (even if small — "pequeñas pero interesantes")
- Frame as information, not pressure ("por lo que de considerar una propuesta...")
- End with an open question, not a demand

---

## 5. Timing & Cadence

| From → To | Wait time | Notes |
|---|---|---|
| First message → Follow-up Type A | 2-3 weeks | Don't chase too fast |
| Meeting → Friendly pressure Type B | 2-4 weeks | Gives them time to think |
| Last follow-up → Re-engage Type C | 4-8 weeks | New hook required |
| Proposal → Close Type D | 1-2 weeks | Weekly check-ins |

**If no response after Type C**: Move to "6. Anulado" or park for 3+ months.

---

## 6. Examples from Real Use

### Re-contact after redirect (EseOese / Jordi Barba, 2026-07-14)
```
Hola Jordi, ¿qué tal? Soy Diego, te escribí hace unas semanas y me comentaste que hablara con German. Te cuento: hemos desarrollado un módulo de planificación pre-season que creo que encaja muy bien con vuestro modelo de compras one shot. Estaría encantado de enseñártelo un día de estos sin compromiso, a ver qué te parece.
```

### Friendly pressure after meeting (Punt Roma, 2026-07-07)
```
Buenos días Alberto,

Espero que os encontréis muy bien en Punt Roma y que no estéis sufriendo con la ola de calor 😅

Han pasado un par de semanas desde que hablamos y quería retomar el hilo. Estoy trabajando con dos empresas del sector en proyectos de forecasting y los resultados están siendo superinteresantes — sin duda serán muy útiles para lo que también estáis buscando en Punt Roma.

Eso sí, gracias a estos desarrollos los timings de entrega para vuestro proyecto se están estirando hasta mediados de octubre. Por lo que de considerar una propuesta para vosotros, tendré que planificarlo un poco para no dilatar demasiado hasta noviembre.

Decidme qué pensáis, porque si el desarrollo se dinamiza os podría encontrar hueco aprovechando el verano y no dilatarlo tanto. Si os parece podemos hacer una llamada y lo comentamos.

Un saludo,
Diego
```

---

## 7. Variables to ask for

Before writing, ask the user for:
- Current status of the contact (which pipeline stage)
- Time since last interaction
- What was discussed in the last interaction
- Any new developments on Diego's side (client wins, product updates)
- Any market hooks (events, news, trends) to use as context
- Language preference for this specific message

---

## 8. Post-follow-up workflow (automático)

Después de cada follow-up, SIEMPRE:

0. **Usar `id`** para buscar historial previo en contacts.yaml (`data/networking/contacts.yaml`):
   - Buscar por `id` para encontrar el contacto
   - Si no existe `id`, usar el nombre de la empresa como referencia

1. **Actualizar contacts.yaml**:
   - Añadir entrada en `historial`: fecha, tipo (Follow-up), resumen corto
   - Actualizar `ultimo_contacto` con la fecha de hoy
   - Actualizar `status` si avanza de pipeline (ej: 1→2)

2. **NO modificar mensajes anteriores** en el fichero de contacto (`data/comercial_contacts/`):
   - Añadir nueva entrada con formato: `## YYYY-MM-DD — [Canal] a [Nombre]`
   - Mantener historial de mensajes intacto
