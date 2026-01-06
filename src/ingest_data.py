import cdsapi
import os

dataset = "reanalysis-era5-land-monthly-means"

request = {
    "product_type": ["monthly_averaged_reanalysis"],
    "variable": ["2m_temperature"],
    "year": [
        "1990", "1991", "1992", "1993", "1994", "1995",
        "1996", "1997", "1998", "1999", "2000", "2001",
        "2002", "2003", "2004", "2005", "2006", "2007",
        "2008", "2009", "2010", "2011", "2012", "2013",
        "2014", "2015", "2016", "2017", "2018", "2019"
    ],
    "month": [
        "01", "02", "03", "04", "05", "06",
        "07", "08", "09", "10", "11", "12"
    ],
    "time": ["00:00"],
    "area": [72, 4, 54, 32],
    
    # CRITICAL FIXES BELOW:
    "format": "netcdf",              # <--- Explicitly request NetCDF
    "download_format": "unarchived"  # <--- Keeps it as .nc, not .zip
}

# Ensure the directory exists (Pro move)
os.makedirs('data/raw', exist_ok=True)

client = cdsapi.Client()

# Define the specific output filename so your next script can find it
target_file = 'data/raw/era5_nordic_temp.nc'

print(f"Downloading to {target_file}...")
client.retrieve(dataset, request).download(target_file)
print("Download complete.")