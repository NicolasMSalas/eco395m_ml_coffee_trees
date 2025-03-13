<h1 align="center"><img src="images/decision_tree.png" width="500"></h1>
<h1 align="center">Coffee Trees Midterm Project</h1>
<div> In this project, we are predicting the global price of coffee using different time series models within machine learning.</div>


# Introduction
The goal of this project is to predict the monthly price of Coffee futures at the Chicago Stock exchange, using data from 1990 to the present day. Specifically, we want to predict the price of coffee futures for a range of dates. We will use several different Machine Learning models and compare their results. 
# Data Sources & Collection 
## Exchange Rates
The exchange rates data was taken from the IMF database. It is measured as the value of the foreign currencies for 1 USD. The data was downloaded from the website and placed into the `raw_data` folder. Since the raw data from the IMF is formatted in a premade table, the `xr_clean_data.py` code is used to put the data in a format that is easily read.

## Commodity Prices

## Futures Closing Prices

## Weather Data
The weather data was extracted from Open-Meteo's Historical Weather API. We extract information for the top 5 coffee exporting nations, namely, Brazil, Vietnam, Colombia, Indonesia, and Honduras. This is because weather patterns would drive supply-side price changes. The code for extracting the information is in 'code/extract_weather_b_v_c.py' and `code/extract_weather_indonesia_honduras.py`. The reason this is in two separate files is due to limitation of API calls. The data from these files are stored in the `raw_data` folder. We clean this data using `code/weather_data_cleaning.ipynb`. The cleaned data files are stored in the `clean_data` folder.

## News Sentiment
The sentiment ratio data is from the Nexis Uni search function. We divided the amount of "marked negative" (as determined by their news reviewing AI) articles about coffee in a finance and banking setting by the total number of articles about coffee in the topics of finance and banking from 1990 to 2025. The data was only yearly so we split the change for each number into 12 equal parts, one for each month, then divided the numbers by one another each month to get a "sentiment ratio."


# Limitations of the Data
EACH PERSON FILL IN WHAT THE LIMITATIONS OF YOUR DATA ARE

## Exchange Rates

## Commodity Prices

## Futures Closing Prices

## Weather Data

## News Sentiment
The Sentiment Ratio data and the import data for the top coffee importing countries is not as helpful as it could have been if we had gathered it on a monthly basis, considering that we are trying to predict coffee prices on a monthly basis. 


# Models
DESCRIBE THE MODEL YOU CHOSE, AND WHY YOU CHOSE IT
## KNN
We fit a Time Series KNN Model. Rather than `train_test_split`, we consider `temporal_train_test_split`, which preserves the order of the data. We used `Standard Scalar` to scale the explanatory variables as KNN is a distance-based model. Through `GridSearchCV`, we got optimal k=5, and `weights = "distance"`, which indicates that this would be a weighted KNN model. 
## Matias

## Nick
I chose the linear regression as it allowed for the use of classic Time Series models. In this case, I am focusing on the ARMA(1,1), the GARCH(1,1) and the ARDL(1,1) models. I am using the ARMA model as the ACF/PACF graphs hint that the coffee data follows this model outline. When looking at a combination of the lowest AIC, BIC, and MSE, the ARMA(1,1) was best fit. The GARCH model was considered as it takes the conditiional heteroskedasticity of the values into account, which is used for financial time series models. Much like the ARMA model, the GARCH(1,1) model was the best combination of lagged coffee prices and lagged variances of the coffee prices. The ARDL model is different when compared to the previous two as it takes other variables into consideration. Much like the previous two models, the ARDL(1,1) model performs best when comparing the combination of lagged variables. 

## Chris
I chose ridge regression because it handles multicollinearity really well and prevents overfitting with time series data that includes multiple correlated features (exchange rates, commodity prices, weather conditions...). Ridge regression  penalizes large coefficients, which helps stabilize predictions. It's especially useful for dealing with noisy and highly correlated data.


# Results
DESCRIBE YOUR MODEL RESULTS
## Vighnesh

## Matias

## Nick

## Chris

## Talk about which model was the "Winner" 



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
