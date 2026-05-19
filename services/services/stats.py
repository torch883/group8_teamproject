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


def get_best_performance(sessions):
    if len(sessions) == 0:
        return None

    best = sessions[0]
    for session in sessions:
        if session["score"] > best["score"]:
            best = session

    return best


def get_daily_best(sessions):
    daily = {}
    for session in sessions:
        date = session["date"]
        score = session["score"]
        name = session["player"]

        if date not in daily:
            daily[date] = {"player": name, "score": score}
        else:
            if score > daily[date]["score"]:
                daily[date] = {"player": name, "score": score}

    return daily
