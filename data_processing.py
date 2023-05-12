import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")

# perform some data processing here
processed_data = data.apply(np.sqrt)

print(processed_data)
