"""Run in terminal as follows: python3 guild_gp.py > filename.txt"""

import json, requests

from tabulate import tabulate

# Unseen swgoh.gg guild id is 1154. Change below value to test on other guilds
guild_id = 1154


def main():
    # Submit a GET request to api for guild info
    res = requests.get(f"https://swgoh.gg/api/guild/{guild_id}/")

    # Check that everything worked
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')

    # Convert response to JSON and format nicely (for dev purposes)
    json_data = json.dumps(res.json(), indent=4, separators=(',', ': '))

    guild_gps = []

    # Print output (ideally piped to a file via command line)
    for player in json.loads(json_data)['players']:
        p_name = player['data']['name']
        p_gp = player['data']['galactic_power']
        p_cgp = player['data']['character_galactic_power']
        p_sgp = player['data']['ship_galactic_power']

        guild_gps.append([p_name, p_cgp, p_sgp, p_gp])

    guild_gps.sort(key=lambda x: x[0])

    print(tabulate(guild_gps, headers=['Player name', 'Character GP', 'Ship GP', 'Total GP']))

if __name__ == '__main__':
    main()
