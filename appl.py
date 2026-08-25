import pandas as pd
import numpy as np
import hashlib
import streamlit as st
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt

from simulator import generate_grid_data
from anomaly_detector import detect_anomalies
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from data_simulator import generate_data
from anomaly_detection import detect_anomaly

st.set_page_config(page_title="Cyber‑Secure Smart Grid for Renewable Energy Infrastructure", layout="wide")

# ===================== SIDEBAR =====================

st.sidebar.title("Project Overview")

st.sidebar.write("""
### Cyber‑Secure Smart Grid for Renewable Energy Infrastructure

This project demonstrates how smart grids are protected from cyber attacks.

### System Goals

**Goal 1 – Solar Energy Prediction**  
Predict solar energy generation using weather data.

**Goal 2 – Intelligent Energy Management**  
Decide whether to use solar, battery, or grid power.

**Goal 3 – Battery Optimization**  
Prevent over‑discharging and maintain reserve battery.

**Goal 4 – Cybersecurity Protection**  
Authentication and anomaly detection for smart grid.

**Goal 5 – Energy Monitoring Dashboard**  
Visual monitoring of energy production and demand.
""")

# ===================== LOAD DATA =====================

data = pd.read_csv("solar_data.csv")

data['timestamp'] = pd.to_datetime(data['timestamp'])
data['hour'] = data['timestamp'].dt.hour
data['day_of_year'] = data['timestamp'].dt.dayofyear

features = ['hour', 'day_of_year', 'temperature', 'humidity', 'cloud_cover']
X = data[features]
y = data['solar_power_generated']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, predictions))

# ===================== TITLE =====================

st.title("Cyber‑Secure Smart Grid for Renewable Energy Infrastructure")

predicted_solar = 0

# ===================== TABS =====================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Solar Prediction",
    "Energy Management",
    "Battery",
    "Cybersecurity",
    "Dashboard",
    "Smart Grid"
])
# ===================== GOAL 1 =====================

with tab1:

    st.header("Solar Energy Prediction")

    st.write(f"Model Test RMSE: {rmse:.2f} kW")

    hour = st.slider("Hour of Day", 0, 23)
    day_of_year = st.slider("Day of Year", 1, 365)
    temperature = st.slider("Temperature (°C)", -10, 50)
    humidity = st.slider("Humidity (%)", 0, 100)
    cloud_cover = st.slider("Cloud Cover (%)", 0, 100)

    if st.button("Predict Solar Energy"):

        input_features = np.array([[hour, day_of_year, temperature, humidity, cloud_cover]])

        input_scaled = scaler.transform(input_features)

        prediction = model.predict(input_scaled)

        predicted_solar = prediction[0]

        st.success(f"Predicted Solar Power: {prediction[0]:.2f} kW")

# ===================== GOAL 2 =====================

with tab2:

    st.header("Intelligent Energy Management")

    demand = st.number_input("Energy Demand (kW)", 0)
    battery = st.slider("Battery Level (%)", 0, 100)

    if st.button("Run Energy Decision"):

        if predicted_solar >= demand:
            decision = "Use Solar Energy"

        elif battery > 30:
            decision = "Use Battery Power"

        else:
            decision = "Use Grid Backup"

        st.success(f"Energy Decision: {decision}")

# ===================== GOAL 3 =====================

with tab3:

    st.header("Battery Usage Optimization")

    battery_capacity = st.number_input("Battery Capacity (kWh)", 0)
    current_battery = st.number_input("Current Battery Level (kWh)", 0)

    if st.button("Optimize Battery Usage"):

        reserve = 0.2 * battery_capacity

        if current_battery > reserve:
            st.success("Battery can supply energy safely.")
            st.write("Available energy:", current_battery - reserve, "kWh")

        elif current_battery == reserve:
            st.warning("Battery at reserve level. Only critical operations allowed.")

        else:
            st.error("Battery too low! Charging required.")

# ===================== GOAL 4 =====================

with tab4:

    st.header("Cybersecurity Protection")

    user_key = st.text_input("Enter System Security Key", type="password")

    correct_key = "smartgrid123"

    if st.button("Authenticate System"):

        hashed_input = hashlib.sha256(user_key.encode()).hexdigest()
        hashed_correct = hashlib.sha256(correct_key.encode()).hexdigest()

        if hashed_input == hashed_correct:
            st.success("Authentication Successful")

        else:
            st.error("Access Denied")

    st.subheader("Energy Data Anomaly Detection")

    energy_value = st.number_input("Incoming Energy Data (kW)", 0)

    if st.button("Check Data Integrity"):

        if energy_value > 1000:
            st.warning("⚠ Suspicious Energy Data Detected")

        else:
            st.success("Energy Data Normal")

# ===================== GOAL 5 =====================

