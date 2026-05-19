import unittest
from services.services.stats import get_leaderboard, get_average_scores, get_best_performance

class TestStats(unittest.TestCase):

    def setUp(self):
        self.sessions = [
            {"player": "Alice", "score": 120, "date": "2026-01-01"},
            {"player": "Bob", "score": 150, "date": "2026-01-01"},
            {"player": "Alice", "score": 180, "date": "2026-01-02"}
        ]

    def test_leaderboard(self):
        result = get_leaderboard(self.sessions)
        self.assertEqual(result[0][0], "Alice")

    def test_average(self):
        result = get_average_scores(self.sessions)
        self.assertEqual(result["Alice"], 150.0)

    def test_best(self):
        result = get_best_performance(self.sessions)
        self.assertEqual(result["player"], "Alice")

if __name__ == "__main__":
    unittest.main()