# ds4
**Group 4 Data Science Project**

**Table of Content**
*Purpose & Overview
    Research Question
Goals & Objectives
    Industry Context
    Stakeholders
    Business Opportunity 
Techniques & Technologies 
    Methodology
Key Contacts
Schedule
Limitations
Key Results & Findings
Ideas for Future Analysis
References
---
**Purpose & Overview**
This project focuses on creating data visualization tools that highlight early-stage patterns of diabetes symptoms to support both patient awareness and clinical decision-making. By transforming symptom data into clear, accessible visual insights, the project aims to empower individuals to better recognize potential warning signs and to provide healthcare providers with intuitive tools to illustrate risk patterns during screening conversations. 

From a business and industry perspective, this work operates within the preventive healthcare and educational health space, where early detection is linked to improved patient outcomes and reduced long-term costs, a strategic priority for providers, insurers, and public health systems. Visualization-driven tools could enhance patient education and strengthen clinical consultations.

Ultimately, the goal is to bridge the gap between symptom experience and clinical action through data-informed, visually driven communication. By making symptom patterns visible and intuitive, these education tools can support earlier intervention, improve preventive care strategies, and contribute to cost-effective healthcare delivery. Ultimately, the project demonstrates how data visualization can serve not only as an analytical tool but also as a strategic asset in advancing public health outcomes.

**Dataset Used**: https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset

----
**Research Question**
What are the top predictors based on genders and age groups that can predict and identify individuals with high risk of diabetes earlier, predict early-stage diabetes risk to enable preventive care?
---
**Goal & Objectives**
**Project Goals**
1. Increase awareness of early-stage diabetes symptoms through clear and accessible data visualization.
2. Identify and visually communicate symptom patterns associated with diabetes diagnosis.
3. Support preventive healthcare efforts by illustrating risk trends without relying on predictive modeling. (TBD)
4. Bridge the gap between patient-reported symptoms and clinical screening conversations.
5. Demonstrate the strategic value of visualization in public health and educational health contexts.

**Project Objectives**
1. Clean and transform the Early-Stage Diabetes Risk dataset for visual analysis.
2. Compare symptom prevalence between diagnosed and non-diagnosed individuals.
3. Visualize symptom clustering and co-occurrence patterns. (TBD?)
4. Illustrate the relationship between symptom accumulation and diagnosis rate.
5. Explore demographic context (e.g., age, obesity) in relation to diagnosis.
6. Develop clear, interpretable charts that prioritize insight over visual complexity.
7. Provide evidence-based recommendations for awareness or screening applications.
----
**Industry Context**
This project is situated within the preventive healthcare and public health sector, where early detection of chronic conditions like diabetes remains a critical challenge. Diabetes prevalence continues to rise globally, contributing to significant long-term health complications and healthcare system costs. Early-stage symptoms are often subtle, misinterpreted, or ignored, leading to delayed diagnosis and preventable disease progression. Leveraging symptom pattern data through clear visual analysis presents an opportunity to improve early awareness and support more timely screening interventions.
----
**Stakeholders**
Key stakeholders include patients, primary care providers, public health organizations, and digital health platforms. Patients benefit from increased awareness of early warning signs that may otherwise be overlooked. Healthcare providers can use symptom pattern insights to inform screening conversations and prioritize testing. Public health agencies may leverage these findings to design targeted education campaigns, while digital health tools could integrate symptom-based insights into screening or triage features.
----
**Business Opportunity**
Visualizing symptom patterns associated with diabetes diagnosis creates opportunities to support earlier identification and preventive care. By highlighting high-risk symptom combinations and accumulation trends, healthcare systems and digital platforms could implement structured screening tools or awareness initiatives. Earlier intervention has the potential to reduce complications, improve patient outcomes, and lower long-term healthcare costs, positioning symptom-based visualization as a valuable asset in preventive health strategy.


ADD $$ VALUE Add for this amazing initative

A conservative “first-year savings” estimate could be predicted using our prevention savings model:
Estimated split:
  - Hospital: $2,000–$2,400
  - Medications/devices: $600–$950
  - Physician/other: $350-$ 1200
  Total ~ 3800 for first-year cost of treating diabetes

  Savings ≈ (cases prevented) × C$3,800 (first-year attributable cost)      
  *Data Souce - https://www.ices.on.ca/publications/journal-articles/impact-of-diabetes-on-healthcare-costs-in-a-population-based-cohort-a-cost-analysi

**Techniques & Technologies**

  **Dataset Used**: https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset
   We have 520 records and 16 features in this dataset

  **Methodology**
  1. Data Audit ( check for missing values, duplicate rows, data types, impossible values)
  2. Data Cleaning (Standardize categorical variables to enable correlation for logistic regression and SHAP)
       Yes → 1
       No → 0
       Positive diabetes → 1
       Negative diabetes → 0
  3. Feature engineering for prevention insights ( create age groups and symptom count)
  4. Multicollinearity check (look for highly correlated symptoms)
  5. Exploratoty Analysis: Used Visualization techniques to understand patterns and correlations between different variables ( age, gender, symptoms)
  6. For prevention analytics, the model we will investigate are
     - Logistic regression
     - Classification Model using Random Forest, to classify symptoms as either ‘High Risk’ or ‘Moderate Risk’ or 'Low Risk'.
     - K-Mode

  7. Identify top predictors ( using multiple methods)
   - correlation with diabetes
   - SHAP values ( Best for explainability)
  8. Validation
     - Train/test split
  9. Visualization: SHAP explainability, Age risk curve, Accessibility-ready visuals, Network correlation
  10. Recommendation to primary care providers and public health organizations (Diabetes prevention Infographics / Diabetes Screening Tool)


TBD - to be updated after the weekend
PCA - to review to show direction of data


---
**Key Contacts (alphabetical by first name)**
Brianna Lowe
Ceilia Leung
Hema Dawonauth
Patricia Rabel
Saranjeet Singh
Shafeeza Hussain
---
**Schedule**
Week 1
Day 1 - February 24
Meet team, review data set, discuss research problem

Day 2- February 25
Review additional datasets, and discuss research problem and real-world applications

Day 3 - February 26
Complete first draft of readme, confirm research questions, determine next steps and action items

Additional Work Over Weekend
Hema and Shafeeza to review data visualization, modelling and data cleaning
Patricia and Brianna to support the read-me file and business case
Hema to review financial KPIs
Group research existing or effective health focused data-visualizations
K-means cluster review, how is it applicable to our work

Week 2 - key activities to be determined in Day 4 stand-up
Day 4 - March 3

Day 5 - March 4

Day 6 - March 5
Prepare powerpoint, align on final presentation, dry run

Final Presentation - Saturday March 7th @ 
---
**Limitations**
Dataset is from patients in Bangladesh. Symptoms might differ based on climate, race etc
Not a large data-set if diving by age category
 
We do not information about degree of symptoms, for example, very itchy etc
 
There is a possibility that some of the negative cases may have prediabetes or very early stage of diabetes.
---
**Key Results & Findings**
TBD
---
**Ideas for Future Analyzes (things we would have done if we had more time)**
TBD
---
**References**
1. https://www.yorku.ca/science/mathstats/acadic/diabetes-in-toronto/
2. https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2022.1029358/full
3. https://www.researchgate.net/publication/356828945_Use_of_Machine_Learning_Techniques_to_Predict_Diabetes_at_an_Early_Stage
4. https://www.ices.on.ca/publications/journal-articles/impact-of-diabetes-on-healthcare-costs-in-a-population-based-cohort-a-cost-analysis


