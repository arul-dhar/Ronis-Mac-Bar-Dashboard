import csv
import numpy as np
import streamlit as st
import pandas as pd

# Mapping from month names to file names
month_to_file = {
    'April': 'april_2024.csv',
    'May': 'may_2024.csv',
    'June': 'june_2024.csv',
    'July': 'july_2024.csv',
    'August': 'august_2024.csv',
    'September': 'september_2024.csv',
    'October': 'october_2024.csv'
}

# Initialize dictionaries for each ingredient category
ingredient_counts = {
    'cheese': {'Alfredo': 0, 'Cheddar': 0, 'Pepper Jack': 0},
    'meat': {'No Meat': 0, 'Grilled Chicken': 0, 'Pulled Pork': 0, 'Brisket': 0, 'Bacon': 0, 'Ham': 0},
    'toppings': {
        'No Toppings': 0, 'Broccoli': 0, 'Corn': 0, 'Onions': 0, 
        'Jalapenos': 0, 'Tomatoes': 0, 'Bell Peppers': 0, 'Mushrooms': 0, 
        'Pineapple': 0, 'Parmesan': 0, 'Breadcrumbs': 0
    },
    'sauces': {'No Drizzle': 0, 'BBQ': 0, 'Garlic Parmesan': 0, 'Buffalo': 0, 'Pesto': 0, 'Ranch': 0, 'Hot Honey': 0}
}

# Sidebar for selecting month and ingredient filters
st.sidebar.header("Filter Options")
selected_month_name = st.sidebar.selectbox("Select Month", list(month_to_file.keys()))

# Convert selected month name back to file name
selected_month = month_to_file[selected_month_name]

selected_cheese = st.sidebar.multiselect("Choose Your Cheese", list(ingredient_counts['cheese'].keys()))
selected_meat = st.sidebar.multiselect("Choose Your Meat", list(ingredient_counts['meat'].keys()))
selected_topping = st.sidebar.multiselect("Pick Your Toppings", list(ingredient_counts['toppings'].keys()))
selected_sauce = st.sidebar.multiselect("Choose Your Sauce", list(ingredient_counts['sauces'].keys()))

# Function to load data from CSV files and count ingredients
def load_data(file_name):
    orders = []
    hours = []
    ingredient_data = ingredient_counts.copy()

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader, None)

        for row in reader:
            if row[5] == "0-0":
                break
            order_time = row[1].split()[1].split(":")[0]
            hours.append(order_time)

            # Count ingredients
            ingredient = row[2]
            for category in ingredient_data:
                if ingredient in ingredient_data[category]:
                    ingredient_data[category][ingredient] += 1
    
    return ingredient_data, hours

# Load data for the selected month
ingredient_data, hours = load_data(selected_month)

# Dashboard Title
st.title("Pizza Orders Dashboard")
st.subheader(f"Monthly Overview for {selected_month_name} 2024")

# Monthly Orders by Hour
st.subheader("Orders by Hour")
hour_counts = pd.Series(hours).value_counts().sort_index()
st.bar_chart(hour_counts)

# Ingredient Popularity Charts
def plot_ingredient_popularity(data, category):
    labels, counts = zip(*data[category].items())
    df = pd.DataFrame({category: labels, 'Count': counts})
    st.bar_chart(df.set_index(category))

# Display charts for selected ingredients
if selected_cheese:
    plot_ingredient_popularity(ingredient_data, 'cheese')
if selected_meat:
    plot_ingredient_popularity(ingredient_data, 'meat')
if selected_topping:
    plot_ingredient_popularity(ingredient_data, 'toppings')
if selected_sauce:
    plot_ingredient_popularity(ingredient_data, 'sauces')

# Insights section
st.subheader("Data Insights")
st.write("Most popular ingredients and combinations can be displayed here.")
