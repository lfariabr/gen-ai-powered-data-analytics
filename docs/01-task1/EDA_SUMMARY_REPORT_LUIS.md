# GenAI Powered Data Analytics Job Simulation – Task 1  
Exploratory Data Analysis (EDA) Summary  
Luis G B A Faria, Sydney, NSW  
📞 +61 0403-278-880  
📧 lfariabr@gmail.com  
🔗 linkedin/lfaria • github/lfaria • dev.to/lfaria • luisfaria.dev  

---

# 1. Introduction
This report explores a credit card customer dataset used to predict whether an account becomes delinquent (*Delinquent_Account*). The goal is to understand data quality, target imbalance, and the main drivers of delinquency before building predictive models.  
The analysis was conducted using an interactive Streamlit application enhanced with GenAI assistance to ensure comprehensive exploration of patterns, anomalies, and risk indicators.

---

# 2. Dataset Overview
The dataset contains information on individual customers’ demographics, credit behavior, and account status.

## Key dataset attributes
- **Number of records:** 500  
- **Number of columns:** 19  
- **Memory usage:** 345.3 KB  
- **Dataset completeness:** 99.26% (70 missing cells out of 9,500 total)

## Key variables
- Customer_ID, Age, Income, Credit_Score, Credit_Utilization, Missed_Payments  
- Delinquent_Account (target)  
- Loan_Balance, Debt_to_Income_Ratio  
- Employment_Status, Credit_Card_Type  
- Account_Tenure, Month_1 … Month_5  

## Data types
- **Numerical:** Age, Income, Credit_Score, Credit_Utilization, Missed_Payments, Loan_Balance, Debt_to_Income_Ratio, Account_Tenure  
- **Categorical:** Customer_ID, Employment_Status, Credit_Card_Type  

## Data quality observations
- No duplicate Customer_ID values observed  
- Dataset is generally clean  
- Good sample size  
- Strong mix of demographic + behavioral features  

---

# 3. Missing Data Analysis
Missing data is concentrated in three numeric variables:

| Variable        | Missing Count | Missing % | Severity |
|----------------|---------------|-----------|----------|
| Income         | 39            | 7.8%      | Moderate |
| Loan_Balance   | 29            | 5.8%      | Moderate |
| Credit_Score   | 2             | 0.4%      | Low     |
| **Total**      | **70**        | **0.74%** | Manageable |

### Proposed Missing Data Treatment

| Variable        | Treatment Method | Justification |
|----------------|------------------|---------------|
| **Income** | Median imputation, stratified by Employment_Status | Preserves group-level distributions |
| **Loan_Balance** | Median imputation, stratified by delinquency | Avoids distortion in imbalanced datasets |
| **Credit_Score** | Straight median imputation | Minimal missingness |

**Rationale:** Avoid row deletion; financial data skew favors median; stratification preserves realism.

---

# 4. Key Findings and Risk Indicators

## 4.1 Target distribution
- **84%** non-delinquent  
- **16%** delinquent  
→ Severe class imbalance requiring weighting, SMOTE, proper metrics (Recall, F1, ROC-AUC)

## 4.2 Correlations with numeric features

| Feature               | Corr | Strength |
|----------------------|------|----------|
| Debt_to_Income_Ratio | +0.12 | Weak |
| Credit_Utilization   | +0.09 | Weak |
| Income               | +0.08 | Weak |
| Age                  | +0.06 | Weak |
| Credit_Score         | +0.05 | Weak |
| Account_Tenure       | -0.07 | Weak |
| Missed_Payments      | -0.04 | Weak |

### Key Insights
- All |r| < 0.3 → delinquency is **multi-factorial**
- Interactions matter more than single variables
- Non-linear effects likely → tree-based models recommended

### Unexpected Finding
**Missed_Payments** shows slight *negative* correlation with delinquency → may indicate data quality or timing issues.

---

# 4.3 Distributions by Target
Observations:
- Age: overlapping; slight middle-age risk bump  
- Income: similar distributions → behavior matters more than earnings  
- Credit_Score: slightly lower for delinquent accounts, but high overlap  
- Utilization: tends to be higher among delinquent accounts  
- DTI: weak positive correlation  

→ No single feature separates classes → multivariate model required.

---

# 4.4 Risk indicators summary
- **Debt_to_Income_Ratio** — strongest stress metric  
- **Credit_Utilization** — liquidity pressure  
- **Credit_Score** — historical risk indicator  
- **Income** — contextual importance  
- **Account_Tenure** — protective effect  
- **Age** — mild middle-age risk  

Suggested interactions:
- Utilization × Missed_Payments  
- DTI × Credit_Score  
- Income × Age  
- Month_1–Month_5 trend features  

---

# 5. AI & GenAI Usage
GenAI tools assisted with:
- EDA structuring  
- Visualizations (missing bar charts, correlation heatmaps, distribution plots)  
- Identifying anomalies & multi-factor risk patterns  
- Suggesting modeling and imputation strategies  

Prompts used included:
- “Summarize key EDA findings…”  
- “Analyze correlation between customer features and delinquency risk…”  

Value delivered: accelerated analysis, clearer insights, best-practice recommendations.

---

# 6. Conclusion & Next Steps

## Key Takeaways
- Dataset is clean and modeling-ready  
- Missingness exists but is manageable  
- Strong class imbalance → must be handled carefully  
- No strong single predictors → interactions + non-linear models essential  
- Visual overlap confirms need for advanced modeling  

## Next Steps

### Data Preparation
- Apply median / stratified imputation  
- Validate distributions post-imputation  

### Feature Engineering
- Create interaction terms  
- Risk bins for continuous variables  
- Temporal trends from Month_1–Month_5  
- Polynomial or non-linear transforms  

### Model Development
- Baselines: Logistic Regression, Decision Trees  
- Advanced: Random Forest, Gradient Boosting  
- Handle imbalance: class weights, SMOTE  
- Stratified K-fold CV  

### Evaluation
- Prioritize Recall, Precision, F1, ROC-AUC  
- Align thresholds with business risk tolerances  
- Fairness checks across demographic groups  

### Deployment
- Ensure interpretability  
- Create monitoring & drift detection  
- Plan integration with business workflows  
