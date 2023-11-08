#coding=utf-8

import pandas as pd

'''
CHARACTER METADATA
Links character stats (name and ID) to actor stats (name, age, ethnicity...)
'''

character_data = pd.read_csv('../MovieSummaries/character.metadata.tsv', delimiter='\t', header=None)
character_data.rename(columns={0: 'Wiki ID', 1: 'Freebase ID', 2: 'Release date', 3: 'Character name', 4: 'Actor DOB', 5: 'Actor gender', 6: 'Actor height', 7: 'Actor ethnicity', 8: 'Actor name', 9: 'Actor age at release', 10: 'Map ID', 11: 'Character ID', 12: 'Actor ID'}, inplace=True)

'''
MOVIE METADATA
Gives info on movies (release, countries, languages...)
'''

movie_data = pd.read_csv('../MovieSummaries/movie.metadata.tsv', delimiter='\t', header=None)
movie_data.rename(columns={0: 'Wiki ID', 1: 'Freebase ID', 2: 'Movie name', 3: 'Release date', 4: 'Revenue', 5: 'Runtime', 6: 'Languages', 7: 'Countries', 8: 'Genres'}, inplace=True)

'''
NAME CLUSTERS
Links character names to Freebase ID
'''

character_names = pd.read_csv('../MovieSummaries/name.clusters.txt', delimiter='\t', header=None)
character_names.rename(columns={0: 'Character name', 1: 'Freebase ID'}, inplace=True)

'''
PLOT SUMMARIES
Links movie summaries to Wiki ID
'''

summaries = pd.read_csv('../MovieSummaries/plot_summaries.txt', delimiter='\t', header=None)
summaries.rename(columns={0: 'Wiki ID', 1: 'Summary'}, inplace=True)

'''
TVTROPES CLUSTERS
Connects characters to achetypal character categories
'''

tvtropes = pd.read_csv('../MovieSummaries/tvtropes.clusters.txt', delimiter='\t', header=None)
tvtropes.rename(columns={0: 'Character type', 1: 'Example'}, inplace=True)