"""Run in terminal as follows: python3 tw_banners.py > filename.txt"""

import json, requests

from tabulate import tabulate

# Unseen swgoh.gg guild id is 1154. Change below value to test on other guilds
guild_id = 1154

banner_goal = 200

# Arbitrary GP to reach banner goal
t_gp = 2800000

def main():
    # Submit a GET request to api for guild info
    res = requests.get(f"https://swgoh.gg/api/guild/{guild_id}/")

    # Check that everything worked
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')

    # Convert response to JSON and format nicely (for dev purposes)
    json_data = json.dumps(res.json(), indent=4, separators=(',', ': '))

    tw_goals = []

    # Print output (ideally piped to a file via command line)
    for player in json.loads(json_data)['players']:
        p_name = player['data']['name']
        p_gp = player['data']['galactic_power']

        p_banner_goal = (p_gp / t_gp) * banner_goal

        tw_goals.append([p_name, round(p_banner_goal)])

    tw_goals.sort(key=lambda x: x[0])

    print(tabulate(tw_goals, headers=['Player name', 'Banner goal']))

if __name__ == '__main__':
    main()
