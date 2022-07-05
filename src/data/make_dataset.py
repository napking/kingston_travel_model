# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:55:02 2022

To convert from raw data (./data/raw/) to more usable forms (./data/interim/)

@author: napking
"""

import logging
from pathlib import Path
from config.definitions import *


#%%


#%%

def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    while True:
        try:
            response = input("Do you want to create(c) all interim data?") \
                .lower().strip()
            if response == "c" or response == "create":
                # Insert code or function reference to convert raw data into interim data
                from src.util import store_interim_data, get_data_from_api
                
                nrows = int(input("How many records would you like to generate from source API?"))
                data = get_data_from_api(nrows=100)
                
                              
                store_interim_data(data,key=str(nrows) + 'records')
        
                
                print('~~\nYou chose to create data. \n ')                    
                break
            elif response == "exit":
                print('~~\nNo data was stored or retrieved')
                break
            else:
                print('Invalid input. Try Again. \n -> Type "exit" to leave.')
        except:
            print('Invalid input. Try Again')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
