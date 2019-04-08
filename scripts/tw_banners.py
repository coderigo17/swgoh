"""
    Run in terminal as follows: python3 tw_banners.py > filename.txt
    Remember to set environment variables (swgoh api username and password)
"""

from csv import reader
from os import environ
from tabulate import tabulate

from api_swgoh_help import api_swgoh_help, settings

# TW banner goal and Arbitrary GP to reach banner goal
banner_goal = 200
t_gp = 2800000

# Authorization
creds = settings(environ['SWGOH_API_USER'], environ['SWGOH_API_PW'])
client = api_swgoh_help(creds)

# Import guild allycodes from csv file
with open('members.csv', 'r') as f:
  reader = reader(f)
  temp = list(reader)

allycodes = []
for t in temp:
    allycodes.append(int(t[0]))

# API request
players = client.fetchPlayers(allycodes[11:14])

tw_goals = []

for player in players:
    p_name = player['name']
    p_gp = player['stats'][0]['value']

    p_banner_goal = (p_gp / t_gp) * banner_goal

    tw_goals.append([p_name, round(p_banner_goal)])

print(tabulate(tw_goals, headers=['Player name', 'Banner goal']))
