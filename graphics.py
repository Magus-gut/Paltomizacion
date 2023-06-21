# Load pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file into DataFrame df
df = pd.read_csv('result_variables.csv')
num_rows = len(df.index)
num_hours = 24*7*52

aq = []
req = []
ca = []
time_a1 = []
time_a2 = []

# print(df['Value'][0])
for i in range(num_rows):
    if i < num_hours:
        aq.append(df['Value'][i])
    elif i < 2*num_hours:
        req.append(df['Value'][i])
    elif i < 3*num_hours:
        ca.append(df['Value'][i])
    elif i < 4*num_hours:
        time_a1.append(df['Value'][i])
    else:
        time_a2.append(df['Value'][i])

hr = np.arange(1, num_hours+1)
plt.figure(figsize=(10, 5))
# plt.plot(hr, aq, label='Agua en la tierra')
# plt.plot(hr, req, label='Requerimiento de agua')
# plt.plot(hr, ca, label='Consumo de agua')
plt.plot(hr, time_a1, label='Tiempo de riego sistema 1')
# plt.plot(hr, time_a2, label='Tiempo de riego sistema 2')
plt.show()
# Show dataframe
# print(df)