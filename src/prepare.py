import pandas as pd
import numpy as np


############################# Prepare Codeup Log Data ##################################
def prep_log_cohort_data(df_logs, df_cohorts):
    '''
    This function accepts the user log and cohort id datasets and 
    returns a merged and prepared dataset of user logs with associated cohort information.
    
    parameters
    ----------
    df_logs : pandas DataFrame
        dataframe returned from the function acquire.get_log_data()
    
    df_cohorts : pandas DataFrame
        dataframe returned from the function acquire.get_cohort_data()
    
    returns
    -------
    pandas DataFrame of merged and prepared data of user logs with associated cohort information.
    '''
    df = df_logs.merge(df_cohorts, on='cohort_id', how='left')
    df = df.fillna(0)
    
    df = df.assign(

    date = pd.to_datetime(df['date']),
    time = pd.to_datetime(df['time']),
    start_date = pd.to_datetime(df['start_date']),
    end_date = pd.to_datetime(df['end_date']),
        
    cohort_id = df.cohort_id.astype(np.int),
    program_id = df.program_id.astype(np.int)
    
    )
    return df
    