import pandas as pd

#Cualquier duda sobre este codigo preguntarle al Magus

#PARAMS, en cuanto queremos que suba/baje la temperatura de cada dia?
MINUS_VALUE = -2
PLUS_VALUE = 2

def change_every_value_by(amount, series):
    for i in range(len(series)):
        series[i] = series[i] + amount
        



dfTminus = pd.read_csv("bddT.csv", sep=";")
dfTminus = dfTminus['Valor medicion']
change_every_value_by(MINUS_VALUE, dfTminus)
Tminus = dfTminus.to_dict()


dfTplus = pd.read_csv("bddT.csv", sep=";")
dfTplus = dfTplus['Valor medicion']
change_every_value_by(PLUS_VALUE, dfTplus)
Tplus = dfTplus.to_dict()

print(Tminus[0])



