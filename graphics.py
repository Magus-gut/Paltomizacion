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

#A PARTIR DE ACA ARCHIVO NUEVO


def plotting(param):

    title = param['title']
    xlabel = param['xlabel']
    ylabel = param['ylabel']
    x = param['x']
    y = param['y']
    label = param['label']
    color = param['color']
    filename = param['filename']

    plt.figure(figsize=(10, 5))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x, y, label=label, color=color)
    plt.show()
    # plt.savefig(filename, bbox_inches='tight')


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

parameters = []
parameteraq = {'title': 'Agua en la tierra', 'xlabel': 'Hora', 'ylabel': 'Agua [mm]', 'x': hr, 'y': aq, 'label': 'Agua en la tierra', 'color': 'blue', 'filename': 'aq.png'}
parameters.append(parameteraq)
parametersreq = {'title': 'Requerimiento de agua', 'xlabel': 'Hora', 'ylabel': 'Agua [mm]', 'x': hr, 'y': req, 'label': 'Requerimiento de agua', 'color': 'blue', 'filename': 'req.png'}
parameters.append(parametersreq)
parametersca = {'title': 'Consumo de agua de palto', 'xlabel': 'Hora', 'ylabel': 'Agua [mm]', 'x': hr, 'y': ca, 'label': 'Consumo de agua', 'color': 'blue', 'filename': 'ca.png'}
parameters.append(parametersca)
parameterstime_a1 = {'title': 'Tiempo de riego sistema 1', 'xlabel': 'Hora', 'ylabel': 'Tiempo [hr]', 'x': hr, 'y': time_a1, 'label': 'Tiempo de riego sistema 1', 'color': 'red', 'filename': 'time_a1.png'}
parameters.append(parameterstime_a1)
parameterstime_a2 = {'title': 'Tiempo de riego sistema 2', 'xlabel': 'Hora', 'ylabel': 'Tiempo [hr]', 'x': hr, 'y': time_a2, 'label': 'Tiempo de riego sistema 2', 'color': 'green', 'filename': 'time_a2.png'}
parameters.append(parameterstime_a2)

for param in parameters:
    plotting(param)
