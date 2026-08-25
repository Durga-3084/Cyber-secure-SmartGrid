import joblib

model = joblib.load("model.pkl")

def detect_anomalies(df):

    features = df[["Power_Usage", "Voltage", "Frequency"]]

    predictions = model.predict(features)

    df["Anomaly"] = predictions

    df["Status"] = df["Anomaly"].apply(
        lambda x: "⚠️ Cyber Threat / Fault" if x == -1 else "Normal"
    )

    return df