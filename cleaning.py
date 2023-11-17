#coding=utf-8

import dataframes as RAW
import pandas as pd
import numpy as np

# Clean movie data

clean_movie_data = pd.read_csv("../Clean data/clean_movie_data.csv")

# Clean character data

clean_character_data = pd.read_csv("../Clean data/clean_character_data.csv")