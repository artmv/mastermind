allcolors = ['black', 'blue', 'brown', 'green', 'orange', 'red', 'white', 'yellow']

import re
from itertools import product
perm11 = list(product(allcolors, repeat = 4))

# guess 1
colors1 = ('black', 'black', 'blue', 'blue')
print('-'*30)
print("guess #1: ", end=', '.join(colors1))
print()
print("is it right? (yes/no): ")
answer1 = input (" > ")
if re.match('[y, Y]', answer1):
    print("A N S W E R: ", end=', '.join(colors1))
    exit()
print("how many WHITE pegs? (correct colors at incorrect slots): ")
white1 = input (" > ")
while (int(white1) < 0 or int(white1) > 4):
    print("input error!")
    print("how many WHITE pegs? (correct colors at incorrect slots): ")
    white1 = input (" > ")
print("how many BLACK pegs? (correct colors at correct slots): ")
black1 = input (" > ")
while (int(black1) < 0 or int(black1) > 3):
    print("input error!")
    print("how many BLACK pegs? (correct colors at correct slots): ")
    black1 = input (" > ")
score1 = int(white1), int(black1)

perm12 = []
perm13 = []
perm14 = []

for i in perm11:
    if colors1[0] in i and colors1[0] != i[0]:
        i = i + tuple('w')
    if colors1[0] in i and colors1[0] == i[0]:
        i = i + tuple('b')
    if colors1[1] in i and colors1[1] != i[1]:
        i = i + tuple('w')
    if colors1[1] in i and colors1[1] == i[1]:
        i = i + tuple('b')
    if colors1[2] in i and colors1[2] != i[2]:
        i = i + tuple('w')
    if colors1[2] in i and colors1[2] == i[2]:
        i = i + tuple('b')
    if colors1[3] in i and colors1[3] != i[3]:
        i = i + tuple('w')
    if colors1[3] in i and colors1[3] == i[3]:
        i = i + tuple('b')
    perm12.append(i)
for i in perm12:
    if i.count('w') == score1[0] and i.count('b') == score1[1]:
        perm13.append(i)
for i in perm13:
    perm14.append(i[0:4])


# guess 2
colors2 = perm14[0]
print('-'*30)
print("guess #2: ", end=', '.join(colors2))
print()
print("is it right? (yes/no): ")
answer2 = input (" > ")
if re.match('[y, Y]', answer2):
    print("A N S W E R: ", end=', '.join(colors2))
    exit()
print("how many WHITE pegs? (correct colors at incorrect slots): ")
white2 = input (" > ")
while (int(white2) < 0 or int(white2) > 4):
    print("input error!")
    print("how many WHITE pegs? (correct colors at incorrect slots): ")
    white2 = input (" > ")
print("how many BLACK pegs? (correct colors at correct slots): ")
black2 = input (" > ")
while (int(black2) < 0 or int(black2) > 3):
    print("input error!")
    print("how many BLACK pegs? (correct colors at correct slots): ")
    black2 = input (" > ")
score2 = int(white2), int(black2)

perm21 = []
perm22 = []
perm23 = []

for i in perm14:
    if colors2[0] in i and colors2[0] != i[0]:
        i = i + tuple('w')
    if colors2[0] in i and colors2[0] == i[0]:
        i = i + tuple('b')
    if colors2[1] in i and colors2[1] != i[1]:
        i = i + tuple('w')
    if colors2[1] in i and colors2[1] == i[1]:
        i = i + tuple('b')
    if colors2[2] in i and colors2[2] != i[2]:
        i = i + tuple('w')
    if colors2[2] in i and colors2[2] == i[2]:
        i = i + tuple('b')
    if colors2[3] in i and colors2[3] != i[3]:
        i = i + tuple('w')
    if colors2[3] in i and colors2[3] == i[3]:
        i = i + tuple('b')
    perm21.append(i)
for i in perm21:
    if i.count('w') == score2[0] and i.count('b') == score2[1]:
        perm22.append(i)
for i in perm22:
    perm23.append(i[0:4])


# guess 3
colors3 = perm23[0]
print('-'*30)
print("guess #3: ", end=', '.join(colors3))
print()
print("is it right? (yes/no): ")
answer3 = input (" > ")
if re.match('[y, Y]', answer3):
    print("A N S W E R: ", end=', '.join(colors3))
    exit()
print("how many WHITE pegs? (correct colors at incorrect slots): ")
white3 = input (" > ")
while (int(white3) < 0 or int(white3) > 4):
    print("input error!")
    print("how many WHITE pegs? (correct colors at incorrect slots): ")
    white3 = input (" > ")
print("how many BLACK pegs? (correct colors at correct slots): ")
black3 = input (" > ")
while (int(black3) < 0 or int(black3) > 3):
    print("input error!")
    print("how many BLACK pegs? (correct colors at correct slots): ")
    black3 = input (" > ")
score3 = int(white3), int(black3)

perm31 = []
perm32 = []
perm33 = []

