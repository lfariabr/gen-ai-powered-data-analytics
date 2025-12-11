# Step by Step on Tackling Task #1

# Step by Step on Tackling Task #1

1. Build a Streamlit EDA app (`app.py`) and upload the dataset as CSV:
   - Implement a sidebar with file uploader and option to show raw data.
   - Section **1 – Dataset Overview**:
     - Show total records, total columns, and memory usage.
     - Optional raw data preview in an expander.
     - Column types summary (counts per dtype + detailed table).

2. Add rich missing-data analysis:
   - Section **2 – Missing Data Analysis**:
     - Table of missing counts and percentages per column (only columns with missing values).
     - Bar chart visualising missing percentage per column.
     - Short interpretation (how many columns / cells are missing).
     - Imputation recommendations for Income, Loan_Balance and Credit_Score (median, possibly stratified).

3. Add target & relationship analysis:
   - Section **3 – Target Variable Analysis**:
     - Select target column (`Delinquent_Account`).
     - Show target distribution table with counts and percentages.
     - Highlight class imbalance with guidance on metrics and class weighting.
     - Bar chart of target distribution with labels.
   - Section **4 – Correlation Analysis**:
     - Table of correlations between numeric features and the target.
     - Bar chart of correlations with colour-coded sign.
     - Optional full correlation heatmap for all numeric features.

4. Analyse feature distributions by target and overall:
   - Section **5 – Feature Distributions by Target**:
     - Multi-select of key numeric features.
     - Boxplot + violin overlays of each feature split by `Delinquent_Account`.
     - Statistical summary tables by target group.
   - Section **6 – Overall Feature Distributions**:
     - Multi-select of numeric features.
     - Histograms with KDE, plus mean/median lines for each feature.

5. Capture key insights and next steps in the app and documentation:
   - Section **7 – Key Insights & Recommendations** in the app summarises strengths, challenges and next steps.
   - Summarise EDA findings into `EDA_summary.md`:
     - Fill in dataset size, key variables and data types.
     - Describe missing data patterns (Income, Loan_Balance, Credit_Score).
     - Highlight target imbalance (420 non‑delinquent vs 80 delinquent).
     - Capture main relationships (e.g. how Credit_Score, Income, utilisation relate to delinquency).
   - Define an imputation and modelling plan for the next task:
     - Propose how to handle missing numeric values (e.g. median / model‑based imputation).
     - Note that the target is imbalanced → plan to use appropriate metrics and/or class weighting.