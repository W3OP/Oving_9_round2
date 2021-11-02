# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 13:30:09 2021

@author: palme
"""

kladd = "sporsmaalsfil.txt"



class question:
    def __init__(self, quest, alts, answer):
        self.question = quest
        self.alternatives = alts
        self.answer = answer
    
    def ask(self):
        q = ""
        a = 1
        for i in self.alternatives:
            q = q + str(a)+ ": " + i + "\n" 
            a += 1        
        return(self.question + "\n" + q)
    
    def Sjekk_svar(self, a):
        return(a == self.answer)
    
    def korrekt_svar_teks(self):
        return(self.alternatives[int(self.answer)])
    
    
