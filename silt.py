import pandas as pd
import numpy as np
df=pd.read_excel("D:\GVPCEW\SIH\data\siltdata.xlsx")
draft = df['depth']
import random

# Function to generate a random number between a given range
def generate_random_number(start, end):
    return random.uniform(start, end)

# Generate 56 numbers
depth = []
siltation=[]
for _ in range(56):
    random_number1 = generate_random_number(10, 20)
    random_number2 = generate_random_number(1, 4)
    result = random_number1 * random_number2
    depth.append(round(result, 2))  # Round to two decimal places
    silt = 2 * depth + 3 * humidity + 1.5 * wind - 1.8 * Temperature + 0.5 * pressure + np.random.normal(0,10,100)
    siltation.append(round(silt, 2))

# Print the generated numbers
print(depth)
print(siltation)



