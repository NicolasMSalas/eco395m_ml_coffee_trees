import os
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

notebook_dir = os.path.dirname(os.path.abspath("__file__"))
csv_path = os.path.join(notebook_dir, '..', 'clean_data')

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

commodity_path = os.path.join(csv_path, 'commodity_prices_clean.csv')
df_commodity = pd.read_csv(commodity_path)

merged_df = df_brl.copy()
for df in [df_vnd, df_hnl, df_idr, df_commodity, df_cop, df_futures]:
    merged_df = pd.merge(merged_df, df, on="Date", how="inner")
    
imputer = IterativeImputer(random_state=42)
merged_df.iloc[:, 1:] = imputer.fit_transform(merged_df.iloc[:, 1:])

merged_df["Date"] = pd.to_datetime(merged_df["Date"], errors="coerce", format="%m/%Y")
merged_df["Date"] = pd.PeriodIndex(merged_df["Date"], freq="M")

output_dir = os.path.join(csv_path, '..', 'clean_data')
output_file = os.path.join(output_dir, "main_df_clean.csv")

os.makedirs(output_dir, exist_ok=True)

merged_df.to_csv(output_file, index=True)