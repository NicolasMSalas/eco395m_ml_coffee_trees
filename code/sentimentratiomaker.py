import pandas as pd

monthly_df = pd.read_csv("raw_data/monthly_transformed_data.csv")
monthly_df['Negative_News_Ratio'] = monthly_df['Negative_News'] / monthly_df['Total_News']
monthly_df.to_csv("clean_data/sentiment_data.csv", index=False)
print(monthly_df.head())