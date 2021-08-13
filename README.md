## Analyzing Cookpad Reviews from Google device users


## Introduction
The goal of this project is to perform analysis on user-sumbitted reviews of the Cookpad app in order to identify trends and explore user feedback.

![cook](./images/conscious-design-I4e1cY1I0FQ-unsplash.jpg)

## Data Description and Preparation
This project uses user-provided reviews of the Cookpad app. Reviews from January 2019 through March 2021 were collected using [google-play-scraper](https://github.com/JoMingyu/google-play-scraper). 

See the [Data Prep Notebook](./code/nb1_data_collect_and_prep.ipynb) for additional information on data collection and preparation. 


## Analysis
This project includes EDA and general text analysis of user reviews of the Cookpad app. The following questions are addressed:

* Was there a difference in number of reviews submitted in 2019 (pre-pandemic) and 2020 (during pandemic)?
* Was there a difference in ratings submitted in 2019 (pre-pandemic) and 2020 (during)?
* What are the top 30 words used in 5 star ratings?
* What are the top 30 words used in 2 and 1 star ratings?

See the [EDA Notebook](./code/nb2_eda.ipynb) for more details.

## Repository Structure
```
--code
----nb1_data_collect_and_prep.ipnyb 
----nb2_eda.ipynb
--data (dir for all data files ingested/generated)
--images (dir for images)
```

## For More Information
* Contact the author [Leah Pope](https://www.linkedin.com/in/leahspope/)
