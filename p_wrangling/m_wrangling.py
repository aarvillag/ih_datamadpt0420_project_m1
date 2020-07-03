import pandas as pd

import re

# wrangling functions

# the function to clean age column and transform into integer value
def clean_age(x):
    if (len(re.findall('[0-9]{4}', x)) > 0 and len(x) == 4):
        return 2016 - int(x)
    else:
        y = re.findall('[0-9]{2}', x)
        return int(y[0])

# the function to clean gender column and transform into (male, female)
def clean_gender(x):
    if (x=='Fem'):
        return 'female'
    else:
        return x.lower()

# the function to clean gender column and transform into (male, female)
def clean_has_children(x):
    return x.lower()

# the function to clean gender column and transform into (male, female)
def clean_age_group(x):
    if (x=='juvenile'):
        return '14_25'
    else:
        return x

# the function to clean rural column and transform into (rural, non-rural)
def clean_rural(x):
    if (x=='urban' or x=='city'):
        return 'non_rural'
    elif x=='Country' or x=='countryside':
        return 'rural'
    else:
        return x.lower()

# the function to clean country_code column and transform GB to UK and GR to EL
def clean_country_code(x):
    if (x=='GR'):
        return 'EL'
    elif x=='GB':
        return 'UK'
    else:
        return x

# the function to clean the data frame
def data_clean(df_new):
# Now I clean the country_code column
    df_new['country_code']=df_new['country_code'].map(clean_country_code)
# Now I clean the rural column
    df_new['rural']=df_new['rural'].map(clean_rural)
# Now I clean the age_group column
    df_new['age_group']=df_new['age_group'].map(clean_age_group)
# Now I clean the dem_has_children column
    df_new['dem_has_children']=df_new['dem_has_children'].map(clean_has_children)
# Now I clean the gender column
    df_new['gender']=df_new['gender'].map(clean_gender)
# Now I clean the age column
    df_new['age'] = df_new['age'].map(clean_age)
    return df_new

def data_arguments(df_total):
    my_dict = df_total['question_bbi_2016wave4_basicincome_argumentsagainst'].value_counts().to_dict()
    list_arg = []                                 # information data manipulation to adapt and count it
    list_qty = []
    for i, j in my_dict.items():
        l = i.split('|')                           # split arguments joined in a list elements
        for m in l:
            list_arg.append(m.strip())
            list_qty.append(j)
    # create a dataframe for arguments against
    df_against = pd.DataFrame(list_arg, columns=['arguments_against'])
    df_against['qty'] = list_qty

    my_dict = df_total['question_bbi_2016wave4_basicincome_argumentsfor'].value_counts().to_dict()
    list_arg = []
    list_qty = []
    for i, j in my_dict.items():
        l = i.split('|')
        for m in l:
            list_arg.append(m.strip())
            list_qty.append(j)
    # create a dataframe for arguments for
    df_for = pd.DataFrame(list_arg, columns=['arguments_for'])
    df_for['qty'] = list_qty
    # dataframe with results
    df_result=pd.DataFrame(data=None, index=['In Favor', 'Against'],
                                             columns=['Number of Pro Arguments','Number of Cons Arguments'])
    df_result.iloc[1,0] = df_for[df_for['arguments_for']=='None of the above']['qty'].sum()
    df_result.iloc[0,0] = df_for['qty'].sum() - df_for[df_for['arguments_for']=='None of the above']['qty'].sum()

    df_result.iloc[1,1] = df_against[df_against['arguments_against']=='None of the above']['qty'].sum()
    df_result.iloc[0,1] = df_against['qty'].sum() - df_against[df_against['arguments_against']=='None of the above']['qty'].sum()
    df_result.to_csv(f'./data/results/df_final_arg.csv',index=True)
    return df_result