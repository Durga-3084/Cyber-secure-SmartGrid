import pandas as pd
import numpy as np

def generate_data():

    nodes = ["Grid A", "Grid B", "Grid C", "Grid D"]

    data = {
        "Node": np.random.choice(nodes, 20),
        "Power_Usage": np.random.normal(100, 15, 20),
        "Voltage": np.random.normal(220, 5, 20),
    }

    df = pd.DataFrame(data)

    return df
