---
name: weekly-plan
description: Use when the user asks for their weekly commercial plan, time allocation, or LinkedIn/commercial activities schedule. Generates a personalized weekly plan based on ApplyChain's Challenger methodology, prioritizing contacts over publications as per Diego's preference.
---

# Weekly Commercial Plan — ApplyChain

Use this skill when Diego asks for his weekly plan, time allocation, or commercial activities schedule.

## Default Configuration (Diego's Preference)

**Priority:** More contacts, fewer posts
**Total time:** 3h/week (2 blocks of 1.5h)
**Distribution:** 5 contacts + 1 publication + interaction + follow-ups

## Time Allocation Template

| Activity | Time | Frequency | Notes |
|----------|------|-----------|-------|
| **LinkedIn Publication** | 25 min | 1x/week | High-impact post (insight or Etnia case study). English |
| **Semi-cold Contacts** | 75 min | 5x 15 min | Research + personalized Challenger message |
| **LinkedIn Interaction** | 20 min | 3-5 comments | Comment on relevant posts from sector contacts |
| **Pipeline Follow-ups** | 10 min | 1x/week | Update contacts.yaml, review pending actions |

## Weekly Structure (2 Days)

### Day 1 (e.g., Tuesday) — 1.5h
- 1 LinkedIn publication (25 min)
- 3 semi-cold contacts (45 min)
- 20 min interaction/commentary

### Day 2 (e.g., Thursday) — 1.5h
- 2 semi-cold contacts (30 min)
- 10 min pipeline follow-ups
- *(free time to prepare next week)*

## Pipeline Targets

- **Weekly:** 5 contacts + 1 publication
- **Monthly:** ~20 contacts + 4 publications
- **Year 1 Goal:** 4 consulting clients (€7,000 avg billing)

## When Generating the Plan

1. **Read current pipeline** from `data/networking/contacts.yaml`
2. **Identify next 5 contacts** based on:
   - Pipeline stage (prioritize Stage 1-2: first contact / follow-up)
   - Last contact date (>2 weeks = priority)
   - Tier classification (Tier 1 = personal connections)
3. **Suggest publication topic** based on:
   - Recent sector news or trends
   - Success stories (Etnia Barcelona case)
   - Pain points from current contacts
4. **List pending follow-ups** that need attention
5. **Format output** as a clean weekly agenda

## Output Format

```
## Plan Semanal [Date Range]

### Prioridades de la Semana
1. [Contact 1] — [Company] — [Stage] — [Action]
2. [Contact 2] — [Company] — [Stage] — [Action]
...

### Publicación LinkedIn
- **Tema:** [Suggested topic]
- **Enfoque:** [Insight/Case study/Ref frame]
- **CTA:** [Conversation starter]

### Seguimientos Pendientes
- [Contact] — [Last action] — [Recommended next step]

### Tiempo Asignado
- Martes: 1.5h (publicación + 3 contactos + interacción)
- Jueves: 1.5h (2 contactos + seguimientos)
```

## Variables to Consider

Before generating the plan, check:
- Current pipeline status (contacts.yaml)
- Recent LinkedIn activity (linkedin_get_own_posts)
- Upcoming events or deadlines
- Seasonal factors (buying seasons, trade shows)
- Any blocked contacts needing re-engagement

## Adjustments

Diego can request adjustments:
- **More contacts, fewer posts:** Increase to 6-7 contacts, keep 1 post
- **More posts, fewer contacts:** 2 posts, 3-4 contacts
- **More time:** Increase to 4-5h/week (3 blocks)
- **Less time:** Minimum 2h/week (2 posts, 3 contacts, no interaction)

Always ask for confirmation before applying major changes to the template.