with tab5:

    st.header("Real-Time Energy Monitoring Dashboard")

    solar_output = st.slider("Current Solar Generation (kW)", 0, 200, key="solar_dashboard")
    battery_level_dashboard = st.slider("Battery Level (%)", 0, 100, key="battery_dashboard")
    energy_demand_dashboard = st.slider("Energy Demand (kW)", 0, 200, key="demand_dashboard")

    dashboard_data = {
        "Solar Generation": solar_output,
        "Battery Level": battery_level_dashboard,
        "Energy Demand": energy_demand_dashboard
    }

    st.subheader("Energy System Status")

    st.bar_chart(dashboard_data)

    if solar_output > energy_demand_dashboard:
        st.success("Solar energy is sufficient for current demand")

    else:
        st.warning("Solar energy insufficient, battery/grid may be used")
with tab6:
    st.header("Smart Grid Cyber Attack & Fault Simulation")

    # ---------------- GRID NODES ----------------
    nodes = ["Solar Plant", "Battery Storage", "Substation", "City Load"]

    df = pd.DataFrame({
        "Node": nodes,
        "Power_Usage": np.random.normal(100, 15, 4),
        "Voltage": np.random.normal(220, 5, 4),
        "Frequency": np.random.normal(50, 0.3, 4)
    })

    # ---------------- ATTACK / FAULT SIMULATOR ----------------
    st.subheader("Attack & Fault Simulator")

    col1, col2, col3, col4, col5 = st.columns(5)

    attack_type = "None"

    if col1.button("Normal Operation"):
        attack_type = "None"

    if col2.button("Power Spike Attack"):
        attack_type = "Power"

    if col3.button("Voltage Manipulation"):
        attack_type = "Voltage"

    if col4.button("Frequency Attack"):
        attack_type = "Frequency"

    if col5.button("Equipment Fault"):
        attack_type = "Fault"


    # ---------------- APPLY ATTACK / FAULT ----------------

    if attack_type == "Power":
        df.loc[2, "Power_Usage"] = 220

    elif attack_type == "Voltage":
        df.loc[1, "Voltage"] = 260

    elif attack_type == "Frequency":
        df.loc[3, "Frequency"] = 55

    elif attack_type == "Fault":
        df.loc[0, "Voltage"] = 150
        df.loc[0, "Power_Usage"] = 40


    # ---------------- ANOMALY CLASSIFIER ----------------
    def detect_issue(row):

        if row["Power_Usage"] > 150:
            return "Cyber Attack: Power Spike"

        elif row["Voltage"] > 240:
            return "Cyber Attack: Voltage Manipulation"

        elif row["Frequency"] > 52:
            return "Cyber Attack: Frequency Attack"

        elif row["Voltage"] < 180 and row["Power_Usage"] < 60:
            return "Physical Grid Fault"

        else:
            return "Normal"

    df["Status"] = df.apply(detect_issue, axis=1)


    # ---------------- GRID METRICS ----------------
    st.subheader("Grid Status")

    total_nodes = len(df)
    alerts = len(df[df["Status"] != "Normal"])

    col1, col2 = st.columns(2)

    col1.metric("Active Grid Nodes", total_nodes)
    col2.metric("Detected Issues", alerts)


    # ---------------- GRID DATA ----------------
    st.subheader("Grid Sensor Data")

    st.dataframe(df)


    # ---------------- MONITORING GRAPH ----------------
    st.subheader("Smart Grid Monitoring")

    fig = px.scatter(
        df,
        x="Voltage",
        y="Power_Usage",
        color="Status",
        size="Frequency",
        hover_name="Node",
        title="Smart Grid Node Monitoring"
    )

    st.plotly_chart(fig, use_container_width=True)


    # ---------------- ALERT PANEL ----------------
    st.subheader("Grid Security Alerts")

    alerts_df = df[df["Status"] != "Normal"]

    if len(alerts_df) > 0:
        st.error("⚠ Issue Detected in Smart Grid!")
        st.dataframe(alerts_df)
    else:
        st.success("All Grid Nodes Operating Normally")


    # ---------------- 3D SMART GRID ----------------
    st.subheader("Real-Time Smart Grid 3D Visualization")

    import plotly.graph_objects as go

    x = df["Voltage"]
    y = df["Power_Usage"]
    z = df["Frequency"]

    node_trace = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers+text',
        text=df["Node"],
        textposition="top center",
        marker=dict(
            size=12,
            color=df["Status"].apply(lambda x: "red" if x != "Normal" else "green"),
            showscale=False
        )
    )

    fig3d = go.Figure(data=[node_trace])

    fig3d.update_layout(
        title="Smart Grid Parameter Space",
        scene=dict(
            xaxis_title="Voltage (V)",
            yaxis_title="Power Usage (kW)",
            zaxis_title="Frequency (Hz)"
        )
    )

    st.plotly_chart(fig3d, use_container_width=True)