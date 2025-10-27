import pandas as pd
import numpy as np
df = pd.read_csv('movies_metadata_v2.csv', encoding='iso-8859-1').dropna(axis=1,how='all')
print(df.head())
print('How many ros and columns in the whole Dataset')
print(df.shape)
print(df.info()) # Summery of columns
budget_df = df['budget' > 1000000]
print(budget_df.shape)
budget_lookup = pd.Series()
print