import pandas as pd

artists = pd.read_csv('artists.dat', sep = '\t', usecols = ['id', 'name'])
print (artists)