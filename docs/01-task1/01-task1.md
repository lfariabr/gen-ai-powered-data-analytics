# Task 01 overview

## What you'll learn
- How to conduct exploratory data analysis (EDA) using GenAI. 
- Techniques to handle missing values and ensure data quality. 
- Understanding customer risk factors for delinquency. 
- How to leverage synthetic data generation to enhance datasets when real data is insufficient.

## What you'll do
- Identify key datasets required to predict delinquency. 
- Perform an exploratory analysis on provided datasets, using GenAI tools to assist with summarization, treatment of missing data, risk profiling, and synthetic data creation. 
- Document your findings, including data patterns and anomalies that may impact predictions.

---

## Let's get started

Your team has been working closely with Geldium to enhance their risk assessment strategy. Charithra, your senior manager, has assigned you the first stage of the project: **conducting an exploratory data analysis (EDA)** to assess dataset completeness, identify patterns, and flag potential gaps that could impact delinquency predictions.

In a recent discussion with Geldium’s Head of Collections, they emphasized the need for a more structured, data-driven approach to identifying at-risk customers. Their current methods rely on historical trends and broad segmentation models, which lack the precision required for proactive intervention strategies. Geldium’s leadership is interested in leveraging AI-driven insights, but before any predictive models can be deployed, we need to ensure that the foundational data is reliable and usable.

During your check-in, Charithra outlines your key objectives:

- Review the provided dataset and assess its structure, completeness, and key attributes, and then identify any missing or inconsistent data points that could affect predictions.
- Use GenAI-assisted tools to generate insights while ensuring data confidentiality and avoiding the exposure of sensitive financial information.
- Summarize the patterns, anomalies, and risk indicators that should be considered in later stages of the project in a report.
- This phase is important for setting up a robust predictive modeling process. Your findings will be reviewed by the wider Analytics team and Geldium’s decision-makers to shape the next steps.

With the dataset available and AI tools at your disposal, it’s time to dive into the analysis and provide clear, actionable insights.

---

## AI, Machine Learning, and GenAI – What’s the Difference?

Before diving into exploratory data analysis (EDA), it’s important to understand the broader AI landscape and where Machine Learning (ML) and Generative AI (GenAI) fit into financial risk modeling. Here is a brief run-down:

### What is Artificial Intelligence (AI)?
AI refers to any system that can perform tasks requiring human intelligence, such as recognizing patterns, making decisions, or processing language. It is a broad category that includes both traditional rule-based systems and Machine Learning (ML) models that improve based on data.
 
### What is Machine Learning (ML)?
Machine learning is a subset of AI that learns from historical data to predict future outcomes. In financial services, ML models are used for credit scoring, fraud detection, and risk assessment.

> - Example: A logistic regression model trained on customer repayment history to predict the likelihood of delinquency.
 
### What is Generative AI (GenAI)?
GenAI is a specialized form of AI that can create new content, such as text, images, or structured code, based on training data. Unlike ML, which is designed for structured predictions, GenAI assists with automation, summarization, and data exploration—making it a valuable tool in EDA.

> - Example: Using GenAI to generate a summary of credit risk trends instead of manually coding an exploratory analysis.

---

You won’t be building an ML model from scratch, but you will:

- 📊 Explore patterns in financial data that inform risk assessment.
- ⚙️ Use GenAI tools to summarize insights and guide predictive modeling.
- 🌍 Understand how AI-driven predictions influence real-world decisions.

Now, let’s dive into exploratory data analysis (EDA)!

---

## Introduction to exploratory data analysis (EDA)
Before you start working on your project, it's important to build a solid foundation in the key topics you'll need to understand. This preparation will ensure you have the tools and knowledge necessary to approach your tasks with confidence and skill.

### What is exploratory data analysis?
Exploratory data analysis (EDA) is the first step in understanding a dataset before applying any predictive models or making business decisions. EDA helps analysts uncover patterns, trends, inconsistencies, and missing values to ensure data quality and reliability. In the context of financial services, EDA plays a crucial role in risk assessment, allowing teams to identify key factors contributing to credit card delinquency and build stronger prediction models. Here is why EDA matters in predicting delinquency:

