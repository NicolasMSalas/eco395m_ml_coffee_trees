<h1 align="center"><img src="images/decision_tree.png" width="500"></h1>
<h1 align="center">Coffee Trees Midterm Project</h1>
<div> In this project, we are predicting the global price of coffee using different time series and machine learning models.</div>


# Introduction
The goal of this project is to predict the global monthly price of Coffee using data from 1990 to the present day. Specifically, we are training various models based on an 80-20 train-test split to predict the price of the last 20% of the prices based on the first 80%. We will use several different Machine Learning models and compare their results. 
# Data Sources & Collection 
## [Exchange Rates](https://data.imf.org/regular.aspx?key=61545850)
The data for the exchange rates of the top 5 coffee exporting countries was taken from the IMF database. It is measured as the value of the foreign currencies for 1 USD. The data was downloaded from the website and placed into the `raw_data` folder. I also renamed the files to make extracting easier, as they were all downloaded with the exact same name. Since the raw data from the IMF is formatted in a premade table, the `xr_clean_data.py` code is used to put the data in a format that is easily read.

## Commodity Prices
Commodity prices came from a dataset issued by the IMF. We focused on finding the global price of coffee as well as 2 complements (milk, sugar) and 1 substitue (tea). Some of the prices for these commodities vary based on different weights and volumes so they had to be normalized to (USD/pound).

## Futures Closing Prices
We also wanted to track the prices of coffee in the futures contract market so we grabbed a dataset from TradingView that contained the average closing price of a coffee futures contract on a month by month basis dating back to 1990. 

## [Weather Data](https://open-meteo.com/en/docs/historical-weather-api)
The weather data was extracted from Open-Meteo's Historical Weather API. We extract information for the top 5 coffee exporting nations, namely, Brazil, Vietnam, Colombia, Indonesia, and Honduras. This is because weather patterns would drive supply-side price changes. The code for extracting the information is in `code/extract_weather_b_v_c.py` and `code/extract_weather_indonesia_honduras.py`. The reason this is in two separate files is due to limitation of API calls. The data from these files are stored in the `raw_data` folder. We clean this data using `code/weather_data_cleaning.ipynb`. The cleaned data files are stored in the `clean_data` folder. The features here include : temperature, rainfall, wind speed, wind gusts, daylight duration, sunshine duration, and evapotranspiration.

## News Sentiment
The sentiment ratio data is from the Nexis Uni search function. We divided the amount of "marked negative" (as determined by their news reviewing AI) articles about coffee in a finance and banking setting by the total number of articles about coffee in the topics of finance and banking from 1990 to 2025. The data was only yearly so we split the change for each number into 12 equal parts, one for each month, then divided the numbers by one another each month to get a "sentiment ratio."

## Data Cleaning
Before fitting any models we derive mutual information scores to reduce our number of features from 44 to 25. Mutual information essentially computes feature importance by computing how much of the variance of the target variable each feature explains.

We had to take first differences of all our data to make it stationary, then we take the cumulative sum of the first differences to predict the actual price of coffee.

## Global Coffee Prices (Jan 1990 - Nov 2024)

