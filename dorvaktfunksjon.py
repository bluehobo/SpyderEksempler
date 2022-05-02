# -*- coding: utf-8 -*-
"""
Spyder Editor


"""

def dorvakt(alder):
    if alder < 18:
        return "Du slipper ikke inn, dessverre"
    
    elif alder < 20 :
        return "Du får rødt armbånd"
    else :
        return "Du får grønt armbånd"


print(dorvakt(17))