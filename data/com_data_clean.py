import pandas as pd

file_path = "commodity_prices.csv"
df = pd.read_csv(file_path)

commodities = [
    "Tea, Kolkata ",
    "Tea, Colombo ",
    "Tea, Kenyan ",
    "Tea, Mombasa ",
    "Coffee, Other Mild Arabica ",
    "Coffee, Robustas ",
    "Dairy Products, Milk",
    "Sugar, No. 11, World "
]

df_filtered = df[(df["Commodity Name"].isin(commodities)) & (df["Unit Code"] == "USD")]

monthly_columns = [col for col in df.columns if "M" in col and (col.startswith("19") or col.startswith("20"))]
columns_to_keep = ["Commodity Name"] + monthly_columns
df_monthly = df_filtered[columns_to_keep]

df_transposed = df_monthly.set_index("Commodity Name").T
df_transposed.dropna(axis=1, how='all', inplace=True)
df_transposed.index.name = "Year"

output_file = "global_commodity_prices.csv"
df_transposed.to_csv(output_file)