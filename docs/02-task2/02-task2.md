# Task 02 overview

## What you'll learn
- How to leverage GenAI for predictive modeling without coding. 
- Common techniques for credit risk modeling (e.g., decision trees, logistic regression, neural networks). 
- Evaluating model performance and ethical considerations (bias, explainability, fairness). 
- How to utilize GenAI tools like ChatGPT or Google Gemini to generate model code and refine predictions.

## What you'll do
- Use GenAI tools to generate model logic for predicting customer delinquency.
- Choose and justify the best predictive approach.
- Outline a plan to evaluate model accuracy and reliability.

---

## Let's get started

You’re back in a virtual check-in with Charithra to discuss the next phase of your work with Geldium. After completing the report, you now have a clearer understanding of the dataset—its gaps, inconsistencies, and key risk indicators. Now, it’s time to move beyond exploration and into prediction.

"Geldium wants to use AI to predict which customers are at risk of missing payments so they can take proactive steps to reduce delinquency. Our goal is to develop a model that supports the Collections team in prioritizing outreach and intervention strategies."

Your role in this phase is to:
- Use **GenAI tools** to develop a **predictive model** for identifying high-risk customers.
- Choose and **justify the best approach**—whether decision trees, logistic regression, or another technique.
- Define a plan to evaluate model performance while ensuring fairness and explainability.

Geldium will rely on this model to enhance risk assessment and guide intervention decisions. Your structured approach will help determine how accurate and reliable the AI-driven predictions will be.

"Think critically about your approach," Charithra adds. "Explain why you selected a particular method and how we’ll ensure the model performs well in real-world conditions. This isn't just about prediction—it’s about making responsible, data-driven decisions."

It’s time to take the insights from your EDA findings and transform them into an actionable AI-driven delinquency prediction model.

---

## How to leverage GenAI for predictive modeling without coding

### First, what is predictive modeling?

Predictive modeling is the process of **using historical data to forecast future outcomes**. In the context of financial services, it helps institutions like Geldium identify customers who are at risk of delinquency so they can take proactive measures. Traditional predictive modeling typically requires coding expertise, but GenAI tools can assist analysts in building, testing, and refining models with less manual coding.

Instead of manually programming statistical models, GenAI can:
- Suggest appropriate modeling techniques based on dataset characteristics.
- Draft a description of model logic, or even sample code.
- Assist in interpreting results and refining model performance.

By leveraging no-code AI solutions, analysts and business professionals can conceptualize predictive models without needing to be machine learning experts. However, while these tools simplify the modeling process, the outputs they generate must still be validated and refined by experienced analysts to ensure accuracy and reliability in decision-making.

---

## How GenAI assists in predictive modeling

GenAI simplifies the predictive modeling process by guiding users through key steps.

### 1. Selecting the right model type
Predictive modeling involves choosing the best algorithm for the task. GenAI can analyze dataset characteristics and recommend the most suitable techniques. However, understanding these models yourself is key to making an informed decision.
- Decision trees – Good for explaining why a prediction was made.
- Logistic regression – Useful for predicting binary outcomes (e.g., delinquent vs. non-delinquent).
- Neural networks – Effective for complex patterns but harder to interpret.

We will explore these models further in the next section to help you select the right approach for this task.

> -💡 Example GenAI prompt: "Based on this dataset, which predictive modeling techniques are best suited for identifying customers likely to miss payments? Explain why."

### 2. Generating model code without coding
With the right prompts, GenAI can generate an initial modeling workflow in Python, R, or SQL. However, these outputs should be viewed as a starting point—manual review and refinement are essential to ensure alignment with best practices..

> -💡 Example GenAI prompt:"Generate a logistic regression model framework using this dataset to predict customer delinquency. Provide an explanation of each step, ensuring outputs are reviewed and refined for accuracy and fairness."

### 3. Evaluating model performance
Once a model is built, its accuracy must be assessed. GenAI can:

- Suggest evaluation metrics (e.g., accuracy, precision, recall).
- Interpret results and suggest improvements.
- Highlight ethical concerns, such as potential biases.

> -💡 Example GenAI prompt: "Evaluate the performance of this predictive model using precision and recall. Identify any biases in the predictions."

By using GenAI-powered modeling, analysts can efficiently build and refine predictive models without needing a technical background, making AI-powered decision-making more accessible in financial services.

---

## Common techniques for credit risk modeling

