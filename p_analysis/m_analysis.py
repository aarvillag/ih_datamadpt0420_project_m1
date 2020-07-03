import pandas as pd

# analysis functions

# the function to merge all information of dataframes (cleaned,jobs,countries)
def merge_information(df_new,df_jobs,df_countries,my_country):
    df_total = pd.merge(df_new, df_jobs, how='left', on='normalized_job_code')
    df_total = pd.merge(df_total, df_countries, how='left', on='country_code')
    df_total.to_csv('./data/processed/df_total_data.csv', index=False)  # write a total dataframe processed to a file
    if my_country is None:
        grouped = df_total.groupby(['country', 'title', 'rural']).size().reset_index()
        grouped = grouped.rename(columns={0: 'Quantity', 'country': 'Country', 'title': 'Job Title', 'rural': 'Rural'})
        grouped['Percentage'] = grouped['Quantity'] / grouped['Quantity'].sum() * 100
        grouped.to_csv(f'./data/results/df_total_result.csv', index=False)  # write a total dataframe processed to a file
    else:
        grouped = df_total[df_total['country'] == my_country].groupby(['country', 'title', 'rural']).size().reset_index()
        grouped = grouped.rename(columns={0: 'Quantity', 'country': 'Country', 'title': 'Job Title', 'rural': 'Rural'})
        grouped['Percentage'] = grouped['Quantity'] / grouped['Quantity'].sum() * 100
        my_country_ = my_country.replace(' ', '')
        grouped.to_csv(f'./data/results/df_total_result_{my_country_}.csv',index=False)  # write a country dataframe processed to a file
    return grouped
