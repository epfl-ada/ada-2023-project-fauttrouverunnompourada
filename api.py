from flask import Flask, request, jsonify
import json
import requests
from flask_cors import CORS
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math
import numpy as np
import matplotlib.pyplot as plt
from xgboost import plot_importance
# from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import joblib

app = Flask(__name__)
CORS(app)

def create_zero_dataframe(columns_list,rows):
    data = {col: [0] * rows for col in columns_list}
    return pd.DataFrame(data)



def play_models_critics(data, model):
    if model == 'RandomForest':
        loaded_model = joblib.load('RandomForest_critics_model.pkl')
    elif model == 'XGB':
        loaded_model = joblib.load('XGB_critics_model.pkl')
    elif model == 'GBM':
        loaded_model = joblib.load('GBM_critics_model.pkl')
    else:
        raise ValueError("Invalid model type")

    unseen_data_predictions = loaded_model.predict(data)
    return unseen_data_predictions

def find_optimal_configuration_for_score(goal_score, model, data, features_to_predict, num_samples=10):
    closest_configuration = None
    closest_score_difference = float('inf')  # Initialize with a large value
    closest_score_achieved = None

    feature_ranges = {
        # Numerical features + Actors gender
        'Runtime': [30, 300],  # Example range for runtime values
        'Release year_x': [1913, 2010],
        'Actor height_x': [0.5, 2.5],
        'Actor age at release_x': [18, 100],
        'Actor height_y': [0.5, 2.5],
        'Actor age at release_y': [18, 100],
        'M-onehot_x' : [0,1],
        'M-onehot_y' : [0,1],
           # Languages
        'English Language-onehot': [0, 1],
        'Tamil Language-onehot': [0, 1],
        'Hindi Language-onehot': [0, 1],
        'Malayalam Language-onehot': [0, 1],
        'German Language-onehot': [0, 1],
        'Japanese Language-onehot': [0, 1],
        'Korean Language-onehot': [0, 1],
        'Spanish Language-onehot': [0, 1],
        'Italian Language-onehot': [0, 1],
        'French Language-onehot': [0, 1],
        'Standard Mandarin-onehot': [0, 1],
        'Standard Cantonese-onehot': [0, 1],
        'Bengali Language-onehot': [0, 1],
        'Cantonese-onehot': [0, 1],
        'Telugu language-onehot': [0, 1],
        'Russian Language-onehot': [0, 1],
        'Portuguese Language-onehot': [0, 1],
        'Urdu Language-onehot': [0, 1],
        'Arabic Language-onehot': [0, 1],
        'Tagalog language-onehot': [0, 1],
        'Swedish Language-onehot': [0, 1],
        # Countries
        'United States of America-onehot': [0, 1],
        'United Kingdom-onehot': [0, 1],
        'India-onehot': [0, 1],
        'Canada-onehot': [0, 1],
        'Germany-onehot': [0, 1],
        'Japan-onehot': [0, 1],
        'South Korea-onehot': [0, 1],
        'Argentina-onehot': [0, 1],
        'France-onehot': [0, 1],
        'Spain-onehot': [0, 1],
        'Ireland-onehot': [0, 1],
        'Hong Kong-onehot': [0, 1],
        'China-onehot': [0, 1],
        'Russia-onehot': [0, 1],
        'Australia-onehot': [0, 1],
        'Italy-onehot': [0, 1],
        'Mexico-onehot': [0, 1],
        'New Zealand-onehot': [0, 1],
        'Brazil-onehot': [0, 1],
        'Belgium-onehot': [0, 1],
        'Denmark-onehot': [0, 1],
        'Sweden-onehot': [0, 1],
        'Netherlands-onehot': [0, 1],
        'Philippines-onehot': [0, 1],
        # Genres
        'Thriller-onehot': [0, 1],
        'Science Fiction-onehot': [0, 1],
        'Horror-onehot': [0, 1],
        'Adventure-onehot': [0, 1],
        'Action-onehot': [0, 1],
        'Drama-onehot': [0, 1],
        'Comedy-onehot': [0, 1],
        'Romance Film-onehot': [0, 1],
        'Musical-onehot': [0, 1],
        'Fantasy-onehot': [0, 1],
        'Family Film-onehot': [0, 1],
        'Crime Fiction-onehot': [0, 1],
        'Indie-onehot': [0, 1],
        'World cinema-onehot': [0, 1],
        'Mystery-onehot': [0, 1],
        'Black-and-white-onehot': [0, 1],
        'Crime Thriller-onehot': [0, 1],
        # Ethnicities
        'White_x': [0, 1],
        'Black/African American_x': [0, 1],
        'South Asian_x': [0, 1],
        'East Asian_x': [0, 1],
        'American Indian/Alaska Native_x': [0, 1],
        'Pacific Islander_x': [0, 1],
        'Arab/Middle East_x': [0, 1],
        'Central and South Americans_x': [0, 1],
        'Other_x': [0, 1],
        'White_y': [0, 1],
        'Black/African American_y': [0, 1],
        'South Asian_y': [0, 1],
        'East Asian_y': [0, 1],
        'American Indian/Alaska Native_y': [0, 1],
        'Pacific Islander_y': [0, 1],
        'Arab/Middle East_y': [0, 1],
        'Central and South Americans_y': [0, 1],
        'Other_y': [0, 1]
    }

    feature_values = {}
    for feature in feature_ranges.keys():
        if feature in features_to_predict:
            if feature_ranges[feature][1] == 1:
                feature_values[feature] = [0, 1]  # For one-hot encoded features
            else:
                feature_values[feature] = np.linspace(feature_ranges[feature][0], feature_ranges[feature][1], num_samples)
    # Forms all different possible combinations to test
    combinations = np.array(np.meshgrid(*feature_values.values())).T.reshape(-1, len(feature_values))

    for idx, combo in enumerate(combinations):
        data_copy = data.copy()  # Create a copy of the original DataFrame

        for idx, feature in enumerate(feature_values.keys()):
            data_copy[feature] = combo[idx]

        predicted_critics = play_models_critics(data_copy, model)
        score_difference = abs(predicted_critics - goal_score)

        if score_difference < closest_score_difference:
            closest_configuration = tuple(combo)
            closest_score_difference = score_difference
            closest_score_achieved = predicted_critics

    return closest_configuration, closest_score_achieved


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api', methods = ['POST'])
def get_post_javascript_data():
    # print(request.json["name"])

    columns =  [
# Movie nurmerical features   
'Runtime', 'Release year_x', 
# Language categorical feature
'English Language-onehot','Tamil Language-onehot', 'Hindi Language-onehot','Malayalam Language-onehot', 'German Language-onehot','Japanese Language-onehot', 'Korean Language-onehot','Spanish Language-onehot', 'Italian Language-onehot','French Language-onehot', 'Standard Mandarin-onehot','Standard Cantonese-onehot', 'Bengali Language-onehot','Cantonese-onehot', 'Telugu language-onehot', 'Russian Language-onehot','Portuguese Language-onehot', 'Urdu Language-onehot','Arabic Language-onehot', 'Tagalog language-onehot','Swedish Language-onehot', 
# Country categorical feature
'United States of America-onehot', 'United Kingdom-onehot', 'India-onehot', 'Canada-onehot', 'Germany-onehot', 'Japan-onehot', 'South Korea-onehot', 'Argentina-onehot', 'France-onehot', 'Spain-onehot', 'Ireland-onehot', 'Hong Kong-onehot', 'China-onehot', 'Russia-onehot', 'Australia-onehot', 'Italy-onehot', 'Mexico-onehot', 'New Zealand-onehot', 'Brazil-onehot', 'Belgium-onehot', 'Denmark-onehot', 'Sweden-onehot', 'Netherlands-onehot', 'Philippines-onehot', 
# Genre categorical feature
'Thriller-onehot', 'Science Fiction-onehot', 'Horror-onehot', 'Adventure-onehot', 'Action-onehot', 'Drama-onehot', 'Comedy-onehot', 'Romance Film-onehot', 'Musical-onehot', 'Fantasy-onehot', 'Family Film-onehot', 'Crime Fiction-onehot', 'Indie-onehot', 'World cinema-onehot', 'Mystery-onehot', 'Black-and-white-onehot', 'Crime Thriller-onehot',
# Primary actor numerical features
'Actor height_x', 'Actor age at release_x',
# Primary actor gender categorical feature
'F-onehot_x','M-onehot_x',
# Primary actor ethnicity categorical feature
'White_x', 'Black/African American_x', 'South Asian_x', 'East Asian_x', 'American Indian/Alaska Native_x', 'Pacific Islander_x', 'Arab/Middle East_x', 'Central and South Americans_x', 'Other_x',
# Secondary actor numerical features
'Actor height_y', 'Actor age at release_y',
# Secondary actor gender categorical feature
'F-onehot_y', 'M-onehot_y',
# Secondary actor ethnicity categorical feature
'White_y', 'Black/African American_y', 'South Asian_y', 'East Asian_y', 'American Indian/Alaska Native_y', 'Pacific Islander_y', 'Arab/Middle East_y', 'Central and South Americans_y', 'Other_y'] # Replace this with your list of columns

