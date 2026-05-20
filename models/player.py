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
class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_scores(self):
        return self.scores

    def __str__(self):
        return f"Player: {self.name}"


class GameSession:
    def __init__(self, player_name, score, date):
        self.player_name = player_name
        self.score = score
        self.date = date
class BaseEntity:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class Player(BaseEntity):
    def __init__(self, name):
        super().__init__(name)
        self._scores = []

    def add_score(self, score):
        self._scores.append(score)

    def get_scores(self):
        return self._scores

    def __str__(self):
        return f"Player: {self.name}, games played: {len(self._scores)}"


class GameSession(BaseEntity):
    def __init__(self, player_name, score, date):
        super().__init__(player_name)
        self.score = score
        self.date = date

    def to_dict(self):
        return {
            "player": self.name,
            "score": self.score,
            "date": self.date
        }

    def __str__(self):
        return f"{self.name} scored {self.score} on {self.date}"
    def __str__(self):
        return f"{self.player_name} - {self.score} - {self.date}"
