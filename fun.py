# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 16:54:53 2017

@author: Lukas
"""
from database import DB

class work(DB):
    def __init__(self):
        DB.__init__(self)
        
    def show(self):
        self.db.execute("""
        SELECT D1.DOMAIN, L1.LINK, D2.DOMAIN, L2.LINK FROM REFERENCE
        JOIN 
            (SELECT * FROM LINK JOIN DOMAIN ON LINK.DOMAIN = DOMAIN.ID)AS L1
            ON REFERENCE.SRC = L1.ID
        JOIN 
            (SELECT * FROM LINK JOIN DOMAIN ON LINK.DOMAIN = DOMAIN.ID) AS L2
            ON REFERENCE.REF = L2.ID
        JOIN
            (SELECT * FROM DOMAIN) AS D1
            ON L1.DOMAIN = D1.ID
        JOIN 
            (SELECT * FROM DOMAIN) AS D2
            ON L2.DOMAIN = D2.ID;""")
            
        for tupel in self.db.fetchmany(100):
            print tupel[0] + tupel[1] +"\n \\\n\t-->  "+ tupel[2] + tupel[3] + "\n"

db = work()
db.show()