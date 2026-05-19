from services.file_handler import load_data, save_data
from services.services.stats import get_leaderboard, get_average_scores, get_best_performance, get_daily_best

DATA_FILE = "data/games.json"

def show_menu():
    print("=== Game Statistics Analyzer ===")
    print("1. Show leaderboard")
    print("2. Show average scores")
    print("3. Show best performance")
    print("4. Show daily best")
    print("5. Add new session")
    print("6. Filter by player")
    print("0. Exit")

def main():
    sessions = load_data(DATA_FILE)

    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "0":
            break
        elif choice == "1":
            print("Leaderboard:", get_leaderboard(sessions))
        elif choice == "2":
            print("Averages:", get_average_scores(sessions))
        elif choice == "3":
            print("Best:", get_best_performance(sessions))
        elif choice == "4":
            print("Daily best:", get_daily_best(sessions))
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        else:
            print("Wrong option")

main()