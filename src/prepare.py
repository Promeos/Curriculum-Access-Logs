import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta


############################# Prepare User Log Data ##################################
def prep_log_cohort_data(df_logs, df_cohorts):
    '''
    This function accepts the user log and cohort id datasets.
    Returns a merged and prepared dataset of user logs and cohort information.
    
    parameters
    ----------
    df_logs : pandas DataFrame
        dataframe returned from the function acquire.get_log_data()
    
    df_cohorts : pandas DataFrame
        dataframe returned from the function acquire.get_cohort_data()
    
    returns
    -------
    pandas DataFrame of merged dataset of user logs with associated cohort information.
        Datetime string obejects are cast into datetime data types
        Float data types are cast into integer data types.
    '''
    # Merge datasets together using a left join.
    # Some users are missing a Cohort ID #
    df = df_logs.merge(df_cohorts, on='cohort_id', how='left')
    
    # Fill missing cohort ID with 0's
    df = df.fillna(0)
    
    # Cast date/time columns from object data types into datetime data type
    # Cast float data type columns into integer data type
    df = df.assign(
    date = pd.to_datetime(df['date'] + ' ' + df['time']),
    start_date = pd.to_datetime(df['start_date']),
    end_date = pd.to_datetime(df['end_date']),
        
    cohort_id = df.cohort_id.astype(np.int),
    program_id = df.program_id.astype(np.int)
    
    )

    # drop redunant time column
    df.drop(columns='time', inplace=True)

    # rename columns to be more explicit
    df.rename(columns={'name': 'cohort_name',
                       'start_date': 'program_start',
                       'end_start': 'program_end'},
              inplace=True)
    
    return df


############################# Prepare Codeup Log Data - New Columns ##################################
def append_program_type(df):
    '''
    This function accepts the merged dataframe from prep_log_cohort_data().
    Returns a DataFrame with a new column `program_type`.
    
    definitions
    -----------
    `program_type` : Indicates whether a user is in Data Science, Web Development, or 
                     Data Science and Web Development.
    
    parameters
    ----------
    df : pandas DataFrame
    
    returns
    -------
    df : pandas DataFrame
        Returns a pandas DataFrame with a new column named `program_type`
    '''
    df_programs = pd.DataFrame({ 'program_id' : range(0, 5),
                                'program_type': ['Web Development and Data Science',
                                                'Web Development',
                                                'Web Development',
                                                'Data Science',
                                                'Web Development']})
    df = df.merge(df_programs)
    return df


def append_has_graduated(df):
    '''
    Accepts a merged dataframe of access logs and cohort ids
    Returns original dataset with a new column called `has_graduated`
    
    definitions
    -----------
    `has_graduated` : Indicated whether a user has graduated or is set to graduate.
        1 == Has graduated
        0 == Has NOT graduated
    
    parameters
    ----------
    df : pandas DataFrame
    
    returns
    -------
    df : pandas DataFrame
        Retuns a pandas DataFrame with a new column named `has_graduated`
    '''
    # Create a variable to store today's date.
    today = datetime(2020, 11, 2)

    # Filter the dataset to locate active cohorts.
    active_cohort_ids = df.loc[df['end_date'] < today].cohort_id.value_counts().index.to_list()
    df['has_graduated'] = df.cohort_id.isin(active_cohort_ids).astype(np.int)
    return df


def append_active_status(df):
    '''
    Accepts a merged dataframe of access logs and cohort ids
    Returns original dataset with new columns called:
        `active_within_5_days`
        `active_within_1_month`
        `active_within_3_months`
        `active_within_6_months`
        `active_greater_than_6_months`
    
    definitions
    -----------
    `active_within_5_days`
    `active_within_[1, 3, 6]_month(s)`,
    `active_greater_than_6_months`:
        Indicates whether a user has been accessed the curriculum.
        1 == Logged in during time period.
        0 == Has NOT logged in during time period.
    
    parameters
    ----------
    df : pandas DataFrame
    
    returns
    -------
    df : pandas DataFrame
        Retuns a pandas DataFrame with a new column named `has_graduated`
    '''
    # Create datetime variables
    today = datetime(2020, 11, 2)
    five_days = (today - timedelta(5)).date()
    one_month = (today - timedelta(30)).date()
    three_months = (today - timedelta(90)).date()
    six_months = (today - timedelta(180)).date()
    
    # Groupby user id and aggregate by date to find the first access and the last access
    df_user_age = df.groupby('user_id')['date'].agg(['min', 'max'])

    # Calculate the number of days a user has had access to the curriculum.
    # Convert the timedelta to days. Convert days from float to an integer value.
    df_user_age = df_user_age.assign(
        days_with_access = (df_user_age['max'] \
                            - df_user_age['min']) \
                            .astype('timedelta64[D]') \
                            .astype(np.int64)
        )

    # rename columns for clarity
    df_user_age.rename(columns={'min':'first_access',
                                'max':'last_access'},
                    inplace=True)
    
    df_user_age['first_access'] = pd.to_datetime(df_user_age.first_access).dt.date
    df_user_age['last_access'] = pd.to_datetime(df_user_age.last_access).dt.date
    
    # extract the date from last access to use in a boolean expression
    last_access = df_user_age.last_access
    
    # Users active within the past 5 days
    df_user_age['active_within_5_days'] = (last_access > five_days).astype(np.int)
    
    # Users active within 30 days
    df_user_age['active_within_1_month'] = ((last_access < five_days)\
                                           & (last_access >= one_month)
                                           ).astype(np.int)

    # Users active greater than 30 days and less than less than 90 days
    df_user_age['active_within_3_months'] = ((last_access < one_month)\
                                            & (last_access >= three_months)
                                            ).astype(np.int)

    # Users active greater than 90 days and less than 180 days
    df_user_age['active_within_6_months'] = ((last_access < three_months)\
                                            & (last_access >= six_months)
                                            ).astype(np.int)

    # Users active greater than 180 days
    df_user_age['active_greater_than_6_months'] = (last_access < six_months).astype(np.int)
    
    df_user_age.reset_index(inplace=True)
    df = df.merge(df_user_age)
    return df


    