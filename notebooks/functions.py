import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def format_gender(gender):
    if gender == "M":
        return "M"
    elif gender == "F":
        return "F"
    elif gender == "U":
        return "U"
    else:
        return "Unknown"  

def histo_numerical(df, column):
    """
    The function calculates the skewness and kurtosis of a specified column in a DataFrame. 
    It prints the values of the two characteristics and display the histogram plot of the 
    data distribution.

    Parameters:
        df (DataFrame): The DataFrame containing the data.
        column (str): The name (as string) of the column for which the distribution is shown.
    """

    column_data = df[column]

    skewness = column_data.skew()
    kurtosis = column_data.kurtosis()
    print(f"""Distribution measures:
    Skewness: {skewness}
    Kurtosis: {kurtosis}""")

    plt.figure(figsize = (3,3))
    sns.histplot(column_data, bins = 20, kde = True)


def centrality_dispersion(df, column):
    """
    The function calculates the main measures of centrality and dispersion 
    for a specified column in a DataFrame. It prints the results and return 
    a dictionary containing the same measures.

    Parameters:
        df (DataFrame): The DataFrame containing the data.
        column (str): The name (as string) of the column for which centrality 
        and dispersion measures are calculated.
    """
    column_data = df[column]
    
    mean = column_data.mean().round(2)
    median = column_data.median()
    mode = column_data.mode()[0]
    variance = round(column_data.var(), 2)
    std_dev = round(column_data.std(), 2)

    print(f"""Measures of centrality and dispersion for {column}:
    Mean: {mean}
    Median: {median}
    Mode: {mode}
    Variance: {variance}
    Standard deviation: {std_dev}""")


def replace_nan(value):

    """ 
    Function to replace nan values in the dataframe relative to the clients groups in the experiment (df_final)
    that replaces nan values with "Not inlcuded" (in the experiment, so neither controls nor tested clients)
    Parameter: value
    To be used with .map() function to replace nan values in a dataframe column.
    """
    
    if value == "Test":
        return "Test"
    elif value == "Control":
        return "Control"
    else:
        return "Not included"
    

def categ_age(age):

    """ 
    Function to categorize the age in the dataframe relative to demographic data of clients.

    Replacements:
    Kid/Teenager = 0-15
    Young adult = 16-20
    Adult = 21-35
    Middle-age = 36-55
    Senior = 56-75
    Elderly = 76-100

    Parameter: age
    To be used with .map() function to replace values in the column "age" or to create a new column of age categories.
    """
    if isinstance(age, float):
        if 0 <= age <= 15:
            return "Kid/Teenager"
        elif 16 <= age <= 20:
            return "Young adult"
        elif 21 <= age <= 35:
            return "Adult"
        elif 36 <= age <= 55:
            return "Middle-age"
        elif 56 <= age <= 75:
            return "Senior"
        elif 76 <= age <= 100:
            return "Elderly"
    else:
        return "Unknown"
        
def categ_hour(hour):
    """ 
    Function to categorize the hour and replace them with a specific daytime
    in the dataframe relative to experiment (activity of clients).
    
    Replacements:
    Night = 0-4
    Early morning = 5-8
    Morning = 9-11
    Lunch-time = 12-14
    Afternoon = 15-18
    Evening = 19-23

    Parameter: hour
    To be used with .map() function to replace values in the column "date_time" or to create a new column of daytime values.
    """

    if 0 <= hour <= 4:
        return "Night"
    elif 5 <= hour <= 8:
        return "Early morning"
    elif 9 <= hour <= 11:
        return "Morning"
    elif 12 <= hour <= 14:
        return "Lunch-time"
    elif 14 <= hour <= 18:
        return "Afternoon"
    elif 19 <= hour <= 23:
        return "Evening"
    

def week_day(day):
    """ 
    Function to replace the number associated with the name of the day of the week
    in the dataframe relative to experiment (activity of clients).
    
    Parameters: day
    To be used with .map() function to replace values in the column "date_time" or to create a new column of days of the week values.
    """
     
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    elif day == 6:
        return "Sunday"
    

def completion_rate(df):

    """
    Function to calculate the completion rate of clients visiting the website.
    It returns the average completion rate for the specified dataframe 
    and a pandas series with completion rates for each client.
    
    Parameters:
    df (DataFrame): the dataframe containing the columns needed
      The dataframe columns that the function refers to are: "process_step" and "client_id"

    """
    
    confirm_count =df[df["process_step"] == "confirm"].groupby("client_id").size()   
    total_users = df.groupby("client_id").size()
    completion_rate = (confirm_count / total_users * 100).round(1).dropna()
    average_completion_rate = completion_rate.mean().round(2)

    return average_completion_rate, completion_rate

def tukeys_test_outliers(data):

    """
    Function to detect outliers with Tukey's test.
    """
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    

    lower_q = Q1 - 1.5 * IQR
    upper_q = Q3 + 1.5 * IQR
    

    outliers = data[(data < lower_q) | (data > upper_q)] 
    
    return outliers

