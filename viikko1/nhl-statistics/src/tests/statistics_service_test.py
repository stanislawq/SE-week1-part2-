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
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_found(self):
        p = self.stats.search("Kurri")
        self.assertEqual(p.name, "Kurri")

    def test_search_not_found(self):
        p = self.stats.search("Mironov")
        self.assertIsNone(p)

    def test_team_search(self):
        p = self.stats.team("EDM")
        self.assertEqual(len(p), 3)

    def test_top_players(self):
        best = self.stats.top(2)
        self.assertEqual(len(best), 2)
        self.assertEqual(best[0].name, "Gretzky")
        
    def test_player_string_representation(self):
        player = Player("Kurri", "EDM", 37, 53)
        self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")