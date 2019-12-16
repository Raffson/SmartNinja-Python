"""
Robust (OOP) solution for 6.1/13.1
"""
import players as p
import os
import json
from helpers import read_positive_float, read_positive_integer


class PlayerManager:

    def __init__(self, players=[]):
        if type(players) != list:
            print("Bad argument provided: 'players' should be a list, overwriting with empty list...")
            players = []
        self.players = players  # essentially a list of players is all we need...

    def read_players(self):
        players = []
        read = input("Do you wish to load the contents of 'players.json'? (Y/N) ").upper()
        if read != "N" or read != "NO":
            if os.path.isfile("players.json"):
                with open("players.json", "r") as playersfile:
                    players = json.loads(playersfile.read())  # load the data...
            else:
                print("'players.json' was not found...")
        # since we've got a list of dictionaries,
        # we still have to create actual objects...
        for i in range(len(players)):
            if "points" in players[i].keys():  # implies BasketballPlayer
                self.players.append(p.BasketballPlayer(players[i]["first_name"],
                                            players[i]["last_name"],
                                            players[i]["height_cm"],
                                            players[i]["weight_kg"],
                                            players[i]["points"],
                                            players[i]["rebounds"],
                                            players[i]["assists"]) )
            elif "goals" in players[i].keys():  # implies FootballPlayer
                self.players.append(p.FootballPlayer(players[i]["first_name"],
                                            players[i]["last_name"],
                                            players[i]["height_cm"],
                                            players[i]["weight_kg"],
                                            players[i]["goals"],
                                            players[i]["yc"],
                                            players[i]["rc"]) )
            else:  # implies base class
                self.players.append(p.Player(players[i]["first_name"],
                                   players[i]["last_name"],
                                   players[i]["height_cm"],
                                   players[i]["weight_kg"]) )

    def print_players(self):
        print("Current database of players:")
        counter = 1
        for player in self.players:
            print(f"{counter}: {player}")
            counter += 1


    def add_player(self):
        print("0: Player (base class)")
        print("1: BasketballPlayer")
        print("2: FootballPlayer")
        choice = input("What kind of player do you wish to add? (enter corresponding number) ")
        first_name = input("Enter a first name: ")
        last_name = input("Enter a last name: ")
        height_cm = read_positive_float("Enter a height in cm: ")
        weight_kg = read_positive_float("Enter a weight in kg: ")
        if choice == "0":
            self.players.append(p.Player(first_name, last_name, height_cm, weight_kg))
        elif choice == "1":
            points = read_positive_integer("Enter a number of points: ")
            rebounds = read_positive_integer("Enter a number of rebounds: ")
            assists = read_positive_integer("Enter a number of assists: ")
            self.players.append(p.BasketballPlayer(first_name, last_name, height_cm, weight_kg, points, rebounds, assists))
        elif choice == "2":
            goals = read_positive_integer("Enter a number of goals: ")
            yc = read_positive_integer("Enter a number of yellow cards: ")
            rc = read_positive_integer("Enter a number of red cards: ")
            self.players.append(p.FootballPlayer(first_name, last_name, height_cm, weight_kg, goals, yc, rc))


    def save_players(self):
        dump = []
        for player in self.players:
            dump.append(player.__dict__)
        with open("players.json", "w") as playersfile:
            json.dump(dump, playersfile, indent=4)

