# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 12:57:26 2022

@author: Dave
"""

from pymongo import MongoClient
from pprint import pprint

def main():
    
    # TODO: don't hard code the password
    uri = "mongodb+srv://StOny:fdOLHZqoU8523gus@cluster0.jpevnvt.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(uri)
    
    db = client.kingston_travel
    collection = db.trips_fact
    
    # querying using a cursor object
    cursor = collection.find({"fields.mode1": "Walked (incl. jogging )"})
    
    result = []
    for doc in cursor:
        result.append(doc)
    
    client.close()
    return result

if __name__ == '__main__':
    result = main()
    