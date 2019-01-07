import os
import csv

os.chdir(.../...) # Use the path to the set of OOTP csv files

with open('teams.csv', newline='') as csvfile:
	teams = csv.DictReader(csvfile)
	for row in teams:
		print(row['name'], row['nickname'])

with open('players.csv', newline='') as csvfile:
	players = csv.DictReader(csvfile)
	for row in players:
		print(row['first_name'], row['last_name'])



import pandas as pd
import numpy as np

os.chdir(.../...)

teams = pd.read_csv('teams.csv')
teams.loc[0:10,['name','nickname']]

players = pd.read_csv('players.csv')
players.loc[0:10,['first_name','last_name']]

player_teams = pd.merge(players, teams, left_on='team_id', right_on='team_id')
player_teams.loc[0:10,['first_name','last_name','name','nickname']]

player_sort = player_teams.sort_values(by=['last_name'])
print player_sort[['first_name','last_name']]

bat_stats = pd.read_csv('players_career_batting_stats.csv')

player_stats = pd.merge(player_teams, bat_stats,left_on=['player_id','team_id'],right_on=['player_id','team_id'])

player_avg = player_stats[['first_name','last_name','year','name','nickname','h','ab','split_id']]

player_avg = player_avg[(player_avg['split_id'] == 1) & (player_avg['year'] == 1914)]

player_avg['avg']=player_avg['h']/player_avg['ab']

player_avg.loc[ np.isnan(player_avg['avg']), 'avg' ] = 0.0

