class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_scores(self):
        return self.scores
class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_scores(self):
        return self.scores


class GameSession:
    def __init__(self, player_name, score, date):
        self.player_name = player_name
        self.score = score
        self.date = date
