## import library 
import numpy as np
import pandas as pd
import glob
import os


## concat All File in one file 
path = r'event_data'
all_files = glob.glob(path + "/*.csv")
alldf = []

for filename in all_files:
    df = pd.read_csv(filename)
    alldf.append(df)

AllEvent = pd.concat(alldf, axis=0, ignore_index=True)    
AllEvent.to_csv('event_datafile_new.csv')
