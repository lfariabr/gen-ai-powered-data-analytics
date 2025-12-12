# Project Structure

This application has been refactored into a modular architecture for better maintainability and separation of concerns.

## Directory Structure

```
/workspaces/gen-ai-powered-data-analytics/
├── app.py                           # Main entry point - routes between views
├── views/
│   ├── __init__.py                 # Views package
│   ├── EDA.py                      # Exploratory Data Analysis interface
│   └── ModelPlan.py                # Model Planning and recommendations
├── resolvers/
│   ├── __init__.py                 # Resolvers package
│   ├── analyzer.py                 # EDA logic and data analysis functions
│   └── mlpipeline.py               # ML pipeline logic and model recommendations
└── requirements.txt                 # Python dependencies
```

## Component Descriptions

### `app.py` (Main Entry Point)
- Handles data loading and file upload
- Routes between EDA and Model Planning views
- Manages sidebar navigation

### `views/` (Presentation Layer)
#### `views/EDA.py`
Renders the interactive Exploratory Data Analysis interface with:
- Dataset overview section
- Missing data analysis
- Target variable analysis
- Correlation analysis
- Feature distributions by target
- Overall feature distributions
- Key insights and recommendations

#### `views/ModelPlan.py`
Renders model planning guidance with:
- Data imputation strategy
- Predictive model selection and comparison
- Evaluation metrics guide
- Bias, fairness & explainability considerations
- Feature engineering roadmap
- Implementation roadmap

### `resolvers/` (Business Logic Layer)
#### `resolvers/analyzer.py`
Core EDA analysis functions:
- `analyze_missing_data()` - Missing data statistics
- `get_numeric_columns()` - Extract numeric features
- `get_target_column()` - Auto-detect target variable
- `get_target_distribution()` - Target class statistics
- `get_correlation_with_target()` - Feature correlations
- `get_sample_by_target()` - Sample rows by class
- `get_target_comparison()` - Mean feature comparison
- `get_dataset_overview()` - Basic dataset metrics
- `get_column_types_summary()` - Data type overview

#### `resolvers/mlpipeline.py`
ML pipeline guidance functions:
- `get_imputation_recommendations()` - Missing value strategies
- `get_model_recommendations()` - Model suggestions based on data
- `get_evaluation_metrics_guide()` - Metric definitions and use cases
- `get_bias_fairness_checklist()` - Fairness assessment items
- `get_feature_engineering_suggestions()` - Feature ideas
- `get_next_steps()` - Structured development roadmap

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## Architecture Benefits

1. **Separation of Concerns**: Views (UI) separated from business logic (resolvers)
2. **Reusability**: Analyzer and ML pipeline functions can be used independently
3. **Testability**: Each module can be tested in isolation
4. **Maintainability**: Changes to logic don't require UI modifications and vice versa
5. **Scalability**: Easy to add new views or resolver functions
6. **Navigation**: Sidebar menu allows switching between EDA and Model Planning without re-uploading data

## Adding New Features

### Adding a new analysis section to EDA:
1. Create a function in `resolvers/analyzer.py` for the analysis logic
2. Create a render function in `views/EDA.py` to display results
3. Call the render function from `render_eda_app()`

### Adding a new model recommendation:
1. Add helper functions to `resolvers/mlpipeline.py`
2. Create a render function in `views/ModelPlan.py`
3. Call it from `render_model_plan_app()`
