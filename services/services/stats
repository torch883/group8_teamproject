def get_leaderboard(sessions):
    totals = {}
    for session in sessions:
        name = session["player"]
        score = session["score"]
        if name in totals:
            totals[name] = totals[name] + score
        else:
            totals[name] = score

    leaderboard = []
    for name in totals:
        leaderboard.append((name, totals[name]))

    for i in range(len(leaderboard)):
        for j in range(i + 1, len(leaderboard)):
            if leaderboard[i][1] < leaderboard[j][1]:
                leaderboard[i], leaderboard[j] = leaderboard[j], leaderboard[i]

    return leaderboard
