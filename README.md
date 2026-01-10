# GBD-Style Climate-Mortality Modeling Pipeline

**Author:** Million Tesfaye Eshete, PhD  
**Status:** Active 

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 📌 Overview

This repository demonstrates a computational workflow. It bridges the gap between **raw climate reanalysis data (ERA5)** and **epidemiological health metrics (IHME/GBD)** using a reproducible Python pipeline. The project serves as a proof-of-concept for handling multidimensional spatiotemporal data and implementing probabilistic mortality forecasting.

## 🚀 Key details

### 1. Advanced Data Engineering
* **NetCDF Ingestion:** Automated ingestion and processing of ERA5 weather data using `xarray` and `dask` for memory-efficient handling of multidimensional arrays.
* **GBD Harmonization:** robust merging logic to map gridded climate data to GBD administrative boundaries (ISO3/Location IDs).

### 2. Methodological Rigor (Bayesian Inference)
* **Hierarchical Modeling:** Implementation of a **Hierarchical Bayesian Model** using `PyMC`.
* **Partial Pooling:** Utilizes partial pooling to share statistical strength across countries/regions—a critical strategy for small-area estimation in data-sparse regions.
* **Uncertainty Quantification:** Full posterior sampling to generate rigorous uncertainty intervals (UI), a standard requirement for GBD outputs.

### 3. Reproducibility & Structure
* **Environment Management:** Strict dependency management via `requirements.txt` and virtual environments.
* **Data Lineage:** Clear separation of `raw` (immutable) and `processed` data to prevent contamination.

## 📂 Repository Structure

```text
├── data/
│   ├── raw/                 # (Ignored via .gitignore) Raw GBD CSVs & ERA5 NetCDF
│   └── processed/           # Cleaned datasets ready for modeling
├── notebooks/
│   ├── 01_climate_processing.ipynb   # Xarray workflows for ERA5 reanalysis
│   └── 02_mortality_model.ipynb      # Hierarchical Bayesian inference (PyMC)
├── src/
│   ├── ingest_data.py       # Automation scripts for data fetching
│   └── process_health.py    # Cleaning pipeline for longitudinal health data
├── requirements.txt         # Python dependencies
└── README.md
