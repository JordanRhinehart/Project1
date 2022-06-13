import pandas as pd
import csv

data = pd.read_csv (r'players_20.csv', nrows=5)
df = pd.DataFrame(data, columns= ['short_name','nationality'])

data2 = pd.read_csv (r'players_20.csv')
df2 = pd.DataFrame(data2, columns= ['short_name','wage_eur'])

for i in data2:
    print(i, end= ', ')


row_count = data2.shape[1]
column_count = data2.shape[0]

print("\n")
print (df)
print("\n")
print (df2)
print("\n")
print(f"The number of rows in this dataset are {row_count}")
print(f"The number of columns in this dataset are {column_count}")