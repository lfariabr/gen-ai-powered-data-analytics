import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pathlib import Path

DATA_PATH = Path("docs/01-task1/Delinquency_prediction_dataset.xlsx")


@st.cache_data
def load_data(src) -> pd.DataFrame:
    """Load data from a file path or uploaded file.

    Supports Excel (xlsx/xls/xlsm) and CSV. Raises a ValueError with a
    helpful message if loading fails so the caller can surface it in the UI.
    """

    try:
        # src can be a Path/str or a file-like object from st.file_uploader
        if hasattr(src, "name") and not isinstance(src, (str, Path)):
            name = src.name
        else:
            name = str(src)

        name_lower = name.lower()

        if name_lower.endswith((".xlsx", ".xls", ".xlsm")):
            df = pd.read_excel(src)
        elif name_lower.endswith(".csv"):
            df = pd.read_csv(src)
        else:
            raise ValueError(
                "Unsupported file type. Please upload an Excel (.xlsx/.xls/.xlsm) "
                "or CSV (.csv) file."
            )
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"Failed to load data from '{name}': {exc}") from exc

    if df.empty:
        raise ValueError("Loaded dataset is empty.")

    return df


def main() -> None:
    st.set_page_config(page_title="Delinquency EDA", layout="wide")

    st.title("🏦 Delinquency Prediction – Exploratory Data Analysis")
    st.markdown("""
    This app explores the credit card customer dataset for predicting delinquency risk.
    The analysis focuses on data quality, target imbalance, and key risk indicators.
    """)

    # Sidebar for data source
    with st.sidebar:
        st.header("📊 Data Source")
        uploaded_file = st.file_uploader(
            "Upload dataset (Excel or CSV)",
            type=["xlsx", "xls", "xlsm", "csv"],
            help=(
                "If you don't upload a file, the app will try to use the bundled "
                f"file at `{DATA_PATH}`."
            ),
        )
        show_raw = st.checkbox("Show raw data preview", value=False)

    data_src = uploaded_file if uploaded_file is not None else DATA_PATH

    try:
        df = load_data(data_src)
    except FileNotFoundError:
        st.error(
            f"Could not find data file at `{DATA_PATH}`. "
            "Make sure you are running this app from the project root, or upload "
            "a dataset using the sidebar."
        )
        return
    except ValueError as exc:
        st.error(str(exc))
        return

    # ===== SECTION 1: DATASET OVERVIEW =====
    st.header("1️⃣ Dataset Overview")

    # Check the target encoding
    st.write("### Verify Target Encoding")
    st.write("Sample of Delinquent vs Non-delinquent customers:")

    # Show a few examples
    delinquent_sample = df[df['Delinquent_Account'] == 1][['Customer_ID', 'Missed_Payments', 'Credit_Score', 'Income', 'Delinquent_Account']].head()
    non_delinquent_sample = df[df['Delinquent_Account'] == 0][['Customer_ID', 'Missed_Payments', 'Credit_Score', 'Income', 'Delinquent_Account']].head()

    st.write("**Delinquent Customers (should have MORE missed payments, LOWER scores):**")
    st.dataframe(delinquent_sample)

    st.write("**Non-Delinquent Customers (should have FEWER missed payments, HIGHER scores):**")
    st.dataframe(non_delinquent_sample)

    # Check means
    st.write("### Mean Comparison")
    comparison = df.groupby('Delinquent_Account')[['Missed_Payments', 'Credit_Score', 'Income']].mean()
    st.dataframe(comparison)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", df.shape[0])
    with col2:
        st.metric("Total Columns", df.shape[1])
    with col3:
        st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")

    if show_raw:
        with st.expander("📋 View Raw Data"):
            st.dataframe(df.head(20), use_container_width=True)

    # Column types summary
    with st.expander("📑 Column Types Summary"):
        col_types = df.dtypes.value_counts().rename_axis("Data Type").reset_index(name="Count")
        st.dataframe(col_types, use_container_width=True)
        st.dataframe(df.dtypes.rename("Data Type").to_frame(), use_container_width=True)

    # ===== SECTION 2: MISSING DATA ANALYSIS =====
    st.header("2️⃣ Missing Data Analysis")
    
    missing = df.isna().sum().rename("Missing Count").to_frame()
    missing["Missing %"] = (missing["Missing Count"] / len(df)) * 100
    missing = missing[missing["Missing Count"] > 0].sort_values("Missing %", ascending=False)
    
    if len(missing) > 0:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Missing Values Summary")
            st.dataframe(missing.style.format({"Missing %": "{:.2f}%"}), use_container_width=True)
            
            # Add interpretation
            st.info(f"""
            **Key Findings:**
            - {len(missing)} columns have missing values
            - Total missing cells: {missing['Missing Count'].sum()} ({(missing['Missing Count'].sum() / (len(df) * len(df.columns)) * 100):.2f}% of dataset)
            """)
        
        with col2:
            st.subheader("Missing Data Visualization")
            fig_missing, ax_missing = plt.subplots(figsize=(8, max(4, len(missing) * 0.4)))
            sns.barplot(data=missing.reset_index(), y="index", x="Missing %", ax=ax_missing, palette="Reds_r")
            ax_missing.set_xlabel("Missing Percentage (%)")
            ax_missing.set_ylabel("Column")
            ax_missing.set_title("Missing Data by Column")
            for i, v in enumerate(missing["Missing %"].values):
                ax_missing.text(v + 0.2, i, f"{v:.1f}%", va="center")
            st.pyplot(fig_missing)
    else:
        st.success("✅ No missing values detected in the dataset!")

    # Imputation recommendations
    if len(missing) > 0:
        with st.expander("💡 Recommended Imputation Strategies"):
            st.markdown("""
            **Based on EDA findings:**
            
            - **Income** (7.8% missing): Use **median imputation**, optionally stratified by Employment_Status
            - **Loan_Balance** (5.8% missing): Use **median imputation**, potentially stratified by delinquency status
            - **Credit_Score** (0.4% missing): Simple **median imputation** due to low missing rate
            
            *Rationale:* Median is robust to outliers and maintains distribution shape better than mean for financial data.
            """)

    # ===== SECTION 3: TARGET ANALYSIS =====
    st.header("3️⃣ Target Variable Analysis")
    
    # Heuristic default: pick the first column whose name suggests delinquency/default
    default_target = None
    for col in df.columns:
        lower = col.lower()
        if any(key in lower for key in ["delinquent", "default", "target"]):
            default_target = col
            break

    target_col = st.selectbox(
        "Select target (delinquency) column",
        options=df.columns.tolist(),
        index=(df.columns.tolist().index(default_target) if default_target in df.columns else 0),
        help="Choose the column that represents whether a customer is delinquent.",
    )

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Target Distribution")
        target_counts = df[target_col].value_counts(dropna=False).sort_index()
        target_pct = (target_counts / target_counts.sum() * 100).round(2)
        
        target_df = pd.DataFrame({
            "Value": target_counts.index,
            "Count": target_counts.values,
            "Percentage": target_pct.values
        })
        st.dataframe(target_df.style.format({"Percentage": "{:.2f}%"}), use_container_width=True)
        
        # Class imbalance warning
        if len(target_counts) == 2:
            minority_pct = min(target_pct.values)
            if minority_pct < 30:
                st.warning(f"""
                ⚠️ **Class Imbalance Detected!**
                
                Minority class represents only {minority_pct:.1f}% of data.
                
                **Recommendations:**
                - Use appropriate evaluation metrics (Precision, Recall, F1, ROC-AUC)
                - Consider class weighting in models
                - Apply resampling techniques if needed
                """)
    
    with col2:
        st.subheader("Target Distribution Chart")
        fig_target, ax_target = plt.subplots(figsize=(6, 4))
        bars = ax_target.bar(target_counts.index.astype(str), target_counts.values, 
                             color=['#2ecc71', '#e74c3c'])
        ax_target.set_xlabel(target_col)
        ax_target.set_ylabel("Count")
        ax_target.set_title(f"Distribution of {target_col}")
        
        # Add percentage labels on bars
        for bar, count, pct in zip(bars, target_counts.values, target_pct.values):
            height = bar.get_height()
            ax_target.text(bar.get_x() + bar.get_width()/2., height,
                          f'{count}\n({pct:.1f}%)',
                          ha='center', va='bottom')
        st.pyplot(fig_target)

    # ===== SECTION 4: CORRELATION ANALYSIS =====
    st.header("4️⃣ Correlation Analysis")
    
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    
    if target_col in num_cols:
        st.subheader(f"Feature Correlations with {target_col}")
        
        corr = df[num_cols].corr()[target_col].drop(target_col).sort_values(ascending=False)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.dataframe(
                corr.rename("Correlation").to_frame().style.format("{:.4f}")
                .background_gradient(cmap="RdYlGn", axis=0, vmin=-1, vmax=1),
                use_container_width=True
            )
            
            st.info("""
            **Interpretation:**
            - All correlations are relatively weak (|r| < 0.3)
            - Suggests delinquency is **multi-factorial**
            - No single feature strongly predicts delinquency
            - Model should leverage feature combinations
            """)
        
        with col2:
            fig_corr, ax_corr = plt.subplots(figsize=(6, max(4, len(corr) * 0.35)))
            colors = ['#e74c3c' if x < 0 else '#2ecc71' for x in corr.values]
            sns.barplot(x=corr.values, y=corr.index, ax=ax_corr, palette=colors)
            ax_corr.set_xlabel("Correlation Coefficient")
            ax_corr.set_title(f"Correlation with {target_col}")
            ax_corr.axvline(x=0, color='black', linestyle='--', linewidth=0.8)
            st.pyplot(fig_corr)
        
        # Full correlation heatmap
        with st.expander("🔥 View Full Correlation Heatmap"):
            fig_heatmap, ax_heatmap = plt.subplots(figsize=(12, 10))
            corr_matrix = df[num_cols].corr()
            sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", 
                       center=0, ax=ax_heatmap, square=True, linewidths=0.5)
            ax_heatmap.set_title("Full Correlation Matrix")
            st.pyplot(fig_heatmap)

    # ===== SECTION 5: DISTRIBUTION ANALYSIS =====
    st.header("5️⃣ Feature Distributions by Target")
    
    if len(num_cols) > 0 and df[target_col].nunique() <= 10:
        # Key features from EDA report
        key_features = ["Age", "Income", "Credit_Score", "Credit_Utilization", 
                       "Debt_to_Income_Ratio", "Missed_Payments"]
        available_features = [f for f in key_features if f in num_cols and f != target_col]
        
        selected_box = st.multiselect(
            "Select numeric columns for distribution analysis",
            num_cols,
            default=available_features[:3] if available_features else num_cols[:3],
        )

        if selected_box:
            # Create grid layout
            n_features = len(selected_box)
            n_cols = 2
            n_rows = (n_features + 1) // 2
            
            fig_box, axes = plt.subplots(n_rows, n_cols, figsize=(14, 5 * n_rows))
            axes = axes.flatten() if n_rows > 1 else [axes] if n_cols == 1 else axes
            
            for idx, col in enumerate(selected_box):
                ax = axes[idx]
                
                # Create boxplot with better styling
                df_plot = df[[target_col, col]].dropna()
                sns.boxplot(x=df_plot[target_col].astype(str), y=df_plot[col], 
                           ax=ax, palette="Set2", width=0.5)
                
                # Add violin plot overlay for better distribution view
                sns.violinplot(x=df_plot[target_col].astype(str), y=df_plot[col], 
                              ax=ax, palette="Set2", alpha=0.3, inner=None)
                
                ax.set_xlabel(f"{target_col} (0=Non-delinquent, 1=Delinquent)")
                ax.set_ylabel(col)
                ax.set_title(f"{col} Distribution by Delinquency Status", fontweight="bold")
                ax.grid(axis='y', alpha=0.3)
            
            # Hide extra subplots
            for idx in range(n_features, len(axes)):
                axes[idx].axis('off')
            
            plt.tight_layout()
            st.pyplot(fig_box)
            
            # Statistical summary
            with st.expander("📊 Statistical Summary by Target"):
                for col in selected_box:
                    st.markdown(f"**{col}:**")
                    summary = df.groupby(target_col)[col].describe().T
                    st.dataframe(summary.style.format("{:.2f}"), use_container_width=True)

    # ===== SECTION 6: NUMERIC DISTRIBUTIONS =====
    st.header("6️⃣ Overall Feature Distributions")
    
    if num_cols:
        selected_num = st.multiselect(
            "Select numeric columns to plot",
            num_cols,
            default=num_cols[:6],
            help="View histograms with KDE overlay to understand feature distributions"
        )

        if selected_num:
            n_features = len(selected_num)
            n_cols_plot = 3
            n_rows_plot = (n_features + n_cols_plot - 1) // n_cols_plot
            
            fig, axes = plt.subplots(n_rows_plot, n_cols_plot, 
                                    figsize=(15, 4 * n_rows_plot))
            axes = axes.flatten() if n_rows_plot > 1 else [axes] if n_cols_plot == 1 else axes

            for idx, col in enumerate(selected_num):
                ax = axes[idx]
                data = df[col].dropna()
                
                # Histogram with KDE
                sns.histplot(data, kde=True, ax=ax, color="#3498db", alpha=0.6)
                
                # Add mean and median lines
                mean_val = data.mean()
                median_val = data.median()
                ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
                ax.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')
                
                ax.set_title(f"{col} Distribution", fontweight="bold")
                ax.legend()
                ax.grid(axis='y', alpha=0.3)

            # Hide extra subplots
            for idx in range(n_features, len(axes)):
                axes[idx].axis('off')
            
            plt.tight_layout()
            st.pyplot(fig)

    # ===== SECTION 7: KEY INSIGHTS =====
    st.header("7️⃣ Key Insights & Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ Strengths")
        st.markdown("""
        - Dataset is relatively clean (minimal missing data)
        - Good sample size (500 records)
        - Mix of demographic, credit behavior, and account features
        - All key risk factors are represented
        """)
    
    with col2:
        st.subheader("⚠️ Challenges")
        st.markdown("""
        - Significant class imbalance (~16% delinquent)
        - Weak individual feature correlations
        - Missing data in Income and Loan_Balance
        - Overlapping distributions between classes
        """)
    
    st.subheader("🎯 Next Steps")
    st.markdown("""
    1. **Data Preparation:**
       - Implement median imputation for Income, Loan_Balance, Credit_Score
       - Validate imputation doesn't introduce bias
    
    2. **Feature Engineering:**
       - Create interaction terms (e.g., Credit_Utilization × Missed_Payments)
       - Consider binning continuous variables
       - Explore polynomial features
    
    3. **Modeling Strategy:**
       - Use appropriate metrics: Precision, Recall, F1, ROC-AUC
       - Apply class weighting or SMOTE for imbalance
       - Start with baseline models (Logistic Regression, Random Forest)
       - Tune decision thresholds based on business risk tolerance
    
    4. **Validation:**
       - Cross-validation with stratified splits
       - Monitor for fairness across demographic groups
       - Ensure model interpretability for regulatory compliance
    """)


if __name__ == "__main__":
    main()