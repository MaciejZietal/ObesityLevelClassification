import pandas as pd

data = pd.read_csv("data/rawData.csv")

#Usuniecie Y
data = data.iloc[:,:-1]

Y = [1 if x > 30 else 0 for x in data.iloc[:,5]]

data['Y'] = Y

data = data[data['Wiek:'] <=35]

data = data[(data['Ile zazwyczaj zjadasz posiłków dziennie?']>1) & 
        (data['Ile zazwyczaj zjadasz posiłków dziennie?']<8)]

data.to_csv("data/preparedDataVis.csv", index=False)