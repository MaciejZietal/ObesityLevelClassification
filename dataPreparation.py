import pandas as pd

data = pd.read_csv("data/rawData.csv")

#Usuniecie Y
data = data.iloc[:,:-1]

data = data[data['Wiek:']<=35]
Y = [1 if x > 30 else 0 for x in data.iloc[:,5]]

#Zamianna zmiennych binarnych i nominalnych na 0-1
x1=pd.get_dummies(data[['Czy ktoś z twojej najbliższej rodziny choruje na otyłość?',
                     'Czy zawsze jesz pierwszy posiłek w ciągu 2 godzin po obudzeniu?',
                     'Czy w ciągu dnia jesz posiłki w równych odstępach czasu?',
                     'Czy chodzisz spać i wstajesz o regularnych porach?',
                     'Z jakiego środka transportu korzystasz najczęściej?',
                     'Jak często jesz słodycze?',
                     'Jak często pijesz słodkie napoje?',
                     'Jak często spożywasz alkohol?',
                     'Jak często podejmujesz aktywność fizyczną?']])


#Zmienne ciagle
x1['Ile godzin przed zaśnięciem jesz ostatni posiłek?'] = data['Ile godzin przed zaśnięciem jesz ostatni posiłek?']
x1['Ile godzin średnio sypiasz? (Pytanie dotyczy rzeczywistego czasu snu, który nie musi zgadzać się z czasem spędzonym w łóżku przed zaśnięciem i po przebudzeniu.)'] = data['Ile godzin średnio sypiasz? (Pytanie dotyczy rzeczywistego czasu snu, który nie musi zgadzać się z czasem spędzonym w łóżku przed zaśnięciem i po przebudzeniu.)']
x1['Ile godzin dziennie w czasie wolnym spędzasz korzystając z telefonu, komputera, laptopa, tabletu, oglądając telewizję itd.?']= data['Ile godzin dziennie w czasie wolnym spędzasz korzystając z telefonu, komputera, laptopa, tabletu, oglądając telewizję itd.?']
x1['Jak oceniasz swoje samopoczucie w skali w skali 1-10?']=data['Jak oceniasz swoje samopoczucie w skali w skali 1-10?']
x1['Wiek:'] = data.iloc[:,2]
x1['Wzrost (w cm):'] = data['Wzrost (w cm):']

x1['Y'] = Y

x1.to_csv("data/preparedData.csv", index=False)