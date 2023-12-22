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
- Question on gender
- Question on space
- Question on ethnicity
- How does release year affect IMDB rating and revenue and are there any trends specific to genres?
- Can we build a model that allows us to predict revenue and IMDB rating with high accuracy?

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
Actors are typically driven by either financial gain or prestige. Therefore, it's essential to enhance our dataset by incorporating a metric for film prestige. We opted for IMDB movie ratings to fulfill this requirement. Additionally, we're leveraging the IMDB dataset to supplement our movie box office revenue data. Once again, visualization is employed to validate and deepen our comprehension of the data.

**Step 3: Data preprocessing**
Visualization aids in spotting outliers, which can often be errors that have entered the dataset inadvertently. For instance, instances like actors listed with a height of 510 meters or a negative age can be identified and addressed. Furthermore, when crucial values contain NaN (missing values), the respective data entries containing these missing values are removed to maintain data integrity.

**Step 4: Identification of primary or secondary role**
By parsing summaries, we'll evaluate each character's role as primary or secondary. This distinction becomes crucial for building a model later, with the following structure: 
Output: Box office revenue (focused on financial success) or Critics' ratings (focused on prestige) Input: Movie-specific variables (to be determined), Primary actor variables (to be determined), Secondary actor variables (to be determined)

#### Part 2: Features study
**Step 5: Features study**  
  - *Gender study*  
  - *Space study*  
  - *Ethnicity study*  
  - *Time study*  
  
#### Part 3: Model selection and assessment
**Step 6: Model tuning and training**
We split the data into a train and test dataset. We tune three different tree-based models, XGBRegressor from xgboost, GradientBoostingRegressor from sklearn and RandomForestRegressor from sklearn, using cross validation. Then, we train them to predict IMDB rating and revenue. We get six different models, with 2 of each type, with one predicting revenue and the other IMDB rating.

**Step 7: Model assessment and selection**
Following model training, the different models are tested with the test data. We use RMSE, MAE and look at the distribution of the predictions of each model to determine which should be used for IMDB rating and which should be used for revenue.

#### Part 4: Application
**Step 8: Model Application**
In this phase, we will use the models to show which specificties (e.g. runtime or actor sex) someone's movie should have based on whether he wants critical or monetary success and what type of movie he wants to make.

**Step 9: Creating data story**
To conclude our study, we will prepare a roleplay data story which shows our results interactively as well as enables user to play with our models to make wanted predictions to identify which movies would best suit him or his favorite actors.


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
| Foaleng       | Project plannification. Primary and secondary role indentification. Model selection. Readme and P3|
| Thomas        | Project plannification. Data cleaning.Model selection. Model assesment. Time study. Model application|
| Yaniss        | Initial data visualisation. Data cleaning. Space study. Creating data story.|

### Questions

ADAgency may reach out to you in case of any doubts!

### References

> David Bamman, Brendan O’Connor, and Noah A. Smith. 2013. **Learning Latent Personas of Film Characters**. In *Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 352–361, Sofia, Bulgaria. Association for Computational Linguistics.
