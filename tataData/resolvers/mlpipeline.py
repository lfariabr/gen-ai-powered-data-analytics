"""
ML Pipeline resolver - Handles model preparation and ML logic for delinquency prediction
"""
import pandas as pd
import numpy as np


# ===== DATA PREPARATION FUNCTIONS =====

def get_imputation_recommendations() -> dict:
    """
    Get recommended imputation strategies based on EDA findings.

    Returns:
        Dictionary with imputation recommendations
    """
    return {
        "Income": {
            "strategy": "Median imputation, stratified by Employment_Status",
            "missing_pct": "7.8%",
            "rationale": "Preserves group-level distributions"
        },
        "Loan_Balance": {
            "strategy": "Median imputation, stratified by delinquency status",
            "missing_pct": "5.8%",
            "rationale": "Avoids distortion in imbalanced datasets"
        },
        "Credit_Score": {
            "strategy": "Straight median imputation",
            "missing_pct": "0.4%",
            "rationale": "Minimal missingness"
        }
    }


# ===== MODEL SELECTION FUNCTIONS =====

def get_model_recommendations(df: pd.DataFrame, target_col: str) -> dict:
    """
    Get model recommendations based on dataset characteristics.

    Args:
        df: Input dataframe
        target_col: Target column name

    Returns:
        Dictionary with model recommendations
    """
    # Calculate class balance
    target_counts = df[target_col].value_counts()
    minority_pct = (target_counts.min() / target_counts.sum()) * 100

    recommendations = {
        "class_imbalance": {
            "minority_pct": minority_pct,
            "severity": "severe" if minority_pct < 20 else "moderate" if minority_pct < 40 else "mild",
            "strategies": [
                "Use appropriate evaluation metrics (Precision, Recall, F1, ROC-AUC)",
                "Consider class weighting in models",
                "Apply resampling techniques if needed"
            ]
        },
        "suggested_models": [
            {
                "name": "Logistic Regression",
                "pros": ["Easy to interpret", "Works well with structured data", "Good baseline"],
                "cons": ["May struggle with weak individual correlations"],
                "when_to_use": "For probability-based predictions and business interpretability"
            },
            {
                "name": "Decision Tree",
                "pros": ["Transparent decision paths", "Handles categorical data", "Clear risk segmentation"],
                "cons": ["Prone to overfitting"],
                "when_to_use": "When explainability is critical for stakeholders"
            },
            {
                "name": "Random Forest",
                "pros": ["Handles feature interactions", "Robust to outliers", "Good performance"],
                "cons": ["Less interpretable than decision trees"],
                "when_to_use": "When accuracy is prioritized and data quality is good"
            },
            {
                "name": "Gradient Boosting",
                "pros": ["State-of-the-art performance", "Captures complex patterns"],
                "cons": ["More computational resources needed", "Hyperparameter tuning required"],
                "when_to_use": "When maximum predictive performance is needed"
            }
        ]
    }

    return recommendations


def get_chosen_model_logic() -> dict:
    """
    Get the logic for the chosen predictive model (Logistic Regression).

    Returns:
        Dictionary with model logic and workflow
    """
    return {
        "model_type": "Logistic Regression",
        "description": "A statistical model that predicts the probability of delinquency using a logistic function",
        "workflow": [
            "1. Data preprocessing: Handle missing values, encode categorical variables",
            "2. Feature selection: Choose relevant predictors (Income, Credit_Score, etc.)",
            "3. Model training: Fit logistic regression on training data",
            "4. Probability prediction: Output delinquency probability (0-1)",
            "5. Threshold application: Classify as delinquent if probability > threshold"
        ],
        "key_features": [
            "Income - Financial stability indicator",
            "Credit_Score - Historical credit behavior",
            "Credit_Utilization - Current debt burden",
            "Debt_to_Income_Ratio - Debt capacity measure",
            "Missed_Payments - Recent payment behavior"
        ],
        "pseudocode": """
# Logistic Regression Model Logic
def predict_deliquency_probability(customer_data):
    # Step 1: Preprocess features
    features = preprocess_features(customer_data)

    # Step 2: Calculate log-odds
    log_odds = intercept + sum(coefficient_i * feature_i for all features)

    # Step 3: Convert to probability
    probability = 1 / (1 + exp(-log_odds))

    # Step 4: Return probability and classification
    return {
        'delinquency_probability': probability,
        'prediction': 'Delinquent' if probability > 0.5 else 'Non-delinquent'
    }
        """
    }


