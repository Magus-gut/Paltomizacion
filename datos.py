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


data_inundacion = {'Value': [35] * 364}  # Creates a list of 364 35's
df_inunda = pd.DataFrame(data_inundacion)

data_sequía = {'Value': [0] * 364}  # Creates a list of 364 0's
df_sequia = pd.DataFrame(data_sequía)


# print(df_inunda)
# print(df_sequia)