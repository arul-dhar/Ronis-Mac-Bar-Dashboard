# Roni’s Mac Bar Dashboard (TAMU Datathon 2024)

A Streamlit dashboard built during TAMU Datathon 2024 to help Roni’s Mac Bar analyze ingredient popularity and customer ordering trends using monthly sales CSV data. The app supports month-by-month analysis or aggregation across all available months and highlights patterns like top ingredients by category and peak ordering hours.

[Dashboard Overview](assets/dashboard_overview.png)

## Key Features
- Monthly + All-Months analysis (single month or aggregate across all months)
- Ingredient popularity by category (cheese, meat, toppings, sauces, etc.)
- Order time insights (peak ordering hour in 12-hour AM/PM)
- Interactive filters via sidebar controls

## Tech Stack
Python • Streamlit • pandas • NumPy

## Repo Structure
- app/app.py — Streamlit app
- data/ — monthly CSV inputs
- assets/ — screenshots of app

## Quick Start
### Install dependencies
pip install -r requirements.txt

### Run the dashboard
streamlit run app/app.py

## Data Requirements
Place monthly CSV files inside the `data/` folder.

Each CSV should have:
- A header row
- Order time in the 2nd column
- Ingredient name in the 3rd column

If your CSV format differs, update the column indices in `app/app.py`.

File naming: the app expects filenames to match the `month_to_file` dictionary inside `app/app.py`. If your filenames differ, update `month_to_file`.

## Notes / Future Improvements
- Add a simple data dictionary (column meanings + types)
- Add automated data validation (missing values, column checks)
- Deploy a hosted version (Streamlit Community Cloud) and add the live link here
