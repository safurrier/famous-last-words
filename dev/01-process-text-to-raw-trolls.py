# %% [markdown]
# Imports
import pandas as pd
import numpy as np
import json

# %% [markdown]
# Load Data
df = pd.read_json('data/raw/cyber_trolls.json', lines=True)
# %% [markdown]
# Pull Labels and Drop non aggressive text


def pull_label(x):
    return int(x['label'][0])


df = df.assign(Label=lambda df: df['annotation'].apply(pull_label))
df = df[df['Label'] == 1]

# %% [markdown]
# Split Data

train_text_df = df.sample(frac=0.8)
test_text_df = df.drop(train_text_df.index)

train_text = train_text_df['content'].values
test_text = test_text_df['content'].values

# %% [markdown]
# Write Data
np.savetxt('data/raw/train.txt', train_text, delimiter="\n", fmt="%s")
np.savetxt('data/raw/test.txt', test_text, delimiter="\n", fmt="%s")

# %%
