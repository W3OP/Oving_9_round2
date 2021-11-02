# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:01:44 2021

@author: palme
"""

import sys
import re

class Sporsmaal:
    def __init__(self, tekst, svar, alternativ):
        self.tekst = tekst
        self.svar = svar
        self.alt = alternativ
        
    def undersok(self):
        quest = ""
        adventure = 1
        for i in self.alt:
            quest = quest +str(adventure)+ ":" + i + "\n"
            adventure += 1
        return(self.tekst + "\n" + quest)
    
    def Sjekk_svar(self, ass):
        return(ass == self.svar)
    
    def korrekt_svar_tekst(self):
        return(self.alt[int(self.svar)])
    

inputfilename = "sporsmaalsfil.txt" #Commented out for dev
if inputfilename == "":
    inputfilename = "sporsmaalsfil.txt"

try:
    inputfile = open(inputfilename, mode="r", encoding="utf-8")
except: 
    print("U goofed, file you want must be in the folder")
    sys.exit()
    

thequest = []
for line in inputfile:
    line = line.split(":")
    line[2] = re.findall("\w+", line[2])
    
    thequest.append(Sporsmaal(line[0].strip(),int(line[1].strip()),line[2]))

#for svar in thequest:
#    print(svar.undersok())
#    print(svar.korrekt_svar_tekst()+ "\n")


if __name__ == "__main__" :
    p1score = 0
    p2score = 0
    p1ans = ""
    p2ans = ""
    print("\n" + "\n" +"Skriv inn navnene til spillerne")
    spiller_1 = input("Spiller 1: ")
    spiller_2 = input("spiller 2: ")
    
    for game in thequest:
        print(game.undersok())
        
        p1ans = int(input(f"{spiller_1}: "))-1
        p2ans = int(input(f"{spiller_2}: "))-1
        
        print("Rett svar er: "+ game.korrekt_svar_tekst() + "\n")
        if p1ans == game.svar:
            p1score += 1
            print(f"{spiller_1} Rett!")
        else:
            print(f"{spiller_1} Tok FEIL!")
        if p2ans == game.svar:
            p2score += 1
            print(f"{spiller_2} Rett!")
        else:
            print(f"{spiller_2} Tok FEIL!")
        print("\n")
        
    print(f"{spiller_1} fikk " + str(p1score) + " poeng!")
    print(f"{spiller_2} fikk " + str(p2score) + " Poeng!")
    
    if p1score > p2score:
        print(f"{spiller_1} Vant!")
    elif p1score < p2score:
        print(f"{spiller_2} Vant!")
    else:
        print("Uavjort!")
















