# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:15:15 2017

@author: Lukas
"""

import sqlite3

class DB():
    def __init__(self, path = None):
        try:
            self.conn = sqlite3.connect('crwlr.db')
            self.db = self.conn.cursor()
        except:
            print "Error: DB init"

    def save(self):
        self.conn.commit()
    def clean(self):
        pass
    def close(self):
        self.conn.close()
        