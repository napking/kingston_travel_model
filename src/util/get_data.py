# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:08:26 2022

@author: Dave

#util/get_data.py

Utility functions to retrieve and store interim data elsewhere in the project.
run: from src.util.get_data import {function name}
"""
import shelve, requests
from config.definitions import ROOT_DIR, DATA_DIR, DATA_INTERIM_DIR, SHELF_NAME
import pandas as pd

#%% Shelving

def get_interim_data(interim_directory=DATA_INTERIM_DIR, key='default',
                     shelf_name=SHELF_NAME ):
    with shelve.open(str(interim_directory / shelf_name)) as shelf:
        return shelf[key]

def store_interim_data(interim_data, key, interim_directory=DATA_INTERIM_DIR,
                    shelf_name=SHELF_NAME ):
    with shelve.open(str(interim_directory / shelf_name)) as shelf:
        shelf[key] = interim_data
        return None

def get_interim_keys(interim_directory=DATA_INTERIM_DIR,
                     shelf_name=SHELF_NAME):
    with shelve.open(str(interim_directory / shelf_name)) as shelf:
        return list(shelf.keys())

def get_data_from_api(nrows=100):
    url = 'https://opendatakingston.cityofkingston.ca/api/records/1.0/search/' + \
        '?dataset=household-travel-survey-trips&q=&rows=' + str(nrows)
        
    response = requests.get(url)
    records = response.json()['records']
    
    df = pd.DataFrame()
    for ix, record in enumerate(records):
        df = pd.concat([df, 
                        pd.DataFrame(record['fields'], index=[ix])],
                        )
    return df