---
name: design-system
description: Use when designing or modifying UI, frontend components, CSS, Tailwind config, React visual components, dashboards, metric cards, layouts, colors, typography, spacing, icons, gradients, or Figma-derived visuals for ApplyChain/Replenish Engine.
---

# ApplyChain Design System

Use this skill for every task that touches product design, UI implementation, frontend styling, visual components, dashboards, charts, icons, color, typography, spacing, layout, or design fidelity.

## Source Of Truth

- Primary source: Figma file `ApplyChain_design_system`.
- Figma URL: `https://www.figma.com/design/ljfTBtVWqRzcUg9Krk1Yhd/ApplyChain_design_system?node-id=26-2`.
- Current implementation references: `frontend/components/DashboardLayout.tsx`, `frontend/components/MetricCard.tsx`, `frontend/tailwind.config.cjs`.
- Token reference: `reference/design-tokens.md` in this skill.
- Figma local variables endpoint was not accessible with the current token scope, so these tokens are derived from Figma file styles, the documented node `26-2`, and existing implementation.
- For design tasks, consult Figma first whenever credentials and a file/node URL are available. If Figma cannot be accessed, use this skill as the fallback source and state the limitation.

## Mandatory Behavior

- Prefer existing design tokens over new colors, sizes, shadows, fonts, or gradients.
- Preserve the ApplyChain visual language: clean executive analytics, teal-based brand palette, warm accent highlights, white cards, compact KPI surfaces, and high-fidelity Figma-inspired spacing.
- Prefer every component, pattern, token, and visual rule that already exists in the Figma design system before creating a new variant.
- Use `Montserrat` as the primary UI typeface unless the existing component or brand mark explicitly uses another font.
- Use `Outfit` only for the existing brand wordmark pattern unless the user explicitly asks to expand brand typography.
- Do not introduce arbitrary colors such as generic Tailwind blues, grays, reds, or yellows when a design-system token exists.
- Keep UI changes consistent with existing React patterns in this project: functional components, inline styles where the component already uses inline styles, and minimal abstractions.
- If a requested design requires a missing token, ask a concise clarification instead of inventing a new design direction.
- Design new product screens desktop first. Add mobile adaptations when requested or when a change would clearly break basic usability on smaller viewports.
- For pixel-perfect Figma ports, preserve exact dimensions and positions when the current component intentionally follows Figma. For responsive product screens, keep the desktop composition as the primary layout and adapt down only where needed.

## Color Tokens

Use semantic names when explaining design decisions. Use exact hex values in implementation unless the project has centralized tokens available.

| Token | Hex | Usage |
| --- | --- | --- |
| `White` / `Neutral/0` | `#FFFFFF` | Card backgrounds, inverse text, SVG strokes on dark surfaces |
| `Neutral/100` / `Desert Storm` | `#F8F7F7` | Light neutral fills, secondary icon fills, subtle surfaces |
| `Neutral/900` / `Dark Space` | `#102131` | Main dark text, executive dashboard dark surfaces |
| `Primary/500` / `Bayou` | `#11AFC3` | Main brand color, primary buttons, active filters, icon backgrounds |
| `Primary/700` / `Egyptian Teal` | `#0E848A` | Hover states, chart lines, secondary brand elements, borders |
| `Primary/900` / `Teal Blue` | `#014152` | Badge text, axis labels, deep teal surfaces |
| `Primary/950` | `#042324` | Dark dashboard gradient endpoint, premium dark backgrounds |
| `Accent/Warm` / `Honey` | `#EAA83B` | CTAs, highlights, important metrics, review/warning badges |
| `Accent/Warm/Dark` | `#845F21` | Warm gradient endpoint |
| `Error/400` / `Cinnabar` | `#EC462E` | Moderate alerts, threshold lines, attention badges |
| `Error/600` / `Glossy Red` | `#D60300` | Critical risk, stockout, severe errors |
| `Success/400` | `#28A745` | Positive/on-track status badges |
| `Chart/Area` | `#ECF3F5` | Metric card mini-chart area fill |
| `Border/Default` | `#E7E6E6` | Light card border |

## Gradients

- `Gradient/Primary`: `linear-gradient(135deg, #0E848A 0%, #042224 100%)`.
- Existing dashboard background overlays `Primary/500` at 3% over `Gradient/Primary` at 96% opacity:

```css
linear-gradient(rgba(17, 175, 195, 0.03), rgba(17, 175, 195, 0.03)),
linear-gradient(135deg, rgba(14, 132, 138, 0.96) 0%, rgba(4, 35, 36, 0.96) 100%)
```

