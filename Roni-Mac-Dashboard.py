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

# Add "All Months" to the dropdown options
month_names = ['All Months'] + list(month_to_file.keys())

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
selected_month_name = st.sidebar.selectbox("Select Month", month_names)

# Sidebar options for ingredient categories
selected_cheese = st.sidebar.button("Show Cheese Popularities")
selected_meat = st.sidebar.button("Show Meat Popularities")
selected_topping = st.sidebar.button("Show Topping Popularities")
selected_sauce = st.sidebar.button("Show Drizzle Popularities")
selected_all = st.sidebar.button("Show All Ingredient Popularities")

# Function to load data from a single CSV file and count ingredients
def load_data(file_name):
    ingredient_data = {category: counts.copy() for category, counts in ingredient_counts.items()}
    order_times = []  # Store the full order time (not just the hour)

    with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
        reader = csv.reader(file)
        header = next(reader, None)

        for row in reader:
            try:
                # Extract the full time (hour:minute)
                order_time = row[1].split()[1]  # Assuming the time is in the second column (index 1)
                order_times.append(order_time)  # Add full time to the list
                
                # Count ingredients
                ingredient = row[2]
                for category in ingredient_data:
                    if ingredient in ingredient_data[category]:
                        ingredient_data[category][ingredient] += 1

            except Exception:
                continue

    return ingredient_data, order_times

# Function to get the most popular hour
def get_most_popular_hour(order_times):
    most_popular_hour = pd.Series(order_times).value_counts().idxmax()
    return most_popular_hour

# Load data based on the selected month
if selected_month_name == 'All Months':
    ingredient_data, order_times = load_all_months_data()
else:
    ingredient_data, order_times = load_data(month_to_file[selected_month_name])

# Dashboard Title
st.title("Roni's Mac Bar Dashboard")
st.subheader(f"Overview for {'All Months' if selected_month_name == 'All Months' else selected_month_name + ' 2024'}")

# Get and display the most popular hour before the hour graph
most_popular_hour = get_most_popular_hour(order_times)
st.write(f"Most Popular Hour: {most_popular_hour}")

# Monthly Orders by Time of Day (now with actual time)
st.subheader("Orders by Time of Day")
# Create a Pandas Series with order times
order_time_series = pd.Series(order_times)

# Count the frequency of each order time and sort them
order_time_counts = order_time_series.value_counts().sort_index()

# Plot the bar chart with the actual time of the day as x-axis labels
st.bar_chart(order_time_counts)

# Data Insights section (moved here after hour graph)
st.subheader("Data Insights")
st.write("Most popular ingredients and combinations can be displayed here.")

# Function to plot ingredient popularity
def plot_ingredient_popularity(data, category):
    labels = list(data[category].keys())
    counts = list(data[category].values())
    df = pd.DataFrame({category: labels, 'Count': counts})

    # Ensure all ingredients are represented, even with zero counts
    all_labels = list(ingredient_counts[category].keys())
    for label in all_labels:
        if label not in df[category].values:
            df = pd.concat([df, pd.DataFrame({category: [label], 'Count': [0]})], ignore_index=True)

    # Re-sort the DataFrame to maintain the correct order
    df = df.set_index(category).reindex(all_labels).reset_index()
    st.bar_chart(df.set_index(category))

# Display graphs based on user selection
if selected_cheese:
    st.subheader("Cheese Popularity")
    plot_ingredient_popularity(ingredient_data, 'cheese')
if selected_meat:
    st.subheader("Meat Popularity")
    plot_ingredient_popularity(ingredient_data, 'meat')
if selected_topping:
    st.subheader("Topping Popularity")
    plot_ingredient_popularity(ingredient_data, 'toppings')
if selected_sauce:
    st.subheader("Sauce Popularity")
    plot_ingredient_popularity(ingredient_data, 'sauces')
if selected_all:
    st.subheader("Cheese Popularity")
    plot_ingredient_popularity(ingredient_data, 'cheese')
    st.subheader("Meat Popularity")
    plot_ingredient_popularity(ingredient_data, 'meat')
    st.subheader("Topping Popularity")
    plot_ingredient_popularity(ingredient_data, 'toppings')
    st.subheader("Sauce Popularity")
    plot_ingredient_popularity(ingredient_data, 'sauces')

