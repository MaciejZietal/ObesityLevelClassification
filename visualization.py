import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Reading data
data = pd.read_csv("data/preparedDataVis.csv")

#Changing names
order = {'Wieś':'Wieś',
        'Miasto powyżej 500 tysięcy mieszkańców':'Miasto powyżej 500\ntysięcy mieszkańców',
        'Miasto od 150 tysięcy do 500 tysięcy mieszkańców':
            'Miasto od 150 tysięcy\ndo 500 tysięcy mieszkańców',
            'Miasto do 50 tysięcy mieszkańców':'Miasto do 50\ntysięcy mieszkańców',
            'Miasto od 50 do 150 tysięcy mieszkanców': 'Miasto od 50 do\n150 tysięcy mieszkanców'}

data['Miejsce zamieszkania:'] = data['Miejsce zamieszkania:'].replace(order)

order2 = {1: 'Tak', 0: 'Nie'}
data['Otyłość'] = data['Y'].replace(order2)

d1 = data[data['Otyłość']=='Tak']
d0 = data[data['Otyłość']=='Nie']

#Płeć
fig, ax = plt.subplots(figsize=(6,6))
pieValues=data['Płeć:'].value_counts()
palette_color = sns.color_palette('pastel')
plt.pie(pieValues.values, labels=pieValues.index, colors=palette_color,
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title("Płeć", fontsize=22)
plt.savefig("visualizations/plec.png")

#Miejsce zamieszkania
fig, ax = plt.subplots(figsize=(16,6))
p = sns.countplot(data=data, x='Miejsce zamieszkania:',hue='Otyłość',
                  palette='pastel',
                  order=['Wieś',
                         'Miasto do 50\ntysięcy mieszkańców',
                         'Miasto od 50 do\n150 tysięcy mieszkanców',
                         'Miasto od 150 tysięcy\ndo 500 tysięcy mieszkańców',
                         'Miasto powyżej 500\ntysięcy mieszkańców'])
p.axes.set_title("Występowanie otyłości w zależności od miejsca zamieszkania", 
                 fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Miejsce zamieszkania", fontsize=18)
plt.legend(title="Otyłość", fontsize=16, title_fontsize=16)
p.tick_params(labelsize=14)
fig = p.get_figure()
fig.savefig("visualizations/zamieszkanie.png")

#Otyłosc w rodzinie
fig, ax = plt.subplots(figsize=(6,6))
pieValues=d1['Czy ktoś z twojej najbliższej rodziny choruje na otyłość?'].value_counts()

palette_color = sns.color_palette('pastel')
plt.pie(pieValues.values, labels=pieValues.index, colors=[(1.0, 0.7058823529411765, 0.5098039215686274),
                                                  (0.6313725490196078, 0.788235294117647, 0.9568627450980393)],
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title('osoby otyłe', fontsize=22)
plt.savefig("visualizations/otyloscRodzina1.png")

fig, ax = plt.subplots(figsize=(6,6))
pieValues=d0['Czy ktoś z twojej najbliższej rodziny choruje na otyłość?'].value_counts()

palette_color = sns.color_palette('pastel')
plt.pie(pieValues.values, labels=pieValues.index, colors=palette_color,
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title('osoby o prawidłowej wadze', fontsize=22)
plt.savefig("visualizations/otyloscRodzina0.png")

#Fast food i slodycze
fig, ax = plt.subplots(2,1,figsize=(14,12))
p = sns.countplot(data=data, x='Jak często jesz jedzenie typu fast food?',
                  palette='pastel',ax=ax[0], hue='Otyłość',
                  order=['Rzadziej / wcale',
                         'Raz w tygodniu',
                         'Kilka razy w tygodniu',
                         'Codziennie / prawie codziennie'])
p.axes.set_title("Jak często jesz jedzenie typu fast food?", fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.legend(title="Otyłość", fontsize=16, title_fontsize=16)
p.tick_params(labelsize=14)


p = sns.countplot(data=data, x='Jak często jesz słodycze?',
                  palette='pastel',ax=ax[1], hue='Otyłość',
                  order=['Rzadziej / wcale',
                         'Raz w tygodniu',
                         'Kilka razy w tygodniu',
                         'Codziennie / kilka razy dziennie'])
p.axes.set_title('Jak często jesz słodycze?', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)
p.legend(title="Otyłość", fontsize=16, title_fontsize=16)
fig = p.get_figure()
fig.savefig("visualizations/fastfood.png")

#slodkie napoje
fig, ax = plt.subplots(figsize=(14,6))
p = sns.countplot(data=data, x='Jak często pijesz słodkie napoje?',
                  palette='pastel', hue='Otyłość',
                  order=['Rzadziej / wcale',
                         'Raz w tygodniu',
                         'Kilka razy w tygodniu',
                         'Codziennie / kilka razy dziennie'])
p.axes.set_title('Jak często pijesz słodkie napoje?', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)
p.legend(title="Otyłość", fontsize=16, title_fontsize=16)
fig = p.get_figure()
fig.savefig("visualizations/napoje.png")


#posilki dziennie
fig, ax = plt.subplots(2,1,figsize=(14,12))

p = sns.countplot(data=d1, x=d1['Ile zazwyczaj zjadasz posiłków dziennie?'],
                  ax=ax[0],
                  palette='flare')
p.axes.set_title('Dzienna liczba posiłków\nosoby otyłe', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)

p = sns.countplot(data=d0, x=d0['Ile zazwyczaj zjadasz posiłków dziennie?'],
                  ax=ax[1],
                  palette='flare')
p.axes.set_title('osoby o prawidłowej wadze', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Liczba posiłków", fontsize=18)
p.tick_params(labelsize=14)

fig = p.get_figure()
fig.savefig("visualizations/posilki.png")

# czas przed zasnieciem
fig, ax = plt.subplots(2,1,figsize=(14,13))
p = sns.countplot(data=d1, x='Ile godzin przed zaśnięciem jesz ostatni posiłek?',
                  palette='flare', ax=ax[0])
p.axes.set_title('Ile godzin przed zaśnięciem jesz ostatni posiłek?\nosoby otyłe', 
                 fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)

p = sns.countplot(data=d0, x='Ile godzin przed zaśnięciem jesz ostatni posiłek?',
                  palette='flare', ax=ax[1])
p.axes.set_title('osoby o prawidłowej wadze', 
                 fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Liczba godzin", fontsize=18)
p.tick_params(labelsize=14)

fig = p.get_figure()
fig.savefig("visualizations/godzPosilek.png")

#posilek w ciagu 2 godzin
fig, ax = plt.subplots(figsize=(12,6))
pieValues=d1['Czy zawsze jesz pierwszy posiłek w ciągu 2 godzin po obudzeniu?'].value_counts()
palette_color = sns.color_palette('pastel')
plt.pie(pieValues.values, labels=pieValues.index, colors=palette_color,
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title('Czy zawsze jesz pierwszy posiłek w ciągu 2 godzin po obudzeniu?\nosoby otyłe', fontsize=22)
plt.savefig("visualizations/posilek2h_1.png")

fig, ax = plt.subplots(figsize=(6,6))
pieValues=d0['Czy zawsze jesz pierwszy posiłek w ciągu 2 godzin po obudzeniu?'].value_counts()
plt.pie(pieValues.values, labels=pieValues.index, colors=[(1.0, 0.7058823529411765, 0.5098039215686274),
                                                          (0.6313725490196078, 0.788235294117647, 0.9568627450980393)],
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title('osoby o prawidłowej wadze', fontsize=22)
plt.savefig("visualizations/posilek2h_2.png")

#'Czy w ciągu dnia jesz posiłki w równych odstępach czasu?'
fig, ax = plt.subplots(figsize=(6,6))
pieValues=d1['Czy w ciągu dnia jesz posiłki w równych odstępach czasu?'].value_counts()
palette_color = sns.color_palette('pastel')
plt.pie(pieValues.values, labels=pieValues.index, colors=palette_color,
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title('Czy w ciągu dnia jesz posiłki w równych odstępach czasu?\nosoby otyłe', fontsize=22)
plt.savefig("visualizations/posilekrowne.png")

#srednio sypiasz
d00 = d0[d0['Ile godzin średnio sypiasz? (Pytanie dotyczy rzeczywistego czasu snu, który nie musi zgadzać się z czasem spędzonym w łóżku przed zaśnięciem i po przebudzeniu.)']!=3]
fig, ax = plt.subplots(2,1,figsize=(14,13))
p = sns.countplot(data=d1, x='Ile godzin średnio sypiasz? (Pytanie dotyczy rzeczywistego czasu snu, który nie musi zgadzać się z czasem spędzonym w łóżku przed zaśnięciem i po przebudzeniu.)',
                  palette='flare', ax=ax[0])
p.axes.set_title('Ile godzin średnio sypiasz?\nosoby otyłe', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)

p = sns.countplot(data=d00, x='Ile godzin średnio sypiasz? (Pytanie dotyczy rzeczywistego czasu snu, który nie musi zgadzać się z czasem spędzonym w łóżku przed zaśnięciem i po przebudzeniu.)',
                  palette='flare', ax=ax[1])
p.axes.set_title('osoby o prawidłowej wadze', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Liczba godzin", fontsize=18)
p.tick_params(labelsize=14)

fig = p.get_figure()
fig.savefig("visualizations/dlugoscsnu.png")

#chodzisz spac/wstajesz o regularnych porach
fig, ax = plt.subplots(figsize=(10,6))
pieValues=d1['Czy chodzisz spać i wstajesz o regularnych porach?'].value_counts()
palette_color = sns.color_palette('pastel')
plt.pie(pieValues.values, labels=pieValues.index, colors=palette_color,
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title('Czy chodzisz spać i wstajesz o regularnych porach?\nosoby otyłe', fontsize=22)
plt.savefig("visualizations/regularnepory1.png")

fig, ax = plt.subplots(figsize=(6,6))
pieValues=d0['Czy chodzisz spać i wstajesz o regularnych porach?'].value_counts()
palette_color = sns.color_palette('pastel')
plt.pie(pieValues.values, labels=pieValues.index, colors=[(1.0, 0.7058823529411765, 0.5098039215686274),
                                                          (0.6313725490196078, 0.788235294117647, 0.9568627450980393)],
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title('osoby o prawidłowej wadze', fontsize=22)
plt.savefig("visualizations/regularnepory0.png")

#kontrola liczby kalorii
fig, ax = plt.subplots(figsize=(10,6))
pieValues=d1['Czy kontrolujesz dzienną liczbę spożywanych kalorii?'].value_counts()
palette_color = sns.color_palette('pastel')
plt.pie(pieValues.values, labels=pieValues.index, colors=palette_color,
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title('Czy kontrolujesz dzienną liczbę spożywanych kalorii?\nosoby otyłe', fontsize=22)
plt.savefig("visualizations/kontrolaKalorii1.png")

fig, ax = plt.subplots(figsize=(6,6))
pieValues=d0['Czy kontrolujesz dzienną liczbę spożywanych kalorii?'].value_counts()
palette_color = sns.color_palette('pastel')
plt.pie(pieValues.values, labels=pieValues.index, colors=palette_color,
        autopct='%.0f%%', textprops={'fontsize': 16})
plt.title('osoby o prawidłowej wadze', fontsize=22)
plt.savefig("visualizations/kontrolaKalorii0.png")

#papierosy i alkohol
order = {'Rzadziej / wcale':'Rzadziej /\nwcale',
         'Kilka papierosów w ciągu tygodnia':'Kilka papierosów \nw ciągu tygodnia',
         'Kilka papierosów dziennie':'Kilka papierosów \ndziennie',
         'Przynajmniej paczkę dziennie':'Przynajmniej paczkę \ndziennie'}

d1['Jak często palisz papierosy?'] = d1['Jak często palisz papierosy?'].replace(order)
d0['Jak często palisz papierosy?'] = d0['Jak często palisz papierosy?'].replace(order)

fig, ax = plt.subplots(2,2,figsize=(18,18))
p = sns.countplot(data=d1, x='Jak często palisz papierosy?',
                  palette='flare',ax=ax[0,0], 
                  order=['Rzadziej /\nwcale',
                         'Kilka papierosów \nw ciągu tygodnia',
                         'Kilka papierosów \ndziennie',
                         'Przynajmniej paczkę \ndziennie'])
p.axes.set_title('Jak często palisz papierosy?\nosoby otyłe', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)

p = sns.countplot(data=d0, x='Jak często palisz papierosy?',
                  palette='flare',ax=ax[1,0], 
                  order=['Rzadziej /\nwcale',
                         'Kilka papierosów \nw ciągu tygodnia',
                         'Kilka papierosów \ndziennie',
                         'Przynajmniej paczkę \ndziennie'])
p.axes.set_title('osoby o prawidłowej wadze', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Regularność palenia papierosów", fontsize=18)
p.tick_params(labelsize=14)


p = sns.countplot(data=d1, x='Jak często spożywasz alkohol?',
                  palette='flare',ax=ax[0,1],
                  order=['Rzadziej / wcale',
                         'Raz w tygodniu',
                         'Kilka razy w tygodniu',
                         'Codziennie'])
p.axes.set_title('Jak często spożywasz alkohol?\nosoby otyłe', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)

p = sns.countplot(data=d0, x='Jak często spożywasz alkohol?',
                  palette='flare',ax=ax[1,1],
                  order=['Rzadziej / wcale',
                         'Raz w tygodniu',
                         'Kilka razy w tygodniu',
                         'Codziennie'])
p.axes.set_title('osoby o prawidłowej wadze', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Regularność spożywania alkoholu", fontsize=18)
p.tick_params(labelsize=14)

fig = p.get_figure()
fig.savefig("visualizations/alko.png")

#aktywnosc fizyczna
fig, ax = plt.subplots(2,1,figsize=(14,13))
p = sns.countplot(data=d1, x='Jak często podejmujesz aktywność fizyczną?',
                  palette='flare', ax=ax[0],
                  order=['Rzadziej / wcale',
                         'Raz w tygodniu',
                         '2-3 razy w tygodniu',
                         '4-6 razy w tygodniu',
                         'Codziennie'])
p.axes.set_title('Jak często podejmujesz aktywność fizyczną?\nosoby otyłe', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)

p = sns.countplot(data=d0, x='Jak często podejmujesz aktywność fizyczną?',
                  palette='flare', ax=ax[1],
                  order=['Rzadziej / wcale',
                         'Raz w tygodniu',
                         '2-3 razy w tygodniu',
                         '4-6 razy w tygodniu',
                         'Codziennie'])
p.axes.set_title('osoby o prawidłowej wadze', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Regularność podejmowanie aktywności fizycznej", fontsize=18)
p.tick_params(labelsize=14)

fig = p.get_figure()
fig.savefig("visualizations/aktywnosc.png")

#transport
fig, ax = plt.subplots(2,1,figsize=(14,13))
p = sns.countplot(data=d1, x='Z jakiego środka transportu korzystasz najczęściej?',
                  palette='flare', ax=ax[0])
p.axes.set_title('Z jakiego środka transportu korzystasz najczęściej?\nosoby otyłe', 
                 fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)

p = sns.countplot(data=d0, x='Z jakiego środka transportu korzystasz najczęściej?',
                  palette='flare', ax=ax[1])
p.axes.set_title('osoby o prawidłowej wadze', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Środek transportu", fontsize=18)
p.tick_params(labelsize=14)

fig = p.get_figure()
fig.savefig("visualizations/transport.png")

#'Ile godzin dziennie w czasie wolnym spędzasz korzystając z telefonu, komputera, laptopa, tabletu, oglądając telewizję itd.?'
fig, ax = plt.subplots(2,1,figsize=(14,13))
p = sns.countplot(data=d1, x='Ile godzin dziennie w czasie wolnym spędzasz korzystając z telefonu, komputera, laptopa, tabletu, oglądając telewizję itd.?',
                  palette='flare', ax=ax[0])
p.axes.set_title('Ile godzin dziennie w czasie wolnym spędzasz korzystając z telefonu, komputera itd.?\nosoby otyłe', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)

p = sns.countplot(data=d0, x='Ile godzin dziennie w czasie wolnym spędzasz korzystając z telefonu, komputera, laptopa, tabletu, oglądając telewizję itd.?',
                  palette='flare', ax=ax[1])
p.axes.set_title('osoby o prawidłowej wadze', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Liczba godzin", fontsize=18)
p.tick_params(labelsize=14)

fig = p.get_figure()
fig.savefig("visualizations/czas.png")

#samopoczucie
fig, ax = plt.subplots(2,1,figsize=(14,13))
p = sns.countplot(data=d1, x='Jak oceniasz swoje samopoczucie w skali w skali 1-10?',
                  palette='flare', ax=ax[0])
p.axes.set_title('Jak oceniasz swoje samopoczucie w skali w skali 1-10?\nosoby otyłe',
                 fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("", fontsize=18)
p.tick_params(labelsize=14)

p = sns.countplot(data=d0, x='Jak oceniasz swoje samopoczucie w skali w skali 1-10?',
                  palette='flare', ax=ax[1])
p.axes.set_title('osoby o prawidłowej wadze', fontsize=22)
p.set_ylabel("Liczba osób", fontsize=18)
p.set_xlabel("Samopoczucie", fontsize=18)
p.tick_params(labelsize=14)

fig = p.get_figure()
fig.savefig("visualizations/samopoczucie.png")

#BMI
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(12,6))
p = sns.boxplot(data=data, y='BMI', x='Płeć:',palette='pastel', width=0.7)
p.axes.set_title("BMI", fontsize=22)
p.set_ylabel("BMI", fontsize=18)
p.set_xlabel("Płeć", fontsize=18)
p.tick_params(labelsize=16)

fig = p.get_figure()
fig.savefig("visualizations/bmi.png")

#BMI od wieku
fig, ax = plt.subplots(1,2, figsize=(14,6))

p = sns.boxplot(data=data, y='Wiek:', palette='pastel', width=0.7, ax=ax[0])
p.axes.set_title("Wiek", fontsize=22)
p.set_ylabel("Wiek", fontsize=18)
p.tick_params(labelsize=16)

p = sns.regplot(data=data, x='Wiek:', y='BMI',
                scatter_kws={"color": "blue",'s':12}, 
                line_kws={"color": "red"}, ax=ax[1])
p.axes.set_title("BMI w zależności od wieku", fontsize=22)
p.set_ylabel("BMI", fontsize=18)
p.set_xlabel("Wiek", fontsize=18)
p.tick_params(labelsize=16)
p.set_xlim([18,35])

fig = p.get_figure()
fig.savefig("visualizations/bmi_wiek.png")

#Bmi wzrost
fig, ax = plt.subplots(figsize=(12,6))

p = sns.boxplot(data=data, y='Wzrost (w cm):', hue='Otyłość', x='Płeć:',
                palette='pastel', width=0.6)
p.axes.set_title("Wzrost w zależności od płci i otyłości", fontsize=22)
p.set_ylabel("Wiek", fontsize=18)
p.set_xlabel("", fontsize=18)
plt.legend(title="Otyłość", fontsize=16, title_fontsize=16)
p.tick_params(labelsize=16)

fig = p.get_figure()
fig.savefig("visualizations/bmi_wzrost.png")