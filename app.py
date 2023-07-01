import streamlit as st
import requests
from datetime import datetime

'''
# TaxiFareModel front
'''

date_and_time = st.date_input("Date of ride")
time = st.time_input("Time of ride")
pickup_longitude = st.number_input("Pickup longitude", value=40.7614327)
pickup_latitude = st.number_input("Pickup latitude", value=-73.9798156)
dropoff_longitude = st.number_input("Dropoff longitude", value=40.6513111)
dropoff_latitude = st.number_input("Dropoff latitude", value=-73.8803331)
passenger_count = st.number_input("Passenger count", value=1, min_value=1, max_value=8, step=1)

url = 'https://taxifare-prod-oainjatqlq-ew.a.run.app/predict'

# Combining date and time into a single datetime object
pickup_datetime = datetime.combine(date_and_time, time)

# Let's build a dictionary containing the parameters for our API...
params = {
    "pickup_datetime": pickup_datetime.isoformat(),  # format should match the expected format from API
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count,
}

# Let's call our API using the `requests` package...
response = requests.get(url, params=params)

# Let's retrieve the prediction from the **JSON** returned by the API...
prediction = response.json()['fare_amount']

## Finally, we can display the prediction to the user
st.write(f"The predicted fare is: ${prediction:.2f}")
