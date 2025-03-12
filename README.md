<h1 align="center"><img src="images/decision_tree.png" width="500"></h1>
<h1 align="center">Coffee Trees Midterm Project</h1>
<div> In this project, we are predicting the global price of coffee using different time series models within machine learning.</div>


# Introduction
The goal of this project is to predict the monthly price of Coffee futures at the Chicago Stock exchange, using data from 1990 to the present day. We want to both predict the price of coffee futures for a range of dates and also forecast the price of coffee futures one month in the future, using information up to that day. We will use several different Machine Learning models and compare their results. 
# Data Sources & Collection 
EACH PERSON FILL IN WHERE YOU GOT YOUR DATA
The sentiment ratio data is from the Nexis Uni search function. We divided the amount of "marked negative" (as determined by their news reviewing AI) articles about coffee in a finance and banking setting by the total number of articles about coffee in the topics of finance and banking from 1990 to 2025. The Data was only yearly so we split the change for each number into 12 equal parts, one for each month, then divided the numbers by one another each month to get a "sentiment ratio."

## Exchange Rates

## Commodity Prices

## Futures Closing Prices

## Weather Data

# Limitations of the Data
EACH PERSON FILL IN WHAT THE LIMITATIONS OF YOUR DATA ARE

The Sentiment Ratio data and the import data for the top coffee importing countries is not as helpful as it could have been if we had gathered it on a monthly basis, considering that we are trying to predict coffee prices on a monthly basis. 



# Models
DESCRIBE THE MODEL YOU CHOSE, AND WHY YOU CHOSE IT
## Vighnesh

## Matias

## Nick

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
