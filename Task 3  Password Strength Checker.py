# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 11:10:36 2023

@author: hp
"""
import re
class PasswordStrength:
    def create_password(self):
        self.password=input("Enter your password: ")
    def check_length(self):
        if len(self.password)>=8:
            return True
        return False
    def check_lowercase(self):
        for char in self.password:
            if char.islower():
                return True 
        return False
    def check_uppercase(self):
        for char in self.password:
            if char.isupper():
                return True 
        return False
    def check_digit(self):
        for char in self.password:
            if char.isdigit():
                return True
        return False
    def check_specialcharacters(self):
        special_characters=r"[!@#$%^&*()\-_=+[\]{};:'\",<.>/?\\|]"
        if re.search(special_characters,self.password):
            return True
        return False
obj=PasswordStrength()
obj.create_password()
length_check=obj.check_length()
lowercase_check=obj.check_lowercase()
uppercase_check=obj.check_uppercase()
digit_check=obj.check_digit()
special_char=obj.check_specialcharacters()
if length_check and lowercase_check and uppercase_check and digit_check and special_char:
    print("Strong password! Good job!")
else:
    print("Weak password. Please choose a stronger one.")