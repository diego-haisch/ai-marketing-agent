"""Build the CV HTML applying the ApplyChain design system tokens."""

import html

from . import cv_data
from .tokens import BORDER, COLORS, FONTS, GRADIENTS, RADIUS, SHADOW

C = COLORS


def _esc(value: str) -> str:
    return html.escape(value, quote=False)


def _chips(items, hot: bool = False) -> str:
    parts = []
    for item in items:
        cls = "chip hot" if hot else "chip"
        parts.append(f'<span class="{cls}">{_esc(item)}</span>')
    return "".join(parts)


def _contact_strip() -> str:
    items = [
        ("Location", cv_data.PROFILE["contact"]["location"]),
        ("Phone", cv_data.PROFILE["contact"]["phone"]),
        ("Email", cv_data.PROFILE["contact"]["email"]),
        ("LinkedIn", cv_data.PROFILE["contact"]["linkedin"]),
    ]
    parts = "".join(
        f'<div class="c-item"><span class="c-lbl">{label}</span>'
        f'<span class="c-val">{_esc(value)}</span></div>'
        for label, value in items
    )
    return f'<div class="contact-strip">{parts}</div>'


def _competency_cell(groups) -> str:
    blocks = []
    for group in groups:
        blocks.append(
            '<div class="comp-cat">'
            f'<div class="comp-cat-name">{_esc(group["name"])}</div>'
            f'{_chips(group["items"], hot=group.get("hot", False))}'
            "</div>"
        )
    return "".join(blocks)


def _competencies_card() -> str:
    groups = cv_data.COMPETENCY_GROUPS
    left = groups[:4]
    right = groups[4:]
    return (
        '<div class="card">'
        '<div class="section-title">Core Competencies</div>'
        '<table class="two-col"><colgroup>'
        '<col style="width:50%"><col style="width:50%">'
        "</colgroup><tr>"
        f"<td>{_competency_cell(left)}</td>"
        f"<td>{_competency_cell(right)}</td>"
        "</tr></table>"
        "</div>"
    )


def _languages_block() -> str:
    blocks = ["<h4 class='sub-title'>Languages</h4>"]
    for lang in cv_data.LANGUAGES:
        blocks.append(
            '<div class="lang">'
            f'<div class="lang-top"><span class="lang-name">{_esc(lang["name"])}</span>'
            f'<span class="lang-level">{_esc(lang["level"])}</span></div>'
            f'<div class="bar"><div class="fill" style="width:{lang["pct"]}%"></div></div>'
            "</div>"
        )
    return "".join(blocks)


def _education_block() -> str:
    blocks = ["<h4 class='sub-title'>Education</h4>"]
    for edu in cv_data.EDUCATION:
        blocks.append(
            '<div class="edu-row">'
            f'<div class="edu-deg">{_esc(edu["degree"])}</div>'
            f'<div class="edu-school">{_esc(edu["school"])}</div>'
            f'<div class="edu-years">{_esc(edu["years"])}</div>'
            "</div>"
        )
    return "".join(blocks)


def _skills_block() -> str:
    chips = "".join(f'<span class="skill-chip">{_esc(s)}</span>' for s in cv_data.SKILLS)
    return f"<h4 class='sub-title'>IT Skills</h4><div class='skill-list'>{chips}</div>"


def _background_card() -> str:
    return (
        '<div class="card">'
        "<h3 class='section-title'>Education, Languages &amp; IT Skills</h3>"
        '<table class="two-col"><colgroup>'
        '<col style="width:50%"><col style="width:50%">'
        "</colgroup><tr>"
        f"<td>{_education_block()}{_languages_block()}</td>"
        f"<td>{_skills_block()}</td>"
        "</tr></table>"
        "</div>"
    )


def _role_block(role) -> str:
    bullets = "".join(f"<li>{_esc(b)}</li>" for b in role["bullets"])
    return (
        '<div class="role">'
        '<div class="role-head">'
        f'<span class="role-date">{_esc(role["dates"])}</span>'
        f'<span class="role-title">{_esc(role["role"])}</span>'
        f'<span class="role-company"> · {_esc(role["company"])}</span>'
        "</div>"
        f'<ul class="role-bullets">{bullets}</ul>'
        "</div>"
    )


def _fit_table(section) -> str:
    rows = "".join(
        f"<tr><td>{_esc(req)}</td><td>{_esc(evidence)}</td></tr>"
        for req, evidence in section["rows"]
    )
    return (
        '<table class="fit-table" style="table-layout:fixed">'
        '<colgroup>'
        '<col style="width:34%">'
        '<col style="width:66%">'
        "</colgroup>"
        f"<caption>{_esc(section['title'])}</caption>"
        "<thead><tr><th>micro1 requirement</th><th>Evidence</th></tr></thead>"
        f"<tbody>{rows}</tbody>"
        "</table>"
    )


