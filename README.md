# CatchUp : News Recommender Chrome Extension

### Introduction

We are in a world bombarded with information. We can access all kinds of information easily but we do not want to do that. Everybody reads only news or articles that are new and relevant to themselves. To keep users coming back, there are many recommender systems.

### Problem Statement 

I want to create a project that users can access the news they want easily. I decided to create a chrome extension as it lives on on browser and users do not need to go to a particular website to get their news.  

### Project Structure

1. Data Analysis and Modeling
   This folder contains the EDA, analysis and topic modeling for the project.
2. LR Model API
   This is the Flask api hosted on Heroku. It will return predictions based on the articles sent to it.
3. Link Text Extraction
   This is the api to scrape the user's history links content. It is hosted on Amazon.
4. News Article Extraction
   This is an api hosted on Amazon to perform scheduled webscraping on news sites. However, it is easier to code with News API.

### About The Data

There are 2 sets of news articles dataset. One is from Harvard University, one is from webhose. Total there are more than 170k articles.

##### EDA

1. As the articles from webhose are in json format, I process them into dataframes. I also merged the 2 datasets together and export as a csv.

### How CatchUp Works

1. The chrome extension will retrieve uses's history to determine user reading habits. 
2. The list will be sent to a webscraping api where the actual content of the links are extracted.
3. The extracted text will then be sent to another text cleaning api to preprocess the text to be sent to the model for predictions.
4. Based on the predictions, the topics are retrieved from News API to be displayed in the extension.

### Modeling

##### General Approach: 

1. LDA is first used on the text to get the topics needed.
2. To further improve the coherence score and get the topics of each articles, Mallet LDA is used.
3. We create a new articles dataframe but with the topic column.
4. This new dataset will be used to train the model for classification.
5. For classification, we explored Linear Regression and Naive Bayes. This model is extracted out and hosted on Heroku.

### Conclusion & Recommendations 

1. Currently the recommendation system works on a very simple premise. There are many ways to improve the model like using user based filtering. As we do not have many users now, we are unable to create users profile.

2. The model can be further improved by creating a weighted approach. Means the app should allow the user to like an article and the article type will be weighted more.

   

   
