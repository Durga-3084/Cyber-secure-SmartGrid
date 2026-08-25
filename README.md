# Cyber-Secure Smart Grid

A simulation-based **Cyber-Secure Smart Grid platform** that integrates Machine Learning, renewable energy management, battery monitoring, anomaly detection, attack simulation, and cybersecurity mechanisms to demonstrate how smart-grid infrastructure can be monitored and protected.

---

## Overview

Modern smart grids rely heavily on digital systems, sensors, communication networks, and automated energy-management mechanisms. While these technologies improve efficiency, they also introduce cybersecurity risks such as manipulated sensor readings and abnormal energy behavior.

This project provides a **simulation-based smart-grid environment** where solar energy generation is predicted using Machine Learning, available energy is intelligently managed between solar, battery, and grid sources, and cybersecurity mechanisms are used to monitor abnormal activity.

The project combines:

- Solar Power Prediction
- Intelligent Energy Management
- Battery Management
- SHA-256 Authentication
- Anomaly Detection
- Attack Simulation
- Smart Grid Simulation

---

## Objectives

The main objectives of this project are:

- Predict solar power generation using Machine Learning.
- Improve utilization of renewable energy.
- Manage energy between solar, battery, and grid sources.
- Monitor battery status and maintain a reserve capacity.
- Demonstrate cryptographic authentication using SHA-256.
- Detect potentially abnormal smart-grid energy data.
- Simulate cyberattack scenarios.
- Provide an interactive dashboard for monitoring smart-grid operations.

---

# Key Features

## 1. Solar Power Prediction

The project uses a **Random Forest Regression** model to predict solar power generation.

The model uses environmental and time-related parameters such as:

- Hour
- Day of Year
- Temperature
- Humidity
- Cloud Cover

### Machine Learning Workflow

```text
Solar Dataset
     ↓
Data Preprocessing
     ↓
Feature Selection
     ↓
Train/Test Split
     ↓
Random Forest Regressor
     ↓
Model Evaluation
     ↓
Solar Power Prediction