for i in perm23:
    if colors3[0] in i and colors3[0] != i[0]:
        i = i + tuple('w')
    if colors3[0] in i and colors3[0] == i[0]:
        i = i + tuple('b')
    if colors3[1] in i and colors3[1] != i[1]:
        i = i + tuple('w')
    if colors3[1] in i and colors3[1] == i[1]:
        i = i + tuple('b')
    if colors3[2] in i and colors3[2] != i[2]:
        i = i + tuple('w')
    if colors3[2] in i and colors3[2] == i[2]:
        i = i + tuple('b')
    if colors3[3] in i and colors3[3] != i[3]:
        i = i + tuple('w')
    if colors3[3] in i and colors3[3] == i[3]:
        i = i + tuple('b')
    perm31.append(i)
for i in perm31:
    if i.count('w') == score3[0] and i.count('b') == score3[1]:
        perm32.append(i)
for i in perm32:
    perm33.append(i[0:4])


# guess 4
colors4 = perm33[0]
print('-'*30)
print("guess #4: ", end=', '.join(colors4))
print()
print("is it right? (yes/no): ")
answer4 = input (" > ")
if re.match('[y, Y]', answer4):
    print("A N S W E R: ", end=', '.join(colors4))
    exit()
print("how many WHITE pegs? (correct colors at incorrect slots): ")
white4 = input (" > ")
while (int(white4) < 0 or int(white4) > 4):
    print("input error!")
    print("how many WHITE pegs? (correct colors at incorrect slots): ")
    white4 = input (" > ")
print("how many BLACK pegs? (correct colors at correct slots): ")
black4 = input (" > ")
while (int(black4) < 0 or int(black4) > 3):
    print("input error!")
    print("how many BLACK pegs? (correct colors at correct slots): ")
    black4 = input (" > ")
score4 = int(white4), int(black4)

perm41 = []
perm42 = []
perm43 = []

for i in perm33:
    if colors4[0] in i and colors4[0] != i[0]:
        i = i + tuple('w')
    if colors4[0] in i and colors4[0] == i[0]:
        i = i + tuple('b')
    if colors4[1] in i and colors4[1] != i[1]:
        i = i + tuple('w')
    if colors4[1] in i and colors4[1] == i[1]:
        i = i + tuple('b')
    if colors4[2] in i and colors4[2] != i[2]:
        i = i + tuple('w')
    if colors4[2] in i and colors4[2] == i[2]:
        i = i + tuple('b')
    if colors4[3] in i and colors4[3] != i[3]:
        i = i + tuple('w')
    if colors4[3] in i and colors4[3] == i[3]:
        i = i + tuple('b')
    perm41.append(i)
for i in perm41:
    if i.count('w') == score4[0] and i.count('b') == score4[1]:
        perm42.append(i)
for i in perm42:
    perm43.append(i[0:4])


# guess 5
colors5 = perm43[0]
print('-'*30)
print("guess #5: ", end=', '.join(colors5))
print()
print("is it right? (yes/no): ")
answer5 = input (" > ")
if re.match('[y, Y]', answer5):
    print("A N S W E R: ", end=', '.join(colors5))
    exit()
print("how many WHITE pegs? (correct colors at incorrect slots): ")
white5 = input (" > ")
while (int(white5) < 0 or int(white5) > 4):
    print("input error!")
    print("how many WHITE pegs? (correct colors at incorrect slots): ")
    white5 = input (" > ")
print("how many BLACK pegs? (correct colors at correct slots): ")
black5 = input (" > ")
while (int(black5) < 0 or int(black5) > 3):
    print("input error!")
    print("how many BLACK pegs? (correct colors at correct slots): ")
    black5 = input (" > ")
score5 = int(white5), int(black5)

perm51 = []
perm52 = []
perm53 = []

for i in perm43:
    if colors5[0] in i and colors5[0] != i[0]:
        i = i + tuple('w')
    if colors5[0] in i and colors5[0] == i[0]:
        i = i + tuple('b')
    if colors5[1] in i and colors5[1] != i[1]:
        i = i + tuple('w')
    if colors5[1] in i and colors5[1] == i[1]:
        i = i + tuple('b')
    if colors5[2] in i and colors5[2] != i[2]:
        i = i + tuple('w')
    if colors5[2] in i and colors5[2] == i[2]:
        i = i + tuple('b')
    if colors5[3] in i and colors5[3] != i[3]:
        i = i + tuple('w')
    if colors5[3] in i and colors5[3] == i[3]:
        i = i + tuple('b')
    perm51.append(i)
for i in perm51:
    if i.count('w') == score5[0] and i.count('b') == score5[1]:
        perm52.append(i)
for i in perm52:
    perm53.append(i[0:4])


# guess 6
colors6 = perm53[0]
print('-'*30)
print("guess #6: ", end=', '.join(colors6))
print()
print("is it right? (yes/no): ")
answer6 = input (" > ")
if re.match('[y, Y]', answer6):
    print("A N S W E R: ", end=', '.join(colors6))
    exit()
print("how many WHITE pegs? (correct colors at incorrect slots): ")
white6 = input (" > ")
while (int(white6) < 0 or int(white6) > 4):
    print("input error!")
    print("how many WHITE pegs? (correct colors at incorrect slots): ")
    white6 = input (" > ")