# ===== EVALUATION FUNCTIONS =====

def get_evaluation_metrics_guide() -> dict:
    """
    Get guide for model evaluation metrics.

    Returns:
        Dictionary with metric definitions and interpretation
    """
    return {
        "Accuracy": {
            "definition": "Overall correctness of the model (correct predictions / total predictions)",
            "use_case": "General performance overview",
            "limitation": "Misleading for imbalanced datasets"
        },
        "Precision": {
            "definition": "Of predicted delinquent customers, how many are actually delinquent",
            "use_case": "When false positives are costly",
            "formula": "TP / (TP + FP)"
        },
        "Recall": {
            "definition": "Of actual delinquent customers, how many are correctly identified",
            "use_case": "When false negatives are costly (financial loss)",
            "formula": "TP / (TP + FN)"
        },
        "F1 Score": {
            "definition": "Weighted balance between precision and recall",
            "use_case": "When both false positives and negatives matter",
            "formula": "2 * (Precision * Recall) / (Precision + Recall)"
        },
        "ROC-AUC": {
            "definition": "Assesses model's ability to distinguish between classes",
            "use_case": "Comprehensive model ranking ability assessment",
            "interpretation": "Close to 1.0 = excellent, Close to 0.5 = random guessing"
        }
    }


# ===== FAIRNESS & ETHICS FUNCTIONS =====

def get_bias_fairness_checklist() -> list:
    """
    Get checklist for bias and fairness assessment.

    Returns:
        List of items to check for bias and fairness
    """
    return [
        "Historical bias: Does the training data contain past unfair decisions?",
        "Selection bias: Are all demographic groups equally represented?",
        "Proxy bias: Could certain variables act as proxies for protected characteristics?",
        "Disparate impact: Does the model disproportionately predict risk for specific groups?",
        "Fairness testing: Use formal metrics (demographic parity, equalized odds)",
        "Explainability: Can predictions be justified to customers?",
        "Regulatory compliance: Does the model comply with fair lending laws?"
    ]


# ===== FEATURE ENGINEERING FUNCTIONS =====

def get_feature_engineering_suggestions() -> dict:
    """
    Get suggestions for feature engineering.

    Returns:
        Dictionary with feature engineering ideas
    """
    return {
        "Interaction Terms": [
            "Credit_Utilization × Missed_Payments",
            "Debt_to_Income_Ratio × Credit_Score",
            "Income × Age"
        ],
        "Temporal Features": [
            "Payment trend from Month_1 to Month_5",
            "Recent payment volatility",
            "Account activity trend"
        ],
        "Binning/Discretization": [
            "Age groups (young, middle-age, senior)",
            "Income brackets (low, medium, high)",
            "Credit score tiers (poor, fair, good, excellent)"
        ],
        "Polynomial Features": [
            "Credit_Score^2",
            "Income^2",
            "Debt_to_Income_Ratio^2"
        ]
    }


# ===== DEPLOYMENT FUNCTIONS =====

def get_next_steps() -> dict:
    """
    Get structured next steps for model development.

    Returns:
        Dictionary with action items
    """
    return {
        "Data Preparation": [
            "Apply median imputation for Income, Loan_Balance, Credit_Score",
            "Validate imputation doesn't introduce bias",
            "Check for outliers and anomalies"
        ],
        "Feature Engineering": [
            "Create interaction terms",
            "Consider binning continuous variables",
            "Explore polynomial features"
        ],
        "Model Development": [
            "Start with baseline models (Logistic Regression, Decision Trees)",
            "Apply class weighting or SMOTE for imbalance",
            "Use stratified K-fold cross-validation"
        ],
        "Evaluation": [
            "Prioritize Recall, Precision, F1, ROC-AUC",
            "Align decision thresholds with business risk tolerance",
            "Perform fairness audits across demographic groups"
        ],
        "Deployment": [
            "Ensure model interpretability",
            "Create monitoring and drift detection",
            "Plan integration with business workflows"
        ]
    }
