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
top_countries2 = gr.nlargest(5,'short_name')
print(top_countries)
print("\n")


############################################################
###################### NUMBER SIX : ########################


plt.bar(top_countries2['nationality'], top_countries2['short_name'], color='green')
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

print("\n")
############################################################
################ NUMBER EIGHT : ############################

print("QUESTION NUMBER EIGHT:")
top_wages = pd.DataFrame(data2, columns= ['short_name','wage_eur'])
highest_wages = top_wages.nlargest(5, 'wage_eur')
print(highest_wages)


############################################################
################# NUMBER NINE : ############################

New_Colors = ['green','blue','purple','brown','teal']
plt.bar(highest_wages['short_name'], highest_wages['wage_eur'], color=New_Colors)
plt.title('Top Paid Players and Their Wages', fontsize=14)
plt.xlabel('Player', fontsize=14)
plt.ylabel('Salary', fontsize=14)
plt.grid(True)
plt.show()


print("\n")
############################################################
################## NUMBER TEN : ############################

print("QUESTION NUMBER TEN:")
germany = data2[data2['nationality'].str.contains('Germany')]
print(germany.head(10))


print("\n")

############################################################
################## NUMBER ELEVEN : #########################
print("QUESTION NUMBER ELEVEN:")

print("The Heaviest German Players:")
print(germany.nlargest(5,"weight_kg"))
print("\n")
print("The Tallest German Players:")
print(germany.nlargest(5,"height_cm"))
print("\n")
print("The Most Paid German Players:")
print(germany.nlargest(5,"wage_eur"))

print("\n")

############################################################
################## NUMBER TWELVE : #########################
print("QUESTION NUMBER TWELVE:")

wages = pd.DataFrame(germany, columns= ['short_name','wage_eur'])
print(wages.head(5))


print("\n")
############################################################
################## NUMBER THIRTEEN : #######################
print("QUESTION NUMBER THIRTEEN:")

top_shooters = pd.DataFrame(data2, columns= ['short_name','shooting'])
print(top_shooters.nlargest(5,"shooting"))

print("\n")
############################################################
################## NUMBER FOURTEEN : #######################
print("QUESTION NUMBER FOURTEEN:")

top_defenders = pd.DataFrame(data2, columns= ['short_name','defending', 'nationality', 'club'])
print(top_defenders.nlargest(5,"defending"))


print("\n")
############################################################
################## NUMBER FIFTEEN : #######################
print("QUESTION NUMBER FIFTEEN:")

real_madrid = data2[data2['club'].str.contains('Real Madrid')]
madrid_wages = pd.DataFrame(real_madrid, columns= ['short_name','wage_eur'])
print(madrid_wages.head(5))


print("\n")
############################################################
################## NUMBER SIXTEEN : #######################
print("QUESTION NUMBER SIXTEEN:")

madrid_shooting = pd.DataFrame(real_madrid, columns= ['short_name','shooting'])
print(madrid_shooting.head(5))

print("\n")

############################################################
################## NUMBER SEVENTEEN : ######################
print("QUESTION NUMBER SEVENTEEN:")

madrid_defending = pd.DataFrame(real_madrid, columns= ['short_name','defending'])
print(madrid_defending.head(5))

print("\n")

############################################################
################## NUMBER EIGHTEEN : #######################
print("QUESTION NUMBER EIGHTEEN:")

madrid_nationality = pd.DataFrame(real_madrid, columns= ['short_name','nationality'])
print(madrid_nationality.head(5))

print("\n")

############################################################
############################################################