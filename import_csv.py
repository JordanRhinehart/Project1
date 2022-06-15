import csv
import pandas as pd
from pandas import DataFrame, read_csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

###### Task 1: Load the csv file and show top 5 records from it ######

# Define DataFrame variable with the file path
df = pd.read_csv (r'D:\Users\yaima\Documents\Projects\players_20.csv')

# Show top 5 records on the CSV file   
print('\n'"###Top 5 records from CSV File###"'\n')
print(df.head())


###### Task 2: Name of columns ######

print('\n'"###CSV File columns' names###"'\n')

# Get and print the names of all columns on the CSV file
for col in df.columns:
    print(col, end = ", ")


##### Task 3: Number of rows and columns #####
# Define variable to get the number of rows
count_row = df.shape[0]

# Define variable to get the number of columns
count_col = df.shape[1]

print('\n'"###CSV File number of rows and columns###"'\n')

print(f"The number of rows in this dataset are {count_row}"'\n')
print(f"The number of columns in this dataset are {count_col}"'\n')


###### Task 4: Group by number of players and their countries ######

# Group by nationality and count number of players with that nationality
gr = df.groupby(['nationality'])['nationality'].count()

# Print the nationalitiesand their amount of players
print('\n'"### CSV File nationalities and amount of players per nationality ###\n")
print(gr)


###### Task 5: Top 10 countries and their number of players ######

# Print the nationalities with the most players
print('\n'"### Top 10 countries and their number of players ###\n")
print(gr.nlargest(10))


###### Task 6: Top 5 countries and their number of players, try to fill green color in bars ######

# Define countries to group by nationality without setting the column ID as the index and counting by the instances in the short_name column
countries = df.groupby(['nationality'], as_index=False)['short_name'].count()

# Define country_bar to call the top 5 nationalities 
country_bar = countries.nlargest(5,'short_name')

# Print top 5 nationalities 
print('\n'"### Bar-graph of top 5 countries and their number of players with green color bars.###\n")
print(country_bar)

# Create bar-graph of top 5 countries and their number of players
print('\n'"### Bar-graph of top 5 countries and their number of players with green color bars.###\n")

# Code for bar-graph
plt.figure(figsize=(15,6))
plt.bar(country_bar['nationality'],country_bar['short_name'],color='green')
plt.xlabel('Nationality', size = 15)
plt.ylabel('Number of Players', size=15)
plt.title('Players per Country')
plt.show()


###### Task 7: Show top 5 players short name and wages ######

# Define variable to find players' names and their wages
top_wages = pd.DataFrame(df, columns= ['short_name','wage_eur'])

# Print top 5 world players on CSV File
print('\n'"### Top 5 world players on CSV File by short name and wages #####\n")
print(top_wages.head(5))

# Print top 5 paid world players 
print('\n'"### Top 5 paid world players #####\n")
print(top_wages.nlargest(5, 'wage_eur'))


###### Task 8: Show top 5 players getting highest salaries ######

# Define variables for top salaries on the list
top_salaries = top_wages.head(5)

# Define variables for highest salaries on the list
highest_salaries = top_wages.nlargest(5, 'wage_eur')

# Print top 5 salaries on the CSV file
print('\n'"### Top 5 world players getting highest salaries ###\n")
print(top_salaries)

# Print highest 5 salaries
print('\n'"### Top 5 world players getting highest salaries ###\n")
print(highest_salaries)


###### Task 9: Bar plot of top 5 players getting highest salaries ######

# Create a bar-graph for top 5 world players getting highest salaries
print('\n'"### Bar plot of top 5 world players getting highest salaries ###")
print('\n')

# Code to create the bar-graph
plt.figure(figsize=(15,6))
plt.bar(highest_salaries['short_name'],highest_salaries['wage_eur'],color='green')
plt.xlabel('Player Names', size = 15)
plt.ylabel('Players Wages', size=15)
plt.title('Top 5 Wages per Player')
plt.show()


###### Task 10: Show top 10 records of Germany ######

# Define variable to find instances or Germany in nationalities column
Germany = df[df['nationality'].str.contains('Germany')]

# Print first 10 reco9rds that appear on the list
print('\n'"### Top 10 records of Germany ###")
print(Germany.head(10))


###### Task 11: Show top 5 records of Germany players who have maximum height, weight and wages ######

# Define variable to get players' records in terms of 'height_cm', 'weight_kg', and 'wage_eur'
records = df[['short_name', 'height_cm', 'weight_kg', 'wage_eur']]

