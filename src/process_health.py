import pandas as pd
import os

def clean_gbd_data():
    # Define paths
    raw_path = 'data/raw/IHME-GBD_2019_DATA.csv'  # Make sure this matches your actual filename
    processed_path = 'data/processed/gbd_clean_nordic.csv'

    # Check if raw file exists
    if not os.path.exists(raw_path):
        print(f"Error: Raw file not found at {raw_path}")
        print("Please place the downloaded GBD CSV in the data/raw/ folder.")
        return

    # 1. Load the raw data
    print(f"Loading raw data from {raw_path}...")
    df = pd.read_csv(raw_path)

    # 2. Filter for columns we need
    # Adjust these column names if your CSV header is different
    keep_cols = ['location_name', 'year', 'val', 'upper', 'lower']
    
    # Safety check: do these columns exist?
    missing_cols = [c for c in keep_cols if c not in df.columns]
    if missing_cols:
        print(f"Warning: Columns {missing_cols} not found. Available columns: {df.columns}")
        return

    df_clean = df[keep_cols].copy()

    # 3. Rename columns
    df_clean = df_clean.rename(columns={
        'location_name': 'country',
        'val': 'deaths_per_100k',
        'upper': 'deaths_upper',
        'lower': 'deaths_lower'
    })

    # 4. Filter for Nordics (just in case the download included others)
    nordic_countries = ['Norway', 'Sweden', 'Finland', 'Denmark']
    df_clean = df_clean[df_clean['country'].isin(nordic_countries)]

    # 5. Save processed data
    os.makedirs('data/processed', exist_ok=True)
    df_clean.to_csv(processed_path, index=False)
    print(f"Success! Processed data saved to {processed_path}")
    print(df_clean.head())

if __name__ == "__main__":
    clean_gbd_data()