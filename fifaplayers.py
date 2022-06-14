import pandas as pd
import csv
import matplotlib.pyplot as plt


############################################################
################ NUMBER ONE : ##############################
print("QUESTION NUMBER ONE:")
data = pd.read_csv (r'players_20.csv', nrows=5)
df = pd.DataFrame(data, columns= ['short_name','nationality'])
print(data)
print("\n")


############################################################
################ NUMBER TWO : ##############################

print("QUESTION NUMBER TWO:")
data2 = pd.read_csv (r'players_20.csv')
for i in data2:
    print(i, end= ', ')
print("\n")


############################################################
################ NUMBER THREE : ############################

print("QUESTION NUMBER THREE:")
row_count = data2.shape[0]
column_count = data2.shape[1]
print(f"The number of rows in this dataset are {row_count}")
print(f"The number of columns in this dataset are {column_count}")
print("\n")



############################################################
################ NUMBER FOUR : #############################

print("QUESTION NUMBER FOUR:")
gr = data2.groupby(['nationality'], as_index=False)['short_name'].count()
print(gr)
print("\n")

############################################################
###################### NUMBER FIVE : #######################

print("QUESTION NUMBER FIVE:")
top_countries = gr.nlargest(10,'short_name')
print(top_countries)
print("\n")


############################################################
###################### NUMBER SIX : ########################


plt.bar(top_countries['nationality'], top_countries['short_name'], color='green')
plt.title('Top Countries and Their Number of Players', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Number of Players', fontsize=14)
plt.grid(True)
plt.show()


############################################################
################ NUMBER SEVEN : ############################


print("QUESTION NUMBER SEVEN:")
wages = pd.DataFrame(data, columns= ['short_name','wage_eur'])
print(wages)


############################################################
################ NUMBER EIGHT : ############################

print("QUESTION NUMBER EIGHT:")
top_wages = pd.DataFrame(data2, columns= ['short_name','wage_eur'])
highest_wages = top_wages.nlargest(5, 'wage_eur')
print(highest_wages)


############################################################
################# NUMBER NINE : ############################

print("QUESTION NUMBER NINE:")

plt.bar(highest_wages['short_name'], highest_wages['wage_eur'], color='green')
plt.title('Top Countries and Their Number of Players', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Number of Players', fontsize=14)
plt.grid(True)
plt.show()



############################################################
################## NUMBER TEN : ############################

print("\n")
print (df)
print("\n")
print (df3)

# country_count = data2.shape[0]

# print(f"This is what we get {df3.shape[0]}")
loc = data2['nationality'].tolist()

nationality_list = []
for i in loc:
    if i not in nationality_list:
        nationality_list.append(i)
john = nationality_list.sort()

############################################################
################ NUMBER SEVEN : ############################

gr = data2.groupby(['nationality'], as_index=False)['short_name'].count()
country_bar = gr.nlargest(5,'short_name')
# gr.get_group(list(gr.groups)[0]).groupby('short_name').count()
# gd = data2.groupby('short_name').count()
df5 = pd.DataFrame(gr, columns= ['nationality', 'short_name'])
# six = df5.sort_values(['short_name'],ascending=[False])






#####################################################

# Data = {'Country': ['USA','Canada','Germany','UK','France'],
#         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
#        }
# df4 = pd.DataFrame(data2,columns=['short_name', 'wage_eur'])

# New_Colors = ['green','blue','purple','brown','teal']
# plt.bar(country_bar['nationality'], country_bar['short_name'], color=New_Colors)
# plt.title('Country Vs GDP Per Capita', fontsize=14)
# plt.xlabel('Country', fontsize=14)
# plt.ylabel('GDP Per Capita', fontsize=14)
# plt.grid(True)
# plt.show()

#####################################################
#####################################################

# print("\n")


# print("\n")
# print(f"There are {row_count} players ranging from the countries of {nationality_list}")
# print("\n")
# # print(df5)
# print("\n")
# # print(six.nlargest(10, 'short_name'))
# print("\n")
# print(country_bar)