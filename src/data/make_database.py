# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:47:42 2022

@author: Dave
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

