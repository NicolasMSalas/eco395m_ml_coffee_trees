import os
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.feature_selection import mutual_info_regression

notebook_dir = os.path.dirname(os.path.abspath("__file__"))
csv_path = os.path.join(notebook_dir, '..', 'clean_data')

def load_weatcher_data(filename, suffix):
    """Load weather data from csv file and add suffix to columns"""
    full_path = os.path.join(csv_path, filename)
    df = pd.read_csv(full_path)
    df = df.add_suffix(suffix)
    df.rename(columns={f'Date{suffix}': 'Date'}, inplace=True)
    return df

df_br = load_weatcher_data('Brazil_weather_cleaned.csv', '_br')
df_col = load_weatcher_data('Colombia_weather_cleaned.csv', '_col')
df_vn = load_weatcher_data('Vietnam_weather_cleaned.csv', '_vn')
df_hon = load_weatcher_data('Honduras_weather_cleaned.csv', '_hon')
df_in = load_weatcher_data('Indonesia_weather_cleaned.csv', '_in')

def load_exchange_data(filename):
    """Load currency exchange data from csv file"""
    full_path = os.path.join(csv_path, filename)
    df = pd.read_csv(full_path)
    return df

df_vnd = load_exchange_data('vnd_data_clean.csv')
df_brl = load_exchange_data('brl_data_clean.csv')
df_hnl = load_exchange_data('hnl_data_clean.csv')
df_idr = load_exchange_data('idr_data_clean.csv')
df_cop = load_exchange_data('cop_data_clean.csv')

futures_path = os.path.join(csv_path, 'futures_clean.csv')
df_futures = pd.read_csv(futures_path)

sentiment_path = os.path.join(csv_path, 'sentiment_clean.csv')
df_sentiment = pd.read_csv(sentiment_path)

commodity_path = os.path.join(csv_path, 'commodity_prices_clean.csv')
df_commodity = pd.read_csv(commodity_path)

merged_df = df_brl.copy()
for df in [df_vnd, df_hnl, df_idr, df_commodity, df_cop, df_sentiment, df_futures, df_col, df_vn, df_hon, df_in]:
    merged_df = pd.merge(merged_df, df, on="Date", how="inner")
    
imputer = IterativeImputer(random_state=42)
merged_df.iloc[:, 1:] = imputer.fit_transform(merged_df.iloc[:, 1:])

merged_df["Date"] = pd.to_datetime(merged_df["Date"], errors="coerce", format="%m/%Y")
merged_df["Date"] = pd.PeriodIndex(merged_df["Date"], freq="M")

y_diff = merged_df['Coffee']

X = merged_df.drop(columns=['Date'])

X, y_diff = X.align(y_diff, join='inner', axis=0)

mi_scores = mutual_info_regression(X, y_diff)

mi_scores_series = pd.Series(mi_scores, index=X.columns).sort_values(ascending=False)

non_zero_mi_scores = mi_scores_series[mi_scores_series > 0]
X_filtered = X[non_zero_mi_scores.index]

X_filtered = X_filtered.copy()
X_filtered.loc[:, 'Date'] = merged_df['Date']

X_filtered['Date'] = X_filtered['Date'].dt.strftime('%m/%Y')

date_column = X_filtered.pop('Date')
X_filtered.insert(0, 'Date', date_column)

output_dir = os.path.join(csv_path, '..', 'clean_data')
output_file = os.path.join(output_dir, "main_df_clean.csv")

os.makedirs(output_dir, exist_ok=True)

X_filtered.to_csv(output_file, index=False)