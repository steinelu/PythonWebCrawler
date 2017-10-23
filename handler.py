# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:28:49 2017

@author: Lukas
"""

from database import DB

class Handler(DB):
    def __init__(self,pos, DBPath = None):
        DB.__init__(self, DBPath)
        self.pos = pos
        
    def word(self, word):
        tab = self.isWord(word)
        # zu inlist hinzufügen
        self.db.execute("SELECT * FROM INLIST WHERE WORD='"+str(tab[0])+"' AND LINK='"+str(self.pos[1][0])+"';")
        inlist = self.db.fetchall()
        if inlist == []:
            self.db.execute("INSERT INTO INLIST VALUES('"+str(tab[0])+"','"+str(self.pos[1][0])+"');")
            #self.save()
        
    def isWord(self, word):
        self.db.execute("SELECT ID FROM WORD WHERE WORD = '"+ str(word) +"';")
        tab = self.db.fetchone()
        if tab is None:
            self.db.execute("SELECT COUNT(ID) FROM WORD;")
            tab = self.db.fetchone()
            self.db.execute("INSERT INTO WORD VALUES('"+str(tab[0])+"','"+word+"');")
            #self.save()
        return tab
        
    def link(self, link):
        if(link == ""):
            return
        if self.check(link): # neue Webseite
            dom,link = self.splitUrl(link)
        else:
            dom = self.pos[0][1]
        
        if (self.blacklist(link)): # keine bilder oder sowas
            return
        self.db.execute("SELECT ID FROM DOMAIN WHERE DOMAIN = '"+dom+"';")
        domid = self.db.fetchone()
        if domid is None:
            #domain hinzufügen
            self.db.execute("SELECT COUNT(ID) FROM DOMAIN;")
            domid = self.db.fetchone()
            self.db.execute("INSERT INTO DOMAIN VALUES('"+str(domid[0])+"','"+dom+"');")
            #self.save()
        
        #link abspeichern
        self.db.execute("SELECT ID FROM LINK WHERE LINK = '"+link+"';")
        linkid = self.db.fetchone()
        if linkid is None:
            self.db.execute("SELECT COUNT(ID) FROM LINK;")
            linkid = self.db.fetchone()
            self.db.execute("INSERT INTO LINK VALUES('"+str(linkid[0])+"','"+str(domid[0])+"','"+link+"');")
            #self.save()
        
        #refs ghinzufügen
        if self.pos[1][0] == linkid[0]:
            return
            
        self.db.execute("SELECT * FROM REFERENCE WHERE SRC='"+str(self.pos[1][0])+"' AND REF='"+str(linkid[0])+"'")
        ref = self.db.fetchone()
        if ref is None:#hinzufügen
            self.db.execute("INSERT INTO REFERENCE VALUES('"+str(self.pos[1][0])+"','"+str(linkid[0])+"');")
            #self.save()
            
        
    def check(self, link):# interner oder externer link
        if (("http" in link[:4]) or ("www." in link[:4])):
            return True
        return False
            
    def blacklist(self, url):
        
        if url[0] != '/':
           
            return True
        
        #Blacklist
        ends = ["doc", "pdf", "jpg", "JPG", "Jpg"]  # alle nicht gewollten Endungen
        for end in ends:
            end = "." + end
            if (end in url):
                return True
        return False
    
    def splitUrl(self, url):
        cnt = 0
        for i,c in enumerate(url):
            if c =='.':
                cnt = cnt +1
            if cnt >=2:
                if c == '/':
                    cnt = i
                    break
        return url[:cnt], url[cnt:]
    
    def next(self):
        #neuen link raussuchen und zurückgebeb und setzten
        self.db.execute("SELECT DOMAIN.ID, DOMAIN.DOMAIN, LINK.ID, LINK.LINK FROM DOMAIN JOIN LINK ON LINK.DOMAIN = DOMAIN.ID WHERE LINK.ID = '"+str(self.pos[1][0]+1)+"';")
        n = self.db.fetchone()
        if n is None:
            n = [0,"",0,""]
            n[0] = self.pos[0][0]
            n[1] = self.pos[0][1]
            n[2] = self.pos[1][0]
            n[3] = self.pos[1][1]
        self.pos[0] = (n[0], n[1])
        self.pos[1] = (n[2], n[3])
        return self.pos[0][1] + self.pos[1][1]
        
