# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:55:02 2022

To convert from raw data (./data/raw/) to more usable forms (./data/interim/)

@author: napking
"""

import logging
from pathlib import Path
from config.definitions import *

import requests
import pandas as pd

#%%

def get_from_api(nrows=10, start=0):
    
    api_url = 'https://opendatakingston.cityofkingston.ca/api/records/1.0/search/' + \
    '?dataset=household-travel-survey-trips'
    params = {'rows': nrows,
              'start': start,
              }
    
    response = requests.get(api_url, params=params)
    
    return response.json()

def get_dataframe_from_response(response_json: dict):
    try:
        df = pd.json_normalize(response_json['records'])
        '''
        the normalize function colapses all nested entries into the same 'rank'
        but adds pre-fixes for each nested entry.
        For example, the structure of 'records' is similar to:
            new entry
            ├── 'datasetid'
            ├── 'recordid'
            ├── 'record_timestamp'
            └── 'fields'
                    ├── 'modesummary'
                    ├── 'personid'
                    ├── 'originada'
                    ├── ...
        
        the result is that all end-points nested in fields now have column names:
            'fields.modesummary', 'fields.personid' ...
        we want to bring those end-points up to the top level
        '''
        df.columns = df.columns.str.replace('fields.','',regex=False)
        # don't need datasetid as it is the same for all end-points
        df.drop('datasetid', axis=1, inplace=True)
        
        return df
        
    except:
        print('pandas could not parse the JSON')

#%%

def get_OD_table(data):
    try:
        return pd.pivot_table(data, values='recordid', aggfunc='count',
                              index='originada', columns='destada')
    except:
        print('pandas could not create the OD matrix')
        return None

#%%

def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    
    try:
        data = get_dataframe_from_response(get_from_api())
        print(data.shape)
        return data
    except:
        print('error')
    


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    data = main()
    
