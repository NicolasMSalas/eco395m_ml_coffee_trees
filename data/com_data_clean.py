import pandas as pd

file_path = "commodity_prices.csv"
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
        df_monthly.loc[index, monthly_columns] = row[monthly_columns] / 100
    elif "Tea, Kenyan" in commodity:
        df_monthly.loc[index, monthly_columns] = (row[monthly_columns] / 2.20462) / 100
        # normalizes the price of all commodities to USD per pound

df_transposed = df_monthly.set_index("Commodity Name").T
df_transposed.dropna(axis=1, how='all', inplace=True)
df_transposed.index.name = "Year/Month"

output_file = "global_commodity_prices.csv"
df_transposed.to_csv(output_file)