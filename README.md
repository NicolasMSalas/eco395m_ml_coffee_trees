<h1 align="center"><img src="images/decision_tree.png" width="500"></h1>
<h1 align="center">Coffee Trees Midterm Project</h1>
<div> In this project, we are predicting the global price of coffee using different time series models within machine learning.</div>


# Introduction
The goal of this project is to predict the global monthly price of Coffee using data from 1990 to the present day. Specifically, we are training various models based on an 80-20 train-test split to predict the price of the last 20% of the prices based on the first 80%. We will use several different Machine Learning models and compare their results. 
# Data Sources & Collection 
## Exchange Rates
The data for the exchange rates of the top 5 coffee exporting countries was taken from the IMF database. It is measured as the value of the foreign currencies for 1 USD. The data was downloaded from the website and placed into the `raw_data` folder. I also renamed the files to make extracting easier, as they were all downloaded with the exact same name. Since the raw data from the IMF is formatted in a premade table, the `xr_clean_data.py` code is used to put the data in a format that is easily read.

## Commodity Prices

## Futures Closing Prices

## Weather Data
The weather data was extracted from Open-Meteo's Historical Weather API. We extract information for the top 5 coffee exporting nations, namely, Brazil, Vietnam, Colombia, Indonesia, and Honduras. This is because weather patterns would drive supply-side price changes. The code for extracting the information is in 'code/extract_weather_b_v_c.py' and `code/extract_weather_indonesia_honduras.py`. The reason this is in two separate files is due to limitation of API calls. The data from these files are stored in the `raw_data` folder. We clean this data using `code/weather_data_cleaning.ipynb`. The cleaned data files are stored in the `clean_data` folder.

## News Sentiment
The sentiment ratio data is from the Nexis Uni search function. We divided the amount of "marked negative" (as determined by their news reviewing AI) articles about coffee in a finance and banking setting by the total number of articles about coffee in the topics of finance and banking from 1990 to 2025. The data was only yearly so we split the change for each number into 12 equal parts, one for each month, then divided the numbers by one another each month to get a "sentiment ratio."

# Models
## KNN
We fit a Time Series KNN Model. Rather than `train_test_split`, we consider `temporal_train_test_split`, which preserves the order of the data. We used `Standard Scalar` to scale the explanatory variables as KNN is a distance-based model. Through `GridSearchCV`, we got optimal k=5, and `weights = "distance"`, which indicates that this would be a weighted KNN model. 
## Matias

## Linear Regression
We fit on linear regression as it allowed for the use of classic Time Series models. In this case, we are focusing on the ARMA(1,1), the GARCH(1,1) and the ARDL(1,1) models. The ARMA model is selected as the ACF/PACF graphs hint that the coffee data follows this model outline. The GARCH model was considered as it takes the conditiional heteroskedasticity of the values into account, which is used for financial time series models. The ARDL model is different when compared to the previous two as it takes other variables into consideration. The number of lags for each model was determined by looking for the combination that gave the smallest AIC, BIC, and MSE. Much like the KNN, the `temporal_train_test_split` was used to train and test the model while maintaining the order of the data.

## Chris
We fit chose ridge regression because it handles multicollinearity really well and prevents overfitting with time series data that includes multiple correlated features (exchange rates, commodity prices, weather conditions...). Ridge regression is a linear model which penalizes large coefficients. The penalty shrinks large weights, which helps reduce variance in predictions. It's especially useful for dealing with noisy and highly correlated data. We're dealing with a lot of features and I wanted a straightforward way to incorporate them all without inflating the model parameters.


# Results
## Vighnesh

## Matias

## Linear Regression
When looking at the various models used within the linear regression format, the following models are created.

![image](https://github.com/user-attachments/assets/85e2c36d-21e7-4157-adf8-96956614b407)

![image](https://github.com/user-attachments/assets/010b9ffc-0987-4aa6-ad55-a4d101b36854)

![image](https://github.com/user-attachments/assets/7100a325-e1c3-4aea-b7cd-c16e38a80e2b)

| Models  | ARMA(1,1) | GARCH(1,1) | ARDL(1,1) |
|---------|----------|-----------|----------|
| **AIC** | -546.940 | -533.7 | -789.4 |
| **BIC** | -531.696 | -526.1 | -628.3 |
| **Test MSE** | 0.3708 | 0.3971 | 0.0538 |

When comparing the three models, we can see that the ARDL model has the lowest AIC, BIC, and Test MSE. This is most likely due to the inclusion of other features that might help explain the price changes beyond changes in the previous coffee prices. However, there is potential overfitting when including the large selection of features, even when they have been reduced to fit better. 

## Chris
We looked at the differenced coffee price data. I built lagged features from all available numeric columns and then used Ridge regression to fit those features. The optimal alpha value was found to be 100, which yielded an RMSE of about 0.095 on the test set and an R² of about 0.29. The model outperformed trivial baselines that produced RMSE values around 0.115, but didn't achieve exceptional accuracy. Overall, the model succeeded in extracting meaningful signals from the lagged features.

Coffee's differenced values are likely correlated strongly with each other (and other variables), so Ridge regression was probably beneficial here since the penalty reduces random noise without sacrificing the more stable relationships, resulting in a more robust model.


## Talk about which model was the "Winner" 


# Limitations of the Data
Since the top 5 coffee exporting countries have more volatile currencies when compared to the USD, there are rapid changes to the values which may undermine its effect on trade between these countries. This may reflect in a muted effect in the various models used. The Sentiment Ratio data and the import data for the top coffee importing countries is not as helpful as it could have been if we had gathered it on a monthly basis, considering that we are trying to predict coffee prices on a monthly basis. 

You’ll produce a README.md which will explain your problem, explain and present relevant analysis of your dataset, show the results of evaluating your models, detailing your modeling process and your final conclusion.

You’ll include an appendix that explains how to use your code to create your results. You must provide your code and README.md in a public GitHub repo.

Use of a New Models, Techniques or Packages - (10 points)

You'll use at least one model, technique or package that we did not cover in class.
The Report in README.md - (20 points)

The report should cover your problem, data sources and your evaluation and your recommendations.

Requirements for reporting your modeling and evaluation:

The problem must be clearly articulated and goals must be clear
Source(s) of dataset(s) must be clearly documented
Data collection methods must be understood and clearly documented. You should read and summarize the documentation of the data, make sure that you understand and document all columns/features that are relevant to your analysis. You should understand and summarize what isn’t in the data too.
Limitations of the data must be clearly outlined
Your modeling approaches must be clearly explained and evaluated.
The limitations of the modeling must be clearly outlined.
You must make recommendations for the best model or approach
You should not include analysis, plots, discoveries, that aren’t directly related to your findings – you can put them as an appendix in another file if you like
Reproducibility - (20 points)

Your work must be reproducible. This means that anyone should be able to follow your instructions to run your code on your data and get the same results you do.

Requirements for reproducibility:

Instructions to rerun that analysis must be included in the README.md
Additional packages should be included in requirements.txt
All data cleaning must be reproducible through code – data must not be manually modified (i.e. no modifications in Excel)
Must use relative paths
Data should be included in the repository if the dataset is small enough, otherwise, instructions for downloading the datasets and placing them in the right locations are required
Your code should have as few entry points as reasonable. I.e. rather than requiring data_cleaning_step_1.py, data_cleaning_step_2.py, etc., to be run, have simply data_cleaning.py