def time_steps(df):

    """
    The function calculates the time spent by clients in the different steps of the process.
    It prints out the results for each step.
    
    It returns three elements:
    1) the average time spent in each steps by all clients in teh dataframe  
    2) the total average time spent by all clients to complete all steps of the process
    3) a new dataframe with the average time spent by each client for each step

    The function handles duplicates (two or more consecutive times the client was in the same step) 
    by considering only the last and it drops outliers.
    
    Parameter:
    df (dataframe)
      The dataframe columns that the function refers to are: "date_time", "process_step", "client_id"
    """

    df["date_time"] = pd.to_datetime(df["date_time"])
    df_sort_date = df.sort_values(by = ["client_id", "visit_id", "date_time"]).copy()
    
    start_step1 = df_sort_date[ df_sort_date["process_step"].isin(["start","step_1"])]
    step1_step2 = df_sort_date[ df_sort_date["process_step"].isin(["step_1","step_2"])]
    step2_step3 = df_sort_date[ df_sort_date["process_step"].isin(["step_2","step_3"])]
    step3_confirm = df_sort_date[ df_sort_date["process_step"].isin(["step_3","confirm"])]

    step_names = ["Start-Step1", "Step1-Step2", "Step2-Step3", "Step3-Confirm"]
    
    time_spent_avg = []
    time_spent_client = {}

    for step_df, step_name in zip([start_step1, step1_step2, step2_step3, step3_confirm], step_names):

        consecutive_duplicates = step_df.duplicated(subset=["client_id", "process_step"], keep = "last")
        step_df = step_df[~consecutive_duplicates]

        time_diff = step_df.groupby("client_id")["date_time"].diff().dt.total_seconds()
        time_diff = time_diff.dropna()
        
        outliers = tukeys_test_outliers(time_diff)

        time_diff_no_outliers = time_diff.iloc[~time_diff.index.isin(outliers.index)]
        average_time = time_diff_no_outliers.mean()
        time_spent_avg.append(average_time)

        time_spent_client[step_name] = time_diff_no_outliers.groupby(step_df["client_id"]).mean()
    

    df_time_client = pd.DataFrame(time_spent_client)
    df_time_client.dropna(inplace=True)

    tot_time = np.mean(time_spent_avg)

    print(f"""The average activity duration of clients for each step is:
    Between Start and Step_1: {time_spent_avg[0]: .2f} seconds
    Between Step_1 and Step_2: {time_spent_avg[1]: .2f} seconds
    Between Step_2 and Step_3: {time_spent_avg[2]: .2f} seconds
    Between Step_3 and Confirm: {time_spent_avg[3]: .2f} seconds
    
    The total average duration to complete the process is: {tot_time: .2f} seconds""")
    
    return time_spent_avg, tot_time, df_time_client


def sequence_individual_errors(df):

    """
    The function calculates the error rates for every client id. 
    Errors are considered every time a client did not follow the order of 
    the steps specified by the list in the function (start, step_1, step_2, step_3, confirm).
    
    The function returns a dataframe including the error rate in percentage for every client.

    Parameter: df (dataframe)
    The dataframe columns that the function refers to are: "date_time", "process_step", "client_id"
    """
    
    df_sort_date = df.sort_values(by = ["client_id", "date_time"])
    list_steps = ["start", "step_1", "step_2", "step_3", "confirm"]
    
    
    errors = ((df_sort_date.groupby("client_id")["process_step"].shift().fillna("") == "") & (df_sort_date["process_step"] != list_steps[0])) | \
          (~df_sort_date.groupby("client_id")["process_step"].shift().fillna("").isin([None, list_steps[4], ""]) & \
           (df_sort_date["process_step"] != df_sort_date.groupby("client_id")["process_step"].shift(-1).fillna("")) & \
           (df_sort_date["process_step"] != df_sort_date.groupby("client_id")["process_step"].shift().map(lambda x: list_steps[(list_steps.index(x) + 1) % len(list_steps)] \
                                                                                                                            if not pd.isna(x) else "").fillna("")))
    
    df_errors = df_sort_date.loc[errors] # errors is a boolean mask that allows to select only the rows of the sorted df where there are the errors specified in the mask 
   
    error_rate = ((df_errors.groupby("client_id").size() / df_sort_date.groupby("client_id").size())*100).fillna(0)

    df_error_rate = pd.DataFrame(error_rate, columns=["Error Rate (%)"])

    return df_error_rate


def sequence_total_errors(df):

    """
    The function calculates the error rates for every client id but 
    prints the total error rate of the entire dataset (df). 
    
    Errors are considered every time a client did not follow the order of 
    the steps specified by the list in the function (start, step_1, step_2, step_3, confirm).

    Parameter: df (dataframe)
    The dataframe columns that the function refers to are: "date_time", "process_step", "client_id"
    """
    
    df_sort_date = df.sort_values(by = ["client_id", "date_time"])
    list_steps = ["start", "step_1", "step_2", "step_3", "confirm"]
    
    errors = ((df_sort_date.groupby("client_id")["process_step"].shift().fillna("") == "") & (df_sort_date["process_step"] != list_steps[0])) | \
          (~df_sort_date.groupby("client_id")["process_step"].shift().fillna("").isin([None, list_steps[4], ""]) & \
           (df_sort_date["process_step"] != df_sort_date.groupby("client_id")["process_step"].shift(-1).fillna("")) & \
           (df_sort_date["process_step"] != df_sort_date.groupby("client_id")["process_step"].shift().map(lambda x: list_steps[(list_steps.index(x) + 1) % len(list_steps)] \
                                                                                                                            if not pd.isna(x) else "").fillna("")))
    df_errors = df_sort_date[errors] # errors is a boolean mask that allows to select only the rows of the sorted df where there are the errors specified in the mask 
   
    error_rate = ((df_errors.groupby("client_id").size() / df_sort_date.groupby("client_id").size())*100).fillna(0)
    
    # general error rate
    
    error_rate_total = (len(df_errors) / len(df_sort_date)) * 100

    if error_rate_total <= 0:
        print("No errors found in the entire dataset.")
    else:
        print(f"The overall error rate for the dataset is: {error_rate_total: .2f}%")