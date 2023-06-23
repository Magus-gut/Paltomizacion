import pandas as pd



df = pd.read_csv("bdd.csv", sep=";")
dfT = pd.read_csv("bddT.csv", sep=";")

df.rename(columns={'Dia':'Dia',	'Precipitaciones':'p_diaria', 'Precipitaciones (hora)':'p_promedio_diaria',	'Evapotransporacion (diaria) [mm]':'evapo_diaria',	'Evapotransporacion (hora) [mm]':'evapo_hora'}, inplace = True)

df1 = df['evapo_hora']

e_repetido = []
for i in range(len(df1)):
    for j in range(24):
        e_repetido.append(df1[i])

evap = {}
for i, value in enumerate(e_repetido):
    evap[i+1] = value



df2 = df["p_promedio_diaria"]

p_repetido = []
for i in range(len(df2)):
    for j in range(24):
        p_repetido.append(df2[i])

pp = {}
for i, value in enumerate(p_repetido):
    pp[i+1] = value


dft = dfT['Valor medicion']
T = dft.to_dict()

print(f"max pp: {max(pp.values())}")
print(f"max evap: {max(evap.values())}")
print(f"max T: {max(T.values())}")

data_cruda = [0.1] * 121 + [2.5] * 152 + [0.01] * (365 - 121 - 152)
data_inundacion = pd.DataFrame({'Value': data_cruda})  # Creates a list of 364 35's
df_inunda = pd.DataFrame(data_inundacion)

p_repetido_inunda = []
for i in range(len(df_inunda)):
    for j in range(24):
        p_repetido_inunda.append(df_inunda.iloc[i])

pp_inunda = {}
for i, value in enumerate(p_repetido_inunda):
    pp_inunda[i+1] = value

data_sequía = {'Value': [0] * 365}  # Creates a list of 364 0's


df_sequia = pd.DataFrame(data_sequía)
p_repetido_sequia = []
for i in range(len(df_sequia)):
    for j in range(24):
        p_repetido_sequia.append(df_sequia.iloc[i])
pp_sequia = {}
for i, value in enumerate(p_repetido_sequia):
    pp_sequia[i+1] = value



# print(df_inunda)
# print(df_sequia)