def _qa_annex() -> str:
    blocks = [
        '<div class="card qa-annex">',
        '<div class="section-title">Application Q&A — micro1 Consulting Domain Expert</div>',
    ]
    for qa in cv_data.APPLICATION_QA:
        blocks.append(
            f'<div class="qa-item"><p class="qa-q">{_esc(qa["question"])}</p>'
        )
        for paragraph in qa["answer"]:
            blocks.append(f'<p class="qa-a">{_esc(paragraph)}</p>')
        blocks.append("</div>")
    blocks.append("</div>")
    return "\n".join(blocks)


def build_html() -> str:
    profile = cv_data.PROFILE
    experience = "".join(_role_block(r) for r in cv_data.EXPERIENCE)
    ai_bullets = "".join(f"<li>{_esc(b)}</li>" for b in cv_data.AI_SECTION["bullets"])
    fit_tables = "".join(_fit_table(s) for s in cv_data.FIT_SECTIONS)
    qa_annex = _qa_annex()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>CV — {profile['name']}</title>
<style>
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: '{FONTS['ui']}', 'Helvetica Neue', Arial, sans-serif;
  color: {C['dark_space']};
  background: {C['desert_storm']};
  font-size: 9pt;
  line-height: 1.5;
}}

/* ---------- Header ---------- */
.header {{
  background: {GRADIENTS['primary']};
  color: {C['white']};
  padding: 12mm 12mm 10mm 12mm;
}}
.header .kicker {{
  font-size: 8pt;
  letter-spacing: 3px;
  color: {C['bayou']};
  text-transform: uppercase;
  font-weight: 700;
  margin-bottom: 2.5mm;
}}
.header .name {{
  font-size: 25pt;
  font-weight: 800;
  letter-spacing: -0.5px;
  line-height: 1.1;
}}
.header .role {{
  font-size: 10.5pt;
  font-weight: 700;
  color: {C['honey']};
  text-transform: uppercase;
  letter-spacing: 1.6px;
  margin-top: 3mm;
}}
.header .tagline {{
  font-size: 9.5pt;
  color: #C9E4E8;
  margin-top: 3mm;
  max-width: 150mm;
}}
.header .accent-bar {{
  height: 1.8mm;
  width: 28mm;
  background: {GRADIENTS['warm']};
  border-radius: {RADIUS['badge']};
  margin-top: 4.5mm;
}}
.contact-strip {{
  display: flex;
  flex-wrap: wrap;
  gap: 4mm 8mm;
  margin-top: 5mm;
  padding-top: 4mm;
  border-top: 1px solid rgba(255,255,255,0.18);
}}
.c-item {{ display: flex; flex-direction: column; }}
.c-lbl {{
  font-size: 6.5pt;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: {C['bayou']};
  font-weight: 600;
}}
.c-val {{ font-size: 8.5pt; color: {C['white']}; margin-top: 0.6mm; }}

/* ---------- Main ---------- */
.main {{ padding: 8mm 12mm 12mm 12mm; }}
.card {{
  background: {C['white']};
  border: {BORDER};
  border-radius: {RADIUS['card']};
  padding: 5mm 6mm;
  margin-bottom: 4mm;
  box-shadow: {SHADOW};
}}
.section-title {{
  font-size: 11.5pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: {C['teal_blue']};
  padding-bottom: 1.5mm;
  border-bottom: 2px solid {C['honey']};
  margin-bottom: 3mm;
}}
.sub-title {{
  font-size: 8.5pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  color: {C['egyptian_teal']};
  margin: 4mm 0 2mm;
}}
.summary {{ font-size: 9pt; text-align: justify; }}

.two-col {{ width: 100%; border-collapse: collapse; }}
.two-col td {{ vertical-align: top; padding: 0; }}
.two-col td + td {{ padding-left: 5mm; border-left: 1px solid {C['border']}; }}
.two-col .comp-cat {{ margin-bottom: 3mm; }}

.comp-cat-name {{
  font-size: 7.5pt;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: {C['teal_blue']};
  margin-bottom: 1.2mm;
}}
.chip {{
  display: inline-block;
  background: {C['egyptian_teal']};
  color: {C['white']};
  border-radius: {RADIUS['badge']};
  padding: 0.8mm 1.8mm;
  font-size: 7pt;
  margin: 0 0.8mm 1mm 0;
}}
.chip.hot {{
  background: {C['honey']};
  color: {C['teal_blue']};
  font-weight: 600;
}}

.role {{ margin-bottom: 3mm; page-break-inside: avoid; }}
.role:last-child {{ margin-bottom: 0; }}
.role + .role {{
  border-top: 1px solid {C['border']};
  padding-top: 3mm;
}}
.role-head {{ margin-bottom: 0.8mm; }}
.role-title {{ font-size: 10pt; font-weight: 700; color: {C['dark_space']}; }}
.role-company {{ color: {C['egyptian_teal']}; font-weight: 700; }}
.role-date {{
  float: right;
  font-size: 8pt;
  font-weight: 600;
  color: {C['honey_dark']};
}}
.role-bullets {{ margin-left: 3.5mm; }}
.role-bullets li {{
  list-style: none;
  position: relative;
  padding-left: 3.2mm;
  margin-bottom: 0.8mm;
  font-size: 8.4pt;
}}
.role-bullets li::before {{
  content: "\\25B8";
  position: absolute;
  left: 0;
  color: {C['bayou']};
  font-weight: 700;
}}

