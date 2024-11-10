#README
Roni's Mac Bar Dashboard
This project is a Streamlit dashboard designed to analyze ingredient popularity and customer ordering trends at Roni's Mac Bar.
The dashboard pulls data from CSV files representing monthly sales data and provides insights into popular ingredients, peak ordering hours, and other valuable information.

#Project Setup and Requirements
To use this dashboard, install the necessary libraries. Ensure you have Python installed, then install these packages:
pip install numpy pandas streamlit

#File Structure
CSV Files: Place CSV files for each month in the same directory. Each file should follow the naming convention specified in the month_to_file dictionary and 
have data organized with order details, including order time and ingredient names.

#CSV File Format
Each CSV file should contain:
A header row.
Columns for order details. This script expects the time of order to be in the second column and ingredient name in the third column.

#Dashboard Overview
Monthly Ingredient Analysis: Use the sidebar dropdown to choose a month or select "All Months" to aggregate data across all available files.
Popular Ingredients by Category: Check boxes for each category to see detailed popularity charts.
Order Time Analysis: Displays the peak ordering hour in a 12-hour format.
Functions
load_data(file_name): Loads and processes ingredient data from a given CSV file.
load_all_months_data(): Aggregates data from all CSV files for multi-month analysis.
convert_to_12_hour_format(hour): Converts a 24-hour formatted hour to a 12-hour format with AM/PM.
get_most_popular_items(data): Identifies the most popular item within each ingredient category.
plot_ingredient_popularity(data, category): Displays a bar chart of ingredient popularity for a specified category.

#How to Use
Start the Dashboard: Run the following command:
streamlit run Roni-Mac-Dashboard.py

-Select Filters: Use the sidebar to filter by month or ingredient categories.
-View Insights: See the most popular items by category, peak ordering times, and ingredient popularity graphs.

#Example Data Insights
Most Popular Hour: Shows the hour when the most orders were placed.
Ingredient Popularity: Displays the most popular items within each category (cheese, meat, toppings, sauces) based on the selection in the sidebar.
Dashboard Components
Sidebar Options: Provides filters for month and ingredient categories.
Most Popular Hour: Shows the busiest hour for orders in a 12-hour format.
Ingredient Popularity Charts: Visual representations of ingredient popularity, which update based on user selections.
This dashboard allows Roni's Mac Bar to make data-driven decisions by analyzing customer preferences and trends across various ingredients and time slots.
