import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == 'FIN':
            players.append(player)

    players_sorted = sorted(players, key=lambda x: x.points, reverse=True)

    print("Players from FIN:\n")

    for player in players_sorted:
        print(player)

if __name__ == "__main__":
    main()
