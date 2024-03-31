## Vanguard Data Analysis Project

This project contains analysis and visualizations of Vanguard data on the enhancement of User Experience through the implementation of a new modern User Interface (UI) and timely in-context prompts in the company's app.

The main goal of the analysis was to evaluate if the new features effectively encourage more clients to complete the process.

- **Data Sources**

Data collected from 3/15/2017 to 6/20/2017.
Three datasets:

  1. Clients’ demographic data 
       (70.609 clients, 9 info categories)

  2. Clients’ online interactions (initial page, three steps, confirmation page)
      (755.405 interactions, 5 info categories)

  3. Clients’ experiment groups inclusion (Control, Test, or Not Included)
     (23.532 Controls, 26.968 Tests, 20.109 clients Not Included)

- **Insights and Analysis**

An initial exploratory analysis was performed on the datasets individually (Code file name "EDA-data_clearing"), together with a slight formatting of data.

 **Demographic dataset**:

 - 4 categorical variables (gender, number of accounts, calls in the last 6 months, and logons in the last 6 months)

 - 4 numerical variables (tenure_years, tenure_months, clients age, and balance)

 - 1 client_id

Categorical variables info:

 - Gender of clients quite uniformly distributed (F, M, and U = unspecified)
 - The majority of clients have 2 or 3 accounts
 - The majority of clients have done 6 calls in the last 6 months
 - The majority of clients have done 9 logons in the last 6 months, but many have also done between 3 and 7 logons
- No correlation between gender and number of accounts

Numerical variables info:

 - The majority of clients have the accounts since 1 to 15 years, with a mean of 12 years ± 6 (std).
 - The mean age of the clients is 46 years ± 12 (std)
 - The balance of the accounts is very variable, with a mean of 147,445 but a very high standard deviation of 301,508

**Clients experiment groups**:

Clients subdivided in two groups having similar sample size:

Control --> 23532
Test --> 26968
Clients are identified by the unique client_id, regardless of how many accounts they have.

**Clients digital footprint**:

 - The activity of all clients is monitored.
 - Each client_id has different indexes relative to the activity (time and steps)
 - The activity is monitored via "start", 3 steps and confirm
 - Not all clients performed the activity uniformly, some go back and forth between steps before reaching the confirm step 


 - **Performance Metrics**

 Three metrics were defined to evaluate clients' engagement:

 1) Completion Rate: The proportion of users who reach the final ‘confirm’ step.

 2) Time Spent on Each Step: The average duration users spend on each step.

 3) Error Rates: If there’s a step where users go back to a previous step, it may indicate confusion or an error. You should consider moving from a later step to an earlier one as an error.

 The code relative to the definition of the metrics is the file called "Performance_metrics"

 - **Statistical analysis** 

 All data were first subjected to distribution analysis, therefore an histogram was used to check for the distribution shape and then Kolmogorov-Smirnof test was employed to check for normality distribution. 
 All data were not-normally distributed, even after data transformation with either log, square root or Box-Cox transformations. 
 Thus, non-parametric tests were used to compare data from control and test groups:

  - Mann-Whitney U test (equivalent to parametric t-test) --> the test ranks all values from low to high and compares the mean of the ranks. This test was employed to compare two independent samples (such as completion rate of control and test groups)

  - Fridman test (equivalent to one-way ANOVA) with posthoc Tuckey's test for multiple comparisons of time spent between the 4 steps.

  - **Tableau visualizations**

  All plots depicting the results of the analysis can be found in the Tableau public repository: 

  https://public.tableau.com/app/profile/laura.monni/viz/IronHack_Project2_vanguard-ab-test/Dashboard1?publish=yes

  - **Slides presentation**

  The slides of a 6 minutes presentation of the main results are public and can be found at:

  https://www.canva.com/design/DAGA0BoS3xo/4ThKDWC4JL2uMBc7U8MOdA/edit







