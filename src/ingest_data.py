import cdsapi
import os

def download_era5_nordics():
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
        "format": "netcdf",              
        "download_format": "unarchived", 
        "area": [72, 4, 54, 32]          # N, W, S, E (Nordic Region)
    }

    # Ensure the directory exists
    os.makedirs('data/raw', exist_ok=True)
    target_file = 'data/raw/era5_nordic_temp.nc'

    if os.path.exists(target_file):
        print(f"File already exists at {target_file}. Skipping download.")
        return

    client = cdsapi.Client()

    print(f"Downloading ERA5 data to {target_file}...")
    client.retrieve(dataset, request).download(target_file)
    print("Download complete.")

if __name__ == "__main__":
    download_era5_nordics()