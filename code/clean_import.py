import os
import pandas as pd

csv_path = os.path.join(os.getcwd(), '..', 'raw_data', 'Coffee_import.csv')

print("Loading data...")
df = pd.read_csv(csv_path)
print(f"Original data shape: {df.shape}")

df["Country"] = df["Country"].str.strip()
print("Cleaned country names of whitespace")

country_mapping = {
    "United States of America": "United States",
}

df["Country"] = df["Country"].replace(country_mapping)
print("Standardized country names")

countries = ["United States", "Germany", "France", "Italy", "Japan"] 
print(f"Filtering for countries: {countries}")
print(f"Available countries in dataset: {df['Country'].unique().tolist()}")

df_filtered = df[df["Country"].isin(countries)]
print(f"After filtering, data shape: {df_filtered.shape}")

if df_filtered.empty:
    print("ERROR: No data left after filtering countries!")
    exit(1)

print("Melting data from wide to long format...")
df_long = df_filtered.melt(id_vars=["Country"], var_name="Year", value_name="Import Volume")

df_long = df_long[df_long["Year"] != "Total_import"]
print(f"Long format data shape: {df_long.shape}")
print(df_long.head())

print("Converting Year to datetime...")
df_long["Year"] = pd.to_datetime(df_long["Year"], format="%Y", errors='coerce')
print(f"NaT values after conversion: {df_long['Year'].isna().sum()}")

print("Resampling by country...")
result = []
for country, group in df_long.groupby("Country"):
    print(f"Processing country: {country}, group size: {len(group)}")
    
    group_indexed = group.set_index("Year")
    
    if group_indexed.index.isna().all():
        print(f"Skipping {country} - all Year values are invalid")
        continue
        
    try:
        group_resampled = group_indexed.resample("ME").ffill()
        group_resampled = group_resampled.reset_index()
        result.append(group_resampled)
        print(f"Successfully resampled {country}, got {len(group_resampled)} rows")
    except Exception as e:
        print(f"Error resampling {country}: {e}")

print(f"Total groups processed: {len(result)}")
if not result:
    print("ERROR: No data after resampling!")
    exit(1)

df_monthly = pd.concat(result, ignore_index=True)

print("Final dataset:")
print(df_monthly.head(10))
print(df_monthly.info())

clean_path = os.path.join(os.getcwd(), '..', 'clean_data', 'Coffee_import_clean.csv')
os.makedirs(os.path.dirname(clean_path), exist_ok=True)  # Create directory if not exists
df_monthly.to_csv(clean_path, index=False)

print("Data cleaned and saved successfully!")