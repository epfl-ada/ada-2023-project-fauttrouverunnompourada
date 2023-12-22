![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)


**FautTrouverUnNomPourADA presents:**

# **ADAgency&trade;: Precision Casting Through Data Insight**

### Abstract

ADAgency&trade; is pleased to welcome you to their agency, where stars are born and dreams become reality. Our mission is very simple: making your wish come true by all means we can. Do you want to start a career to earn a lot of money in big blockbuster movies? Or is your dream to leave an eternal print on the 7th art? We can do all of that for you!

Absolutely! In today's cinematic landscape, we are eager to offer our expertise to help guide your casting choices. Just fill out a quick personal form and define your goals—our algorithms will identify the ideal audition parameters to look out for tailored to you and your starry ambitions!

We eagerly anticipate your rise as the next ADAgency&trade; superstar [click here](https://benjaminaouzir.github.io/adagency-inc/) (Datastory) to join us!

### Research Questions

Throughout our research, we are trying to answer several questions:
- How does the gender of the lead actor in a movie affect the revenue and movie rating in different genres ?
- Which countries are the best to make a movie in depending on whether you want a good review or revenue and what the genre of your movie is?
- How does the diversity of the casting affect both the revenue and movie rating ?
- How does release year affect movie rating and revenue and are there any trends specific to genres?
- Can we build a model that allows us to predict revenue and movie rating with high accuracy?

### Additional datasets

Lately, the agency crawlers have worked to bring new information for our analysis. The two additional datasets are:
- The user ratings of every movie from the IMDb website (at least every movie that had a rating). This will allow the agency to analyse the success of a movie based on two criteria: box-office revenue and critical acclaim.
- The awards won and award nominations of every movie, also from the IMDb website. This allows us to judge even better how a certain movie was received, not only by the public, but also by the industry.

We have also completed the box-office revenue data by grabbing from IMDb every revenue that was not previously there.

All of this scraping was made using the [OMDb API](https://www.omdbapi.com/).

### Methods

#### Part 1 : Data preparation
**Step 1: Familiarisation to data set and planification**
Before jumping into a project, we take time to understand the initial data collection. The first step involves visualising the data to gauge its completeness and evaluate the project feasibility. Finally, we understand what data could be scraped to complete our dataset to achieve our goals.

**Step 2: Data scraping**
An aspect that was not present in the original dataset is the movie ratings, that we took from the IMDb website, along with the nominations and awards. We then used the movie summaries to proceed the identification of primary and secondary actors based on the number of apparitions of their character in each summary. This was done thanks to Flair as a Natural Language Processing (NLP) to extract character names. 

**Step 3: Data preprocessing**
Visualization aids in spotting outliers, which can often be errors that have entered the dataset inadvertently. For instance, instances like actors listed with a height of 510 meters or a negative age can be identified and addressed. We also need to adjust the revenue for inflation so that we compare it across eras. Furthermore, we perform one hot encoding transformation of the categorical data so we can use them in the model. We also need to modify some of the genres as there is often multiple categories per movie.

**Step 4: Identification of primary or secondary role**
By parsing summaries, we'll determine the primary and secondary actor for each movie. We use flair which is an NLP to get a list of every name in each summary. We then take the most and 2nd most mentioned name, make them correspond to the actors whose character shares the name and that gives us our primary and secondary actor. This distinction becomes crucial for building a model later, with the following structure: 
Output: Box office revenue (focused on financial success) or Critics' ratings (focused on prestige) Input: Movie-specific variables , Primary actor variables, Secondary actor variables.

#### Part 2: Features study
**Step 5: Features study**  
  - We make visualizations to see which genres are most done by each gender. And, by doing a matching to remove cofounders, we analyse whether the gender influence ratings and revenue in each genre. 
  - With the ethnicities, we try to understand how does the diversity of the cast influence the revenues and ratings. To make this possible, we need to introduce a concept of distances between the different ethnicities to make them more visual. This is done with the help of the Multidimensional scaling (MDS) which consists of a collection of analysis methods for data sets that have three or more variables, which define each data point. 
  - We compare countries revenue and IMDB ratings so we can give an answer on the best country to produce the movie. A Shapiro-Wilk test allowed us to determine that countries were not distributed normally. Once this observation made, we use a Pruskal-Walis test to see whether the differences between the revenues are significant. To see whether there's a correlation between revenue and rating, we run a Pearson linear regression.
  - Lastly, we wanted to check how has evolved the popularity of the genres through the years. This will help us afterwards to determine and highlight trends on genres.
  - All these studies allows to understand more how the features can influence both the revenues and the public acclaim. This results in mind we can start to create the model that will help us to predict either the revenue or the movie rating based on user's selectd features.
  
#### Part 3: Model selection and assessment
**Step 6: Model tuning and training**
We split the data into a train and test dataset. We tune three different tree-based models, XGBRegressor from xgboost, GradientBoostingRegressor from sklearn and RandomForestRegressor from sklearn, using cross validation. Then, we train them to predict IMDB rating and revenue. We get six different models, with 2 of each type, with one predicting revenue and the other IMDB rating.

**Step 7: Model assessment and selection**
Following model training, the different models are tested with the test data. We use RMSE, MAE and look at the distribution of the predictions of each model to determine which should be used for IMDB rating and which should be used for revenue.

#### Part 4: Application
**Step 8: Model Application**
In this phase, we will use the models to show which specificties (e.g. runtime or actor sex) someone's movie should have based on whether he wants critical or monetary success and what type of movie he wants to make.

**Step 9: Creating data story**
To conclude our study, we will prepare a data story which shows our results to answer the research questions. Furthermore, we'll allow user to play with our models to make wanted predictions to identify which movies would best suit him or his favorite actors.


### Timeline

Step 1 to 3: **Deadline milestone 2 17.11.2023**

Step 4: 25.11.2023

*Homework 2: 01.12.2023*

Step 5: 05.12.2023

Step 6: 10.12.2023

Step 7: 15.12.2023

Step 8: 19.12.2023

Step 9: **Deadline Milestone 3 22.12.2023**


### Organisation

| Agency Worker | Job |
|:-------------:|-----|
| Ali           | Initial data visualisation. Data cleaning. Ethnicity study. Creating data story|
| Benjamin      | Data scraping from IMDb website. Data cleaning. Primary and secondary role indentification. Gender Study. Creating data story. |
| Foaleng       | Project plannification. Primary and secondary role indentification. Model selection. ReadME and P3|
| Thomas        | Project plannification. Data cleaning. Model selection. Model assesment. Time study. Model application|
| Yaniss        | Initial data visualisation. Data cleaning. Space study. Creating data story.|

### Questions

ADAgency may reach out to you in case of any doubts!

### References

> David Bamman, Brendan O’Connor, and Noah A. Smith. 2013. **Learning Latent Personas of Film Characters**. In *Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 352–361, Sofia, Bulgaria. Association for Computational Linguistics.
