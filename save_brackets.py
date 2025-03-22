import re
from bs4 import BeautifulSoup

brackets_directory = 'brackets/2025/'

for bracket in bracket_directory:


    with open(f'brackets/2025/{bracket}', 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse HTML
    soup = BeautifulSoup(content, "html.parser")

    # Find all checked inputs
    matchups = soup.find_all(class_ = "BracketPropositionHeader-pick")

    # Store the results
    selected_teams = []

    for matchup in matchups:
        pick 

        selected_teams.append({
            "team_name": = matchup.text.strip()[5:],
            "bracket": 
        })
