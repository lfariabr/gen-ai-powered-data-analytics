"""
Main application entry point for Delinquency Prediction system.
Routes between EDA and Model Planning views.
"""
import pandas as pd
import streamlit as st
from pathlib import Path

from views import EDA, ModelPlan


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
    """Main application entry point."""
    st.set_page_config(page_title="Delinquency Prediction", layout="wide")

    # Sidebar for navigation
    st.sidebar.title("📊 Navigation")
    page = st.sidebar.radio(
        "Select a view:",
        ["Exploratory Data Analysis", "Model Planning"],
        help="Choose between EDA or Model Planning"
    )

    st.sidebar.divider()
    
    # Data upload section
    st.sidebar.header("📂 Data Upload")
    uploaded_file = st.sidebar.file_uploader(
        "Upload dataset (Excel or CSV)",
        type=["xlsx", "xls", "xlsm", "csv"],
        help="Upload a file to analyze",
    )

    # Route to appropriate view
    if page == "Exploratory Data Analysis":
        if uploaded_file is None:
            st.info("👆 Please upload a dataset using the sidebar to begin the analysis")
            return

        try:
            df = load_data(uploaded_file)
        except FileNotFoundError:
            st.error(
                "Could not find data file. "
                "Make sure you are running this app from the project root, or upload "
                "a dataset using the sidebar."
            )
            return
        except ValueError as exc:
            st.error(str(exc))
            return

        # Render EDA view
        EDA.render_eda_app(df)

    else:  # Model Planning
        # Model Planning doesn't require data upload
        ModelPlan.render_model_plan_app()


if __name__ == "__main__":
    main()