import os
from random import randint

first_row_coin_pos1 = randint(0,24)
first_row_coin_pos2 = randint(0,20)
second_row_coin_pos1 = randint(0,27)
second_row_coin_pos2 = randint()
second_row_coin_pos3 = randint()
os.system('printf "\033c"')
for i in range(0,29):
    if i == 0:
        print "X" * 80,
    elif i == 1:
        print "X" + " " * 20 + "X" + " " * 2+ "Q" + " " * 54 + "X",
    elif i == 2:
        print "X" + " " * 20 + "X" * 7 + "H" + "X" * 2 + " " * 48 + "X",
    elif i == 3:
        print "X" + " " * 27 + "H" + " " * 50 + "X",
    elif i==4:
        print "X" + "D" + " " * first_row_coin_pos1 + "C" + " " * (25 - first_row_coin_pos1) + "H" + " " * first_row_coin_pos2 + "C" +  " " * (20-first_row_coin_pos2) + " " * 29 + "X",
    elif i == 5:
        print "X" * 15 + "H" + "X" * 12 + "H" + "X" * 15 + "H" + "X" * 5 + " " * 29 + "X",
    elif i == 6:
        print "X" + " " * 14 + "H" + " " * 28 + "H" + " " * 34 + "X",
    elif i == 7:
        print "X" + " " * 43 + "H" + " " * 34 + "X",
    elif i == 8:
        print "X" + " " * 14 + "H" + " " * second_row_coin_pos1 + "C" + " " * (27 - second_row_coin_pos1) +  "H" + " " * 34 + "X",
    elif i == 28:
        print "X" * 80,
    else:
        print "X" + " " * 78 + "X",
    print
os.system('sleep 0.05')


