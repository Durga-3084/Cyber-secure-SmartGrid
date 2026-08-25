import random

def inject_attack(df):

    attack_node = random.choice(df.index)

    attack_type = random.choice([
        "voltage_spike",
        "frequency_drop",
        "power_spike"
    ])

    if attack_type == "voltage_spike":
        df.loc[attack_node, "Voltage"] = 280

    elif attack_type == "frequency_drop":
        df.loc[attack_node, "Frequency"] = 47

    elif attack_type == "power_spike":
        df.loc[attack_node, "Power_Usage"] = 300

    return df