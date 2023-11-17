![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)


**FautTrouverUnNomPourADA presents:**

# **ADAgency&trade;: Precision Casting Through Data Insight**

### Abstract

ADAgency&trade; is pleased to welcome you to their agency, where stars are born and dreams become reality. Our mission is very simple: making your wish come true by all means we can. Do you want to start a career to earn a lot of money in big blockbuster movies? Or is your dream to leave an eternal print on the 7th art? We can do all of that for you!

Indeed, in the current era of cinema, we would like to bring our insight in order to make informed decisions about casting for you. By filling a quick form on your identity, professional abilities and career goals, our cutting-edge algorithms will allow us to filter from thousands of potential auditions and find the most suited for you!

We eagerly anticipate your rise as the next ADAgency&trade; superstar!

### Research Questions

Throughout our research, we are trying to answer several questions:
- Find out which auditions (external data) best suit an actor in respect to his career goal (critical or monetary focused) as well as his previous experience and characteristics. 
- Does the suitable actor differ based on the desired outcome: critical acclaim or financial success?
- What impact does an actor's previous experience have on a movie's success?

### Additional datasets

Lately, the agency crawlers have worked to bring new information for our analysis. For now, the two additional datasets are:
- The user ratings of every movie from the IMDb website (at least every movie that had a rating). This will allow the agency to analyse the success of a movie based on two criteria: box-office revenue and critical acclaim.
- The awards won and award nominations of every movie, also from the IMDb website. This allows us to judge even better how a certain movie was received, not only by the public, but also by the industry.

We have also completed the box-office revenue data by grabbing from IMDb every revenue that was not previously there.

All of this scraping was made using the [OMDb API](https://www.omdbapi.com/).

In the future, we also wish to collect additional movie and actor data that we have not used to train our model in order to get some testing data. We will probably use the [Cinemagoer](https://cinemagoer.readthedocs.io/en/latest/) library to do so.

### Methods

#### Part 1 : Data preparation
**Step 1: Familiarisation to data set and planification**
Before jumping into a project, we take time to understand the initial data collection. The first step involves visualising the data to gauge its completeness and evaluate the project feasibility. Finally, we understand what data could be scraped to complete our dataset to achieve our goals.

**Step 2: Data scraping**
Actors are typically driven by either financial gain or prestige. Therefore, it's essential to enhance our dataset by incorporating a metric for film prestige. We opted for IMDB movie ratings to fulfill this requirement. Additionally, we're leveraging the IMDB dataset to supplement our movie box office revenue data. Once again, visualization is employed to validate and deepen our comprehension of the data.

**Step 3: Cleaning of data**
Visualization aids in spotting outliers, which can often be errors that have entered the dataset inadvertently. For instance, instances like actors listed with a height of 510 meters or a negative age can be identified and addressed. Furthermore, when crucial values contain NaN (missing values), the respective data entries containing these missing values are removed to maintain data integrity.

**Step 4: Identification of primary or secondary role**
By parsing summaries, we'll evaluate each character's role as primary or secondary. This distinction becomes crucial for building a model later, with the following structure: 
Output: Box office revenue (focused on financial success) or Critics' ratings (focused on prestige) Input: Movie-specific variables (to be determined), Primary actor variables (to be determined), Secondary actor variables (to be determined)

#### Part 2: Model selection and assessment
**Step 5: Model selection**
Choosing a model requires grasping the linearity between variables and the output. The first step thus involves visualising the data to pinpoint the ideal model for our predictions. Using our observations, we'll select the model that aligns best with our dataset. According to our model a splitting of the data will be needed for building coherent models (splitting based on country/time of production). Furthermore, variable selection through correlation analysis will also be required based on the selected models.

**Step 6: Model assessment**
Following model training through cross-validation, different models are tested with never-seen external scraped movie data. Our best models will be chosen for application.

#### Part 3: Application
**Step 7: Exploring research questions**
In this phase, we will leverage our model to address the research questions by delving into its operational intricacies and experimenting with diverse input variables.

**Step 8: Creating data story**
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
| Ali           | Initial data visualisation. Data cleaning. Model selection. Explore first research question.|
| Benjamin      | Data scraping from IMDb website. Data cleaning. Model assesment. Creating data story. |
| Foaleng       | Project plannification. Primary and secondary role indentification. Model selection. Explore third research question.|
| Thomas        | Project plannification. Data cleaning. Primary and secondary role indentification. Model assesment. Creating data story.|
| Yaniss        | Initial data visualisation. Data cleaning. Model selection. Explore second research question. |

### Questions

ADAgency may reach out to you in case of any doubts!

### References

> David Bamman, Brendan O’Connor, and Noah A. Smith. 2013. **Learning Latent Personas of Film Characters**. In *Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 352–361, Sofia, Bulgaria. Association for Computational Linguistics.
