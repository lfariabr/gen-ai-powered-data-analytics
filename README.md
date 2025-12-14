# gen-ai-powered-data-analytics

🎉 **SIMULATION COMPLETED!** Successfully finished Tata's GenAI Powered Data Analytics simulation on Forage.

GenAI-powered delinquency risk toolkit built for the Tata Data Visualisation Forage challenge. The repository combines guided project notes with a Streamlit app that explores credit card customer data and outlines a modeling plan for reducing delinquency at Geldium Finance.

## 🏆 Accomplishments
- ✅ Conducted exploratory data analysis (EDA) using GenAI tools to assess data quality, identify risk indicators, and structure insights for predictive modeling
- ✅ Proposed and justified an initial no-code predictive modeling framework to assess customer delinquency risk, leveraging GenAI for structured model logic and evaluation criteria
- ✅ Designed an AI-driven collections strategy leveraging agentic AI and automation, incorporating ethical AI principles, regulatory compliance, and scalable implementation frameworks
- 🔗 [View the simulation](https://www.theforage.com/simulations/tata/data-analytics-t3zr)

## Overview
- Role: AI transformation consultant using analytics and GenAI to support Geldium’s collections team.
- Goal: predict delinquency risk, surface insights, and recommend ethical, explainable intervention strategies.
- Stack: Streamlit UI, pandas/NumPy for data handling, seaborn/matplotlib for visuals, modular resolver layer for analytics logic.

## What’s in this repo
- Project brief, checkpoints, and submissions in [docs/](docs). Start with [docs/00-intro/00-intro.md](docs/00-intro/00-intro.md); each task folder (01–04) contains prompts, references, and reports.
- Sample dataset for exploration at [docs/01-task1/db/Delinquency_prediction_dataset.csv](docs/01-task1/db/Delinquency_prediction_dataset.csv).
- Streamlit application in [tataData/](tataData) with architecture notes in [tataData/ARCHITECTURE.md](tataData/ARCHITECTURE.md).

## Run the Streamlit app
1) Prerequisites: Python 3.10+ and pip.
2) Install dependencies and launch:

```bash
cd tataData
pip install -r requirements.txt
streamlit run app.py
```

Upload the provided CSV (or your own Excel/CSV file) when prompted.

## App capabilities
- Entry point [tataData/app.py](tataData/app.py): caches uploads, routes between views, and validates file types.
- EDA view [tataData/views/EDA.py](tataData/views/EDA.py): dataset overview, missing data analysis, target distribution and imbalance checks, feature correlations, per-target distributions, overall histograms, and key insight recommendations.
- Model planning view [tataData/views/ModelPlan.py](tataData/views/ModelPlan.py): imputation plan, model recommendations, evaluation metric guide, bias/fairness checklist, feature engineering ideas, and implementation roadmap.
- Analytics logic lives in [tataData/resolvers/analyzer.py](tataData/resolvers/analyzer.py) and [tataData/resolvers/mlpipeline.py](tataData/resolvers/mlpipeline.py) for reuse and testability.

## Quick orientation
- Follow the task guides in [docs/](docs) to understand the storyline and deliverables.
- Use the Streamlit app to replicate the EDA and modeling plan described in the notes, then adapt it to new datasets.
- The architecture is modular to make it easy to extend analyses or plug in real modeling code later.