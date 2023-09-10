# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:26:12 2023

@author: hp
"""

from collections import Counter
import string

def count_words_in_file(filename):
    # Initialize a Counter to count word occurrences
    word_counter = Counter()

    try:
        # Open and read the text file
        with open(filename, 'r') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                cleaned_line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                # Split the line into words and update the counter
                words = cleaned_line.split()
                word_counter.update(words)

        # Display the results in alphabetical order
        for word, count in sorted(word_counter.items()):
            print(f'{word}: {count}')

    except FileNotFoundError:
        print(f'File not found: {filename}')

if __name__ == "__main__":
    # Specify the path to your text file
    filename = 'sample.txt'  # Replace with your file's path
    count_words_in_file(filename)
