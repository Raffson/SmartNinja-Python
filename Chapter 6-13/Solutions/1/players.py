"""
Class definitions for players, OOP part of 6.1/13.1
"""


# class definition for 'Player' which is the base class
# each player should have 4 properties:
#  -first_name: player's first name
#  -last_name: player's last name
#  -height_cm: player's height in cm
#  -weight_kg: player's weight in kg
class Player:  # inherits from built-in type 'object' by default
    # constructor for 'Player',
    # takes 4 parameters to be used for initialisation:
    #  -first_name: player's first name, expected type = string
    #  -last_name: player's last name, expected type = string
    #  -height_cm: player's height in cm, expected type = float or int
    #  -weight_kg: player's weight in kg, expected type = float or int
    # raises TypeError if a parameter received a bad type
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        if type(first_name) != str:
            raise TypeError("A string is expected for 'first_name'")
        if type(last_name) != str:
            raise TypeError("A string is expected for 'last_name'")
        if type(height_cm) != float and type(height_cm) != int:
            raise TypeError("A float or int is expected for 'height_cm'")
        if type(weight_kg) != float and type(weight_kg) != int:
            raise TypeError("A float or int is expected for 'height_cm'")
        # once we get here, we know our types are ok...
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    # implement what should happen if str() is called on "this" object
    def __str__(self):
        height = "%.2f" % self.height_cm if type(self.height_cm) == float \
            else self.height_cm
        weight = "%.2f" % self.weight_kg if type(self.weight_kg) == float \
            else self.weight_kg
        return f"{self.first_name} {self.last_name} " \
            f"is {height}cm tall and weighs {weight}kg."

    # simple method to convert "this" player's weight to pounds
    def weight_to_lbs(self):
        return self.weight_kg * 2.20462262


# class definition for 'BasketballPlayer', extended from Player
# thus this class already has first_name, last_name, height_cm and weight_cm
# each BasketballPlayer should have 3 extra properties:
#  -points: number of points scored by the player
#  -rebounds: number of rebounds taken by the player
#  -assists: number of assists made by the player
class BasketballPlayer(Player):
    # constructor for 'BasketballPlayer',
    # takes 7 parameters to be used for initialisation:
    #  -first_name: player's first name, expected type = string
    #  -last_name: player's last name, expected type = string
    #  -height_cm: player's height in cm, expected type = float or int
    #  -weight_kg: player's weight in kg, expected type = float or int
    #  -points: number of points scored by the player, expected type = int
    #  -rebounds: number of rebounds taken by the player, expected type = int
    #  -assists: number of assists made by the player, expected type = int
    # raises TypeError if a parameter received a bad type
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name, last_name, height_cm, weight_kg)  # calls Player.__init__()
        if type(points) != int:
            raise TypeError("An integer is expected for 'points'")
        if type(rebounds) != int:
            raise TypeError("An integer is expected for 'rebounds'")
        if type(assists) != int:
            raise TypeError("An integer is expected for 'assists'")
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def __str__(self):
        common_part = super().__str__()  # calls Player.__str__()
        string = "Basketball player " + common_part + "\n"
        string += f"{self.last_name} scored {self.points} points, " \
            f"caught {self.rebounds} rebounds and made {self.assists} assists."
        return string


# class definition for 'FootballPlayer', extended from Player
# thus this class already has first_name, last_name, height_cm and weight_cm
# each FootballPlayer should have 3 extra properties:
#  -goals: number of goals scored by the player
#  -yc: number of yellow cards received by the player
#  -rc: number of red cards received by the player
class FootballPlayer(Player):
    # constructor for 'FootballPlayer',
    # takes 7 parameters to be used for initialisation:
    #  -first_name: player's first name, expected type = string
    #  -last_name: player's last name, expected type = string
    #  -height_cm: player's height in cm, expected type = float or int
    #  -weight_kg: player's weight in kg, expected type = float or int
    #  -goals: number of goals scored by the player, expected type = int
    #  -yc: number of yellow cards received the player, expected type = int
    #  -rc: number of red cards received by the player, expected type = int
    # raises TypeError if a parameter received a bad type
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yc, rc):
        super().__init__(first_name, last_name, height_cm, weight_kg)  # calls Player.__init__()
        if type(goals) != int:
            raise TypeError("An integer is expected for 'goals'")
        if type(yc) != int:
            raise TypeError("An integer is expected for 'yc'")
        if type(rc) != int:
            raise TypeError("An integer is expected for 'rc'")
        self.goals = goals
        self.yc = yc
        self.rc = rc

    def __str__(self):
        common_part = super().__str__()  # calls Player.__str__()
        string = "Football player " + common_part + "\n"
        string += f"{self.last_name} scored {self.goals} goals, " \
            f"received {self.yc} yellow cards and {self.rc} red cards."
        return string


# some basic examples to check the behaviour...
if __name__ == "__main__":
    p = Player("Test", "This", 180, 75)
    print(p)
    print(p.__dict__)
    print("%.2f" % p.weight_to_lbs())
    print(dir(p))
    try:
        p2 = Player("ok", "ok", "badType", "badType")
    except TypeError as e:
        print(f"TypeError occurred: {e}")
    print("=====================================")
    bp = BasketballPlayer("Kevin", "Durant", 210, 108, 27, 7, 4)
    print(bp)
    try:
        bp2 = BasketballPlayer("Kevin", "Durant", 210, 108, 27.4, 7, 4)
    except TypeError as e:
        print(f"TypeError occurred: {e}")
    print("=====================================")
    fp = FootballPlayer("Lionel", "Messi", 170, 67, 575, 67, 0)
    print(fp)
    try:
        fp2 = FootballPlayer("Lionel", "Messi", 170, 67, 575, 67, "zero")
    except TypeError as e:
        print(f"TypeError occurred: {e}")
