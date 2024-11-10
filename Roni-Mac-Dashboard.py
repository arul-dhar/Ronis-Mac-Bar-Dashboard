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

# Sidebar options for ingredient categories
selected_cheese = st.sidebar.button("Show Cheese Popularities")
selected_meat = st.sidebar.button("Show Meat Popularities")
selected_topping = st.sidebar.button("Show Topping Popularities")
selected_sauce = st.sidebar.button("Show Drizzle Popularities")
selected_all = st.sidebar.button("Show All Ingredient Popularities")
    
# Convert selected month name back to file name
selected_month = month_to_file[selected_month_name]

# Function to load data from CSV files and count ingredients
def load_data(file_name):
    orders = []
    hours = []
    ingredient_data = ingredient_counts.copy()

    with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
        reader = csv.reader(file)
        header = next(reader, None)

        for row in reader:
            try:
                order_time = row[1].split()[1].split(":")[0]
                hours.append(order_time)
    
                # Count ingredients
                ingredient = row[2]
                for category in ingredient_data:
                    if ingredient in ingredient_data[category]:
                        ingredient_data[category][ingredient] += 1

            except Exception as e:
                # Log or print the error if needed, but continue processing
                print(f"Error processing row: {row} - {e}")
                continue
    
    return ingredient_data, hours

# Load data for the selected month
ingredient_data, hours = load_data(selected_month)

# Dashboard Title
st.title("Roni's Mac Bar Dashboard")
st.subheader(f"Monthly Overview for {selected_month_name} 2024")

# Monthly Orders by Hour
st.subheader("Orders by Hour")
hour_counts = pd.Series(hours).value_counts().sort_index()
st.bar_chart(hour_counts)

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

# Helper function to get the most popular item in each category
def get_most_popular_items(data):
    most_popular = {}
    for category, items in data.items():
        # Find the item with the highest count in each category
        most_popular[category] = max(items, key=items.get)
    return most_popular

# Display graph for selected cheese
if selected_cheese:
    st.subheader("Cheese Popularity")
    plot_ingredient_popularity(ingredient_data, 'cheese')

# Display graph for selected meat
if selected_meat:
    st.subheader("Meat Popularity")
    plot_ingredient_popularity(ingredient_data, 'meat')

# Display graph for selected toppings
if selected_topping:
    st.subheader("Topping Popularity")
    plot_ingredient_popularity(ingredient_data, 'toppings')

# Display graph for selected sauces
if selected_sauce:
    st.subheader("Sauce Popularity")
    plot_ingredient_popularity(ingredient_data, 'sauces')

# Display graph for all ingredients
if selected_all:
    st.subheader("Cheese Popularity")
    plot_ingredient_popularity(ingredient_data, 'cheese')
    
    st.subheader("Meat Popularity")
    plot_ingredient_popularity(ingredient_data, 'meat')
    
    st.subheader("Topping Popularity")
    plot_ingredient_popularity(ingredient_data, 'toppings')

    st.subheader("Sauce Popularity")
    plot_ingredient_popularity(ingredient_data, 'sauces')

# Data Insights section with most popular items
st.subheader("Data Insights")
most_popular_items = get_most_popular_items(ingredient_data)
st.write("Most Popular Items for Each Ingredient Category:")
for category, item in most_popular_items.items():
    st.write(f"- {category.capitalize()}: {item} with {ingredient_data[category][item]} orders")

