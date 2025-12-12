"""
Analyzer resolver - Handles data analysis and EDA logic
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze missing data in the dataframe.
    
    Args:
        df: Input dataframe
        
    Returns:
        DataFrame with missing data statistics
    """
    missing = df.isna().sum().rename("Missing Count").to_frame()
    missing["Missing %"] = (missing["Missing Count"] / len(df)) * 100
    missing = missing[missing["Missing Count"] > 0].sort_values("Missing %", ascending=False)
    return missing


def get_numeric_columns(df: pd.DataFrame) -> list:
    """Get all numeric columns from dataframe."""
    return df.select_dtypes(include=["number"]).columns.tolist()


def get_target_column(df: pd.DataFrame) -> str:
    """
    Heuristically identify the target column.
    Looks for columns with names suggesting delinquency/default/target.
    """
    for col in df.columns:
        lower = col.lower()
        if any(key in lower for key in ["delinquent", "default", "target"]):
            return col
    return df.columns[0] if len(df.columns) > 0 else None


def get_target_distribution(df: pd.DataFrame, target_col: str) -> pd.DataFrame:
    """
    Get target variable distribution.
    
    Args:
        df: Input dataframe
        target_col: Target column name
        
    Returns:
        DataFrame with target distribution statistics
    """
    target_counts = df[target_col].value_counts(dropna=False).sort_index()
    target_pct = (target_counts / target_counts.sum() * 100).round(2)
    
    target_df = pd.DataFrame({
        "Value": target_counts.index,
        "Count": target_counts.values,
        "Percentage": target_pct.values
    })
    return target_df, target_counts


def get_correlation_with_target(df: pd.DataFrame, target_col: str) -> pd.Series:
    """
    Calculate correlation of all numeric features with target.
    
    Args:
        df: Input dataframe
        target_col: Target column name
        
    Returns:
        Series of correlations sorted by absolute value
    """
    num_cols = get_numeric_columns(df)
    
    if target_col not in num_cols:
        return pd.Series(dtype=float)
    
    corr = df[num_cols].corr()[target_col].drop(target_col).sort_values(ascending=False)
    return corr


def get_sample_by_target(df: pd.DataFrame, target_col: str, sample_cols: list = None) -> tuple:
    """
    Get sample rows for each target class.
    
    Args:
        df: Input dataframe
        target_col: Target column name
        sample_cols: Columns to display (if None, uses defaults)
        
    Returns:
        Tuple of (delinquent_sample, non_delinquent_sample)
    """
    if sample_cols is None:
        sample_cols = ['Customer_ID', 'Missed_Payments', 'Credit_Score', 'Income', target_col]
    
    # Filter to available columns
    available_cols = [c for c in sample_cols if c in df.columns]
    
    delinquent_sample = df[df[target_col] == 1][available_cols].head()
    non_delinquent_sample = df[df[target_col] == 0][available_cols].head()
    
    return delinquent_sample, non_delinquent_sample


def get_target_comparison(df: pd.DataFrame, target_col: str, compare_cols: list = None) -> pd.DataFrame:
    """
    Get mean values of key features grouped by target.
    
    Args:
        df: Input dataframe
        target_col: Target column name
        compare_cols: Columns to compare (if None, uses defaults)
        
    Returns:
        DataFrame with grouped statistics
    """
    if compare_cols is None:
        compare_cols = ['Missed_Payments', 'Credit_Score', 'Income']
    
    # Filter to available columns
    available_cols = [c for c in compare_cols if c in df.columns]
    
    if not available_cols:
        return pd.DataFrame()
    
    comparison = df.groupby(target_col)[available_cols].mean()
    return comparison


def get_dataset_overview(df: pd.DataFrame) -> dict:
    """
    Get basic dataset statistics.
    
    Args:
        df: Input dataframe
        
    Returns:
        Dictionary with dataset overview metrics
    """
    return {
        "total_records": df.shape[0],
        "total_columns": df.shape[1],
        "memory_usage_kb": df.memory_usage(deep=True).sum() / 1024,
        "memory_usage_str": f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB",
    }


def get_column_types_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Get summary of data types in the dataframe."""
    col_types = df.dtypes.value_counts().rename_axis("Data Type").reset_index(name="Count")
    return col_types
