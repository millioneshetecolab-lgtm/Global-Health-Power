# Global Health Data Modeling Pipeline (FHI/GBD Proxy)

**Project Status:** Active Portfolio Proof  
**Author:** Million Eshete (PhD)

## Overview
This repository demonstrates a computational workflow for **Global Burden of Disease (GBD)** analysis, designed to mimic key infrastructure requirements of the Future Health Scenarios (FHS) team.

It bridges the gap between **raw climate reanalysis data (ERA5)** and **epidemiological health metrics (IHME/GBD-style CSVs)** using a reproducible Python pipeline.

## Key Capabilities Demonstrated
This project targets technical competencies relevant to global health modeling work:

1. **Advanced Data Engineering:**
   * Automated ingestion of **NetCDF** weather data (ERA5-ready workflow).
   * Processing of multidimensional spatiotemporal arrays using **xarray**.
   * Basic handling of location/year merges typical of GBD-style datasets.

2. **Methodological Rigor:**
   * Implementation of **Hierarchical Bayesian Inference** (using `PyMC`) to estimate mortality risk.
   * Use of **partial pooling** to share statistical strength across countries/regions (a common “small area estimation” strategy).

3. **Reproducibility:**
   * Reproducible environment via `requirements.txt` and a Python virtual environment (`.venv`).
   * Strict separation of `raw` (immutable) and `processed` data.

## Repository Structure
```text
├── data/
│   ├── raw/                 # (Ignored via .gitignore) Raw GBD CSVs & ERA5 NetCDF
│   └── processed/           # Cleaned datasets ready for modeling
├── notebooks/
│   ├── 01_analysis.ipynb             # Weather processing / exploratory analysis
│   └── 02_mortality_model.ipynb      # Hierarchical Bayesian model (PyMC)
├── src/
│   ├── ingest_data.py        # ERA5 ingestion/automation script
│   └── process_health.py     # GBD-style data cleaning pipeline
└── requirements.txt          # Environment dependencies
