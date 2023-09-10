# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 08:08:52 2023

@author: hp
"""

import random

class NumberGuessing:
    def user_choice(self):
        self.user_input = int(input("Enter your choice: "))

    def computer_choice(self):
        self.comp_choice = random.randint(1, 100)

    def play_game(self):
        while True:
            self.user_choice()# We need to call self.user_guess() inside the play_game method 
            #to allow the user to keep entering their guesses until they guess the correct number or exit the game.
            if self.user_input == self.comp_choice:
                print(f"You win the game.")
                break
            elif self.user_input < self.comp_choice:
                print(f"Enter a higher number.")
            elif self.user_input > self.comp_choice:
                print(f"Enter a lower number.")
            else:
                print(f"Invalid pattern.")

obj = NumberGuessing()
obj.user_choice()
obj.computer_choice()
obj.play_game()