- Ensures data integrity: Identifies missing values, duplicates, and inconsistencies before analysis.
- Highlights patterns and anomalies: Helps detect trends in customer behavior, such as spending patterns before delinquency.
- Prevents biased models: Reduces the risk of unfair treatment by ensuring diverse data representation.
- Supports better decision-making: Provides Geldium’s Collections and Risk teams with clear insights for proactive customer engagement.

Without a thorough EDA process, predictive models can be built on flawed data, leading to inaccurate insights, poor risk management, and potentially unfair decision-making. Later in this task, you will examine a dataset related to delinquency risk, identify missing or inconsistent data points, and generate initial insights using GenAI tools.

---

## Key steps in conducting EDA
EDA consists of four main steps, which can be enhanced with GenAI tools:

### 1 - Understanding the dataset
Before jumping into analysis, take time to familiarize yourself with the dataset. Ask yourself:

- What are the key variables (e.g., payment history, income levels, credit utilization)?
- Are there categorical or numerical data points?
- Are there missing or inconsistent values?

**Using GenAI:** You can use AI-powered summarization tools to quickly scan a dataset and generate an overview. Tools such as ChatGPT or Google Gemini can help interpret column headers, suggest relevant features, and summarize key statistics.

> - 💡 Example prompt: "Analyze this dataset and provide a summary of key columns, including common patterns and missing values."

### 2 - Identifying missing values and outliers
Incomplete data can lead to poor predictions. Missing values in credit risk datasets may result from human error, system failures, or unreported financial activity.

Here are some common techniques for handling missing data:

