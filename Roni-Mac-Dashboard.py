import csv
import numpy as np
import streamlit as st
import pandas as pd

# File names for each month
file_names = [
    'april_2024.csv', 'may_2024.csv', 'june_2024.csv', 
    'july_2024.csv', 'august_2024.csv', 'september_2024.csv', 'october_2024.csv'
]

# Month names to display on drop down
month_names = ["April", "May", "June", "July", "August", "September", "October"]

# Initialize dictionaries for each ingredient category
ingredient_counts = {
    'cheese': {'alfredo': 0, 'cheddar': 0, 'pepperjack': 0},
    'meat': {'nomeat': 0, 'chicken': 0, 'pork': 0, 'brisket': 0, 'bacon': 0, 'ham': 0},
    'toppings': {
        'notoppings': 0, 'broccoli': 0, 'corn': 0, 'onion': 0, 
        'jalapeno': 0, 'tomato': 0, 'pepper': 0, 'mushroom': 0, 
        'pineapple': 0, 'parmesan': 0, 'breadcrumbs': 0
    },
    'sauces': {'nodrizzle': 0, 'bbq': 0, 'garlicparm': 0, 'buffalo': 0, 'pesto': 0, 'ranch': 0, 'hothoney': 0}
}

# Sidebar for selecting month and ingredient filters
st.sidebar.header("Filter Options")
selected_month = st.sidebar.selectbox("Select Month", month_names)
selected_cheese = st.sidebar.multiselect("Select Cheese", list(ingredient_counts['cheese'].keys()))
selected_meat = st.sidebar.multiselect("Select Meat", list(ingredient_counts['meat'].keys()))
selected_topping = st.sidebar.multiselect("Select Topping", list(ingredient_counts['toppings'].keys()))
selected_sauce = st.sidebar.multiselect("Select Sauce", list(ingredient_counts['sauces'].keys()))

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
            ingredient = row[2].lower()
            for category in ingredient_data:
                if ingredient in ingredient_data[category]:
                    ingredient_data[category][ingredient] += 1
    
    return ingredient_data, hours

# Load data for the selected month
ingredient_data, hours = load_data(file_names)

# Dashboard Title
st.title("Pizza Orders Dashboard")
st.subheader(f"Monthly Overview for {selected_month.replace('.csv', '').capitalize()}")

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

