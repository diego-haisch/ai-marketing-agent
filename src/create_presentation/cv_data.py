"""CV content for the micro1 applications (AI Consulting & AI Data Science Domain Expert).

Mirrors comercial/contactos/2026-08-15_micro1_ai_expert_cv.md.
"""

PROFILE = {
    "name": "Diego Haisch Timm",
    "kicker": "micro1 · AI Data Lab",
    "role": "AI Consulting & Data Science Domain Expert",
    "tagline": "Supply chain operations leader turned full-stack AI application builder — forecasting and replenishment, evaluated and shipped with AI agents.",
    "contact": {
        "location": "Alella, Barcelona, Spain",
        "phone": "+34 650 969 382",
        "email": "diegohaisch@gmail.com",
        "linkedin": "linkedin.com/in/diego-haisch-32a76136",
    },
    "summary": (
        "Data-driven operations leader with 10+ years of demand planning, forecasting, and business analytics "
        "in analytically rigorous fashion retail settings (Mango, Desigual, Inditex/Lefties, Etnia Barcelona). "
        "I lead the Data Science team at Etnia Barcelona and, as founder of ApplyChain, design and build AI-powered "
        "supply chain applications end to end — sales forecasting with ML (Random Forest) and a multi-SKU / multi-store "
        "replenishment engine — covering backend (Python, FastAPI, PostgreSQL) and frontend (React, TypeScript, Power BI)."
    ),
}

COMPETENCY_GROUPS = [
    {
        "name": "AI Evaluation & Feedback",
        "hot": True,
        "items": [
            "AI Output Evaluation",
            "AI Model Evaluation",
            "AI output evaluation and feedback loops",
            "Prompt Authoring & Refinement",
            "Prompt Engineering",
        ],
    },
    {
        "name": "QA, Content & Data",
        "hot": True,
        "items": [
            "Rubric-Based Evaluation",
            "Content Evaluation",
            "Quality Assurance",
            "Fact-Checking",
            "Data Annotation",
            "Content Review",
        ],
    },
    {
        "name": "Writing & Communication",
        "hot": False,
        "items": [
            "Professional Writing",
            "Report Writing",
            "Technical Documentation",
            "Business Communication",
            "Client Presentations",
            "Recommendation Memos",
            "Professional & Technical Editing",
        ],
    },
    {
        "name": "Reasoning & Research",
        "hot": False,
        "items": [
            "Critical Thinking",
            "Analytical & Logical Reasoning",
            "Data Interpretation",
            "Problem Solving",
            "Independent Research",
            "Market & Data Analysis",
        ],
    },
    {
        "name": "Data Science & ML",
        "hot": False,
        "items": [
            "Forecasting",
            "ML (Random Forest)",
            "Statistics",
            "Feature Engineering",
            "Model Evaluation (MAE, wMAE, RMSE, BIAS)",
        ],
    },
    {
        "name": "Full-Stack Development",
        "hot": False,
        "items": [
            "Python",
            "FastAPI",
            "SQL / PostgreSQL",
            "React",
            "TypeScript",
            "Tailwind",
            "Power BI",
            "DAX",
            "Azure",
        ],
    },
    {
        "name": "Agentic Engineering",
        "hot": True,
        "items": [
            "VS Code",
            "opencode",
            "MCP",
            "Git / GitHub",
            "Harness design (AGENTS.md, skills, specs)",
        ],
    },
]

SKILLS = [
    "Excel",
    "Python",
    "Power BI",
    "SQL",
    "DAX",
    "SAP R3",
    "SAP Business Objects",
    "Azure",
    "Git",
    "GitHub",
    "Sourcetree",
    "Asana",
    "React",
    "TypeScript",
    "FastAPI",
    "PostgreSQL",
    "VS Code",
    "opencode",
    "MCP",
]

LANGUAGES = [
    {"name": "Spanish", "level": "Native", "pct": 100},
    {"name": "English", "level": "Advanced", "pct": 90},
    {"name": "Catalan", "level": "Upper Intermediate", "pct": 70},
    {"name": "German", "level": "Intermediate", "pct": 50},
]

