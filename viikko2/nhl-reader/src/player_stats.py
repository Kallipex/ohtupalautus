from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self._reader = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player in self._reader:
            if player.nationality == nationality:
                players.append(player)

        players_sorted = sorted(players, key=lambda x: x.points, reverse=True)

        return players_sorted
