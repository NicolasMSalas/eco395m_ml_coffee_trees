import pandas as pd
import os
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
import numpy as np 

file_path = os.path.dirname(os.path.abspath("__file__"))
csv_path = os.path.join(file_path, 'clean_data', 'main_df_clean.csv')

df= pd.read_csv(csv_path)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce", format="%Y-%m")
df["Date"] = pd.PeriodIndex(df["Date"], freq="M")
before=df[df["Date"].dt.year < 2018]
after=df[df["Date"].dt.year >=2018]


X_train=before.drop(columns=["Coffee","Date"])
y_train=before["Coffee"].values

X_test=after.drop(columns=["Coffee","Date"])
y_test=after["Coffee"].values


grid_search = GridSearchCV(estimator=make_pipeline(PolynomialFeatures(), LinearRegression(fit_intercept=False)) ,param_grid = {'polynomialfeatures__degree': range(0,5)}, scoring='neg_mean_squared_error')

grid_search.fit(X_train, y_train)

best_degree=grid_search.best_params_['polynomialfeatures__degree']



best_model = make_pipeline(PolynomialFeatures(degree=best_degree), LinearRegression())

best_model.fit(X_train, y_train)

train_mse = mean_squared_error(y_train,best_model.predict(X_train))

coefficients= np.delete(best_model.named_steps["linearregression"].coef_,0)
print(len(coefficients))
test_mse = mean_squared_error(y_test,best_model.predict(X_test))

print("Best Degree: ", best_degree)
print("Train MSE: ", train_mse)
print("Test MSE: ", test_mse)
coef=pd.DataFrame({"variable": X_train.columns,
	"coefficient":coefficients})
print("Best Model Coefficients: \n",coef)





