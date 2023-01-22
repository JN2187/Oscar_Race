import pandas as pd

def standarize_title(df, column_name):

    '''
    Standarize the column names in a dataframe.
    It needs a dataframe and a column name.
    Returns a a list comprehension that is stripping every space contained in the selected column using the .title() method.
    '''

    return (df[column_name].astype(str)).str.title()

def clean_year (df):
    
    '''
    Clean the dataframe.
    It needs a dataframe.
    Returns the first element in our dataframe splitted by " -", using the .split() method.
    '''
    return df.split(" -")[0]

def create_year_range_df(start_year, end_year, df):
    
    '''
    Create a year range in the dataframe.
    This function takes in a start year, an end year and a dataframe.
    Return a filtered dataframe by the specified range of years.
    '''
    new_df = df[(df['year_ceremony'] >= start_year) & (df['year_ceremony'] <= end_year)]
    return new_df

