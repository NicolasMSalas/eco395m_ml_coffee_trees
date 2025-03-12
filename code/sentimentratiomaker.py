import pandas as pd
import os

file_path = os.path.dirname(os.path.abspath("__file__"))
csv_path = os.path.join(file_path, '..', 'raw_data', 'monthly_transformed_data.csv')

monthly_df = pd.read_csv(csv_path)

monthly_df['Date'] = pd.to_datetime(monthly_df['Date'], format='%Y-%m-%d')
monthly_df.set_index('Date', inplace=True)
monthly_df.index = monthly_df.index.strftime('%m/%Y')
monthly_df.index.name = "Date"

if 'Negative_News' in monthly_df.columns and 'Total_News' in monthly_df.columns:
    monthly_df['Negative_News_Ratio'] = monthly_df['Negative_News'] / monthly_df['Total_News']
else:
    print("Required columns 'Negative_News' or 'Total_News' are missing.")
    
output_df = monthly_df[['Negative_News_Ratio']].copy()
output_df.reset_index(inplace=True)

output_dir = os.path.join(file_path, '..', 'clean_data')
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "sentiment_clean.csv")

output_df.to_csv(output_file, index=False)
