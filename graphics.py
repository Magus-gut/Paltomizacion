# Load pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV files
df1 = pd.read_csv('result_variables.csv')
df2 = pd.read_csv('result_variables_sequia.csv')
df3 = pd.read_csv('result_variables_inund.csv')

# Extract the variables from each DataFrame
x1 = df1['Variable']
y1 = df1['Value']
x2 = df2['Variable']
y2 = df2['Value']
x3 = df3['Variable']
y3 = df3['Value']

# Create separate line graphs
plt.figure(figsize=(8, 6))  # Adjust the figure size if needed

# Graph 1
plt.subplot(1, 3, 1)
plt.plot(x1, y1)
plt.xlabel('Horas del año')
plt.ylabel('Tiempo de regado (hrs)')
plt.title('Resultado Normal')

# Graph 2
plt.subplot(1, 3, 2)
plt.plot(x2, y2)
plt.xlabel('Horas del año')
plt.ylabel('Tiempo de regado (hrs)')
plt.title('Resultado Sequía')

# Graph 3
plt.subplot(1, 3, 3)
plt.plot(x3, y3)
plt.xlabel('Horas del año')
plt.ylabel('Tiempo de regado (hrs)')
plt.title('Resultado Altas lluvias')

# Adjust the layout
plt.tight_layout()

# Display the graphs
plt.show()

