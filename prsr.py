# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:11:25 2017

@author: Lukas
"""

from HTMLParser import HTMLParser
import re

class Prsr(HTMLParser):
    def __init__(self, data):
        HTMLParser.__init__(self)
        self.data = data
    
    def handle_starttag(self, tag, attrs):
        if (tag == "a"):# links werden immer gespeichert
            for (key,value)in attrs:
                #print value
                self.data.link(value)
                    
    def handle_data(self, dt):
        for word in re.split("\W+",dt):
            if len(word) <= 0:
                return
            self.data.word(word)
    