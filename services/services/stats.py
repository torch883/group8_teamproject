def get_leaderboard(sessions):
    totals = {}
    for session in sessions:
        name = session["player"]
        score = session["score"]
        if name in totals:
            totals[name] = totals[name] + score
        else:
            totals[name] = score

    leaderboard = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return leaderboard


def get_average_scores(sessions):
    players = {}
    for session in sessions:
        name = session["player"]
        if name not in players:
            players[name] = []
        players[name].append(session["score"])

    averages = {}
    for name in players:
        averages[name] = sum(players[name]) / len(players[name])

    return averages