- Statistical imputation (industry standard): Replace missing values using well-established techniques such as mean, median, or regression-based imputation. (We've provided a resource with further information on imputation below.)
- Understanding missingness patterns: Before filling in missing values, determine whether the data is missing completely at random (MCAR), missing at random (MAR), or missing not at random (MNAR) to avoid introducing bias. This site includes a great overview document explaining the missing data types.
- Removing irrelevant data: If a feature has excessive missing values and cannot be meaningfully imputed without introducing bias, it may be best to exclude it—but only after assessing its impact on model accuracy and fairness..

Using GenAI (for exploration, not direct imputation):
- AI-powered tools can automate missing value detection and summarize data gaps, helping analysts assess which variables require attention.
- GenAI can suggest potential imputation strategies based on statistical best practices, but final decisions should be validated with domain expertise.
- Synthetic data generation may be an option when real data is unavailable, but it should be validated against real-world distributions to prevent bias.

> - 💡 Example prompt: "Identify missing values in this dataset and recommend the best imputation strategy based on industry best practices."

### 3 - Understanding relationships between variables
EDA also involves examining how different features interact. For example:

- Do customers with high credit utilization rates have a higher risk of delinquency?
- Is there a correlation between income levels and late payments?

Using GenAI:
- AI models can automate correlation analysis, helping identify key risk indicators.
- Instead of manually coding formulas, GenAI can summarize variable relationships in natural language.
> - 💡 Example prompt: "Analyze the correlation between customer income and delinquency risk, summarizing key findings in simple terms."

### 4 - Detecting patterns and risk factors
The final step in EDA is to identify patterns that could impact delinquency prediction. These might include:

- Customers who miss one payment often miss multiple.
- Younger customers or those with recently opened accounts may have different risk profiles.

Using GenAI:

- AI models can highlight trends in the data, making it easier to understand how different features contribute to delinquency.
- AI-assisted insights can be refined by asking follow-up questions, ensuring that the analysis remains relevant to Geldium’s objectives.

> - 💡 Example prompt: "Analyze trends in late payments and identify the top 3 risk factors associated with delinquency."

---

Techniques to handle missing values and ensure data quality
Now that you understand how EDA helps assess dataset completeness, the next step is addressing missing values to ensure reliable insights. In financial risk analytics, incomplete or inconsistent data can skew predictions and lead to incorrect risk assessments. When handling missing data, it is critical to first analyze the reason for missingness—whether it is random, systematic, or indicative of underlying biases. While GenAI models can assist in detecting patterns and suggesting imputation strategies, statistical techniques (e.g., mean, median, or regression-based imputation) remain the industry standard due to their transparency and reproducibility. Blindly applying GenAI-generated imputation without understanding data context can introduce significant bias.

What are the common causes of missing data?
Missing data can occur due to:

Random errors (e.g., a system glitch fails to record a payment).
Skewed data collection (e.g., high-income customers are less likely to disclose salary details).
Customer behavior (e.g., financially distressed individuals may avoid reporting debt).
Understanding the cause helps determine the best approach for handling missing values.

How to handle missing values:
Deleting missing data – If only a small percentage of data is missing, removing incomplete entries may be the best approach. However, this can reduce the sample size.
Imputation (replacing missing values) –
Mean, median, or mode imputation fills gaps with typical values.
Forward or backward filling uses existing data trends to estimate missing entries.
AI-Assisted Imputation –
GenAI models can help detect patterns and suggest imputation strategies and statistical techniques (e.g., mean, median, or regression-based imputation).
AI tools can also suggest synthetic data where needed, provided data privacy is maintained.
Beyond missing values, check for duplicates, inconsistent formatting, and logical errors (e.g., high credit scores with multiple missed payments). By maintaining data integrity, you ensure that predictive models generate fair and accurate delinquency assessments.

---

Understanding customer risk factors for delinquency
Now that you’ve learned how to ensure data quality and handle missing values, the next step is identifying key customer risk factors that influence credit card delinquency. Understanding these factors will help refine predictive models and improve intervention strategies.

Why risk factors matter in financial decision-making:
Lenders assess various financial and behavioral indicators to determine whether a customer is likely to miss payments. By analyzing these factors, Geldium’s Collections team can proactively identify customers who may need early intervention, reducing financial losses and improving repayment outcomes.

Key risk factors for delinquency
Payment history – Customers with a history of late or missed payments are more likely to default.
Credit utilization rate – High usage of available credit can indicate financial stress and potential repayment issues.
Debt-to-income (DTI) ratio – A high DTI suggests a customer may struggle to manage their financial obligations.
Recent credit activity – A sudden increase in new credit accounts or loan applications may signal financial instability.
Employment and income stability – Frequent job changes or inconsistent income can contribute to a higher risk of missed payments.
Demographic trends – While AI models must avoid bias, certain patterns (e.g., younger customers with limited credit history) may require additional analysis.
AI-driven models analyze multiple risk factors simultaneously, detecting patterns that may not be immediately obvious. However, ensuring that these models remain fair and explainable is crucial to avoiding biases in decision-making.

---

How to leverage synthetic data generation to enhance datasets
In financial services, incomplete or inconsistent data can make it difficult to build reliable predictive models. If key information is missing—such as payment history or income details—delinquency risk assessments may become inaccurate. When real-world data is limited, sensitive, or incomplete, synthetic data generation can help fill gaps, simulate scenarios, and improve dataset quality while maintaining privacy and compliance.

Synthetic data is artificially generated data that mimics real-world data patterns. Instead of using actual customer records, synthetic data is created using statistical models or AI-driven techniques to supplement missing values or expand datasets for testing. This ensures that no real customer information is exposed while still preserving the integrity of the analysis.

While synthetic data generation can be useful for filling in gaps and expanding datasets, it should be applied with caution in financial risk modeling. Traditional statistical simulation techniques such as Monte Carlo simulations, bootstrapping, and probabilistic modeling are often preferred due to their explainability, reproducibility, and ability to align with industry regulations.

GenAI-generated synthetic data should be:
✔ Validated against real-world distributions to ensure accuracy.
✔ Cross-checked with statistical models to prevent introducing artificial patterns or biases.
✔ Used as a supplementary tool, not a primary data source, especially in regulatory environments.

When to use synthetic data in financial services:
Enhancing small datasets – If real customer data is limited, synthetic records can supplement training data for AI models.
Filling in missing data – When real data is incomplete, synthetic data can approximate realistic values based on existing patterns.
Testing AI models – Before deploying AI risk models, synthetic data can be used to simulate different delinquency scenarios.
Ensuring privacy compliance – Financial data must be handled responsibly. Synthetic data allows analysis without exposing personal customer details.

As you analyze Geldium’s dataset, you may find missing values that could impact delinquency predictions. If removing or imputing data isn’t viable, synthetic data generation can supplement datasets; however, it must be strictly validated to ensure it accurately reflects real-world trends and does not introduce bias. GenAI-assisted synthetic data generation should be used with caution, as improper constraints can lead to unrealistic outputs that misrepresent risk factors.

💡 Example GenAI prompt: “Generate synthetic payment history data for customers with missing records while ensuring that distributions align with historical patterns observed in the dataset (e.g., standard deviations, typical payment behaviors).”

As you explore Geldium’s dataset, consider whether synthetic data could be useful for filling gaps or testing delinquency risk models. Your approach should balance realism, fairness, and privacy to ensure high-quality AI-driven insights.

Ethical considerations:
While synthetic data can enhance dataset completeness, it must be used carefully to avoid:

Introducing bias – Ensure synthetic records reflect realistic patterns.
Misrepresenting risk factors – Avoid generating overly optimistic or pessimistic data.
Compromising compliance – Validate that synthetic data aligns with industry regulations.

---

Here is your task
Before any predictive modeling can take place, it’s crucial to ensure that the dataset you’re working with is complete, accurate, and free of inconsistencies. 

In this task, you will conduct an EDA on Geldium’s dataset to help Tata iQ’s analytics team and Geldium’s decision-makers understand the current state of their data. Your analysis will shape how the company refines its delinquency risk model and improves its intervention strategies.

Here are the steps:

Step 1: Review the dataset and identify key insights
Before predictive modeling can begin, it’s essential to understand the dataset’s structure and assess its quality. In this first step, you'll examine Geldium’s dataset to spot any issues and identify early risk indicators.

What to do:

Open the dataset and review the key columns. Use the Dataset Description Guide to understand what each variable represents.
Use a GenAI tool (like ChatGPT or DeepSeek) to help quickly summarize the dataset and highlight potential issues.
Think about what insights you need from GenAI. What questions would help you explore the dataset effectively? If needed, refer to Section 5 (Key Steps in Conducting EDA) for examples of AI prompts—but feel free to modify them or create your own! For additional guidance on structuring AI prompts, check out this article on prompt engineering techniques.
Identify missing or inconsistent data that could skew your analysis (e.g., missing payment history, unusual credit utilization rates).
Detect early risk indicators. Which variables might be most relevant for predicting delinquency?
Prompts to try:

Summarize key patterns, outliers, and missing values in this dataset. Highlight any fields that might present problems for modeling delinquency.
Identify the top 3 variables most likely to predict delinquency based on this dataset. Provide brief reasoning.
Action: 

Document your findings in bullet points for your report. Focus on:

Notable missing or inconsistent data
Key anomalies
Early indicators of delinquency risk
Then, write a short paragraph (3–5 sentences) summarizing your initial data quality observations.

Step 2: Address missing data and data quality issues
Now that you've identified gaps, it’s time to decide how to handle missing data to maintain accuracy.

What to do:

Identify gaps or missing values in critical features (e.g., payment history, income, credit utilization).
Determine the best treatment approach for each case:
Remove: Drop columns with excessive missing data.
Impute: Fill in missing values using mean, median, or predictive modeling.
Generate synthetic data: Use AI tools to create realistic values while maintaining fairness and distribution patterns.
Use GenAI to assist with suggesting strategies as well as automating parts of the imputation process
Prompts to try:

Suggest an imputation strategy for missing values in this dataset based on industry best practices.
Propose best-practice methods to handle missing credit utilization data for predictive modeling.
Generate realistic synthetic income values for missing entries using normal distribution assumptions.
Action: Create a simple table listing 2–3 missing data issues. For each one, include your chosen handling method and a one-line justification for why you selected it.

Step 3: Detect patterns and risk factors
With a cleaned dataset, your next goal is to uncover patterns and key risk factors that influence delinquency.

What to do:

Analyze relationships between variables and delinquency outcomes (e.g., is high credit utilization associated with missed payments?).
Use GenAI tools to help surface insights and prioritize key variables.
Highlight any unexpected findings that may require further investigation by the analytics team.
Document key risk indicators and any insights that could impact delinquency prediction. Include patterns that seem obvious as well as any surprising trends that might need deeper investigation.
Action: List high-risk indicators, each with a one-sentence explanation of why it’s important, as well as any insights that could impact delinquency prediction.

Step 4: Submit your EDA report
Using the template provided, prepare a brief report summarizing your findings:
Key patterns and anomalies detected in the dataset.
A summary of missing values and how they were handled.
Risk indicators that may impact delinquency predictions.
Deliverable: Submit a Word or PDF file of your report below.