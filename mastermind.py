# Mastermind board game: to find combination of 4 colors (allowing duplicates) of 8.
# 8 ^ 4 = 4096 possible combinations
# code applies algorithm suggested by Donald Knuth
import re
from itertools import product
allcolors = ['black', 'blue', 'brown', 'green', 'orange', 'red', 'white', 'yellow']
# make a list of all possible combinations
perm = list(product(allcolors, repeat = 4))
# make the first try
colors = ('black', 'black', 'blue', 'blue')
# loop until answer is found
j = 1
while True:
    print('-'*40)
    print("try #", j, ": ", end=', '.join(colors))
    print()
# getting user's feedback
    print("is it right? (yes/no): ")
    answer = input (" > ")
    if re.match('[y, Y]', answer):
        print("A N S W E R: ", end=', '.join(colors))
        exit()
    print("how many WHITE pegs? (correct colors at incorrect slots): ")
    white = input (" > ")
    while (int(white) < 0 or int(white) > 4):
        print("input error!")
        print("how many WHITE pegs? (correct colors at incorrect slots): ")
        white = input (" > ")
    print("how many BLACK pegs? (correct colors at correct slots): ")
    black = input (" > ")
    while (int(black) < 0 or int(black) > 3):
        print("input error!")
        print("how many BLACK pegs? (correct colors at correct slots): ")
        black1 = input (" > ")
    score = int(white), int(black)
# marking all combinations according to user's feedback
    perm1 = []
    perm2 = []
    for i in perm:
        if colors[0] in i and colors[0] != i[0]:
            i = i + tuple('w')
        if colors[0] in i and colors[0] == i[0]:
            i = i + tuple('b')
        if colors[1] in i and colors[1] != i[1]:
            i = i + tuple('w')
        if colors[1] in i and colors[1] == i[1]:
            i = i + tuple('b')
        if colors[2] in i and colors[2] != i[2]:
            i = i + tuple('w')
        if colors[2] in i and colors[2] == i[2]:
            i = i + tuple('b')
        if colors[3] in i and colors[3] != i[3]:
            i = i + tuple('w')
        if colors[3] in i and colors[3] == i[3]:
            i = i + tuple('b')
        perm1.append(i)
# clearing the initial list of combination
    perm = []
# scoring combinations
    for i in perm1:
        if i.count('w') == score[0] and i.count('b') == score[1]:
            perm2.append(i)
# making a new list of only suitable combinations
    for i in perm2:
        perm.append(i[0:4])
# new try is the first element in a reduced list of combinations
    colors = perm[0]
    j += 1
