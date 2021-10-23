import pandas as pd

### LOAD DATA ###
data = pd.read_csv('houses_to_rent.csv', sep=',')
data= data[['city', 'rooms', 'bathroom', 'parking spaces', 'fire insurance', 'furniture', 'rent amount']]

print(data.head())


#### PROCESS DATA #####