EDUCATION = [
    {"degree": "Master's in Supply Chain Management", "school": "Universitat Ramon Llull (La Salle), Barcelona", "years": "2006 – 2008"},
    {"degree": "Industrial Engineering", "school": "Universidad Católica Boliviana", "years": "2001 – 2006"},
    {"degree": "Data Science Professional Certificate", "school": "IBM · Coursera", "years": "2020 – 2021"},
]

EXPERIENCE = [
    {
        "company": "ApplyChain",
        "role": "Founder & AI Solutions Architect",
        "dates": "2025 – Present",
        "bullets": [
            "Design and build AI products: in-season sales forecasting at SKC level (Random Forest, 12-month horizon) and a multi-SKU / multi-store replenishment engine with executive dashboard.",
            "Own the full stack: Python/FastAPI backend (data loading, feature engineering, training, prediction APIs, PostgreSQL) and React + TypeScript + Tailwind frontend, with Power BI as the executive reporting layer.",
            "Develop these applications through AI coding agents (VS Code + opencode): author detailed project specs, define reusable agent skills, and configure MCP integrations so agents execute scoped tasks and consolidate a coherent codebase.",
            "Perform harness engineering: translate business needs into structured specs, conventions (AGENTS.md), and GitHub versioning workflows that keep AI-generated code reliable, testable, and auditable.",
            "Evaluate AI-generated code and content against rubrics before release — correctness, performance, business alignment, clarity — and refine prompts iteratively until output meets standard.",
            "Produce technical documentation, architecture decision records, API contracts, business plans, and executive summaries for senior audiences.",
        ],
    },
    {
        "company": "Etnia Barcelona (Eyewear Culture)",
        "role": "Data Science Manager",
        "dates": "Aug 2024 – Nov 2025",
        "bullets": [
            "Lead the Data Science team responsible for data storage and Power BI reporting across the company.",
            "Oversee and optimize SQL and Azure data systems, ensuring scalability, security, and reliability.",
            "Coordinate Business Intelligence developments and manage AI and predictive modeling projects in Python, aligning technical work with company needs.",
            "Review and interpret analytical findings and translate them into clear, actionable reports for operational and strategic decision-making.",
        ],
    },
    {
        "company": "Etnia Barcelona (Eyewear Culture)",
        "role": "Senior Demand Planner – BI Analyst",
        "dates": "Aug 2021 – Aug 2024",
        "bullets": [
            "Led global product forecasting and replenishment using AI-based models; balanced product availability and stock efficiency.",
            "Increased forecast accuracy up to 77% through improved modeling and process design.",
            "Designed and deployed KPI dashboards in Power BI for executive reporting; standardized processes and supply chain levers.",
            "Planned production with suppliers to ensure on-time commercial launches.",
        ],
    },
    {
        "company": "Encuentro Moda",
        "role": "Senior Demand Planner – BI Analyst",
        "dates": "2017 – 2021",
        "bullets": [
            "Defined annual sales, purchase, and production budgets; structured collections, pricing, and assortment strategies.",
            "Established forecasting and replenishment strategies; crafted discount strategies to reduce slow-selling stock and obsolescence.",
            "Developed and deployed Power BI dashboards.",
        ],
    },
    {
        "company": "Mango",
        "role": "Senior Demand Planner",
        "dates": "2016 – 2017",
        "bullets": [
            "Led demand planning for Women's and Men's collections; crafted and tracked sales and merchandise budgets.",
            "Conducted historical analyses to establish merchandise production guidelines.",
            "Generated comprehensive sales reports with SAP Business Objects for data-driven decisions.",
        ],
    },
    {
        "company": "Lefties (Inditex)",
        "role": "Business Controller",
        "dates": "2014 – 2015",
        "bullets": [
            "Oversaw budget preparation and monitoring; produced weekly sales reports and proposed actions to meet budget goals.",
            "Improved stock performance through forecasting and replenishment calculations.",
        ],
    },
    {
        "company": "Desigual",
        "role": "Junior Demand Planner",
        "dates": "2009 – 2014",
        "bullets": [
            "Defined collection budgets and purchase plans; set global store assortment guidelines.",
            "Performed sales tracking, forecasting, and replenishment order planning.",
            "Achievements: reached 120% of budget targets and reduced leftover products by 43%.",
        ],
    },
]

