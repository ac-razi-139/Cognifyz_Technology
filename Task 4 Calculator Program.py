# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 08:14:40 2023

@author: hp
"""

class Calculator:
    def __init__(self):
        self.x=int(input("Enter the value for x: "))
        self.y=int(input("Enter the value for y:"))
        print("\n")
    def Addition(self):
        a=self.x+self.y
        print(f"Addition of x and y is {a}")
    def Subtraction(self):
        s=self.x-self.y
        print(f"Subtraction of x and y is {s}")
    def Multiplication(self):
        m=self.x*self.y
        print(f"Multiplication of x and y is {m}")
    def Division(self):
        if self.y==0:
            print(f"Cannot divide by zero.")
        else:
            d=self.x/self.y
            print(f"Division of x and y is {d}")
            
obj=Calculator()
obj.Addition()
obj.Subtraction()
obj.Multiplication()
obj.Division()
            
       
        
       
