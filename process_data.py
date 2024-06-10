import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """ 
    input - "messages.csv" and "categories.csv"
    
    output - a merged database containing both messages and its categories
    
    """
    
    
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, how="left", on=["id"])
    return df

def clean_data(df):
     """ 
    input - merged df from the previous step
    
    output - df with "caetgories" column replaced with individual categories as columns
    
    1. this function will input category names
    2. split the category on a delimeter
    3. create a list of unique categories
    4. exclude the unwanted characters and append to an empty list
    5. assign the last character numeric in the category to the "categories" data columns
    6. drop the "categories" column from df and add individual categories as columns
    
    """
    
    # creating a categories data frame to clean text
    categories = df["categories"].str.split(";", expand=True)
    
    # a list of unique categories
    row = categories.iloc[:1]
    
    # an empty list to append later
    # with unique category names 
    category_colnames = []

    for category in row.iloc[0]:
        category_colnames.append(category[:-2])
    # this loop will remove the unwanted characters 
    # from the category name
    
    # renaming the columns of "categories" dataframe
    categories.columns = category_colnames
    
    # convert category values to just 0 and 1
    # and convert string to numeric
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str.slice(start=-1)

        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    
    # drop "categories" column from df
    df = df.drop(columns=["categories"])
    
    # adding categories as unique columns in df
    df = pd.concat([df, categories], axis=1)
    
    # dropping durplicate rows from each column
    # keeping the first instance
    df.drop_duplicates(keep="first", inplace=True)
    
    return df


def save_data(df, database_filename):
     """ 
    input - 1. dataframe from previous step
            2. database filename on SQL server to upload df
            
    this step will upload the final database to an SQLite server
    
    """

     # loading dataframe to the SQL server
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql("Message_Categorised", engine, index=False, )  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
