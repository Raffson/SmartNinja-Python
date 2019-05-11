'''
A robust solution for homework 5.2 (12.2)
'''

import casino

def keep_playing():
    ans = input("Do you wish to play a new game? ")
    if ans.upper() == "N" or ans.upper() == "NO":
        return False
    return True


def show_best_scores():
    ans = input("Do you wish to see the best scores before starting? ")
    if ans.upper() == "N" or ans.upper() == "NO":
        return False
    return True

def main():
    while keep_playing():
        if show_best_scores():
            print("Top 3 scores are: ")
            for score in casino.get_score_list("best.txt"):
                print(score)
        casino.play_game()

if __name__ == "__main__":
    main()