Now that you understand how GenAI assists in predictive modeling, let's expand further on three commonly used techniques for credit risk assessment. Each has strengths and trade-offs, and your task will involve choosing the most suitable model for predicting delinquency risk.

### 1. Decision trees – easy to interpret, great for risk assessment

Decision trees split data into branches based on key features (e.g., income level, number of missed payments). At each step, the model asks a yes or no question, guiding decisions down different paths.

**Why use it for credit risk?**

- Transparency – Easy to explain to stakeholders.
- Handles different types of data well – Works with both numerical and categorical data.
- Identifies key risk factors – Shows which customer attributes are most predictive of delinquency.

> - 💡 Example GenAI prompt: "Generate a decision tree model to predict delinquency risk based on income, credit utilization, and missed payments. Explain how the model determines risk categories."

### 2. Logistic regression – simple, reliable, and great for probability estimation
Logistic regression predicts the probability of an event occurring, such as whether a customer will or won’t become delinquent. It assigns a probability score (0 to 1), where a threshold (e.g., 0.5) determines classification.

**Why use it for credit risk?**

- Great for binary predictions (e.g., delinquent vs. non-delinquent).
- Easy to interpret – Shows the impact of each variable on the outcome.
- Works well with structured data – Suitable for datasets with clear numerical patterns.

> - 💡 Example GenAI prompt: "Explain how logistic regression can be used to predict credit card delinquency. Generate a simple model using income, debt-to-income ratio, and payment history."

### 3. Neural networks – powerful for complex patterns but harder to interpret
Neural networks mimic the way human brains process information. They detect complex relationships between variables, making them highly effective for large datasets. However, they operate like a "black box," meaning their decision-making process is less transparent.

**Why use it for credit risk?**

- Can uncover deep patterns in customer financial behavior.
- More accurate on large datasets than simpler models.
- Useful for predicting long-term credit risk trends.

> - 💡 Example GenAI prompt: "Create a basic neural network model for predicting delinquency risk. Compare its strengths and weaknesses against decision trees and logistic regression."

### Which model should you choose?
Each model has strengths and trade-offs. In this task, your goal is to choose the best approach based on Geldium’s dataset and business needs.

- ✅ Use decision trees if you need transparency and clear risk segmentation.
- ✅ Use logistic regression if you need a probability-based approach that is easy to interpret.
- ✅ Use neural networks if you have a complex dataset and need high accuracy at the cost of explainability.

---

## Evaluating model performance

Now that you've explored different modeling techniques for predicting delinquency, it’s crucial to assess how well your chosen model performs and whether it produces fair and explainable results. A model that accurately predicts risk but lacks transparency or fairness can create serious ethical and business risks.

This section will guide you through evaluating model accuracy and reliability while considering bias, explainability, and fairness—all essential for making responsible AI-driven decisions in financial services.

A predictive model is only useful if it produces reliable and actionable insights. To measure this, financial analysts and data scientists use key evaluation metrics to determine how well a model identifies high-risk customers while minimizing false predictions.

### 1. Key metrics for model evaluation

Each metric provides a different perspective on model effectiveness. It’s important to use multiple metrics together rather than relying on a single score:

- Accuracy – Measures the overall correctness of the model by dividing correct predictions by the total number of cases.
- Precision (positive predictive value) – Evaluates how many of the customers predicted to be delinquent actually are.
- Recall (sensitivity) – Measures how many actual delinquent customers were correctly identified by the model. High recall is important when missing a delinquent customer could result in financial loss.
- F1 score – A weighted balance between precision and recall. It is useful when both false positives and false negatives are costly.
- AUC-ROC curve (area under the receiver operating characteristic curve) – Assesses how well the model distinguishes between delinquent and non-delinquent customers. A score close to 1 means the model is highly effective at ranking risk levels, while a score near 0.5 suggests the model is no better than random guessing.
- Confusion matrix – A visual breakdown of actual vs. predicted classifications. It helps diagnose specific types of errors and determine whether the model is favoring one outcome over another.

> - 💡Example GenAI prompt: "Evaluate the performance of my credit risk model using precision, recall, and F1 score. Suggest improvements if needed."

### 2. What to do if model performance is poor

If your model is not performing well, there are several ways to improve it:

