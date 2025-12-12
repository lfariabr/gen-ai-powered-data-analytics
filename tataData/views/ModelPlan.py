"""
Model Plan View - Predictive modeling planning and recommendations
"""
import streamlit as st
from resolvers import mlpipeline


def render_imputation_section() -> None:
    """Render data imputation recommendations section."""
    st.header("1️⃣ Data Imputation Strategy")
    
    recommendations = mlpipeline.get_imputation_recommendations()
    
    st.markdown("""
    ### Missing Data Treatment Plan
    Based on EDA findings, we recommend the following imputation strategies:
    """)
    
    for var, rec in recommendations.items():
        with st.expander(f"📊 {var} ({rec['missing_pct']} missing)"):
            st.markdown(f"""
            **Strategy:** {rec['strategy']}
            
            **Rationale:** {rec['rationale']}
            """)


def render_model_selection_section() -> None:
    """Render model selection and recommendations section."""
    st.header("2️⃣ Predictive Model Selection")
    
    st.markdown("""
    ### Model Recommendations
    Based on the dataset characteristics, we recommend the following approaches:
    """)
    
    # Create placeholder for recommendations
    # In a real scenario, this would analyze the actual data
    recommendations = {
        "class_imbalance": {
            "severity": "severe",
            "minority_pct": 16,
            "strategies": [
                "Use appropriate evaluation metrics (Precision, Recall, F1, ROC-AUC)",
                "Consider class weighting in models",
                "Apply resampling techniques if needed"
            ]
        }
    }
    
    st.warning(f"""
    ⚠️ **Class Imbalance Detected!**
    
    Minority class represents {recommendations['class_imbalance']['minority_pct']}% of data.
    
    **Recommended Handling Strategies:**
    """)
    
    for strategy in recommendations["class_imbalance"]["strategies"]:
        st.write(f"- {strategy}")
    
    # Model options
    models = [
        {
            "name": "Logistic Regression",
            "pros": ["Easy to interpret", "Works well with structured data", "Good baseline"],
            "cons": ["May struggle with weak individual correlations"],
            "when": "For probability-based predictions and business interpretability"
        },
        {
            "name": "Decision Tree",
            "pros": ["Transparent decision paths", "Handles categorical data", "Clear risk segmentation"],
            "cons": ["Prone to overfitting"],
            "when": "When explainability is critical for stakeholders"
        },
        {
            "name": "Random Forest",
            "pros": ["Handles feature interactions", "Robust to outliers", "Good performance"],
            "cons": ["Less interpretable than decision trees"],
            "when": "When accuracy is prioritized and data quality is good"
        },
        {
            "name": "Gradient Boosting",
            "pros": ["State-of-the-art performance", "Captures complex patterns"],
            "cons": ["More computational resources needed", "Hyperparameter tuning required"],
            "when": "When maximum predictive performance is needed"
        }
    ]
    
    st.subheader("Model Comparison")
    
    for model in models:
        with st.expander(f"🤖 {model['name']}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Advantages:**")
                for pro in model['pros']:
                    st.write(f"✅ {pro}")
            
            with col2:
                st.markdown("**Limitations:**")
                for con in model['cons']:
                    st.write(f"⚠️ {con}")
            
            st.markdown(f"**When to Use:** {model['when']}")


def render_evaluation_metrics_section() -> None:
    """Render model evaluation metrics section."""
    st.header("3️⃣ Model Evaluation Strategy")
    
    metrics_guide = mlpipeline.get_evaluation_metrics_guide()
    
    st.markdown("""
    ### Key Performance Metrics
    A robust evaluation strategy requires multiple metrics for imbalanced classification:
    """)
    
    for metric, details in metrics_guide.items():
        with st.expander(f"📈 {metric}"):
            st.markdown(f"""
            **Definition:** {details['definition']}
            
            **Use Case:** {details['use_case']}
            """)
            
            if 'formula' in details:
                st.markdown(f"**Formula:** `{details['formula']}`")
            
            if 'interpretation' in details:
                st.markdown(f"**Interpretation:** {details['interpretation']}")


def render_bias_fairness_section() -> None:
    """Render bias and fairness considerations section."""
    st.header("4️⃣ Bias, Fairness & Explainability")
    
    st.markdown("""
    ### Responsible AI Considerations
    For financial services, it's critical to ensure models are fair, explainable, and unbiased.
    """)
    
    checklist = mlpipeline.get_bias_fairness_checklist()
    
    st.subheader("Fairness & Bias Checklist")
    
    for i, item in enumerate(checklist, 1):
        st.write(f"{i}. {item}")
    
    # Key considerations
    st.info("""
    **Key Principles:**
    - Transparency: Decision-makers must understand why predictions are made
    - Fairness: Model should not systematically disadvantage demographic groups
    - Compliance: Ensure adherence to fair lending and anti-discrimination laws
    - Auditability: Document model decisions and outcomes for regulatory review
    """)


def render_feature_engineering_section() -> None:
    """Render feature engineering suggestions section."""
    st.header("5️⃣ Feature Engineering Roadmap")
    
    suggestions = mlpipeline.get_feature_engineering_suggestions()
    
    st.markdown("""
    ### Enhancing Predictive Power
    Given weak individual feature correlations, feature engineering is essential:
    """)
    
    for category, features in suggestions.items():
        with st.expander(f"🔧 {category}"):
            for feature in features:
                st.write(f"- {feature}")


def render_next_steps_section() -> None:
    """Render actionable next steps section."""
    st.header("6️⃣ Implementation Roadmap")
    
    next_steps = mlpipeline.get_next_steps()
    
    st.markdown("""
    ### Structured Path to Production
    Follow this roadmap to develop and deploy your delinquency prediction model:
    """)
    
    for phase, actions in next_steps.items():
        with st.expander(f"📋 {phase}"):
            for action in actions:
                st.write(f"✓ {action}")


def render_model_plan_app() -> None:
    """
    Render the complete Model Planning application.
    """
    st.title("🤖 Delinquency Prediction – Model Planning & Strategy")
    st.markdown("""
    This application guides you through the process of developing a predictive model 
    for identifying customers at risk of delinquency. We'll cover model selection, 
    evaluation strategies, bias mitigation, and deployment considerations.
    """)
    
    # Render all sections
    render_imputation_section()
    render_model_selection_section()
    render_evaluation_metrics_section()
    render_bias_fairness_section()
    render_feature_engineering_section()
    render_next_steps_section()
    
    # Footer
    st.divider()
    st.markdown("""
    ### 📚 Resources & Best Practices
    - Ensure all team members understand the model logic and limitations
    - Document assumptions and decisions for regulatory compliance
    - Plan for ongoing monitoring and model retraining
    - Establish feedback loops with the Collections team
    """)
