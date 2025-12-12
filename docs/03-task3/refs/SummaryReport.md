# Business Summary Report: Predictive Insights for Collections Strategy

## 1. Summary of Predictive Insights
Geldium’s portfolio is steady on the surface, but a small set of stress signals tells us exactly where to focus to keep customers solvent and the ledger clean. Think of this as the trailer before the feature: here are the three scenes that matter most right now.
- Delinquency base rate is 16%, so every 10-point lift in recall materially reduces losses; precision must stay acceptable to avoid over-contacting good customers.
- Highest-risk patterns combine payment behavior and stress signals: utilization above 60%, debt-to-income above 0.4, and recent missed payments sharply increase risk compared to the baseline.
- Protective factors: longer tenure and stronger credit scores dampen risk; short-tenure customers with moderate scores are more volatile and merit closer monitoring.

### Key Insights Summary Table
| Key Insight | Customer Segment | Influencing Variables | Potential Impact |
|-------------|-----------------|-----------------------|------------------|
| Customers with utilization > 60% and 1–2 missed payments show ~2–3x higher delinquency likelihood than baseline | Revolving users with rising balances | Credit_Utilization, Missed_Payments, Debt_to_Income_Ratio | Prioritize early, empathetic outreach to contain roll rates |
| Short-tenure customers (< 12 months) with mid-tier credit scores are more likely to slip into delinquency during balance growth phases | Newer accounts building history | Account_Tenure, Credit_Score, Loan_Balance trend | Add welcome-to-stability nudges and spending guardrails |
| High debt-to-income (> 0.4) plus utilization > 50% signals liquidity stress even without prior misses | Mixed-age, working customers | Debt_to_Income_Ratio, Credit_Utilization, Income | Offer limit soft caps and payment plan options before first miss |

## 2. Recommendation Framework
The insight is clear; now the move needs to be crisp. This framework turns the risk signal into a controlled pilot the team can run, measure, and either scale or stop with confidence.
**Restated Insight:** Customers with utilization > 60% and at least one missed payment are roughly 2–3x more likely to become 30-day delinquent than the 16% baseline.

**Proposed Recommendation:** Pilot a targeted, human-backed outreach program to this segment.
- **Specific:** Identify customers with utilization > 60% and 1–2 missed payments in the last 90 days; exclude those already in hardship programs.
- **Measurable:** Target 10% relative reduction in 30-day delinquency rate for this segment and a <5% increase in false-positive contacts (non-delinquent customers contacted).
- **Actionable:** Use existing CRM to trigger a 3-touch sequence (SMS + email + agent call) offering payment plan options and utilization coaching; integrate a simple hardship self-assessment form.
- **Relevant:** Focuses on the highest lift segment with clear financial upside while keeping customer experience front and center.
- **Time-bound:** Run a 6-week pilot; evaluate weekly; decide on scale-up in week 7 based on delinquency, contact success, and opt-out rates.

**Justification and Business Rationale:**
- Concentrates resources on the segment with the steepest risk gradient, improving recall without a large precision penalty.
- Uses transparent, explainable triggers (utilization, missed payments) aligned with regulatory expectations.
- Blends digital nudges with human follow-up to preserve customer goodwill and reduce roll rates before they become charge-offs.

## 3. Ethical and Responsible AI Considerations
No recommendation sticks without trust. The checks below keep the program fair, explainable, and proportionate so the outreach helps customers rather than surprises them.
- **Bias and fairness:** Monitor performance by age bands and income bands to ensure the outreach trigger does not disproportionately target specific demographics; review coefficients to remove proxy variables if disparities emerge.
- **Explainability:** Provide customers a plain-language reason for outreach (“recent missed payment and high balance utilization”) and the option to contest or clarify their status.
- **Proportionality and consent:** Outreach offers support and self-service plans rather than punitive actions; all messages should include clear opt-out choices.
- **Privacy and minimization:** Limit feature use to necessary financial variables; log access and ensure data retention follows policy.
- **Human oversight:** Flag high-risk cases for agent review before any limit change; require periodic model and threshold reviews to detect drift.
