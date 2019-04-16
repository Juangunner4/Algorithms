# Seven Wonders is a card drafting game in which players build structures to earn points. The player who ends with the most points wins. One winning strategy is to focus on building scientific structures. There are three types of scientific structure cards: Tablet (‘T’), Compass (‘C’), and Gear (‘G’). For each type of cards, a player earns a number of points that is equal to the squared number of that type of cards played. Additionally, for each set of three different scientific cards, a player scores 7 points.
# For example, if a player plays 3 Tablet cards, 2 Compass cards and 1 Gear card, she gets 32+22+12+7=21 points.
#
# It might be tedious to calculate how many scientific points a player gets by the end of each game. Therefore, you are here to help write a program for the calculation to save everyone’s time.

import sys
given_input = sys.stdin.read()

def seven(a):
    T = a.count('T')
    G = a.count('G')
    C = a.count('C')
    sets = 7*min(T, G, C)
    score = sets + T**2 + C**2 + G**2
    print(score)
seven(given_input)
