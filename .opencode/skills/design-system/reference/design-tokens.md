# ApplyChain Design Tokens

Extracted from Figma file `ApplyChain_design_system` and current frontend implementation.

## Figma Reference

- File key: `ljfTBtVWqRzcUg9Krk1Yhd`
- Reference node: `26-2`
- URL: `https://www.figma.com/design/ljfTBtVWqRzcUg9Krk1Yhd/ApplyChain_design_system?node-id=26-2`

## Colors

| Figma style | Alias | Hex | Notes |
| --- | --- | --- | --- |
| `Neutral/0` | `White` | `#FFFFFF` | Card backgrounds and inverse text |
| `Neutral/100` | `Desert Storm` | `#F8F7F7` | Light surface and icon fill |
| `Neutral/900` | `Dark Space` | `#102131` | Primary dark text and dark surfaces |
| `Primary/500` | `Bayou` | `#11AFC3` | Main brand color |
| `Primary/700` | `Egyptian Teal` | `#0E848A` | Hover, chart lines, secondary brand elements |
| `Primary/900` | `Teal Blue` | `#014152` | Badge text, labels, deep teal surfaces |
| `Primary/950` | none | `#042324` | Existing dashboard gradient endpoint |
| `Accent/Warm` | `Honey` | `#EAA83B` | CTA, highlight, warning/review |
| none | `Accent/Warm/Dark` | `#845F21` | Warm gradient endpoint |
| `Error/400` | `Cinnabar` | `#EC462E` | Moderate alert and thresholds |
| `Error/600` | `Glossy Red` | `#D60300` | Critical risk and severe errors |
| none | `Success/400` | `#28A745` | Positive/on-track state from current implementation |
| none | `Chart/Area` | `#ECF3F5` | Metric chart area fill from current implementation |
| none | `Border/Default` | `#E7E6E6` | Metric card border from current implementation |

## Gradients

| Token | CSS |
| --- | --- |
| `Gradient/Primary` | `linear-gradient(135deg, #0E848A 0%, #042224 100%)` |
| `Gradient/Warm` | `linear-gradient(135deg, #EAA83B 0%, #845F21 100%)` |
| `Gradient/Metrics` | `linear-gradient(180deg, #11AFC3 34.48%, #FFFFFF 83.65%)` |
| `Desert storm - Honey` | `linear-gradient(135deg, #F8F7F7 38.46%, #EAA83B 95.67%)` |
| `Bayou - Egyptian Teal` | `linear-gradient(135deg, #11AFC3 2.88%, #0E848A 95.67%)` |
| `Teal Blue - Dark Space` | `linear-gradient(135deg, #014152 0%, #102131 100%)` |

## Typography

| Style | Font | Weight | Size | Line height | Letter spacing |
| --- | --- | --- | --- | --- | --- |
| `Title Hero` | Montserrat | 700 | 72px | 86.40px | -2.16px |
| `Title Page` | Montserrat | 700 | 48px | 57.60px | -0.96px |
| `Subtitle` | Montserrat | 400 | 32px | 38.40px | 0 |
| `Heading` | Montserrat | 500 | 24px | 28.80px | -0.48px |
| `Subheading` | Montserrat | 400 | 20px | 24px | 0 |
| `Body base` | Montserrat | 400 | 16px | 22.40px | 0 |
| `Body Strong` | Montserrat | 500 | 16px | 22.40px | 0 |
| `Body Emphasis` | Montserrat | 400 | 16px | 22.40px | 0 |
| `Body Link` | Montserrat | 400 | 16px | 22.40px | 0 |
| `Body Small` | Montserrat | 400 | 14px | 19.60px | 0 |
| `Body Small Strong` | Montserrat | 500 | 14px | 19.60px | 0 |
| `Body Code` | Roboto Mono | 400 | 16px | 20.80px | 0 |

## Metric Card Figma Node `26-2`

| Element | Font | Weight | Size | Line height | Color |
| --- | --- | --- | --- | --- | --- |
| Main title | Montserrat | 600 | 20px | 24.38px | `#102131` |
| Current status | Montserrat | 700 | 24px | 29.26px | `#102131` |
| Badge text | Montserrat | 600 | 16px | 19.50px | `#014152` |
| Threshold value | Montserrat | 400 | 15px | 18.28px | `#EC462E` |
| Axis label | Montserrat | 400 | 9px | 10.97px | `#014152` |

## Common Dimensions

| Token | Value | Usage |
| --- | --- | --- |
| `radius.card` | `12px` | Metric cards, dashboard shell, icon containers |
| `radius.badge` | `4px` | Compact status badges |
| `metric-card.width` | `213px` | Figma metric card width |
| `metric-card.height` | `262px` | Figma metric card height |
| `metric-icon.size` | `58px` | Metric icon container |
| `dashboard-filter.size` | `47px` | Dashboard filter action |
| `chart.width` | `173px` | Metric mini-chart width |
| `chart.height` | `72.5px` | Metric mini-chart height |

## Shadows And Borders

| Token | Value | Usage |
| --- | --- | --- |
| `border.default` | `1px solid #E7E6E6` | Metric card border |
| `shadow.card-extended` | `0 1px 50px rgba(0, 0, 0, 0.08)` | Figma extended card shadow |
| `shadow.dashboard` | `0 4px 4px rgba(0, 0, 0, 0.25)` | Existing dashboard container |

## Status Rules

| Status | Rule | Background | Text |
| --- | --- | --- | --- |
| `on-track` | `value >= 90` | `#28A745` | `#014152` |
| `review` | `threshold <= value < 90` | `#EAA83B` | `#014152` |
| `alert` | `value < threshold` | `#EC462E` | `#014152` |
