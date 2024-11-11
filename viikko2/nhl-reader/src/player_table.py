from player_stats import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

class PlayerTable:
    def __init__(self):
        self.console = Console()

    def looper(self):
        seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
        season = Prompt.ask("Select season", choices=seasons)

        while True:
            nationalities = ["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS",  "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"]
            nationality = Prompt.ask("\nSelect nationality", choices=nationalities)

            self.tabulator(season, nationality)

    def tabulator(self, season, nationality):
        table = Table(title=f"Top scorers of {nationality} season {season}")

        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Team", justify="center", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.points)
            )

        self.console.print(table)
