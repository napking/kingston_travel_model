# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:05:10 2022

@author: Dave
"""

import pymongo
from pymongo import MongoClient
import requests
import json
from pathlib import Path
from config.definitions import *
    
def create_mongo():
    # really only need to run this once to create the mongo server
    
    # TODO: don't hard code the password
    uri = "mongodb+srv://StOny:fdOLHZqoU8523gus@cluster0.jpevnvt.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(uri)
    
    db = client.kingston_travel
    
    results = []
    for collection_name in ['trips','households','persons']:
        # generate unique url for each collection
        url = "https://opendatakingston.cityofkingston.ca/api/v2/catalog/"\
            "datasets/household-travel-survey-" + collection_name + \
            "/exports/json?limit=-1&offset=0&timezone=UTC"
        response = requests.get(url)
        # convert the data to json
        documents = response.json()
        
        # 
        results.append(
            db[collection_name + "_facts"].insert_many(documents)
            )
    client.close()
    return results
    
    