import pandas as pd
import os.path
from sqlalchemy import create_engine
import requests

# acquisition functions

def validate_file(path):                                  # Checking if file exists
    if (os.path.isfile(f'./{path}')):
        return True
    else:
        return False

def data_connect(path):
    engine_connection = create_engine(f'sqlite:///./{path}')    # data/raw/raw_data_project_m1.db
    my_tables=engine_connection.table_names()
    for i in range(0,len(my_tables)):
        x=my_tables[i]
        query=f'SELECT * FROM {x}'
        df_i = pd.read_sql(query, con=engine_connection)
        if i==0:
           df_new=df_i
        else:
            df_new=pd.merge(df_new,df_i, how='left', on='uuid')
    # df_new.to_csv(f'./data/raw/df_new')                           # we save the 1st version of dataframe
    return df_new

#the function to bring information from scraping a web for country codes management
def bring_web_country():
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    my_html = pd.read_html(url)                                       # this is a list of dataframes
    countries = dict()
    now = 'C'
    for df in my_html:
        for f in range(0, len(df.index)):
            for c in range(0, len(df.columns)):
                if (isinstance(df.iloc[f, c], str)):
                    if (now == 'C'):
                        my_country = df.iloc[f, c]
                        now = 'CC'
                    else:
                        my_country_code = df.iloc[f, c]
                        my_country_code = my_country_code.replace('(', '')
                        my_country_code = my_country_code.replace(')', '')
                        now = 'C'
                        countries[my_country] = my_country_code
    df_countries = pd.DataFrame(countries.items(), columns=['country', 'country_code'])
    return df_countries

def validate_country(one_country, df_countries):
    if ((one_country in df_countries['country'].unique()) or (one_country is None)):
        return True
    else:
        return False

# the function to bring information from jobs API
def bring_api_data(df_new):
# 1st I create a list with uniq values of normalized_jod_code in the table
    my_l = list(set(df_new['normalized_job_code'].to_list()))
    long=len(my_l)
    my_result = []
    cont=0
    print(f'Log: started bringing jobs information from API')
    for i in my_l:
        cont +=1
        response = requests.get(f'http://api.dataatwork.org/v1/jobs/{i}')
        results = response.json()
        my_result.append(results)
        print(f'Processing {cont} of {long} records')
# Creation a dataframe with information from API
    df_jobs = pd.DataFrame(my_result)
    df_jobs = df_jobs.drop('error', axis=1)                              # Cleaning
    df_jobs = df_jobs.rename(columns={'uuid':'normalized_job_code'})        # Rename a column
    return df_jobs