# Define variable to get only German players' records
german_players = records[df['nationality'].str.contains('Germany')]

# Print all records of top 5 German players in terms of salary
print('\n'"### Full records of top 5 paid German players ###\n")
print(Germany.nlargest(5, ['wage_eur']))
print('\n')

# Print wage, height, and weight records of top 5 German players in terms of salary
print('\n'"### Partial records of top 5 paid German players ###\n")
print(german_players.nlargest(5, ['wage_eur']))
print('\n')

# Print all records of top 5 German players in terms of hight
print('\n'"### Full records of top 5 tallest German players ###\n")
print(Germany.nlargest(5, ['height_cm']))
print('\n')

# Print wage, height, and weight records of top 5 German players in terms of salary
print('\n'"### Partial records of top 5 tallest German players ###\n")
print(german_players.nlargest(5, ['height_cm']))
print('\n')

# Print all records of top 5 German players in terms of weight
print('\n'"### Full records of top 5 heaviest German players ###\n")
print(Germany.nlargest(5, ['weight_kg']))
print('\n')

# Print wage, height, and weight records of top 5 German players in terms of salary
print('\n'"### Partial records of top 5 heaviest German players ###\n")
print(german_players.nlargest(5, ['weight_kg']))
print('\n')


###### Task 12: Show short name and wages of top 5 Germany players ######

# Define variable to get German players' highest salaries and names
German_topWages = pd.DataFrame(Germany, columns= ['short_name','wage_eur'])

# Print top 5 salaries on the CSV file for German players
print('\n'"### Top 5 salaries for German players ###\n")
print(German_topWages.head(5))

# Print top 5 paid German players
print('\n'"### Top 5 paid German players ###\n")
print(German_topWages.nlargest(5, 'wage_eur'))


###### Task 13: Show top 5 players who have great shooting skills among all with short name ######

# Define variable to find top 5 world's shooters
top_shooters = pd.DataFrame(df, columns = ['short_name', 'shooting'])

# Print top 5 records on the shooting column
print('\n'"### Top 5 shooting records on the CSV file ###\n")
print(top_shooters.head(5))

# Print top 5 world's shooters
print('\n'"### Top 5 world players with the greatest shooting skills ###\n")
print(top_shooters.nlargest(5, 'shooting'))


###### Task 14: Show top 5 players records (short name, defending, nationality, and club) that have awesome defending skills ######

# Define variable to find partial records (short name, defending, nationality, and club) with best defending skills
top_defenders = pd.DataFrame(df, columns = ['short_name', 'defending', 'nationality', 'club'])

# print the top 5 world players with the best defending skills
print('\n'"### World's 5 best defenders ###\n")
print(top_defenders.nlargest(5, 'defending'))


###### Task 15: Show wages records of top 5 players of 'Real Madrid' team ######

# Define variable to get the Real Madrid records
real_madrid = df[df['club'].str.contains('Real Madrid')]

# Define variable to get the Real Madrid's highest paid players
RM_topWages = pd.DataFrame(real_madrid, columns= ['short_name','wage_eur'])

# Print Real Madrid' highest paid players
print('\n'"### Real Madrid's 5 highest paid players ###\n")
print(RM_topWages.nlargest(5, 'wage_eur'))


###### Task 16: Show shooting records of top 5 players of 'Real Madrid' team ######

# Define variable to get the Real Madrid's best shooters
RM_topShooters = pd.DataFrame(real_madrid, columns= ['short_name','shooting'])

# Print Real Madrid' top 5 shooters
print('\n'"### Real Madrid's top 5 shooters ###\n")
print(RM_topShooters.nlargest(5, 'shooting'))


###### Task 17: Show defending records of top 5 players of 'Real Madrid' team ######

# Define variable to get the Real Madrid's top defenders
RM_topDefenders = pd.DataFrame(real_madrid, columns= ['short_name','defending'])

# Print Real Madrid's top 5 defenders
print('\n'"### Real Madrid's top 5 defenders ###\n")
print(RM_topDefenders.nlargest(5, 'defending'))


###### Task 18: Show nationality records of top 5 players of 'Real Madrid' team ######

# Define variable to get the nationality of first 5 players on the CSV file under club 'Real Madrid'
RM_topNationality = pd.DataFrame(real_madrid, columns= ['short_name','nationality'])

# Print top 5 records on the CSV file for the 'Real Madrid'
print('\n'"### Top 5 records of appearing on the CSV file for the Real Madrid nationalities ###\n")
print(RM_topNationality.head(5))
