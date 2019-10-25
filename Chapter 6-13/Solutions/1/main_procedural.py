"""
Robust (procedural) solution for 6.1/13.1
"""
import players as p
import os
import json
from helpers import read_positive_float, read_positive_integer



def read_players():
    players = []
    read = input("Do you wish to load the contents of 'players.json'? (Y/N) ").upper()
    if read != "N" or read != "NO":
        if os.path.isfile("players.json"):
            with open("players.json", "r") as playersfile:
                players = json.loads(playersfile.read())  # load the data...
        else:
            print("'players.json' was not found...")
    for i in range(len(players)):
        if "points" in players[i].keys():  # implies BasketballPlayer
            players[i] = p.BasketballPlayer(players[i]["first_name"],
                                        players[i]["last_name"],
                                        players[i]["height_cm"],
                                        players[i]["weight_kg"],
                                        players[i]["points"],
                                        players[i]["rebounds"],
                                        players[i]["assists"])
        elif "goals" in players[i].keys():  # implies FootballPlayer
            players[i] = p.FootballPlayer(players[i]["first_name"],
                                        players[i]["last_name"],
                                        players[i]["height_cm"],
                                        players[i]["weight_kg"],
                                        players[i]["goals"],
                                        players[i]["yc"],
                                        players[i]["rc"])
        else:  # implies base class
            players[i] = p.Player(players[i]["first_name"],
                               players[i]["last_name"],
                               players[i]["height_cm"],
                               players[i]["weight_kg"])
    return players


def print_players(players):
    print("Current database of players:")
    counter = 1
    for player in players:
        print(f"{counter}: {player}")
        counter += 1


def add_player(players):
    print("0: Player (base class)")
    print("1: BasketballPlayer")
    print("2: FootballPlayer")
    choice = input("What kind of player do you wish to add? (enter corresponding number) ")
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    height_cm = read_positive_float("Enter a height in cm: ")
    weight_kg = read_positive_float("Enter a weight in kg: ")
    if choice == "0":
        players.append(p.Player(first_name, last_name, height_cm, weight_kg))
    elif choice == "1":
        points = read_positive_integer("Enter a number of points: ")
        rebounds = read_positive_integer("Enter a number of rebounds: ")
        assists = read_positive_integer("Enter a number of assists: ")
        players.append(p.BasketballPlayer(first_name, last_name, height_cm, weight_kg, points, rebounds, assists))
    elif choice == "2":
        goals = read_positive_integer("Enter a number of goals: ")
        yc = read_positive_integer("Enter a number of yellow cards: ")
        rc = read_positive_integer("Enter a number of red cards: ")
        players.append(p.FootballPlayer(first_name, last_name, height_cm, weight_kg, goals, yc, rc))


def save_players(players):
    dump = []
    for player in players:
        dump.append(player.__dict__)
    with open("players.json", "w") as playersfile:
        json.dump(dump, playersfile, indent=4)


def main():
    print("Welcome to our player-manager...")
    players = read_players()
    while True:
        choice = input("Do you wish to see the current database of players? (Y/N) ").upper()
        if choice == "Y" or choice == "YES":
            print_players(players)
        choice = input("Do you wish to add a player? (Y/N) ").upper()
        if choice != "N" and choice != "NO":
            add_player(players)
        choice = input("Are you done adding players? (Y/N) ").upper()
        if choice == "Y" or choice == "YES":
            break
    print_players(players)
    choice = input("Do you wish to save the current database? (Y/N) ").upper()
    if choice == "Y" or choice == "YES":
        save_players(players)


if __name__ == "__main__":
    main()
