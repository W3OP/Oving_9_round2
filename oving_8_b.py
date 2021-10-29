# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:18:42 2021

@author: palme
"""

# Spørsmål: Hvor mange bein har hester? 
# Svaralternativ 
# 1
# 2
# 3
# 4


class Quiz:
    def __init__(self, spor, svar, fasit):
        self._spor = spor
        self._svar = svar
        self._fasit = fasit 
        
    def svaret(self, sjekk):
        if sjekk == self._fasit:
            return True
        return False
        
        
    def __str__(self):
        dur = self._spor + "\n"
        stuff = self._svar
        
        for key, value in enumerate(stuff):
            dur += f"Alternativ {key+1}: {value} \n"
        
        p = "Hvilket svaralternativ velger du? \n(Skriv bare tallet)"
        
        return dur + p 
        
        
    
    
    
if __name__ == "__main__":
#     print("Spørsmål 1: Hvor mange bein har en hest?")
    
    
    
    
    svarer = int(input("Skriv svar her: "))
    