- Feature engineering – Adjust the dataset by adding or removing variables that may be impacting model predictions. For example, including customer tenure or past delinquency trends may enhance predictive power.
- Rebalancing the dataset – If the dataset is highly skewed (e.g., 95% non-delinquent, 5% delinquent), oversampling delinquent cases or undersampling non-delinquent cases can improve results.
- Trying different models – Some algorithms work better with certain data structures. If logistic regression is underperforming, a decision tree may provide better results.
- Hyperparameter tuning – Fine-tuning model parameters, such as adjusting the threshold for delinquency classification, can improve precision and recall scores.

By applying these strategies, you can refine the predictive model, making it more effective and reliable for Geldium’s credit risk assessments.

---

## Bias, explainability, and fairness in credit risk modeling
AI-driven credit risk models must be accurate, explainable, and fair to ensure responsible financial decision-making. Even well-performing models can introduce bias, produce uninterpretable decisions, or unintentionally disadvantage certain customer groups. Addressing these risks is essential for ethical and legal compliance in financial services.

### Bias
Bias occurs when a model systematically favors or disadvantages certain groups, often due to historical inequalities or imbalanced data.

**Common causes of bias:**

- Historical bias – If past lending decisions were unfair, the model may replicate those patterns.
- Selection bias – If the dataset does not represent all customer demographics equally, predictions may be inaccurate for some groups.
- Proxy bias – Certain variables (e.g., ZIP code) may unintentionally act as proxies for protected characteristics like race or gender.
> - 💡Example GenAI prompt: “Check for bias in this credit risk model. Are certain customer groups unfairly predicted as high risk?”
 
*While GenAI can assist in identifying potential bias patterns, it should not be relied upon as an authoritative tool for bias detection. GenAI itself can embed biases from its training data and may produce misleading results. Best practice is to use formal statistical fairness metrics (e.g., disparate impact analysis, demographic parity) alongside human oversight.

### Explainability
Explainability ensures that decision-makers can understand and justify a model’s predictions.

- Decision trees and logistic regression are more interpretable and show clear decision paths.
- Neural networks are highly complex and function as "black boxes," making explainability difficult.
- Analysts use tools like SHAP (Shapley Additive Explanations) to break down how different factors contribute to predictions.
> - 💡Example GenAI prompt: "Explain why this model predicted high delinquency risk for a specific customer."
*While GenAI is great for assisting in summarizing explanations, relying solely on it for explainability presents significant risks—it may "hallucinate" or generate inaccurate justifications that do not reflect the true model logic. Best practice is to use established interpretability frameworks to ensure transparency and accuracy.

### Fairness
A fair model should:

- Avoid systematic disadvantages for certain demographic groups.
- Be tested for disparate impact to ensure fairness.
- Use diverse and representative training data to prevent reinforcing biases.
> - 💡Example GenAI prompt: "Assess fairness in this model’s predictions. Does it disproportionately flag certain customer demographics as high risk?"

*GenAI should not be solely relied upon to assess fairness, as it does not inherently understand regulatory compliance or ethical considerations in financial decision-making. Responsible AI development requires the application of fairness testing frameworks (e.g., equalized odds, demographic parity) and human judgment.

By applying these principles, analysts can ensure that AI-powered risk assessments are transparent, responsible, and unbiased in financial decision-making. However, achieving truly responsible and unbiased financial decision-making also requires human oversight, regulatory compliance, and formal fairness audits that go beyond what GenAI alone can ensure.

---

## Utilizing GenAI tools to generate model code and refine predictions
GenAI tools like ChatGPT, Google Gemini, and DeepSeek are transforming the way predictive modeling is conducted, enabling analysts to build and refine models without writing complex code. These tools can assist with model selection, code generation, performance evaluation, and troubleshooting, making AI-driven predictions more accessible to non-programmers.

### 1. How GenAI assists in model development
GenAI tools can assist in generating model code in Python, R, or SQL based on simple text-based prompts. While these tools can streamline the coding process, they do not eliminate the need for analysts to understand the underlying logic. AI-generated code may require adjustments, optimization, or debugging to ensure it meets industry standards and performs as expected.

Example use cases:
- Generating a model framework – A user can request a logistic regression model for predicting delinquency, and GenAI will provide an initial code structure. However, it is essential to review, test, and refine the code to ensure correctness and efficiency. 
- Feature selection assistance – GenAI can recommend which variables to include based on the dataset. However, analysts must verify that these selections do not introduce bias or proxy discrimination.
- Hyperparameter tuning – Analysts can optimize model performance by asking for parameter adjustments. While GenAI can suggest modifications, empirical testing and expert judgment are necessary to validate improvements.
> - 💡Example GenAI prompt: "Generate a logistic regression model using this dataset to predict customer delinquency. Include preprocessing steps and evaluation metrics."

