# eco395m_ml_coffee_trees
Topic: Forecasting Coffee Commodity Prices
Variables/Features:
1) Real GDP of top 5 coffee exporting country (Brazil, Vietnam, Colombia, Indonesia, Honduras)
2) News/Sentiment Analysis
3) Complements (Milk/Sugar), Substitutes(Tea)
    * The units used in the FRED data measures by cents per pound. I think it would be helpful to convert to USD per pound.
    * The tea data is measured in cents per kilogram. When using it, convert to USD per POUND.
5) Political Stability
6) Volume of Imports to top importing countries (US, Germany, France, Italy, Canada)
7) Exchange Rates
8) Price of Coffee Futures in Commodity Markets
9) Weather????????????????????

Possible Methods:
1) Linear Regression (AR, MA, ARIMA, GARCH models)
2) Polynomial Regression models 
3) KNN Regression
4) Random Forests ?
5) Ridge Regression
6) Neural Networks common in research papers

<h1 align="center"><img src="images/coffee_bean.png" witdh="600"></h1>
<h1 align="center">Coffee Trees Midterm Project</h1>
<div> In this project, we are predicting the global price of coffee using different time series models within machine learning.</div>
