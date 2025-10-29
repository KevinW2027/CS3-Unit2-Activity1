import pandas as pd
import numpy as np
df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1,how='all')
print(df.head())
print('How many ros and columns in the whole Dataset')
print(df.shape)
print(df.info()) # Summery of columns
budget_df = df[df['budget'] > 1000000]
print(budget_df.shape)
#Create a series form the budget column
#that uses the title column for the indicies
budget_lookup = pd.Series(budget_df['budget'].values, index=budget_df['title'])
print(budget_lookup)
print(budget_lookup['Heat'])
 
#define the condition to be checked:, .index is the title of the movie
condition = (budget_lookup.index >= 'A Bag of Hammers') & (budget_lookup.index <= 'Byzantium')
budget_lookup_a_b = budget_lookup[condition]

# Part C, numbers as indicies

runtime_lookup = pd.Series(df['title'].values, index= df['runtime'])
runtime_lookup = runtime_lookup.sort_index()
print(runtime_lookup)

# Filter Series by removing movies that are longer than 180 min and shorter than 10min
condition2 = (runtime_lookup.index < 180) & (runtime_lookup.index > 10)
runtime_lookup = runtime_lookup[condition2]
print(runtime_lookup)

#how many movies are exactly 40 minutes long
print(runtime_lookup.loc[40])
# How many movies are 40 mins
print(runtime_lookup.loc[40].shape)
print(runtime_lookup.iloc[100])