import unittest
from services.services.stats import get_leaderboard, get_average_scores, get_best_performance, filter_by_player

class TestStats(unittest.TestCase):

    def setUp(self):
        self.sessions = [
            {"player": "Alice", "score": 120, "date": "2026-01-01"},
            {"player": "Bob", "score": 150, "date": "2026-01-01"},
            {"player": "Alice", "score": 180, "date": "2026-01-02"}
        ]

    def test_leaderboard_first_place(self):
        result = get_leaderboard(self.sessions)
        self.assertEqual(result[0][0], "Alice")

    def test_leaderboard_empty(self):
        result = get_leaderboard([])
        self.assertEqual(result, [])

    def test_average_alice(self):
        result = get_average_scores(self.sessions)
        self.assertEqual(result["Alice"], 150.0)

    def test_average_bob(self):
        result = get_average_scores(self.sessions)
        self.assertEqual(result["Bob"], 150.0)

    def test_best_performance(self):
        result = get_best_performance(self.sessions)
        self.assertEqual(result["score"], 180)

    def test_best_performance_empty(self):
        result = get_best_performance([])
        self.assertIsNone(result)

    def test_filter_by_player(self):
        result = filter_by_player(self.sessions, "Alice")
        self.assertEqual(len(result), 2)

    def test_filter_no_results(self):
        result = filter_by_player(self.sessions, "Unknown")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()