AI_SECTION = {
    "title": "AI Application Development & Agentic Engineering",
    "bullets": [
        "Full-stack AI application builder. Forecast and replenishment products where the ML models, backend services, and frontend dashboards are designed and shipped end to end by a single person with deep supply chain domain knowledge.",
        "Agentic development workflow. Daily use of VS Code + opencode with multiple AI agents, configured through agent skills and MCP server integrations; all work versioned on GitHub (branching, review, reproducible artifacts).",
        "Harness engineering. I design the environment that makes AI agents productive and reliable: project specs, AGENTS.md conventions, reusable skills, and test contracts. This is how business requirements become scoped, executable tasks that agents consolidate into a powerful, coherent project.",
        "Evaluation and refinement loops. I evaluate AI outputs against rubrics — model quality, code correctness, documentation clarity, business alignment — and iterate prompts and harness configuration until the output is professional and production-ready.",
        "Fact-checking and data quality. Independent research and data validation embedded in every deliverable: data reconciliation before reporting, fact-checking of AI outputs, and annotation of edge cases in forecasting data.",
    ],
}

FIT_SECTIONS = [
    {
        "title": "Fit — AI Consulting Domain Expert",
        "rows": [
            ("3+ years in strategy consulting, corporate strategy, business transformation or operations in analytically rigorous settings", "10+ years in operations: demand planning, budgeting, forecasting, replenishment at Mango, Inditex/Lefties, Desigual, Etnia Barcelona"),
            ("Excellence in professional writing, business communication, report creation for senior audiences", "Executive Power BI dashboards, budget and merchandise reports, business plans, executive summaries, architecture decision records"),
            ("Strong critical thinking, analytical reasoning, independent research", "Built forecasting models from scratch; customer discovery program (11 interviews with retailers); strategy and market analysis documents"),
            ("Exceptional attention to detail, QA, technical/business editing", "Rubric-based evaluation and QA of AI-generated code and content; professional and technical editing of reports and specs"),
            ("Proven experience in client presentations, recommendation memos, market analyses with structured methodologies", "Assortment and pricing strategies, budget proposals, collection-flow purchase and allocation recommendations"),
            ("Bachelor's required; advanced degree a plus", "Industrial Engineering + Master's in Supply Chain Management"),
        ],
    },
    {
        "title": "Fit — AI Data Science Domain Expert",
        "rows": [
            ("3+ years in Data Science, ML, Applied AI, Statistics, Quantitative Analytics", "Data Science Manager at Etnia Barcelona; ML forecasting (Random Forest) with model evaluation (MAE, wMAE, RMSE, BIAS); 10+ years of quantitative analytics"),
            ("Producing or reviewing research papers, analytical reports, experiment summaries, notebooks, technical documentation", "Model documentation, API contracts, technical specs, ADRs, business plans, data-driven recommendations for senior audiences"),
            ("Data annotation, content review, rubric-based evaluation", "Annotation and QA of AI outputs; rubric-based evaluation of model and code quality"),
            ("Prompt engineering, AI output evaluation, fact-checking, RLHF advantageous", "Daily agentic development and evaluation loops; prompt authoring and refinement; fact-checking and data validation before release"),
            ("Advanced degree preferred", "Master's in Supply Chain Management (La Salle — Ramon Llull) + Data Science Professional Certificate (IBM)"),
        ],
    },
]

