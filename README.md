# DS4 - **Group 4 Data Science Project**



## 📑 Table of Contents

- [Purpose & Overview](#purpose--overview)
  - [Research Question](#research-question)
- [Goals & Objectives](#goal--objectives)
  - [Industry Context](#industry-context)
  - [Stakeholders](#stakeholders)
  - [Business Opportunity](#business-opportunity)
- [Techniques & Technologies](#techniques--technologies)
  - [Methodology](#methodology)
- [Key Contacts](#key-contacts-alphabetical-by-first-name)
- [Schedule](#schedule)
- [Limitations & Mitigations Strategies](#limitations)
- [Key Results & Findings](#key-results--findings)
- [Ideas for Future Analysis](#ideas-for-future-analyzes-things-we-would-have-done-if-we-had-more-time)
- [References](#references)

---

## Purpose & Overview

This project focuses on creating data visualization tools that highlight early-stage patterns of diabetes symptoms to support both patient awareness and clinical decision-making. By transforming symptom data into clear, accessible visual insights, the project aims to empower individuals to better recognize potential warning signs and to provide healthcare providers with intuitive tools to illustrate risk patterns during screening conversations.

From a business and industry perspective, this work operates within the preventive healthcare and educational health space, where early detection is linked to improved patient outcomes and reduced long-term costs — a strategic priority for providers, insurers, and public health systems. Visualization-driven tools could enhance patient education and strengthen clinical consultations.

Ultimately, the goal is to bridge the gap between symptom experience and clinical action through data-informed, visually driven communication. By making symptom patterns visible and intuitive, these education tools can support earlier intervention, improve preventive care strategies, and contribute to cost-effective healthcare delivery.

**Dataset Used**:  
https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset

---

## Research Question

What are the top predictors based on gender and age groups that can identify individuals at high risk of diabetes earlier and enable preventive care?

---

## Goal & Objectives

### Project Goals

1. Increase awareness of early-stage diabetes symptoms through clear and accessible data visualization.  
2. Identify and visually communicate symptom patterns associated with diabetes diagnosis.  
3. Support preventive healthcare efforts by illustrating risk trends without relying on predictive modeling (TBD).  
4. Bridge the gap between patient-reported symptoms and clinical screening conversations.  
5. Demonstrate the strategic value of data visualization in public health and patient education contexts.

### Project Objectives

1. Clean and transform the Early-Stage Diabetes Risk dataset for visual analysis.  
2. Compare symptom prevalence between diagnosed and non-diagnosed individuals.  
3. Visualize symptom clustering and co-occurrence patterns (TBD).  
4. Illustrate the relationship between symptom accumulation and diagnosis rate.  
5. Explore demographic context (e.g., age, obesity) in relation to diagnosis.  
6. Develop clear, interpretable charts that prioritize insight over visual complexity.  
7. Provide evidence-based recommendations for awareness or screening applications.  

---

## Industry Context

This project is situated within the preventive healthcare and public health sector, where early detection of chronic conditions like diabetes remains a critical challenge. Diabetes prevalence continues to rise globally, contributing to significant long-term health complications and healthcare system costs.

Early-stage symptoms are often subtle, misinterpreted, or ignored, leading to delayed diagnosis and preventable disease progression. Leveraging symptom pattern data through clear visual analysis presents an opportunity to improve early awareness and support more timely screening interventions.

---

## Stakeholders

Key stakeholders include:

- Patients  
- Primary care providers  
- Public health organizations  
- Digital health platforms  

Patients benefit from increased awareness of early warning signs that may otherwise be overlooked. Healthcare providers can use symptom pattern insights to inform screening conversations and prioritize testing. Public health agencies may leverage these findings to design targeted education campaigns, while digital health tools could integrate symptom-based insights into screening or triage features.

---

## Business Opportunity

Visualizing symptom patterns associated with diabetes diagnosis creates opportunities to support earlier identification and preventive care. By highlighting high-risk symptom combinations and accumulation trends, healthcare systems and digital platforms could implement structured screening tools or awareness initiatives.

Earlier intervention has the potential to:

- Reduce complications  
- Improve patient outcomes  
- Lower long-term healthcare costs  

---

### 💰 Estimated Economic Value

A conservative first-year savings estimate could be predicted using our prevention savings model:

**Estimated cost split (Year 1 per case):**

- Hospital: $2,000–$2,400  
- Medications/devices: $600–$950  
- Physician/other: $350–$1,200  

**Total ≈ $3,800 per new diabetes case**

**Savings formula:**
Savings ≈ (cases prevented) × C$3,800
## Techniques & Technologies

**Dataset Used**:  
https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset  

Dataset contains **520 records and 16 features**.

---

### Methodology

1. **Data Audit**
   - Check for missing values  
   - Duplicate rows  
   - Data types  
   - Impossible values  

2. **Data Cleaning**
   - Standardize categorical variables  
   - Yes → 1  
   - No → 0  
   - Positive diabetes → 1  
   - Negative diabetes → 0  

3. Feature engineering for prevention insights  
   - Create age groups  
   - Create symptom count  

4. Multicollinearity check  

5. Exploratory Analysis  
   - Visualization of age, gender, symptoms  

6. Prevention analytics models investigated:
   - Logistic Regression  
   - Random Forest classification  
   - K-Mode clustering  

7. Identify top predictors using:
   - Correlation  
   - SHAP values  

8. Validation
   - Train/test split  

9. Visualization outputs:
   - SHAP explainability  
   - Age risk curve  
   - Accessibility-ready visuals  
   - Network correlation  

10. Recommendations to primary care providers and public health organizations  

---

## Key Contacts (alphabetical by first name)

- Brianna Lowe  
- Cecilia Leung 
- Hema Dawonauth  
- Patricia Rabel  
- Saranjeet Singh  
- Shafeeza Hussain  

---

## Schedule

### Week 1

**Day 1 — February 24**  
- Meet team  
- Review dataset  
- Discuss research problem  

**Day 2 — February 25**  
- Review additional datasets  
- Discuss real-world applications  

**Day 3 — February 26**  
- Complete first draft of README  
- Confirm research questions  
- Determine next steps  

**Weekend Work**

- Hema & Shafeeza: visualization, modelling, cleaning  
- Patricia & Brianna: README and business case  
- Hema: financial KPIs  
- Group: research health visualizations  
- Review K-means applicability  

---

### Week 2

**Day 4 — March 3**  
TBD  

**Day 5 — March 4**  
TBD  

**Day 6 — March 5**  
- Prepare PowerPoint  
- Align on final presentation  
- Dry run  

**Final Presentation — March 7**

---

## Limitations & Mitigation Strategies

1. Dataset is from patients in Bangladesh; symptoms may vary by region or population.
 Risk: Findings may not generalize to Canadian or North American populations.
 Mitigation: Frame insights as exploratory and pattern-based rather than universal predictors. Compare findings to Canadian epidemiology literature to validate directional trends.
2. Limited sample size (520 records), especially when segmented by age groups.
 Risk: Reduced statistical reliability in subgroup analysis.
 Mitigation: Use broader age group bins to maintain statistical power. Avoid over-segmentation and clearly label findings as indicative, not definitive.
3. No data on symptom severity (binary only).
 Risk: Cannot differentiate between mild vs. clinically significant symptom presentation.
 Mitigation: Focus analysis on symptom accumulation and co-occurrence patterns rather than intensity. Highlight this as a future dataset enhancement opportunity.
4. Possible misclassification (negative cases may include prediabetes).
 Risk: Blurs diagnostic boundary.
 Mitigation: Treat outcome variable as “diagnosed vs. not diagnosed” rather than definitive absence of disease. Include disclaimer in findings. 
5. Gender Distribution Imbalance
Risk: The dataset contains 328 males (63%) and 192 females (37%), so findings based on females are derived from a smaller sample. This may reduce the stability of percentage comparisons and limit the reliability of gender-specific conclusions.
Mitigation: We will report the gender distribution transparently, use proportional comparisons rather than raw counts, and interpret female-specific trends with caution, framing them as exploratory rather than definitive.

---

## Key Results & Findings

TBD

---

## Ideas for Future Analyses (things we would have done if we had more time)
- Expand the dataset to include patients from additional geographic regions to assess whether symptom patterns remain consistent across populations.
- Incorporate additional clinical variables (e.g., BMI, blood glucose levels, family history) to improve risk identification.
- Develop an interactive dashboard or simple risk scoring tool to help visualize symptom-based risk patterns for patients and clinicians.

---

## References

1. https://www.yorku.ca/science/mathstats/acadic/diabetes-in-toronto/  
2. https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.1029358/full  
3. https://www.researchgate.net/publication/356828945_Use_of_Machine_Learning_Techniques_to_Predict_Diabetes_at_an_Early_Stage  
4. https://www.ices.on.ca/publications/journal-articles/impact-of-diabetes-on-healthcare-costs-in-a-population-based-cohort-a-cost-analysis  
