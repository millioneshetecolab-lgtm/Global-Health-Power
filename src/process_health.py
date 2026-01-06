import pandas as pd

def clean_gbd_data():
    # 1. Load the raw data (Adjust filename to match your download)
    # The 'header=0' argument implies the first row contains column names
    df = pd.read_csv('data/raw/IHME-GBD_2019_DATA.csv')

    print(f"Raw shape: {df.shape}")

    # 2. Filter for columns we actually need
    # 'val' is the value (Deaths), 'upper' and 'lower' are the uncertainty intervals
    keep_cols = ['location_name', 'year', 'val', 'upper', 'lower']
    df_clean = df[keep_cols].copy()

    # 3. Rename columns to be "Coder Friendly" (No spaces, lowercase)
    df_clean = df_clean.rename(columns={
        'location_name': 'country',
        'val': 'deaths_per_100k',
        'upper': 'deaths_upper',
        'lower': 'deaths_lower'
    })

    # 4. The "0.1%" Move: Standardize Country Names
    # GBD uses "Norway", but standard libraries might expect "Norway" or "NO".
    # We ensure specific Nordic filtering here just in case.
    nordic_countries = ['Norway', 'Sweden', 'Finland', 'Denmark']
    df_clean = df_clean[df_clean['country'].isin(nordic_countries)]

    # 5. Sanity Check (Print the first few rows to verify)
    print("Filtered data preview:")
    print(df_clean.head())

    # 6. Save the processed version
    # distinct from 'raw' to preserve data lineage
    df_clean.to_csv('data/processed/gbd_clean_nordic.csv', index=False)
    print("Saved processed data to data/processed/gbd_clean_nordic.csv")

if __name__ == "__main__":
    clean_gbd_data()
