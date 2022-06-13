import pandas as pd
import csv
import matplotlib.pyplot as plt

data = pd.read_csv (r'players_20.csv', nrows=5)
df = pd.DataFrame(data, columns= ['short_name','nationality'])

data2 = pd.read_csv (r'players_20.csv')
df2 = pd.DataFrame(data2, columns= ['short_name','wage_eur'])
df3 = pd.DataFrame(data2, columns= ['nationality'])

for i in data2:
    print(i, end= ', ')


row_count = data2.shape[0]
column_count = data2.shape[1]

# country_count = data2.shape[0]

# print(f"This is what we get {df3.shape[0]}")
loc = data2['nationality'].tolist()

nationality_list = []
for i in loc:
    if i not in nationality_list:
        nationality_list.append(i)
john = nationality_list.sort()

print("\n")
print (df)
print("\n")
print (df3)
print("\n")
print(f"The number of rows in this dataset are {row_count}")
print(f"The number of columns in this dataset are {column_count}")
print("\n")
print(f"There are {row_count} players ranging from the countries of {nationality_list}")