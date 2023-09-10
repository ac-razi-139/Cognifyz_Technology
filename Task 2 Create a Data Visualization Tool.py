# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:20:51 2023

@author: hp
"""

import pandas as pd
import plotly.express as px

# Load your dataset (replace 'data.csv' with your dataset file)
data = pd.read_csv('sample_data.csv')

def generate_interactive_plots(data):
    # Define a function to generate interactive plots
    # You can customize this function based on your dataset and visualization needs
    fig = px.scatter(data, x='x_column', y='y_column', color='category_column', title='Interactive Scatter Plot')
    
    # Customize the plot as needed (add labels, change plot type, etc.)
    
    # Show the interactive plot
    fig.show()

if __name__ == '__main__':
    generate_interactive_plots(data)
