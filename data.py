# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:29:30 2017

@author: Lukas
"""

from handler import Handler

class Data():
    def __init__(self):
        self.pos = [(),()]
        self.handler = Handler(self.pos)
        
    def word(self, word):
        if word != "":
            self.handler.word(word)
    
    def link(self, link):
        link = str(link).replace(' ', '%20') # Leerzeichen entfernen, da diese Fehler hervorrufen
        self.handler.link(link)
    
    def nextLink(self):
         #self.pos = self.handler.get()
         self.handler.save()
         print self.handler.next()
         return self.pos[0][1]+ self.pos[1][1]
