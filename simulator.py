import numpy as np
import pandas as pd

nodes = ["Node_A", "Node_B", "Node_C", "Node_D"]

def generate_grid_data():

    data = {
        "Node": np.random.choice(nodes, 50),
        "Power_Usage": np.random.normal(100, 20, 50),
        "Voltage": np.random.normal(220, 10, 50),
        "Frequency": np.random.normal(50, 0.5, 50)
    }

    df = pd.DataFrame(data)

    return df