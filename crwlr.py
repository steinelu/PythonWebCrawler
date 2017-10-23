# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:05:49 2017

@author: Lukas
"""
from prsr import Prsr
from data import Data
import urllib2, sys, signal

url = "http://www.j3l7h2.de/crawlertest/0"

class Crwlr():
    def __init__(self):
        self.data = Data()
        self.prsr = Prsr(self.data)
        
        
    def loop(self):
        while True:
            self.next()
            self.prsr.reset()
            #break
            
    def next(self):
        link = self.data.nextLink()
        print link
        try:
            f = urllib2.urlopen(link)
            self.prsr.feed(f.read())
        except:
            print "Error: URLOpen"
    
    def close(self):
        self.data.handler.close()



if __name__ == "__main__":
    c = Crwlr()
    c.data.pos[0] = (0, "http://www.j3l7h2.de")
    c.data.pos[1] = (0, "/crawlertest/0")
    c.loop()

    def signal_handler(signal, frame):
        c.close()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)






    