![image](https://github.com/user-attachments/assets/145919e8-dc83-424f-a258-9c2927e85da7)

# Models and Results
## KNN
We fit a Time Series KNN Model. Rather than `train_test_split`, we consider `temporal_train_test_split`, which preserves the order of the data. We used `Standard Scalar` to scale the explanatory variables as KNN is a distance-based model. Through `GridSearchCV`, we got optimal k=11, and `weights = "distance"`, which indicates that this would be a weighted KNN model. 

Test MSE is 0.5820. I do a mutual information score on the differenced variables as well and reduce it to 14 features mostly to allow faster computation with KNN.
![image](https://github.com/NicolasMSalas/eco395m_ml_coffee_trees/blob/03294979d6c1af072a34b631d7954f331553ddf9/images/knn.png)


## Polynomial Regression
We fit a Polynomial Regression model, using data before 2018 as the training set and data during and after 2018 as the test set. We did this to see if there were any non-linear relationships between coffee prices and any of the features.

We ran intervals of `GridSearchCV` , finding that the best degree was one. Therefore, we moved to linear regression.

## Linear Regression
We fit on linear regression as it allowed for the use of classic Time Series models. In this case, we are focusing on the ARMA(1,1), the GARCH(1,1) and the ARDL(1,1) models. The ARMA model is selected as the ACF/PACF graphs hint that the coffee data follows this model outline. The GARCH model was considered as it takes the conditiional heteroskedasticity of the values into account, which is used for financial time series models. The ARDL model is different when compared to the previous two as it takes other variables into consideration. The number of lags for each model was determined by looking for the combination that gave the smallest AIC, BIC, and MSE. Much like the KNN, the `temporal_train_test_split` was used to train and test the model while maintaining the order of the data.

When looking at the various models used within the linear regression format, the following models are created.

![image](https://github.com/user-attachments/assets/85e2c36d-21e7-4157-adf8-96956614b407)

![image](https://github.com/user-attachments/assets/010b9ffc-0987-4aa6-ad55-a4d101b36854)

![image](https://github.com/user-attachments/assets/7100a325-e1c3-4aea-b7cd-c16e38a80e2b)

When comparing the three models, we can see that the ARDL model has the lowest AIC, BIC, and Test MSE. This is most likely due to the inclusion of other features that might help explain the price changes beyond changes in the previous coffee prices. However, there is potential overfitting when including the large selection of features, even when they have been reduced to fit better. There are also other forms of GARCH that take the conditional means and other parameters into consideration when building the model.

## Random Forest
Traditional Random Forest regressors are not inherently designed for time series seasonality, trends, or autocorrelation. However we wanted to see how well a random forest model could predict coffee prices. Random Forest is an ensemble learning method that combines multiple decision trees. Each tree is trained on a bootstrap sample (i.e., a random subset) of the training data, and the final prediction is typically the average of all the individual trees’ predictions.

The model forecasts the differenced series. To convert these forecasts back to level forecasts, we perform a cumulative sum of the predicted differences and add the last observed Coffee price from the training period. We do the same with the test set differences to obtain actual levels, then compute the Mean Squared Error on these level forecasts. The Mean Squared Error on Level Predictions: '0.0568'. In terms of the RMSE value, on average our model’s predictions are off by around $0.24 per pound.

![image](https://github.com/user-attachments/assets/bc671c3c-4260-40b6-a6a3-ae5db69f4130)


## Ridge Regression
We chose ridge regression because it handles multicollinearity really well and prevents overfitting with time series data that includes multiple correlated features (exchange rates, commodity prices, weather conditions...). Ridge regression is a linear model which penalizes large coefficients. The penalty shrinks large weights, which helps reduce variance in predictions. It's especially useful for dealing with noisy and highly correlated data. We're dealing with a lot of features and I wanted a straightforward way to incorporate them all without inflating the model parameters.

![output6](https://github.com/user-attachments/assets/18246c86-c023-4767-a92d-20d5fd994975)

We looked at the differenced coffee price data. The optimal alpha value was found to be 100, and our best MSE was 0.0090. Overall, the model succeeded in extracting meaningful signals.

## Which model was the "Winner" ?
The ridge regression performs better in terms of MSE, but when looking at the results when compared to the simplicity of generating them, the ARDL(1,1) model performs best as it does not need to tranform data beyond taking the first difference. 

### Result Tables
| Models  | ARMA(1,1) | GARCH(1,1) | ARDL(1,1) | KNN | Random Forest | Ridge |
|---------|----------|-----------|----------|---|---|---|
| **AIC** | -546.940 | -533.7 | -789.4 | -5.903 | -196.945 |-65.1932 |
| **BIC** | -531.696 | -526.1 | -628.3 | 30.56 | -143.467 |290.6698 |
| **Test MSE** | 0.3708 | 0.3971 | 0.0538 | 0.6522 | 0.0568 |0.0090 |
| **Test MAE** | 0.4572 | 0.4713 | 0.2048 | 0.6580 | 0.1947 |0.0727 |
| **R-Squared** | 0.4619 | 0.1632 | 0.1099 | -1.349 | 0.7955 |0.2922 |


# Limitations  
1) Since the top 5 coffee exporting countries have more volatile currencies when compared to the USD, there are rapid changes to the values which may undermine its effect on trade between these countries. This may reflect in a muted effect in the various models used.
2) The Sentiment Ratio data and the import data for the top coffee importing countries is not as helpful as it could have been if we had gathered it on a monthly basis, considering that we are trying to predict coffee prices on a monthly basis.  The Data itself is monthly, which means that particularly for stock prices, it might be helpful to have more frequent data. Additionally, our desire to forecast years into the future gives us some instability given the inherent volatility of the stock market, meaning that we could find much higher success if we picked a smaller prediction period.
3) For the weather data, we only get weather information from the top 5 coffee exporting countries. We don't consider how global weather patterns might affect global supply chains.

# Extensions
1) We considered measures of poltical stability, but it was difficult to get monthly data for that. With that information we could possibly look at how geopolitical factors might drive global coffee prices.
2) We don't focus too much on how demand-side factors might drive prices, so that would be an important factor that future work could consider.
3) More advanced methods such as Neural Networks, like, Long Short-Term Memory (LSTM) might give more accurate predictions.

# Declaration of Work
### Vignesh Avadhanam
Extracted and cleaned weather information. Fit optimal KNN model using GridSearchCV. 

### Chris Cain
Fit Ridge Regression model, gathered (unused) data on coffee imports from the top 5 coffee importing countries.

### Juan Guerra
Cleaned/pulled commodities data, and futures data. Created one data frame with all merged features. Worked on the random forest model code.

### Benjamin Hinrichs
Extracted and cleaned sentiment data, troubleshot on several models, organized readme, gathered info for requirement file

### Matias Ibarburu
Polynomial Regression, Cleaning and organization of the data folders. Gathered GDP data that was not used.

### Nicolas Salas
Extracted and cleaned Exchange Rate data. Fit optimal Linear Regression Predictions on Time Series Models.
