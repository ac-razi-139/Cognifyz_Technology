# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:23:56 2023

@author: hp
"""

import os

# Define the directory where your files are located
directory = 'path_to_directory'

# Define the new naming pattern (you can customize this)
new_name_prefix = 'file'
file_extension = '.txt'  # Change this to match your file type

# List all files in the directory
file_list = os.listdir(directory)

# Iterate through the files and rename them
for index, filename in enumerate(file_list):
    # Create the new file name
    new_name = f"{new_name_prefix}_{index+1}{file_extension}"
    
    # Construct the full paths for old and new names
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)
    
    print(f'Renamed: {filename} to {new_name}')

print('Renaming complete.')
