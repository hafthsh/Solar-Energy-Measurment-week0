import os
import pandas as pd
def calculate_z_scores(data, columns):
    z_scores = pd.DataFrame()
    
    for col in columns:
        z_scores[col] = (data[col] - data[col].mean()) / data[col].std()
    
    return z_scores