"""
    Run in terminal as follows: python3 guild_gp.py > filename.txt
    Remember to set environment variables (swgoh api username and password)
"""

from csv import reader
from os import environ
from tabulate import tabulate

from api_swgoh_help import api_swgoh_help, settings


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
players = client.fetchPlayers(allycodes)

guild_gps = []

for player in players:
    p_name = player['name']
    p_gp = player['stats'][0]['value']
    p_cgp = player['stats'][1]['value']
    p_sgp = player['stats'][2]['value']

    guild_gps.append([p_name, p_cgp, p_sgp, p_gp])

print(tabulate(guild_gps, headers=['Player name', 'Character GP', 'Ship GP', 'Total GP']))
