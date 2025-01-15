import streamlit as st
import pandas as pd

# Load the historical weather data
file_path = "historical_weather_data.xlsx"
try:
    data = pd.read_excel(file_path, engine='openpyxl')
except FileNotFoundError:
    st.error(f"The file {file_path} was not found. Please check the path.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while reading the Excel file: {e}")
    st.stop()

# Streamlit app
st.title("Weather Report")

if "City" not in data.columns or "Date" not in data.columns:
    st.error("The Excel file must contain 'City' and 'Date' columns.")
    st.stop()

# User input: Select a city
city = st.selectbox("Select a city", options=data["City"].unique())

# Filter data based on selected city
filtered_data = data[data["City"] == city]

# Display historical data for the selected city
st.subheader(f"Historical Weather Data for {city}")
st.dataframe(filtered_data)

# User input: Select a date
try:
    selected_date = st.date_input("Select a date", value=filtered_data["Date"].min())
    # Filter data based on selected date
    selected_date_data = filtered_data[filtered_data["Date"] == pd.Timestamp(selected_date)]

    # Display weather report for the selected date
    if not selected_date_data.empty:
        st.subheader(f"Weather Report for {city} on {selected_date}")
        st.write(f"**Temperature:** {selected_date_data['Temperature (°C)'].values[0]} °C")
        st.write(f"**Humidity:** {selected_date_data['Humidity (%)'].values[0]}%")
        st.write(f"**Condition:** {selected_date_data['Condition'].values[0]}")
    else:
        st.write("No data available for the selected date.")
except KeyError:
    st.error("Date column not formatted correctly. Ensure it contains valid dates.")
