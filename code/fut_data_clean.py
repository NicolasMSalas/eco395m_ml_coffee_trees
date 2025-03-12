import pandas as pd
import os

file_path = os.path.dirname(os.path.abspath("__file__"))
csv_path = os.path.join(file_path, '..', 'raw_data', 'futures_raw.csv')

df = pd.read_csv(csv_path)

df_filtered = df[['time', 'close']].copy()

df_filtered['time'] = pd.to_datetime(df_filtered['time'], errors='coerce')

df_filtered = df_filtered.dropna(subset=['time'])

df_filtered = df_filtered[df_filtered['time'].dt.year >= 1990]

output_dir = os.path.join(file_path, '..', 'clean_data')
output_file = os.path.join(output_dir, "futures_clean.csv")

os.makedirs(output_dir, exist_ok=True)

df_filtered.to_csv(output_file, index=False)