.highlight {{
  background: {C['chart_area']};
  border: 1px solid {C['bayou']};
  border-left: 1.8mm solid {C['egyptian_teal']};
  border-radius: {RADIUS['card']};
  padding: 5mm 6mm;
  margin-bottom: 4mm;
  page-break-inside: avoid;
}}
.highlight .section-title {{ border-bottom-color: {C['egyptian_teal']}; }}
.highlight ul {{ margin-left: 3.5mm; }}
.highlight li {{
  list-style: none;
  position: relative;
  padding-left: 3.2mm;
  margin-bottom: 1.2mm;
  font-size: 8.6pt;
}}
.highlight li::before {{
  content: "\\25B8";
  position: absolute;
  left: 0;
  color: {C['egyptian_teal']};
  font-weight: 700;
}}

.edu-row {{ margin-bottom: 2.2mm; page-break-inside: avoid; }}
.edu-deg {{ font-size: 8.5pt; font-weight: 700; color: {C['dark_space']}; }}
.edu-school {{ font-size: 8pt; color: {C['egyptian_teal']}; }}
.edu-years {{ font-size: 7.5pt; color: #7A8A90; }}

.lang {{ margin-bottom: 2.2mm; }}
.lang-top {{ display: flex; justify-content: space-between; font-size: 8pt; }}
.lang-name {{ font-weight: 600; }}
.lang-level {{ color: {C['egyptian_teal']}; font-size: 7pt; }}
.bar {{
  margin-top: 1.2mm;
  height: 1.8mm;
  background: {C['desert_storm']};
  border-radius: 1mm;
}}
.fill {{
  height: 100%;
  border-radius: 1mm;
  background: {GRADIENTS['warm']};
}}
.skill-chip {{
  display: inline-block;
  background: rgba(17,175,195,0.12);
  border: 1px solid rgba(14,132,138,0.4);
  color: {C['teal_blue']};
  border-radius: {RADIUS['badge']};
  padding: 0.7mm 1.7mm;
  font-size: 7pt;
  margin: 0 0.8mm 1mm 0;
}}

.fit-table {{
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 4mm;
  font-size: 8pt;
  page-break-inside: avoid;
}}
.fit-table:last-child {{ margin-bottom: 0; }}
.fit-table caption {{
  text-align: left;
  font-weight: 700;
  color: {C['teal_blue']};
  font-size: 10pt;
  margin-bottom: 1.5mm;
}}
.fit-table th {{
  background: {C['egyptian_teal']};
  color: {C['white']};
  text-align: left;
  padding: 1.6mm 2mm;
  font-size: 8pt;
  font-weight: 600;
}}
.fit-table td {{
  border: {BORDER};
  padding: 1.6mm 2mm;
  vertical-align: top;
  word-wrap: break-word;
}}
.fit-table tr:nth-child(even) td {{ background: {C['desert_storm']}; }}
.fit-table td:first-child {{ font-weight: 600; color: {C['teal_blue']}; }}

.qa-annex {{ page-break-inside: auto; }}
.qa-item {{ page-break-inside: avoid; margin-bottom: 3mm; }}
.qa-q {{ font-size: 9pt; font-weight: 700; color: {C['teal_blue']}; margin-bottom: 1.2mm; }}
.qa-a {{ font-size: 8.4pt; margin-bottom: 1.5mm; text-align: justify; }}
</style>
</head>
<body>

<div class="header">
  <div class="kicker">{_esc(profile['kicker'])}</div>
  <div class="name">{_esc(profile['name'])}</div>
  <div class="role">{_esc(profile['role'])}</div>
  <div class="tagline">{_esc(profile['tagline'])}</div>
  <div class="accent-bar"></div>
  {_contact_strip()}
</div>

<main class="main">

  <div class="card">
    <div class="section-title">Professional Summary</div>
    <div class="summary">{_esc(profile['summary'])}</div>
  </div>

  <div class="card">
    <div class="section-title">Professional Experience</div>
    {experience}
  </div>

  <div class="highlight">
    <div class="section-title">{_esc(cv_data.AI_SECTION['title'])}</div>
    <ul>{ai_bullets}</ul>
  </div>

  {_competencies_card()}
  {_background_card()}

  <div class="card">
    <div class="section-title">Position Fit — micro1</div>
    {fit_tables}
  </div>

  {qa_annex}

</main>

</body>
</html>
"""


def save_pdf(output_path: str) -> None:
    from weasyprint import HTML

    html = build_html()
    HTML(string=html).write_pdf(output_path)
