from services.file_handler import load_data, save_data
from services.services.stats import get_leaderboard, get_average_scores, get_best_performance, get_daily_best, filter_by_player
from models.player import GameSession
from utils.helpers import get_today, is_valid_date, is_valid_score

DATA_FILE = "data/games.json"


def show_menu():
    print("\n=== Game Statistics Analyzer ===")
    print("1. Show leaderboard")
    print("2. Show average scores")
    print("3. Show best performance")
    print("4. Show daily best")
    print("5. Add new session")
    print("6. Filter by player")
    print("0. Exit")


def show_leaderboard(sessions):
    leaderboard = get_leaderboard(sessions)
    if len(leaderboard) == 0:
        print("No data")
        return
    print("\n--- Leaderboard ---")
    place = 1
    for name, total in leaderboard:
        print(f"{place}. {name} - {total} points")
        place += 1


def show_averages(sessions):
    averages = get_average_scores(sessions)
    if len(averages) == 0:
        print("No data")
        return
    print("\n--- Average Scores ---")
    for name in averages:
        print(f"{name}: {averages[name]:.1f}")


def show_best(sessions):
    best = get_best_performance(sessions)
    if best is None:
        print("No data")
        return
    print("\n--- Best Performance ---")
    print(f"{best['player']} - {best['score']} points on {best['date']}")


def show_daily_best(sessions):
    daily = get_daily_best(sessions)
    if len(daily) == 0:
        print("No data")
        return
    print("\n--- Daily Best ---")
    for date in daily:
        entry = daily[date]
        print(f"{date}: {entry['player']} - {entry['score']} points")


def add_session(sessions):
    name = input("Player name: ")
    if name.strip() == "":
        print("Name cannot be empty")
        return

    score_input = input("Score: ")
    if not is_valid_score(score_input):
        print("Score must be a positive number")
        return

    date_input = input(f"Date (YYYY-MM-DD), press Enter for today ({get_today()}): ")
    if date_input.strip() == "":
        date_input = get_today()

    if not is_valid_date(date_input):
        print("Invalid date format")
        return

    session = GameSession(name, int(score_input), date_input)
    sessions.append(session.to_dict())
    save_data(DATA_FILE, sessions)
    print("Session added!")


def show_player_stats(sessions):
    name = input("Enter player name: ")
    result = filter_by_player(sessions, name)
    if len(result) == 0:
        print("Player not found")
        return
    print(f"\n--- Stats for {name} ---")
    for s in result:
        print(f"  {s['date']}: {s['score']} points")


def main():
    sessions = load_data(DATA_FILE)

    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            show_leaderboard(sessions)
        elif choice == "2":
            show_averages(sessions)
        elif choice == "3":
            show_best(sessions)
        elif choice == "4":
            show_daily_best(sessions)
        elif choice == "5":
            add_session(sessions)
        elif choice == "6":
            show_player_stats(sessions)
        else:
            print("Wrong option, try again")


main()