import csv
import pandas as pd
from pandas import DataFrame, read_csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

# Question 1: Load the csv file and show top 5 records from it.
df = pd.read_csv (r'D:\Users\yaima\Documents\Projects\players_20.csv')   

# print('\n'"###Top 5 records from CSV File###"'\n')
# print(df.head())

# #  Question 2: Name of columns
# print('\n'"###CSV File columns' names###"'\n')
# for col in df.columns:
#     print(col, end = ", ")

# #  Question 3: Number of rows and columns
# print('\n'"###CSV File number of rows and columns###"'\n')
count_row = df.shape[0] # Gives number of rows
count_col = df.shape[1] # Gives number of columns
# print(f"The number of rows in this dataset are {count_row}"'\n')
# print(f"The number of columns in this dataset are {count_col}"'\n')


# #  Question 4: Group by number of players and their countries.
# print('\n'"###CSV File number of players and their countries###"'\n')
gr = df.groupby(['nationality', 'short_name'])
# print(gr.first())

# #  Question 5: Top 10 countries and their number of players.
# print('\n'"###Top 10 countries and their number of players###"'\n')
gr = df.groupby('nationality').count()
df5 = pd.DataFrame(gr, columns= ['short_name'])
# print(df5.nlargest(10, 'short_name'))

# #  Question 6: Top 5 countries and their number of players, try to fill green color in bars.
# print('\n'"###Bar-graph of top 5 countries and their number of players with green color bars.###"'\n')
countries = df.groupby(['nationality'], as_index=False)['short_name'].count()
country_bar = countries.nlargest(5,'short_name')
# print(country_bar'\n')
# plt.figure(figsize=(15,6))
# plt.bar(country_bar['nationality'],country_bar['short_name'],color='green')
# plt.xlabel('Nationality', size = 15)
# plt.ylabel('Number of Players', size=15)
# plt.title('Players per Country')
# plt.show()

# #  Question 7: Show top 5 players short name and wages.
# print('\n'"###Top 5 world players short name and wages###")
top_wages = pd.DataFrame(df, columns= ['short_name','wage_eur'])
# print(top_wages.head(5, 'wage_eur'))
# print(top_wages.nlargest(5, 'wage_eur'))

# #  Question 8: Show top 5 players getting highest salaries.
# print('\n'"###Top 5 world players getting highest salaries###")
top_salaries = top_wages.head(5, 'wage_eur')
# print('\n'top_salaries)
highest_salaries = top_wages.nlargest(5, 'wage_eur')
# print('\n'highest_salaries)

# #  Question 9: Bar plot of top 5 players getting highest salaries.
# print('\n'"###Bar plot of top 5 world players getting highest salaries###")
# plt.figure(figsize=(15,6))
# plt.bar(highest_salaries['short_name'],highest_salaries['wage_eur'],color='green')
# plt.xlabel('Player Names', size = 15)
# plt.ylabel('Players Wages', size=15)
# plt.title('Top 5 Wages per Player')
# plt.show()

# Question 10: Show top 10 records of Germany.
# print('\n'"###Top 10 records of Germany###")
Germany = df[df['nationality'].str.contains('Germany')]
# print(Germany.head(10))

# # Question 11: Show top 5 records of Germany players who have maximum height, weight and wages.

records = df[['height_cm', 'weight_kg', 'wage_eur']]
german_players = records[df['nationality'].str.contains('Germany')]
# print('\n'"###Top 5 records of Germany players who have maximum salary###")
# print(Germany.head(5, ['wage_eur']))
# print(Germany.nlargest(5, ['wage_eur']))
# print('\n')
# print(german_players.head(5, ['wage_eur']))
# print(german_players.nlargest(5, ['wage_eur']))
# print('\n'"###Top 5 records of Germany players who have maximum height###")
# print(Germany.head(5, ['height_cm']))
# print(Germany.nlargest(5, ['height_cm']))
# print('\n')
# print(german_players.head(5, ['height_cm']))
# print(german_players.nlargest(5, ['height_cm']))
# print('\n'"###Top 5 records of Germany players who have maximum weight###")
# print(Germany.head(5, ['weight_kg']))
# print(Germany.nlargest(5, ['weight_kg']))
# print('\n')
# print(german_players.head(5, ['weight_kg']))
# print(german_players.nlargest(5, ['weight_kg']))

# Question 12: Show short name and wages of top 5 Germany players.
# print('\n'"###Top 5 salaries for German players###")
German_topWages = pd.DataFrame(Germany, columns= ['short_name','wage_eur'])
# print(German_topWages.head(5, 'wage_eur'))
# print(German_topWages.nlargest(5, 'wage_eur'))

# Question 13: Show top 5 players who have great shooting skills among all with short name.
# print('\n'"###Top 5 world players with great shooting skills###")
top_shooters = pd.DataFrame(df, columns = ['short_name', 'shooting'])
# print(top_shooters.head(5, 'shooting'))
# print(top_shooters.nlargest(5, 'shooting'))

# Question 14: Show top 5 players records (short name, defending, nationality, and club) that have awesome defending skills.
# print('\n'"###Top 5 world players with great  defending skills###")
top_defenders = pd.DataFrame(df, columns = ['short_name', 'defending', 'nationality', 'club'])
# print(top_defenders.head(5, 'defending'))
# print(top_defenders.nlargest(5, 'defending'))

# Question 15: Show wages records of top 5 players of 'Real Madrid' team.
# print('\n'"###Top 5 RM player wages###")
real_madrid = df[df['club'].str.contains('Real Madrid')]
RM_topWages = pd.DataFrame(real_madrid, columns= ['short_name','wage_eur'])
# print(RM_topWages.head(5, 'wage_eur'))
# print(RM_topWages.nlargest(5, 'wage_eur'))

# Question 16: Show shooting records of top 5 players of 'Real Madrid' team.
# print('\n'"###Top 5 RM shooters###")
RM_topShooters = pd.DataFrame(real_madrid, columns= ['short_name','shooting'])
# print(RM_topShooters.head(5, 'shooting'))
# print(RM_topShooters.nlargest(5, 'shooting'))


# Question 17: Show defending records of top 5 players of 'Real Madrid' team.
# print('\n'"###Top 5 RM defenders###")
RM_topDefenders = pd.DataFrame(real_madrid, columns= ['short_name','defending'])
# print(RM_topDefenders.head(5, 'defending'))
# print(RM_topDefenders.nlargest(5, 'defending'))


# Question 18: Show nationality records of top 5 players of 'Real Madrid' team.
print('\n'"###Top 5 RM Nationaly###")
RM_topNationality = pd.DataFrame(real_madrid, columns= ['short_name','nationality'])
print(RM_topNationality.head(5))
