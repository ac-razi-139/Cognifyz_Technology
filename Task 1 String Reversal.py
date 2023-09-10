# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:14:58 2023

@author: hp
"""

class StringReversal:
    def create_string(self):
        self.my_string=input("Enter a string: ")
    def reverse_string(self):
        my_str=''
        for char in self.my_string:
            my_str=char+my_str
        print("Reverse of string is: ",my_str)
obj=StringReversal()
obj.create_string()
obj.reverse_string()