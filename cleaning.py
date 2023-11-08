#coding=utf-8

import dataframes as RAW
import pandas as pd
import numpy as np

# add archetype names to the character metadata

archetypes = [
    'Hero', 'Anti-Hero', 'Villain', 'Mentor', 'Sidekick', 'Love Interest',
    'Herald', 'Threshold Guardian', 'Shapeshifter', 'Trickster',
    'Damsel in Distress', 'Ally', 'Outlaw', 'Innocent', 'Jester', 'Shadow'
]

character_data_ft_archetypes = RAW.character_data.copy()

for archetype in archetypes:
    character_data_ft_archetypes[archetype] = 0

# filter for NaN character names

character_data_ft_archetypes = character_data_ft_archetypes.dropna(subset=['Character name'])

# merge the character and summary dataframes on the Wiki ID column

character_data_ft_archetypes['Wiki ID'] = character_data_ft_archetypes['Wiki ID'].astype(str)
RAW.summaries['Wiki ID'] = RAW.summaries['Wiki ID'].astype(str)

character_data_ft_summaries = character_data_ft_archetypes.merge(RAW.summaries, on='Wiki ID', how='left')

# filter for NaN valued summaries

character_data_ft_summaries = character_data_ft_summaries.dropna(subset=['Summary'])