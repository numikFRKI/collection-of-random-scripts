#i use this to determine what rick and morty episode i will watch next but really it can be applied to any show i GUESS.

import random

good_season_six_episodes = [4, 5, 8]

def randomize():
    s = random.randint(1,9)
    if s == 1: 
        e = random.randint(1,11)
    elif s >= 2:
        e = random.randint(1,10)
    print(f"Season {s} Episode {e}")
    if s == 6 and e not in good_season_six_episodes:
        print("fuck naw")
        s = random.randint(1,9)
        if s == 1: 
            e = random.randint(1,11)
        elif s >= 2:
            e = random.randint(1,10)
        print(f"Season {s} Episode {e}")

randomize()