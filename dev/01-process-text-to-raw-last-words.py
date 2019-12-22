# %% [markdown]
# Imports
import pandas as pd
import numpy as np

# %% [markdown]
# Load Data
df = pd.read_csv('data/raw/Texas_Last_Statement.csv', encoding='iso-8859-1')

# %% [markdown]
# Replace 'None' and drop nulls
df = (df.assign(LastStatement=lambda df: df['LastStatement'].replace('None', np.nan))
      .dropna(subset=['LastStatement']))

# %% [markdown]
# Split Data
train_text_df = df.sample(frac=.7)
test_text_df = df[~df['Execution'].isin(train_text_df['Execution'])]

train_text = train_text_df['LastStatement'].values
test_text = test_text_df['LastStatement'].values

# %% [markdown]
# Write Data
np.savetxt('data/raw/train.txt', train_text, delimiter="<|endoftext|>", fmt="%s")
np.savetxt('data/raw/test.txt', test_text, delimiter="<|endoftext|>", fmt="%s")

# %%
