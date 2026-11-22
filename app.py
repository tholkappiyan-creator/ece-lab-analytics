import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="ECE Lab Analytics", layout="wide")
st.title("📡 ECE Lab - Sensor Analytics Dashboard")
st.write("By tholkappiyan-creator | ECE Department")

# Fake Sensor Data Create Panrom
np.random.seed(42)
time = pd.date_range("2026-11-22 09:00", periods=50, freq="min")
temp = np.random.normal(28, 2, 50)
humidity = np.random.normal(65, 5, 50)
voltage = np.random.normal(3.3, 0.2, 50)

df = pd.DataFrame({"Time": time, "Temperature (C)": temp, "Humidity (%)": humidity, "Voltage (V)": voltage})

# 3 Box - Numbers Kaatrom
col1, col2, col3 = st.columns(3)
col1.metric("Avg Temperature", f"{temp.mean():.1f} °C")
col2.metric("Avg Humidity", f"{humidity.mean():.1f} %")
col3.metric("Avg Voltage", f"{voltage.mean():.2f} V")

st.divider()

# Graph 1
st.subheader("Temperature Over Time")
fig1 = px.line(df, x="Time", y="Temperature (C)", markers=True)
st.plotly_chart(fig1, use_container_width=True)

# Graph 2
st.subheader("Humidity vs Voltage")
fig2 = px.scatter(df, x="Humidity (%)", y="Voltage (V)", color="Temperature (C)")
st.plotly_chart(fig2, use_container_width=True)

st.success("Data Source: Lab Sensors (Demo Data)")
