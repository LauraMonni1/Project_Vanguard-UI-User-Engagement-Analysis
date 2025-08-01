# 📊 Vanguard A/B Testing – UI & User Engagement Analysis

This project analyzes client behavior and engagement in response to a **UI redesign and in-context prompts** implemented in Vanguard’s app. The goal is to determine whether these UX improvements result in **higher completion rates** and **better user flow**.

## Objective

Evaluate the impact of a new **modern UI** and **in-context prompts** on user behavior across different customer segments. The project uses A/B testing data to answer:   *Do the changes improve user engagement and completion of the process?*

---
## Datasets Overview

Data collected from **March 15, 2017 to June 20, 2017**. Three datasets were used:

| Dataset                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `clients.csv`          | Demographics (70,609 clients, 9 variables)                                  |
| `interactions.csv`     | App navigation logs (755,405 records, 5 features)                           |
| `groups.csv`           | A/B group assignment (Control: 23,532 | Test: 26,968 | Not included: 20,109)|

---
## Variables Summary

### Demographic Features
- **Categorical**: Gender, number of accounts, # of calls, # of logons (last 6 months)
- **Numerical**: Age, tenure (years & months), account balance
- **ID**: `client_id`

### Interaction Log Features
- User steps: `start`, `step_1`, `step_2`, `step_3`, `confirm`
- Timestamped user actions per `client_id`

---

## Key Metrics

Three performance indicators were defined:

1. **Completion Rate**  
   → Proportion of users reaching the final ‘confirm’ step

2. **Time on Each Step**  
   → Average time spent on each of the four steps

3. **Error Rate**  
   → Frequency of users moving **backward** in the step sequence (e.g. step 3 → step 2)

Metric calculations are implemented in `Performance_metrics.ipynb`.

---

## Analysis Pipeline

1. **Exploratory Data Analysis (EDA)**  
   - Individual dataset analysis (demographics, interactions, groups)
   - Initial plots and summary statistics  
   *(see `EDA_data_cleaning.ipynb`)*

2. **Distribution & Statistical Tests**  
   - Histograms, Kolmogorov-Smirnov for normality  
   - All metrics were non-normal → non-parametric tests used:
     - **Mann-Whitney U test** → Compare control vs test (e.g., completion rate)
     - **Friedman test** + **posthoc Tukey** → Compare times across steps

3. **Visualization**  
   - Dashboard built in Tableau Public

---

## Key Insights

- Test group showed a **higher completion rate** compared to control.
- Certain steps had **longer dwell time** in the control group, suggesting UI confusion.
- Higher **backward navigation** in control users flagged usability bottlenecks.

---

## Presentations

- **🔗 Tableau Dashboard:**  
  [Vanguard A/B Test Results – Dashboard](https://public.tableau.com/app/profile/laura.monni/viz/IronHack_Project2_vanguard-ab-test/Dashboard1?publish=yes)

- **🎞️ 6-Minute Slide Presentation (Canva):**  
  [Canva Slide Deck](https://www.canva.com/design/DAGA0BoS3xo/4ThKDWC4JL2uMBc7U8MOdA/edit)

---

## Tech Stack

- **Languages**: Python (pandas, NumPy, matplotlib, seaborn, scipy.stats)
- **Statistical Testing**: Kolmogorov-Smirnov, Mann-Whitney U, Friedman test
- **Visualization**: Tableau Public, matplotlib, seaborn
- **Tools**: Jupyter Notebooks











