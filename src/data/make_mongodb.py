# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:05:10 2022

@author: Dave
"""

import pymongo
from pymongo import MongoClient, InsertOne
import json
from pathlib import Path
from config.definitions import *


def get_from_file():
    json_path = DATA_DIR / 'raw/household-travel-survey-trips.json'
    with open(json_path) as file:
        return json.load(file)
    
def update_mongo():
    
    # TODO: don't hard code the password
    uri = "mongodb+srv://StOny:fdOLHZqoU8523gus@cluster0.jpevnvt.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(uri)
    
    db = client.kingston_travel
    collection = db.trips_fact
    
    documents = get_from_file()
    result = collection.insert_many(documents)
    del documents
    client.close()
    return result
    
    