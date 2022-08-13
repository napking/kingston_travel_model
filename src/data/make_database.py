# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:47:42 2022

@author: Dave
"""

from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import sqlite3
from sqlite3 import Error

#%%

Base = declarative_base()

class trip_fact(Base):
    __tablename__ = "trip_fact"
    # Creating all the table attributes
    trip_id = Column(Integer, primary_key=True)
    person_id = Column(Integer)
    mode1 = Column(Integer)
    mode2 = Column(Integer)
    mode3 = Column(Integer)
    originspecialgenerator = Column(Integer)
    destspecialgenerator = Column(Integer)
    schoollevel_id = Column(Integer)
    trippurpose_id = Column(Integer)
    hbgroupdesc = Column(String)
    destreportzone = Column(Integer)
    originreportzone = Column(Integer)
    triptype_id = Column(Integer)
    weekday_id = Column(Integer)
    primarymode = Column(Integer)
    destfocusarea = Column(String)
    originfocusarea = Column(String)
    modesummary = Column(String)
    walkingdistance = Column(Float)
    drivingdistance = Column(Float)
    bikingdistance = Column(Float)
    walkable = Column(Boolean)
    bikingduration = Column(Float)
    eucliddistance = Column(Float)
    drivingduration = Column(Float)
    numvehocc = Column(Integer)
    bikeable = Column(Boolean)
    walkingduration = Column(Float)
    tripnum = Column(Integer)
    departtime = Column(Integer)
    tripfactorrounder = Column(Float)
    # defining relationships
    
    #TODO
    

#%%

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:/Users/Dave/MyPythonScripts/kingston_travel/data/processed/kingston_travel.db")
    
#%%

