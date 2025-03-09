import pandas as pd

file_path = "data/commodity_prices.csv"

# Read the CSV file
df = pd.read_csv(file_path)

commodities = [
    "Tea, Kenyan ",
    "Coffee, Other Mild Arabica ",
    "Dairy Products, Milk",
    "Sugar, No. 11, World "
]

df_filtered = df[(df["Commodity Name"].isin(commodities)) & (df["Unit Code"] == "USD")]

monthly_columns = [col for col in df.columns if "M" in col and (col.startswith("19") or col.startswith("20"))]

columns_to_keep = ["Commodity Name"] + monthly_columns
df_monthly = df_filtered[columns_to_keep]

for index, row in df_monthly.iterrows():
    commodity = row["Commodity Name"].strip()
    
    if commodity in ["Coffee, Other Mild Arabica", "Coffee, Robustas", "Sugar, No. 11, World", "Dairy Products, Milk"]:
        for col in monthly_columns:
            df_monthly.at[index, col] = row[col] / 100
    elif "Tea, Kenyan" in commodity:
        for col in monthly_columns:
            df_monthly.at[index, col] = (row[col] / 2.20462) / 100
        # Converts price to USD per pound

df_transposed = df_monthly.set_index("Commodity Name").T
df_transposed.dropna(axis=1, how='all', inplace=True)

# Format the index as MM/YYYY
df_transposed.index = pd.to_datetime(df_transposed.index, format='%YM%m').strftime('%m/%Y')
df_transposed.index.name = "Date"

output_file = "data/global_commodity_prices.csv"

df_transposed.to_csv(output_file)