print("how many BLACK pegs? (correct colors at correct slots): ")
black6 = input (" > ")
while (int(black6) < 0 or int(black6) > 3):
    print("input error!")
    print("how many BLACK pegs? (correct colors at correct slots): ")
    black6 = input (" > ")
score6 = int(white6), int(black6)

perm61 = []
perm62 = []
perm63 = []

for i in perm53:
    if colors6[0] in i and colors6[0] != i[0]:
        i = i + tuple('w')
    if colors6[0] in i and colors6[0] == i[0]:
        i = i + tuple('b')
    if colors6[1] in i and colors6[1] != i[1]:
        i = i + tuple('w')
    if colors6[1] in i and colors6[1] == i[1]:
        i = i + tuple('b')
    if colors6[2] in i and colors6[2] != i[2]:
        i = i + tuple('w')
    if colors6[2] in i and colors6[2] == i[2]:
        i = i + tuple('b')
    if colors6[3] in i and colors6[3] != i[3]:
        i = i + tuple('w')
    if colors6[3] in i and colors6[3] == i[3]:
        i = i + tuple('b')
    perm61.append(i)
for i in perm61:
    if i.count('w') == score6[0] and i.count('b') == score6[1]:
        perm62.append(i)
for i in perm62:
    perm63.append(i[0:4])

# guess 7
colors7 = perm63[0]
print('-'*30)
print("guess #7: ", end=', '.join(colors7))
print()
print("is it right? (yes/no): ")
answer7 = input (" > ")
if re.match('[y, Y]', answer7):
    print("A N S W E R: ", end=', '.join(colors7))
    exit()
print("how many WHITE pegs? (correct colors at incorrect slots): ")
white7 = input (" > ")
while (int(white7) < 0 or int(white7) > 4):
    print("input error!")
    print("how many WHITE pegs? (correct colors at incorrect slots): ")
    white7 = input (" > ")
print("how many BLACK pegs? (correct colors at correct slots): ")
black7 = input (" > ")
while (int(black7) < 0 or int(black7) > 3):
    print("input error!")
    print("how many BLACK pegs? (correct colors at correct slots): ")
    black7 = input (" > ")
score7 = int(white7), int(black7)

perm71 = []
perm72 = []
perm73 = []

for i in perm63:
    if colors7[0] in i and colors7[0] != i[0]:
        i = i + tuple('w')
    if colors7[0] in i and colors7[0] == i[0]:
        i = i + tuple('b')
    if colors7[1] in i and colors7[1] != i[1]:
        i = i + tuple('w')
    if colors7[1] in i and colors7[1] == i[1]:
        i = i + tuple('b')
    if colors7[2] in i and colors7[2] != i[2]:
        i = i + tuple('w')
    if colors7[2] in i and colors7[2] == i[2]:
        i = i + tuple('b')
    if colors7[3] in i and colors7[3] != i[3]:
        i = i + tuple('w')
    if colors7[3] in i and colors7[3] == i[3]:
        i = i + tuple('b')
    perm71.append(i)
for i in perm71:
    if i.count('w') == score7[0] and i.count('b') == score7[1]:
        perm72.append(i)
for i in perm72:
    perm73.append(i[0:4])

# guess 8
colors8 = perm73[0]
print('-'*30)
print("guess #8: ", end=', '.join(colors8))
print()
print("is it right? (yes/no): ")
answer8 = input (" > ")
if re.match('[y, Y]', answer8):
    print("A N S W E R: ", end=', '.join(colors8))
    exit()
print("how many WHITE pegs? (correct colors at incorrect slots): ")
white8 = input (" > ")
while (int(white8) < 0 or int(white8) > 4):
    print("input error!")
    print("how many WHITE pegs? (correct colors at incorrect slots): ")
    white8 = input (" > ")
print("how many BLACK pegs? (correct colors at correct slots): ")
black8 = input (" > ")
while (int(black8) < 0 or int(black8) > 3):
    print("input error!")
    print("how many BLACK pegs? (correct colors at correct slots): ")
    black8 = input (" > ")
score8 = int(white8), int(black8)

perm81 = []
perm82 = []
perm83 = []

for i in perm73:
    if colors8[0] in i and colors8[0] != i[0]:
        i = i + tuple('w')
    if colors8[0] in i and colors8[0] == i[0]:
        i = i + tuple('b')
    if colors8[1] in i and colors8[1] != i[1]:
        i = i + tuple('w')
    if colors8[1] in i and colors8[1] == i[1]:
        i = i + tuple('b')
    if colors8[2] in i and colors8[2] != i[2]:
        i = i + tuple('w')
    if colors8[2] in i and colors8[2] == i[2]:
        i = i + tuple('b')
    if colors8[3] in i and colors8[3] != i[3]:
        i = i + tuple('w')
    if colors8[3] in i and colors8[3] == i[3]:
        i = i + tuple('b')
    perm81.append(i)
for i in perm81:
    if i.count('w') == score8[0] and i.count('b') == score8[1]:
        perm82.append(i)
for i in perm82:
    perm83.append(i[0:4])
