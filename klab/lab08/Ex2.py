import pandas as pd

data = pd.read_csv("population.csv", delimiter = ',')

print(data.head(5))

tmp =  data["Country Name"].drop_duplicates()
CountryNameData = tmp
tmp  = data["Country Code"].drop_duplicates()
CountryCodeData = tmp
data['Mean'] = data['Year']
data['Std'] = data['Year']
data['Min'] = data['Year']
data['Max'] = data['Year']
df = data.groupby('Country Name').agg({'Country Code' : 'unique','Mean' : 'mean', 'Std' : 'std', 'Min' : 'min', 'Max' : 'max'})
print(df)
# mean = data.loc[data["Country Code"] == 'ARB']
# print(mean)

# x = {'Country Name': CountryNameData.unique(), 'Country Code': CountryCodeData.unique() , }
# df = pd.DataFrame(x)
# print(df)
