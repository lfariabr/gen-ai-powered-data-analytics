"""
EDA View - Exploratory Data Analysis interface
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from resolvers import analyzer


def render_data_overview_section(df: pd.DataFrame) -> None:
    """Render the dataset overview section."""
    st.header("1️⃣ Dataset Overview")
    
    # Get overview metrics
    overview = analyzer.get_dataset_overview(df)
    
    # Display sample data
    st.write("### Verify Target Encoding")
    st.write("Sample of Delinquent vs Non-delinquent customers:")
    
    target_col = analyzer.get_target_column(df)
    delinquent_sample, non_delinquent_sample = analyzer.get_sample_by_target(df, target_col)
    
    st.write("**Delinquent Customers (should have MORE missed payments, LOWER scores):**")
    st.dataframe(delinquent_sample)
    
    st.write("**Non-Delinquent Customers (should have FEWER missed payments, HIGHER scores):**")
    st.dataframe(non_delinquent_sample)
    
    # Check means
    st.write("### Mean Comparison")
    comparison = analyzer.get_target_comparison(df, target_col)
    st.dataframe(comparison)
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", overview["total_records"])
    with col2:
        st.metric("Total Columns", overview["total_columns"])
    with col3:
        st.metric("Memory Usage", overview["memory_usage_str"])
    
    # Raw data preview (optional)
    if st.checkbox("Show raw data preview", value=False):
        with st.expander("📋 View Raw Data"):
            st.dataframe(df.head(20), use_container_width=True)
    
    # Column types summary
    with st.expander("📑 Column Types Summary"):
        col_types = analyzer.get_column_types_summary(df)
        st.dataframe(col_types, use_container_width=True)
        st.dataframe(df.dtypes.rename("Data Type").to_frame(), use_container_width=True)


def render_missing_data_section(df: pd.DataFrame) -> None:
    """Render the missing data analysis section."""
    st.header("2️⃣ Missing Data Analysis")
    
    missing = analyzer.analyze_missing_data(df)
    
    if len(missing) > 0:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Missing Values Summary")
            st.dataframe(missing.style.format({"Missing %": "{:.2f}%"}), use_container_width=True)
            
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
        
        # Imputation recommendations
        with st.expander("💡 Recommended Imputation Strategies"):
            st.markdown("""
            **Based on EDA findings:**
            
            - **Income** (7.8% missing): Use **median imputation**, optionally stratified by Employment_Status
            - **Loan_Balance** (5.8% missing): Use **median imputation**, potentially stratified by delinquency status
            - **Credit_Score** (0.4% missing): Simple **median imputation** due to low missing rate
            
            *Rationale:* Median is robust to outliers and maintains distribution shape better than mean for financial data.
            """)
    else:
        st.success("✅ No missing values detected in the dataset!")


def render_target_analysis_section(df: pd.DataFrame, target_col: str = None) -> str:
    """
    Render the target variable analysis section.
    
    Args:
        df: Input dataframe
        target_col: Target column (if None, will be auto-detected)
        
    Returns:
        The selected target column
    """
    st.header("3️⃣ Target Variable Analysis")
    
    # Auto-detect target if not provided
    if target_col is None:
        target_col = analyzer.get_target_column(df)
    
    # Allow user to select target
    target_col = st.selectbox(
        "Select target (delinquency) column",
        options=df.columns.tolist(),
        index=(df.columns.tolist().index(target_col) if target_col in df.columns else 0),
        help="Choose the column that represents whether a customer is delinquent.",
    )
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Target Distribution")
        target_df, target_counts = analyzer.get_target_distribution(df, target_col)
        target_pct = (target_counts / target_counts.sum() * 100)
        
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
        fig_target, ax_target = plt.subplots(figsize=(7, 5))
        
        explode = [0.05 if i == target_counts.values.argmin() else 0 for i in range(len(target_counts))]
        colors = ['#2ecc71', '#e74c3c'] if len(target_counts) == 2 else sns.color_palette("Set2", len(target_counts))
        
        wedges, texts, autotexts = ax_target.pie(
            target_counts.values,
            labels=[f'{label}\n({count:,})' for label, count in zip(target_counts.index.astype(str), target_counts.values)],
            autopct='%1.1f%%',
            startangle=140,
            colors=colors,
            explode=explode,
            shadow=True,
            textprops={'fontsize': 10, 'weight': 'bold'}
        )
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(11)
            autotext.set_weight('bold')
        
        ax_target.axis('equal')
        ax_target.set_title(f"Distribution of {target_col}", fontsize=12, fontweight='bold', pad=20)
        st.pyplot(fig_target)
    
    return target_col


def render_correlation_analysis_section(df: pd.DataFrame, target_col: str) -> None:
    """Render the correlation analysis section."""
    st.header("4️⃣ Correlation Analysis")
    
    num_cols = analyzer.get_numeric_columns(df)
    
    if target_col not in num_cols:
        st.info(f"Target column '{target_col}' is not numeric. Skipping correlation analysis.")
        return
    
    st.subheader(f"Feature Correlations with {target_col}")
    
    corr = analyzer.get_correlation_with_target(df, target_col)
    
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


def render_distribution_by_target_section(df: pd.DataFrame, target_col: str) -> None:
    """Render feature distributions by target section."""
    st.header("5️⃣ Feature Distributions by Target")
    
    num_cols = analyzer.get_numeric_columns(df)
    
    if len(num_cols) == 0 or df[target_col].nunique() > 10:
        st.info("Not enough numeric columns or too many target classes for this analysis.")
        return
    
    key_features = ["Age", "Income", "Credit_Score", "Credit_Utilization",
                   "Debt_to_Income_Ratio", "Missed_Payments"]
    available_features = [f for f in key_features if f in num_cols and f != target_col]
    
    selected_box = st.multiselect(
        "Select numeric columns for distribution analysis",
        num_cols,
        default=available_features[:3] if available_features else num_cols[:3],
    )
    
    if selected_box:
        n_features = len(selected_box)
        n_cols_plot = 2
        n_rows = (n_features + 1) // 2
        
        fig_box, axes = plt.subplots(n_rows, n_cols_plot, figsize=(14, 5 * n_rows))
        axes = axes.flatten() if n_rows > 1 else [axes] if n_cols_plot == 1 else axes
        
        for idx, col in enumerate(selected_box):
            ax = axes[idx]
            df_plot = df[[target_col, col]].dropna()
            
            sns.boxplot(x=df_plot[target_col].astype(str), y=df_plot[col],
                       ax=ax, palette="Set2", width=0.5)
            sns.violinplot(x=df_plot[target_col].astype(str), y=df_plot[col],
                          ax=ax, palette="Set2", alpha=0.3, inner=None)
            
            ax.set_xlabel(f"{target_col} (0=Non-delinquent, 1=Delinquent)")
            ax.set_ylabel(col)
            ax.set_title(f"{col} Distribution by Delinquency Status", fontweight="bold")
            ax.grid(axis='y', alpha=0.3)
        
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


def render_overall_distributions_section(df: pd.DataFrame) -> None:
    """Render overall feature distributions section."""
    st.header("6️⃣ Overall Feature Distributions")
    
    num_cols = analyzer.get_numeric_columns(df)
    
    if not num_cols:
        st.info("No numeric columns found.")
        return
    
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
            
            sns.histplot(data, kde=True, ax=ax, color="#3498db", alpha=0.6)
            
            mean_val = data.mean()
            median_val = data.median()
            ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
            ax.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')
            
            ax.set_title(f"{col} Distribution", fontweight="bold")
            ax.legend()
            ax.grid(axis='y', alpha=0.3)
        
        for idx in range(n_features, len(axes)):
            axes[idx].axis('off')
        
        plt.tight_layout()
        st.pyplot(fig)


def render_key_insights_section() -> None:
    """Render key insights and recommendations section."""
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


def render_eda_app(df: pd.DataFrame) -> None:
    """
    Render the complete EDA application.
    
    Args:
        df: Input dataframe to analyze
    """
    st.title("🏦 Delinquency Prediction – Exploratory Data Analysis")
    st.markdown("""
    This app explores the credit card customer dataset for predicting delinquency risk.
    The analysis focuses on data quality, target imbalance, and key risk indicators.
    """)
    
    # Render all sections
    render_data_overview_section(df)
    render_missing_data_section(df)
    target_col = render_target_analysis_section(df)
    render_correlation_analysis_section(df, target_col)
    render_distribution_by_target_section(df, target_col)
    render_overall_distributions_section(df)
    render_key_insights_section()