- `Gradient/Warm`: `linear-gradient(135deg, #EAA83B 0%, #845F21 100%)`.
- `Gradient/Metrics`: `linear-gradient(180deg, #11AFC3 34.48%, #FFFFFF 83.65%)`.
- `Desert storm - Honey`: `linear-gradient(135deg, #F8F7F7 38.46%, #EAA83B 95.67%)`.
- `Bayou - Egyptian Teal`: `linear-gradient(135deg, #11AFC3 2.88%, #0E848A 95.67%)`.
- `Teal Blue - Dark Space`: `linear-gradient(135deg, #014152 0%, #102131 100%)`.

## Typography

- Primary UI font: `Montserrat, sans-serif`.
- Brand wordmark pattern: `Outfit, Montserrat, sans-serif` when matching existing `ApplyChain` footer branding.
- Code font: `Roboto Mono, monospace` only for code-like content.
- Use the typography scale in `reference/design-tokens.md`.
- Existing metric-card typography to preserve:
- Main title: Montserrat 600, 20px, 24.38px line-height, `Neutral/900`.
- Current status: Montserrat 700, 24px, 29.26px line-height, `Neutral/900`.
- Badge text: Montserrat 600, 16px, 19.50px line-height, `Primary/900`.
- Threshold value: Montserrat 400, 15px, 18.28px line-height, `Error/400`.
- Axis label: Montserrat 400, 9px, 10.97px line-height, `Primary/900`.
- Existing dashboard title: Montserrat 700, 32px, 39.01px line-height, `Accent/Warm`.

## Spacing, Radius, Shadows

- Default card radius: `12px`.
- Compact badge radius: `4px`.
- Existing dashboard shell radius: `12px`.
- Metric card size: `213px x 262px` when reproducing the Figma KPI card.
- Metric icon container: `58px x 58px`, radius `12px`, `Primary/500` fill, `Primary/700` border.
- Dashboard filter button: `47px x 47px`, radius `12px`, `Primary/500` fill.
- Existing card border: `1px solid #E7E6E6`.
- Figma extended card shadow: `0 1px 50px rgba(0, 0, 0, 0.08)`.
- Existing dashboard shadow: `0 4px 4px rgba(0, 0, 0, 0.25)`.

## Component Guidance

- KPI/metric cards should use white surfaces, dark text, teal chart lines, light chart area fills, and semantic status badges.
- Dashboard backgrounds should prefer dark teal gradients with warm accent headings.
- Badges should use these states unless the user gives a different product rule:
- `on-track`: background `Success/400`, text `Primary/900`, typically `value >= 90`.
- `review`: background `Accent/Warm`, text `Primary/900`, typically `threshold <= value < 90`.
- `alert`: background `Error/400`, text `Primary/900`, typically `value < threshold`.
- Charts should use `Primary/700` for positive/primary lines and `Error/400` for thresholds or risk lines.
- Icons should use brand teal surfaces with `Neutral/100` or `White` internal glyphs unless a specific semantic status is required.

## Implementation Rules

- Before editing UI, inspect nearby components and reuse their styling approach.
- Before designing or editing UI, attempt to consult the relevant Figma file/node first. Use local code and this skill to resolve implementation details after checking Figma.
- If the project has centralized tokens, update or reuse them. If not, keep token constants local and named clearly, as current components do with `C` and `T` objects.
- Do not migrate the styling architecture unless the user explicitly asks for that refactor.
- Tailwind may be used where already appropriate, but do not replace existing inline Figma-port styles solely for preference.
- Use desktop-first responsive behavior for new screens. Fixed Figma coordinates are acceptable only for components explicitly intended as pixel-perfect previews.
- Use accessible contrast. If a requested color combination appears low contrast, flag it and choose the closest design-system-safe alternative.
- If a requested UI element is not visible in Figma or cannot be matched to an existing design-system component, ask before inventing it.

## Ask For Clarification When

- The task needs a new color, gradient, typography role, icon style, breakpoint, motion pattern, or spacing scale not present here.
- The task needs a button, input, table, modal, navigation pattern, chart type, card variant, or form control that is not present or identifiable in Figma.
- The user asks for a visual change that conflicts with Figma tokens or current implementation.
- The UI target is unclear: pixel-perfect Figma reproduction vs responsive production component.
- A Figma node or page is referenced but no file/node URL is provided.

## Maintenance Notes

- When Figma tokens change, refresh this skill from the Figma file and update `reference/design-tokens.md`.
- To access Figma local variables through the REST API, the token needs `file_variables:read` scope.
- After editing this skill, restart OpenCode so the running session loads the updated instructions.
