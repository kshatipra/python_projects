# streamlit_app.py
import streamlit as st
import numpy as np
import pandas as pd
import time
from datetime import datetime
import math

# Simulate data
def simulate_data():
    temperature = np.random.normal(22, 0.5)  # Celsius
    rh = np.random.normal(0.8, 0.1)          # Relative humidity (%)
    pressure = np.random.normal(101325, 50)  # Pascals
    dew_point = calc_dew_point(temperature, rh)
    return temperature, rh, pressure, dew_point

# Calculate Dew Point using Magnus formula
def calc_dew_point(T, RH):
    A, B = 17.62, 243.12
    alpha = ((A * T) / (B + T)) + math.log(RH / 100.0)
    return (B * alpha) / (A - alpha)

# Initialize app
st.set_page_config("Dry Room Monitor", layout="wide")
st.title("🌡️ Dry Room Environmental Monitor (Simulated)")
st.markdown("This dashboard simulates dry room parameters and triggers alerts if thresholds are breached.")

# Create or load data storage
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Temp (°C)", "RH (%)", "Pressure (Pa)", "Dew Point (°C)"])

# Run the simulation in a loop
placeholder = st.empty()
run = st.checkbox("Run Simulation")

if run:
    while run:
        temp, rh, pressure, dew_point = simulate_data()
        now = datetime.now().strftime("%H:%M:%S")
        new_row = pd.DataFrame([[now, temp, rh, pressure, dew_point]],
                               columns=st.session_state.data.columns)
        st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True).tail(100)

        with placeholder.container():
            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Temperature (°C)", f"{temp:.2f}")
            col2.metric("Humidity (%)", f"{rh:.2f}", delta="⚠️ High" if rh > 1.0 else "")
            col3.metric("Pressure (Pa)", f"{pressure:.0f}")
            col4.metric("Dew Point (°C)", f"{dew_point:.2f}")

            st.line_chart(st.session_state.data.set_index("Time")[["Temp (°C)", "RH (%)", "Dew Point (°C)"]])

        time.sleep(1)
