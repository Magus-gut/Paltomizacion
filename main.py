from gurobipy import GRB, Model, quicksum
from random import randint, seed, uniform, random
from datos import T, pp, evap
from tempchanger import Tminus, Tplus
import numpy as np
from math import ceil
import csv

#from bd import *

seed(10)
m = Model()

weeks = 52
days = 7*weeks
hours = 24*days


# INDICES
#P = range(1, 4) # 3 Tipos de paltos. [HASS, FUERTE, BACON]
A = [i for i in range(1, 3)] # 2 Tipos de riegos [GOTEO, MICROASPERSION]
I = [i for i in range(1, weeks+1)] # 52 Semanas
D = [i for i in range(1, days+1)] # 364 Dias
H = [i for i in range(1, hours+1)] # 8736 Horas del año 
#T = range(1, 3) # 2 Tipos de suelos [FRANCO-ARCILLOSO, VOLCANICO]


# PARAMS

#Choose which temperature table to use
tempTables = {"normal": T, "minus": Tminus, "plus": Tplus}
T = tempTables["normal"]

# Max values for temperature and evaporation
maxT = max(T.values()) 
maxevap = max(evap.values())

# Evaporation rate
e = .8

# Area occupied by each palto
s = 50. #m**2,
 
# Minimum water consumption threshold per hour
w = 1.375  # [L]

# Maximum water consumption threshold per hour
u = 3.125 # [L]

# Tank capacity
maxEstanque = 200

# Water consumption by irrigation system 'a'
r = {1: 11.6, 2: 36.} # [L/Hora]

# Bugdet for water
wb = 40000

# Cost of water per liter
wc = 1.89


# Number of trees 
na = 150

# BIG M
M1 = 1000
M2 = M1


# VARIABLES
aq = m.addVars(H, vtype=GRB.CONTINUOUS, lb=0., ub=1000, name = "aq_hr")
req = m.addVars(H, vtype=GRB.BINARY, name = "req")
ca = m.addVars(H, vtype=GRB.CONTINUOUS, lb=0., ub=1000, name = "ca_hr")
time = m.addVars(A, H, vtype=GRB.CONTINUOUS, lb=0., ub=1, name = "time_hr")

m.update()

# RESTRICTIONS
#agregar distintos tipos de palto y suelo. Los tipos de palto tienen distintos consumos de agua y los tipos de suelo tienen distintos umbrales de consumo de agua

#Si el consumo de agua en una hora dado por ca_hr es mayor a w, entonces req_hr se activa #checked
m.addConstrs(( w >= ca[hr] - M1*(req[hr]) for hr in H), name = "R1")
m.addConstrs((w <= ca[hr] + M2*(1-req[hr]) for hr in H), name="R2")

# El palto debe consumir w litros, al menos, 3 veces al dia #checked
m.addConstrs((3 <= quicksum(req[hr] for hr in range(24*(d-1) + 1, 24*d)) for d in D), name = "R3")

# El consumo de agua de un palto tipo p, en un dia, no puede superar un umbral u_p. #checked
# m.addConstrs((quicksum(quicksum(ca[hr] for hr in range(24*(d-1) + 1, 24*d)) for a in A) <= u * 24 for d in D), name="R4")

#No se pueden usar 2 sistemas de regadío simultáneamente #checked
m.addConstrs((quicksum(time[a,hr] for a in A) <= 1 for hr in H), name="R5")

#El agua solo puede provenir del sistema de riego y precipitaciones, y solo puede se puede reducir por evaporacion o por el consumo del palto #unfeasible
m.addConstrs((aq[hr] == r[a] * time[a, hr] + pp[hr-1] * s + aq[hr-1] - ca[hr] - 0.5*(T[hr-1]/maxT)*aq[hr-1] for a in A for hr in H if hr != 1), name="R6")

#No se puede superar la capacidad maxima del estanque en el regadío de un día 
m.addConstrs((quicksum(quicksum(r[a] * time[a, hr] for hr in range(24*(d-1) + 1, 24*d)) for a in A) <= maxEstanque for d in D ), name="R7")

#No se puede superar el presupuesto anual dedicado al agua#checked
m.addConstr((quicksum(quicksum(r[a] * time[a, hr] for hr in H) for a in A) * wc <= wb), name="R8")

# Conservación de masa de agua en la tierra
# m.addConstrs((r[a] * time[a,hr-1] + pp[hr-1]*s + aq[hr-1] - aq[hr] - ca[hr] - (T[hr-1]/maxT)*aq[hr-1] == 0 for hr in H for a in A if hr != 1), name = "R7")
            

# La cantidad de agua presente en la tierra debe ser mayor o igual a 0
m.addConstrs((aq[hr] >= 0 for hr in H), name = "R8")

# Cantidad de agua inicial
m.addConstr((aq[1] == w * 24), name= "R9")

# El consumo de agua de un palto debe ser mayor o igual a 0
m.addConstrs((ca[hr] >= 0 for hr in H), name = "R10")

# #Estanque se recarga diario
# m.addConstrs((quicksum(quicksum(r[a] * time[a, hr] for hr in range(24*(d-1) + 1, 24*d)) for a in A) <= maxEstanque for d in D ), name="R13")

# Un palto no consume mas de 1.375 L por hora
m.addConstrs((ca[hr] <= w for hr in H), name = "R14")



m.update()

funcion_objetivo = (quicksum(quicksum(time[a, hr] * r[a] for hr in H)for a in A) * wc)
m.setObjective(funcion_objetivo, GRB.MINIMIZE)
# m.Params.timeLimit = 50.0
# m.Params.MIPGapAbs = 1e-2
m.optimize()
m.printStats()
m.printAttr('X')
print(f"El valor objetivo es de: {m.ObjVal}[CLP]")
print(f"Se rego un total de {quicksum(time[1, hr] for hr in H).getValue()} horas ({quicksum(r[1] * time[1, hr] for hr in H).getValue()} [L]) con el sistema 1 y un total de {quicksum(time[2, hr] for hr in H).getValue()} horas ({quicksum(r[2] * time[2, hr] for hr in H).getValue()} [L]) con el sistema 2")
print(
    f"Cada palto consumio {quicksum(ca[hr] for hr in H).getValue() } Litros de agua, esto es {(quicksum(ca[hr] for hr in H).getValue() ) / (52*7)} por dia")
print(
    f"El gasto es de {(quicksum(quicksum(time[a, hr] * r[a] for hr in H)for a in A) * wc).getValue() }[CLP]")
# if m.status == GRB.OPTIMAL:
    # Open a CSV file for writing
with open('result_variables.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    header = []
    writer.writerow(['Variable', 'Value'])

    # Iterate over the variables in the model and print their values
    for var in m.getVars():
        writer.writerow([var.varName, var.x])
        # header.append(var.varName)
    # writer.writerow(header)
    # for hr in H:
    #     row = []
    #     for var in m.getVars():
    #         row.append(var.x)
    #     writer.writerow(row)
