import numpy as np
import pandas as pd


############################# Acquire Codeup Log Data ##################################
def get_log_data():
    '''
    This function loads Codeup's access log data.
    
    parameters
    ----------
    None
    
    returns
    -------
    pandas DataFrame of Codeup's curriculum access logs.
    '''
    colnames=['date', 'time', 'page_viewed','user_id','cohort_id','ip']

    df = pd.read_csv('../data/anonymized-curriculum-access.txt',          
                    engine='python',
                    header=None,
                    index_col=False,
                    names=colnames,
                    sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
                    na_values='"-"',
                    usecols=[0,1,2,3,4,5])
    return df


def get_cohort_data():
    '''
    This function loads Codeup's Cohort ID Table.
    
    parameters
    ----------
    None
    
    returns
    -------
    pandas DataFrame of Codeup's Cohort ID's.
    '''
    df_cohorts = pd.read_csv('../data/cohorts.csv')
    return df_cohorts
