player = {}

def create_player(name, xp, team_name):
    return {
    "name": name,
    "XP": xp,
    "team": team_name
}

def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")

son = create_player("Son", 1000, "Team X")
nico = create_player("Nico", 1500, "Team Blue")

teams = {
    "Team X": [son],
    "Team Blue": [nico]
}

print(teams)