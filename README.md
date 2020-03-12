# CatchUp : News Recommender Chrome Extension

### Introduction

We

In this project, we will make use of the data collected by the Department of Public Health to predict the presence of the West Nile Virus in Chicago with the aim of developing a cost effective plan to deploy pesticides throughout the city. 

### Problem Statement 

Predicting the presence of the West Nile Virus in order to recommend a deployment plan for the pesticides throughout the city. 

### Project Structure



### About The Data

The [data](https://www.kaggle.com/c/predict-west-nile-virus/) is made up of 4 datasets, weather.csv, spray.csv, train.csv and test.csv.

##### What was fixed?

1. For the spray dataset, the outliers (spray information on 2011-08-29) were dropped as the location of the spray did not have any corresponding information for that region in the other datasets. 
2. For the weather dataset, the individual columns were analysed and rows with null values were dropped. Some of the features that displayed collinearity were also combined or dropped during EDA and Feature Engineering steps
3. For the train dataset, there were duplicated rows which corresponding to observations will be dealt with in Feature Engineering.
4. Upon comparison of the train data set and the test data set, the feature indicating the number of mosquitos was absent in the test data set. The categorical feature (mosquito species) was one-hot-encoded.

The final test and train data sets can be found as [train_clean.csv](./datasets/train_clean.csv) and [test_clean.csv](./datasets/test_clean.csv) , respectively. 

### EDA, Cleaning and Pre-processing

##### General Approach: 

1. Deal with Null Values 
2. One hot encoding of Nominal Features
3. Certain collinear features in weather were dropped. This includes Tmin, Tmax, Wetbulb, Heat and Cool which are closely related to temperature Tavg and Dewpoint. The goal was to reduce the features, leaving those that were reflective of how hot/cold and how dry/wet the weather is. 
4. Relationship between number of mosquitos various periods and other features were analysed. 
5. Features were analysed to see if there are any trends for the presence for WNV. 
6. Weather data had records of the daily measurements from 2 station per day and the weather corresponding to station with the closer longitude. 

##### Some Findings:

<u>Presence of WNV</u>

- Increment in WNV presence starts from June and peaks in Aug and decreases from Sep onwards. 

<u>Mosquitos Species</u>

- In terms of species, pipiens and pipiens/restuans are the 2 major species observed to have the WNV.

<u>Effect of Spray on Number of Mosquitos</u>

- When comparing the number of mosquitos before and after a spray was carried out it can be observed that there is a reduction in the total number of mosquitos (intensity of the plots reduced). 
- It can also be observed in 2013, that there were clusters with a high number of mosquitos in certain areas but no spray was carried out. As such the aim of the model hopes to recommend more targeted spray regions.

### Feature Engineering

##### <u>Relative Humidity</u>

Dry/wet weather is influenced by the precipitation level and presence of moisture in the air. With the presence of dewpoint temperature and average temperature, the relative humidity, which reflects the percentage of moisture in the air, was created. 

##### <u>Conversion of Months to reflect Cyclical Nature</u>

Months of the year are cyclical, as such this feature was converted to cyclical nature to the model using sin and cosine functions. 

##### <u>Total Mosquito by Species</u>

Summed up the observation for duplicate rows, for the same trap and mosquito species to get the total number. 

### Modeling: To Determine Presence of WNV

##### General Approach: 

1. The dataset was imbalanced, with 95% of observations belonging to observations where the WNV is not present (class 0). SMOTETomek, a combination of oversampling (of class 1) and undersampling (class 0) was used. 

2. Train-test-split will be applied on train set for model validation and selection. 

3. The following models were used: 

   ​		a) Decision Tree with hyperparameter tuning

   ​		b) Random Forest Classifier with hyperparameter tuning

   ​        c) Ada Boost 

   ​        d) Gradient Boost 

   ​        e) Support Vector Machine

##### Metrics Used to Validate Model:

1. ROC AUC Score: this metric is used for evaluation on Kaggle 
2. Mean Accuracy Score of Model

##### Findings:

Ada Boost model performed the best and was selected. 

| Model                    | ROC\-AUC Score |
| ------------------------ | -------------- |
| Decision Tree            | 0\.869         |
| Random Forest Classifier | 0\.947         |
| Ada Boost                | 0\.949         |
| Gradient Boost           | 0\.905         |
| Support Vector Machine   | 0\.626         |

### Kaggle Scores

| S/N  | Description                                                  | Public Score |
| ---- | ------------------------------------------------------------ | :----------: |
| 1    | Final Model  (Ada Boost)                                     |   0.67954    |
| 2    | Ada Boost Model (One Hot Encoded Year)                       |   0.64243    |
| 3    | Ada Boost Model (Feature Engineer - Cyclical Nature for Month, Year Removed) |   0.57082    |
| 4    | Ada Boost Model (Feature Engineer - Cyclical Nature for Month) |   0.63181    |
| 5    | Baseline Model (Ada Boost: Feature Engineer - Relative Humidity) |   0.49437    |

### Recommending the Spray Locations 

1. Spray locations will be recommended based on higher probability of occurrence of WNV.

### Conclusion & Recommendations 

1. The months of Jul to Sep, corresponding to the hot months, is the season with a high number of mosquitos which in turn leads to a high risk of a WNV outbreak. Pipiens & Pipiens/Restuans are the 2 main mosquito breeds where the presence of WNV was detected.

2. Based on the previous spray data in 2011 and 2013, it can be observed that vector control can be more targeted with the use of our model.

3. Based on the model developed, we have predicted 9 clusters in 2014 with a higher risk of WNV outbreak.

4. The cost of pesticide control should also factor other trade-offs such impact on health, medical bills and loss in productivity in order to have a better sense of the overall economic cost. Future work would include the use of medical data and the costs to have a more complete analysis. 

   
