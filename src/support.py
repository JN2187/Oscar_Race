import pandas as pd

def standarize_title(df, column_name):

    '''
    Standarize the column names in a dataframe.
    It needs a dataframe and a column name.
    Returns a a list comprehension that is stripping every space contained in the selected column using the .title() method
    '''

    return (df[column_name].astype(str)).str.title()

def clean_year (df):
    '''
    Clean the dataframe.
    It needs a dataframe.
    Returns the first element in our dataframe splitted by " -", using the .split() method
    '''
    return df.split(" -")[0]
