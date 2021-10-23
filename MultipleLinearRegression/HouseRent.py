import pandas as pd
from sklearn import preprocessing

### LOAD DATA ###
data = pd.read_csv('houses_to_rent.csv', sep=',')
data = data[['city', 'rooms', 'bathroom', 'parking spaces', 'fire insurance', 'furniture', 'rent amount']]

print(data.head())

#### PROCESS DATA #####
data ['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',','')))
data ['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:].replace(',','')))

le = preprocessing.LabelEncoder()
data['furniture'] =  le.fit_transform((data['furniture']))

print(data.head())