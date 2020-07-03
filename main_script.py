import argparse
import datetime
import sys
from p_acquisition import m_acquisition as mac           # import from pack acquisition the module
from p_wrangling import m_wrangling as mwr               # import from pack wrangling the module
from p_analysis import m_analysis as man                 # import from pack analysis the module
#from p_reporting import m_reporting as mre


def argument_parser():
    parser = argparse.ArgumentParser(description = 'Set arguments path and file')
    parser.add_argument("-p", "--path", help="introduce your path and file location", type=str, dest="file", required=True)
    parser.add_argument("-c", "--country", help="introduce one country in case you want the result", type=str, dest="country", required=False)
    args = parser.parse_args()
    return args

def main(path):
    valid_pathfile = mac.validate_file(path)
    if valid_pathfile==False:
        sys.exit(f'Error: file/path <{path}> does not exist')
    data_raw = mac.data_connect(path)
    my_time=datetime.datetime.now()
    print(f'{my_time} Log: file database {path} already connected and imported and dataframe built')
    data_countries = mac.bring_web_country()
    my_time = datetime.datetime.now()
    print(f'{my_time} Log: country codes information already in a dataframe from a web')
    valid_country = mac.validate_country(one_country,data_countries)
    if valid_country==False:
        sys.exit(f'Error: country <{one_country}> does not exist or misspelled')
    data_cleaned = mwr.data_clean(data_raw)
    my_time = datetime.datetime.now()
    print(f'{my_time} Log: main dataframe already cleaned')
    data_jobs = mac.bring_api_data(data_cleaned)
    my_time = datetime.datetime.now()
    print(f'{my_time} Log: jobs information already in a dataframe from an API')
    data_merge = man.merge_information(data_cleaned,data_jobs,data_countries,one_country)
    my_time = datetime.datetime.now()
    print(f'{my_time} Log: information already merged and grouped and here the result')
    print(data_merge)
    data_arg= mwr.data_arguments(data_cleaned)
    my_time = datetime.datetime.now()
    print(f'{my_time} Log: arguments information already merged and grouped and here the result')
    print(data_arg)
    print('===>>>> Pipeline is complete. You may find the results in the folder ./data/results <<<<==========')

if __name__ == '__main__':
    arguments = argument_parser()
    path=arguments.file
    one_country=arguments.country
    main(path)