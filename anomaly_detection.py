def detect_anomaly(power):

    if power > 140 or power < 60:
        return "⚠️ Possible Attack"

    else:
        return "Normal"