### 2. Refining and improving model predictions
After generating a model, it’s crucial to refine predictions to ensure accuracy and fairness. GenAI tools can:

- Suggest modifications to improve precision and recall.
- Evaluate model outputs and identify overfitting or biases.
- Generate alternative models to compare performance.
> - 💡Example GenAI prompt: "Analyze this model’s performance and suggest improvements to increase accuracy and reduce bias."

By leveraging GenAI in this way, analysts can efficiently develop, refine, and validate predictive models, ensuring they are both effective and ethical in credit risk assessment.

---

## Here is your task
Now that you’ve explored Geldium’s dataset and conducted EDA, it’s time to take the next step: outline a predictive modeling approach to forecast which customers are most at risk of delinquency.

Your goal is to use GenAI tools (like ChatGPT, Google Gemini, or DeepSeek) to help scaffold a predictive model concept, select an appropriate modeling approach, and plan how you would evaluate its performance. 

Here’s how to approach the task:

### Step 1: Generate model logic using GenAI
Use a GenAI tool to outline a structured approach for a predictive model based on the dataset provided.  Rather than coding the model, focus on conceptualizing key components, including:

- The type of model you would use (e.g., logistic regression, decision trees, neural networks).
- Key input features and how they contribute to predictions.
- The general workflow of how the model would process the data to generate outputs.
> Note: You’ll be working with the same dataset from Task 1. While you don't have to clean or modify the data, your analysis should reflect what you learned during EDA.

**Prompts to try:**

- Outline a predictive modeling pipeline to forecast credit delinquency, from feature selection to model evaluation.
- Suggest 2 modeling options (simple and complex) for predicting delinquency, and recommend one.
- Explain how the delinquency risk model transforms customer input variables into a final risk prediction, from data ingestion to prediction output.
- Generate sample code or clear pseudocode for building a credit risk prediction model, using relevant features like income, credit utilization, and missed payments.
Action: Summarize your chosen model type in 2–3 sentences and highlight your top 5 input features.

### Step 2: Justify your model choice
Once you've outlined your model, it’s important to explain why you chose it. Use what you’ve learned about model interpretability, accuracy, and use cases in financial services.

- Justify why the selected model is appropriate for predicting delinquency.
- Discuss strengths, trade-offs, and why the model fits Geldium’s needs.
- Consider interpretability, ease of deployment, and handling of financial data.
- Connect your reasoning to real-world business needs (e.g., regulatory compliance, transparency).

Use GenAI to help you draft a justification for your model choice.
    
**Prompts to try:**

- Explain the pros and cons of using logistic regression vs. decision trees for financial risk prediction.
- Compare model options for predicting delinquency and explain how they balance performance and explainability.
- Explain how different model options fit operational needs like speed, scalability, and ease of monitoring.

**Action: Write a 1-paragraph justification connecting your model choice to Geldium’s goals.**

### Step 3: Plan how to evaluate model performance
A good model must predict both accurately and fairly. It’s critical to assess the model’s success and ensure it avoids biased or misleading outcomes. Think about how you would: 

- Identify appropriate evaluation metrics (accuracy, F1 score, AUC, fairness checks).
- Assess the model’s accuracy and reliability
- Check for bias or unfair treatment across different customer groups
- Interpret evaluation metrics and decide when the model needs improvements

Use GenAI to refine your evaluation plan by asking it to suggest evaluation frameworks and bias-detection methods.

**Prompts to try:**

- Suggest a set of metrics to evaluate a financial risk prediction model for fairness, bias, and accuracy.
- Provide examples of bias mitigation techniques in predictive modeling for credit risk.

**Action:**
Outline your evaluation strategy, identifying key metrics (accuracy, F1 score, AUC, fairness checks) and how you would interpret them.

### Step 4: Submit your plan
Using the provided template, submit a structured plan that includes:

- Your generated model logic (either GenAI output or a paraphrased version)
- Your model justification — why you chose it and how it fits the task.
- Your evaluation strategy, explaining how you would assess accuracy and fairness.

> Note: This is a conceptual exercise — you are not expected to write working code. Focus on explaining your thinking and showing how you used GenAI for support.

Deliverable: Submit a Word or PDF file of your plan below.