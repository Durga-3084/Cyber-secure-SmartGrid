# Cyber-Secure Smart Grid

A simulation-based smart grid security platform that combines **Machine Learning, renewable energy management, battery optimization, anomaly detection, and cybersecurity mechanisms** to monitor and protect smart-grid operations.

The project simulates a renewable-energy-powered smart grid where solar power generation is predicted using Machine Learning, energy demand is managed between solar, battery, and grid sources, and abnormal energy behavior can be detected through cybersecurity mechanisms.

---

## Key Features

### 1. Solar Power Prediction

Uses a **Random Forest Regression** model to predict solar power generation based on environmental and time-related parameters such as:

- Temperature
- Humidity
- Cloud Cover
- Hour
- Day of Year

The prediction helps the energy-management system determine how much renewable energy is expected to be available.

---

### 2. Intelligent Energy Management

The system dynamically determines the preferred energy source based on solar availability, energy demand, and battery status.

The priority is:

```text
Solar Energy
     ↓
Battery
     ↓
Grid Backup
