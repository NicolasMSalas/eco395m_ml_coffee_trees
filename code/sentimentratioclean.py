import pandas as pd


df = pd.read_csv("raw_data/newsratioml.csv")

df['Date'] = pd.to_datetime(df['Coverage over Time'])

df = df.sort_values('Date')

df['Negative_News_Change'] = df['Coverage'].diff()
df['Total_News_Change'] = df['Coverage.1'].diff()

df['Monthly_Negative_News_Change'] = df['Negative_News_Change'] / 12
df['Monthly_Total_News_Change'] = df['Total_News_Change'] / 12

monthly_data = []

for i in range(len(df) - 1):  
    year = df.iloc[i]['Date'].year  
    monthly_neg_change = df.iloc[i + 1]['Monthly_Negative_News_Change']
    monthly_total_change = df.iloc[i + 1]['Monthly_Total_News_Change']
    
    for month in range(1, 13):
        monthly_data.append({
            'Date': pd.Timestamp(year=year, month=month, day=27),  
            'Negative_News': df.iloc[i]['Coverage'] + (monthly_neg_change * month),
            'Total_News': df.iloc[i]['Coverage.1'] + (monthly_total_change * month)
        })

monthly_df = pd.DataFrame(monthly_data)

monthly_df.to_csv("raw_data/monthly_transformed_data.csv", index=False)

print(monthly_df.head(24))