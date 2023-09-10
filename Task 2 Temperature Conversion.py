# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 07:42:18 2023

@author: hp
"""

class TemperatureConversion:
    def __init__(self):
        self.celcius=int(input("Enter a temperature in celcius: "))
    def Conversion(self):
        fehrenheit=1.8*self.celcius+32
        print(f"Temperature in Fehrenheit scale is {fehrenheit}F.")
obj=TemperatureConversion()
obj.Conversion()