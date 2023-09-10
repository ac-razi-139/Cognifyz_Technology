# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:21:05 2023

@author: hp
"""
import re
class EmailValidator:
    def __init__(self):
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    def email(self):
        self.my_email=input("Enter an email address: ")
    def check_isvalid(self):
        if re.match(self.email_pattern,self.my_email):
            return True
        return False
obj=EmailValidator()
obj.email()
is_validity=obj.check_isvalid()
if is_validity:
    print("Valid email address.")
else:
    print("Invalid email address. Please enter a valid one.")
        
