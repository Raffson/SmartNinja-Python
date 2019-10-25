"""
Robust (OOP) solution for 6.1
"""
from player_manager import PlayerManager


def main():
    pm = PlayerManager()  # player manager
    print("Welcome to our player-manager...")
    pm.read_players()
    while True:
        choice = input("Do you wish to see the current database of players? (Y/N) ").upper()
        if choice == "Y" or choice == "YES":
            pm.print_players()
        choice = input("Do you wish to add a player? (Y/N) ").upper()
        if choice != "N" and choice != "NO":
            pm.add_player()
        choice = input("Are you done adding players? (Y/N) ").upper()
        if choice == "Y" or choice == "YES":
            break
    pm.print_players()
    choice = input("Do you wish to save the current database? (Y/N) ").upper()
    if choice == "Y" or choice == "YES":
        pm.save_players()


if __name__ == "__main__":
    main()
