import streamlit as st
import pandas as pd

# Load the historical weather data
file_path = "C://Users//kotra//OneDrive//Desktop//kushal projects//whether//historical_weather_data.xlsx"
data = pd.read_excel(file_path)

# Streamlit app
st.title("Weather Report")

# User input: Select a city
city = st.selectbox("Select a city", options=data["City"].unique())

# Filter data based on selected city
filtered_data = data[data["City"] == city]

# Display historical data for the selected city
st.subheader(f"Historical Weather Data for {city}")
st.dataframe(filtered_data)

# User input: Select a date
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
