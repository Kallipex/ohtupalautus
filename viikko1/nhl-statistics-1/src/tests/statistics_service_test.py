import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")

        player = self.stats.search("NonExistent")
        self.assertIsNone(player)

    def test_team(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertTrue(all(player.team == "EDM" for player in edm_players))

        pit_players = self.stats.team("PIT")
        self.assertEqual(len(pit_players), 1)
        self.assertTrue(all(player.team == "PIT" for player in pit_players))

        no_team_players = self.stats.team("NON")
        self.assertEqual(len(no_team_players), 0)

    def test_top(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")