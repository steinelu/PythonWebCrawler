# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:03:11 2017

@author: Lukas
"""
from sqlalchemy import create_engine

#engine1 = create_engine("mysql+mysqldb:///crwlr.db")
engine = create_engine("sqlite:///crwlr.db")

connection = engine.connect()

#print engine2.table_names()

