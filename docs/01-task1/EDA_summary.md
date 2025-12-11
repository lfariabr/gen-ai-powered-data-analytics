Exploratory Data Analysis (EDA) Summary 
Report Template


Exploratory Data Analysis (EDA) Summary 

1. Introduction  
This report explores a credit card customer dataset used to predict whether an account becomes delinquent (`Delinquent_Account`).  
The goal is to understand data quality, target imbalance, and the main drivers of delinquency before building predictive models.

2. Dataset Overview  
The dataset contains information on individual customers’ demographics, credit behaviour, and account status.

Key dataset attributes:
- Number of records: **500**
- Number of columns: **19**
- Key variables:
  - `Customer_ID`: unique customer identifier (categorical, ID).
  - `Age`: customer age in years (numeric).
  - `Income`: annual income (numeric).
  - `Credit_Score`: credit score (numeric).
  - `Credit_Utilization`: utilisation ratio of available credit (numeric).
  - `Missed_Payments`: count of recent missed payments (numeric).
  - `Delinquent_Account`: target variable; 1 = delinquent, 0 = non‑delinquent (numeric / binary).
  - `Loan_Balance`: outstanding balance (numeric).
  - `Debt_to_Income_Ratio`: debt relative to income (numeric).
  - `Employment_Status`, `Credit_Card_Type`: categorical descriptors.
  - `Account_Tenure`, `Month_1` … `Month_5`: tenure and recent history.

Data types:
- Numerical: `Age`, `Income`, `Credit_Score`, `Credit_Utilization`, `Missed_Payments`, `Delinquent_Account`, `Loan_Balance`, `Debt_to_Income_Ratio`, `Account_Tenure`, monthly metrics.
- Categorical: `Customer_ID`, `Employment_Status`, `Credit_Card_Type`.

No obvious duplicate IDs were observed in the EDA app (can be revisited if needed).

3. Missing Data Analysis  
Missing data is concentrated in a few numeric variables:

- `Income`: **39** missing values (**7.8%** of records).
- `Loan_Balance`: **29** missing values (**5.8%**).
- `Credit_Score`: **2** missing values (**0.4%**).
- All other columns show **no missing values**.

Proposed missing data treatment:
- For numeric variables with moderate missingness (`Income`, `Loan_Balance`), use **median imputation**, optionally stratified by segments such as `Employment_Status` or delinquency status if needed.
- For `Credit_Score` (very low missing rate), simple median imputation is sufficient.
- No deletion of rows is planned at this stage to avoid losing delinquent examples in an already imbalanced dataset.

4. Key Findings and Risk Indicators  

4.1 Target distribution (delinquency)  
- `Delinquent_Account = 0` (non‑delinquent): **420** customers (~84%).  
- `Delinquent_Account = 1` (delinquent): **80** customers (~16%).  

Implication: the target is **imbalanced**, so modelling should use appropriate metrics (e.g. recall/precision, ROC‑AUC) and possibly class weighting.

4.2 Correlations with numeric features  
A correlation analysis between numeric features and `Delinquent_Account` shows:
- All single feature correlations are **relatively weak** (low absolute values), which suggests delinquency is multi‑factorial.
- Slight positive correlations with `Income`, `Credit_Score`, `Debt_to_Income_Ratio`, `Credit_Utilization`, and `Age`.
- Slight negative correlations with `Missed_Payments` and `Account_Tenure`.

These weak but non‑zero relationships indicate that combinations of variables, rather than any single field, are likely to drive delinquency risk.

4.3 Distributions by target  
Boxplots of `Age`, `Income` and `Credit_Score` by `Delinquent_Account` show:

- **Age**: delinquent and non‑delinquent customers have overlapping age distributions; there is no sharp age cutoff, but delinquent customers may skew slightly towards middle age.
- **Income**: both groups cover a similar income range; delinquent accounts are not restricted to the lowest‑income band.
- **Credit_Score**: delinquent customers tend to exhibit somewhat lower credit scores on average, but with substantial overlap with non‑delinquent customers.

No single variable is sufficient on its own to flag delinquency, reinforcing the need for a multivariate model.

5. AI & GenAI Usage  
Generative AI was used to:
- Scaffold a **Streamlit EDA application** to interactively explore the dataset (distributions, missing values, correlations, boxplots).
- Summarise the observed patterns and translate them into this structured report.
- Suggest high‑level strategies for missing‑data imputation and handling target imbalance.

Example prompts used:
- “Create a Streamlit EDA app for the Delinquency_prediction_dataset with dataset overview, missingness, numeric distributions, and target relationships.”
- “Summarise the key EDA findings and propose an imputation strategy for Income and Loan_Balance.”

6. Conclusion & Next Steps  
Key takeaways:
- The dataset is relatively clean, with missingness focused in `Income`, `Loan_Balance`, and a small number of `Credit_Score` values.
- The target (`Delinquent_Account`) is **imbalanced** (16% delinquent), which will impact evaluation and training.
- No feature shows a very strong individual correlation with delinquency, but moderate patterns across credit behaviour variables (e.g. credit score, utilisation, income) suggest that a multivariate model should perform better than simple rules.

Next steps:
- Implement the agreed imputation strategy for numeric variables and validate its impact on distributions.
- Engineer additional features if needed (e.g. binned risk scores, interaction terms).
- Train baseline classification models (e.g. logistic regression, tree‑based models) using metrics that account for class imbalance.
- Iterate on feature selection and threshold tuning based on business risk appetite.