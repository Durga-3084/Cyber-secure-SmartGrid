import numpy as np
import pandas as pd

class SmartGridSimulator:

    def __init__(self):

        self.nodes = [
            "Node_A",
            "Node_B",
            "Node_C",
            "Node_D"
        ]

        self.power_plant_capacity = 500

    def generate_node_data(self):

        data = []

        for node in self.nodes:

            voltage = np.random.normal(220, 8)
            power = np.random.normal(100, 25)
            frequency = np.random.normal(50, 0.3)

            data.append({
                "Node": node,
                "Voltage": round(voltage,2),
                "Power_Usage": round(power,2),
                "Frequency": round(frequency,2)
            })

        df = pd.DataFrame(data)

        return df