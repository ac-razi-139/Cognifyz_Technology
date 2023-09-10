# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:21:53 2023

@author: hp
"""

class PalindromeChecker:
    def create_string(self):
        self.my_str=input("Enter a string: ")
    def check_palindrome(self):
        new_str=''
        for char in self.my_str:
            new_str=char+new_str
        if self.my_str==new_str:
            print("Our string is palindrome.")
        else:
            print("String is not palindrome")
obj=PalindromeChecker()
obj.create_string()
obj.check_palindrome()