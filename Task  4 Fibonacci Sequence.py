# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:33:30 2023

@author: hp
"""

class FibbonaciSequence:
    def __init__(self):
        self.n1=0
        self.n2=1
        self.num=int(input("Enter a desired number: "))
    def fibbonacci(self):
        for x in range(self.n1,self.num):
            print(self.n1)
            nxt=self.n1+self.n2
            self.n1=self.n2
            self.n2=nxt
obj=FibbonaciSequence()
obj.fibbonacci()