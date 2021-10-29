# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:13:37 2021

@author: palme
"""

import oving_8_b as o8b

test = o8b.Quiz("Hvor mange bein har en hest", [1, 2, 3, 4],4)


print(test)

dude = int(input("Svar: "))
svar1 = test.svaret(dude)
if svar1:
    print("Svaret er rett")
else:
    print("Svaret er feil")

print("\n \n")


test2 = o8b.Quiz("Hvilket land er i i nå?", ["norge", "sverie", "danmark"],1)

print(test2)

dude2 = int(input("Svar: "))
svar2 = test2.svaret(dude2)
if svar2:
    print("Svaret er rett!")
else:
    print("Svaret er feil")
    