APPLICATION_QA = [
    {
        "question": "Q4. Describe your professional background and the type of complex work you've been responsible for over the past 3+ years. Include examples of projects or decisions that best demonstrate your expertise.",
        "answer": [
            "10+ years in demand planning, forecasting and analytics at Mango, Desigual, Inditex and Etnia Barcelona. Last 3+ years: leadership and applied AI.",
            "As Data Science Manager at Etnia Barcelona, I led the data team (SQL, Azure, Power BI) and predictive modeling in Python. My most complex decision: balancing stock availability against tied-up cash — I redesigned the global forecasting/replenishment model, raising accuracy to 77% while keeping launches on time.",
            "As founder of ApplyChain, I build AI supply chain products end to end (backend Python/FastAPI, frontend React/Power BI), authoring prompts and rubrics, and evaluating AI outputs for correctness and business alignment before release.",
        ],
    },
    {
        "question": "Q5. What types of professional documents do you regularly create or review (e.g., technical documentation, reports, research papers, legal memoranda, investment memos, strategy presentations, design documents)? Please describe your role in producing them.",
        "answer": [
            "I create and review documents at three levels: technical, executive, and commercial.",
            "At Etnia Barcelona, as Data Science Manager, I regularly produced two types of documents. First, technical requirements and specifications for external service providers — defining scope, data, deliverables and acceptance criteria for vendors. Second, internal business presentations to \"sell\" projects to stakeholders: I translated technical work (forecasting models, data architecture, BI developments) into business cases that internal clients and management could evaluate and approve.",
            "As founder of ApplyChain, I create client-facing presentations that explain the value of our forecasting and replenishment products in business terms, and I write the technical documentation for everything we build — architecture decisions, API contracts, model configuration, and business plans. I also review and edit AI-generated documentation and content, checking it against the original requirements for accuracy and clarity before release.",
            "Throughout my career I've also produced executive reports and dashboards (Power BI) for senior audiences, budget and merchandising strategy documents, and data-driven recommendations used in decision-making.",
        ],
    },
    {
        "question": "Q6. Describe a time you identified a significant error, inconsistency, or opportunity for improvement in a document, analysis, or technical deliverable. What did you change, and why?",
        "answer": [
            "At Etnia Barcelona, the replenishment forecasts that guided our stock planning were being produced with spreadsheet-based tools and manual rules. I identified two problems in that process: the forecasts were fragile (dependent on manual updates and individual criteria) and there was no way to measure their accuracy, which led to recurring stockouts in some items and overstock in others. I proposed replacing the approach with Machine Learning-based forecasting. I led the implementation of the models, defined the evaluation metrics, and redesigned the process around them. The change improved forecast accuracy up to 77% and made inventory management measurable and auditable instead of judgment-based.",
            "I found a second, related inconsistency in reporting: the same business metric often showed different values depending on who was asked, because each department accessed fragmented data. I designed and developed the company's central semantic model, a single source of truth that standardized definitions across all dashboards and departments. What changed was structural: instead of fixing individual reports, I fixed the data layer they all depend on, so decisions were based on one consistent version of the truth.",
        ],
    },
    {
        "question": "Q7. If you were asked to instruct an AI to complete a task within your area of expertise, how would you approach writing the prompt? What information would you include, and how would you refine it if the output wasn't accurate or complete?",
        "answer": [
            "Before writing the prompt, I check whether part of the task maps to general knowledge or conventions that already exist in the project — if so, I encode that as a reusable skill instead of repeating it in every prompt, to avoid duplicities and keep the prompt focused.",
            "The prompt itself includes three elements: the need (the business problem to solve), the procedure (steps, constraints, data sources, acceptance criteria), and the objective (what a correct, complete output looks like).",
            "Instead of asking the AI to implement directly, I first ask it to produce specifications as documentation (e.g., an Architecture Decision Record): proposed approach, scope, assumptions, and open decisions. I review that document carefully to surface deviations or ambiguities, and correct them before implementation.",
            "Once the ADR is validated, I instruct the agent to implement following it. This two-stage workflow (spec first, implementation second) prevents hallucinations and off-target results, because the agent works against defined specifications instead of its own assumptions — and deviations are caught in review, not after delivery.",
        ],
    },
]