# Creates one row to play with a singular made-up movie
    num_rows = 1

# Create the dataframe (zero_df is just a name, it will eventually be filled with made-up information)
    zero_df = create_zero_dataframe(columns,num_rows)
    zero_df

    Runtime = 110
    Release_year = 2007
    Languages= ['English']
    Countries = ['United States of America', 'United Kingdom']
    Genres = ['Thriller', 'Science Fiction']
    Primary_actor_height = 140
    Primary_actor_age = 42
    Primary_actor_gender = 'M'
    Primary_actor_ethnicity = 'Arab/Middle East'
    Secondary_actor_height = 180
    Secondary_actor_age = 18
    Secondary_actor_gender = 'F'
    Secondary_actor_ethnicity = 'Black/African American'
    # The differents features introduced above are entered in 'zero_df' through different ways according to their nature
    # Runtime
    zero_df['Runtime'] = Runtime
    # Release year
    zero_df['Release year_x'] = Release_year
    # Languages (one movie can have multiple languages)
    for lang in Languages:
        lang_column = f'{lang} Language-onehot'
        if lang_column in zero_df.columns:
            zero_df[lang_column] = 1
    # Countries (one movie can have multipe countries of production)
    for country in Countries:
        country_column = f'{country}-onehot'
        if country_column in zero_df.columns:
            zero_df[country_column] = 1
    # Genres (one movie can have multiple genres)
    for genre in Genres:
        genre_column = f'{genre}-onehot'
        if genre_column in zero_df.columns:
            zero_df[genre_column] = 1
    # Primary actor height
    zero_df['Actor height_x'] = Primary_actor_height
    # Primary actor age at release
    zero_df['Actor age at release_x'] = Primary_actor_age
    # Primary actor gender
    if Primary_actor_gender == 'M':
        zero_df['M-onehot_x'] = 1
    else:
        zero_df['F-onehot_x'] = 1
    # Primary actor ethnicity
    ethni = f'{Primary_actor_ethnicity}_x'
    if ethni in zero_df.columns:
        zero_df[ethni] = 1
    # Secondary actor height
    zero_df['Actor height_y'] = Secondary_actor_height
    # Secondary actor age at release
    zero_df['Actor age at release_y'] = Secondary_actor_age
    # Secondary actor gender
    if Secondary_actor_gender == 'M':
        zero_df['M-onehot_y'] = 1
    else:
        zero_df['F-onehot_y'] = 1
    # Secondary actor ethnicity
    ethni = f'{Secondary_actor_ethnicity}_y'
    if ethni in zero_df.columns:
        zero_df[ethni] = 1
    desired_score = 10
    features_to_predict = ['Runtime', 'Release year_x', 'Genres']

    # We reuse the 'zero_df' dataframe containing our made-up movie data
    # Call the function to find the closest values for specified features to the desired 'IMDb rating' using the 'RandomForest' model
    optimal_config, achieved_score = find_optimal_configuration_for_score(
        desired_score, 'RandomForest', zero_df, features_to_predict
    )
    data = {'optimal config': optimal_config}
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)