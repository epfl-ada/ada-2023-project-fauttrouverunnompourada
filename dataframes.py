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

# Change release dates to datetime objects
movie_data['Release date'] = pd.to_datetime(movie_data['Release date'], errors='coerce')

# Drop rows with invalid dates
movie_data = movie_data.dropna(subset=['Release date'])

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

tvtropes_path = r'../MovieSummaries/tvtropes.clusters.txt'

types = []
characters = []
movies = []
ids = []
actors = []

with open(tvtropes_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            name = parts[0]
            data = eval(parts[1]) 
            character = data.get('char', '')
            movie = data.get('movie', '')
            _id = data.get('id', '')
            actor = data.get('actor', '')

            types.append(name)
            characters.append(character)
            movies.append(movie)
            ids.append(_id)
            actors.append(actor)

data = {
    'Character type': types,
    'Character name': characters,
    'Movie': movies,
    'Freebase ID': ids,
    'Actor name': actors
}

tvtropes = pd.DataFrame(data)