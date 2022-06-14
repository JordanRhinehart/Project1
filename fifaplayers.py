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

###################################################

gr = data2.groupby(['nationality'], as_index=False)['short_name'].count()
country_bar = gr.nlargest(5,'short_name')
# gr.get_group(list(gr.groups)[0]).groupby('short_name').count()
# gd = data2.groupby('short_name').count()
df5 = pd.DataFrame(gr, columns= ['nationality', 'short_name'])
# six = df5.sort_values(['short_name'],ascending=[False])
graph = df2.nlargest(5, 'wage_eur')

# idx = data2.index.get_level_values(0)
# df7 = data2[idx == idx[10]]
# gr.loc([gr.index.levels[0][0]])




#####################################################

# Data = {'Country': ['USA','Canada','Germany','UK','France'],
#         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
#        }
# df4 = pd.DataFrame(data2,columns=['short_name', 'wage_eur'])

New_Colors = ['green','blue','purple','brown','teal']
plt.bar(country_bar['nationality'], country_bar['short_name'], color=New_Colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()

#####################################################
#####################################################

print("\n")
print (df)
print("\n")
print (df3)
print("\n")
print(f"The number of rows in this dataset are {row_count}")
print(f"The number of columns in this dataset are {column_count}")
print("\n")
print(f"There are {row_count} players ranging from the countries of {nationality_list}")
print("\n")
# print(df5)
print("\n")
# print(six.nlargest(10, 'short_name'))
print("\n")
print(country_bar)