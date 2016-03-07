import sys
from random import randint

board = [
    ["X" for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    [" " for x in xrange(0, 80)],
    ["X" for x in xrange(0, 80)],
]

for i in xrange(0,30):
    board[i][0] = board[i][79] = "X"

def generateBoard(level):
    if level == 1:
        print len(board[1])
        board[1][15] = "X"
        board[1][18] = "Q"
        for i in xrange(15,25):
            board[2][i] = "X"
        board[2][22] = "H"
        board[3][22] = board[4][22] = "H"
        board[4][1] = "D"
        board[4][randint(2,21)] = "C"
        board[4][22 + randint(1,20)] = "C"
        board[4][32 + randint(1,20)] = "C"
        board[4][42 + randint(1,8)] = "C"
        for i in xrange(1,60):
            board[5][i] = "X"
        board[5][20] = board[5][50] = "H"
        board[6][50] = board[6][20] = "H"
        board[7][50] = "H"
        board[8][20] = board[8][50] = "H"
        board[8][randint(21,49)] = "C"
        board[8][randint(51,70)] = board[8][randint(71,78)] = "C"
        for i in xrange(19,79):
            board[9][i] = "X"
        for i in xrange(9,13):
            board[i][40] = "H"
        board[12][randint(1,10)] = "C"
        board[12][randint(11,20)] = "C"
        board[12][randint(21,39)] = "C"
        board[12][randint(41,56)] = "C"
        for i in xrange(1,60):
            board[13][i] = "X"
        board[13][56] = board[13][34] = "H"
        board[14][56] = board[14][34] = "H"
        board[15][34] = "H"
        board[16][56] = board[16][34] = "H"
        board[16][randint(30,33)] = board[16][randint(35,55)] = board[16][randint(57,65)] = "C"
        for i in xrange(29,79):
            board[17][i] = "X"
        board[17][30] = "H"
        board[18][30] = "H"
        board[19][30] = "H"
        board[20][30] = "H"
        board[20][randint(1,5)] = board[20][randint(6,10)] =  board[20][randint(11,15)] = board[20][randint(21,29)] = "C"
        for i in xrange(1,39):
            board[21][i] = "X"
        board[21][31] = "H"
        board[22][31] = "H"
        board[23][31] = "H"
        board[24][31] = "H"
        board[24][randint(32,40)] = board[24][randint(41,50)] = board[24][randint(51,60)] = board[24][randint(61,70)] = "C"
        for i in xrange(25,79):
            board[25][i] = "X"
        board[25][50] = "H"
        board[26][50] = "H"
        board[27][50] = "H"
        board[28][50] = "H"
        board[28][1] = "P"
        board[28][randint(2,10)] = board[28][randint(11,18)] = board[28][randint(19,25)] = board[28][randint(26,40)] = board[28][randint(41,49)] = board[28][randint(51,60)] = "C"
        return board


def printBoard():
    for i in xrange(0,30):
        for j in xrange(0,80):
            sys.stdout.write(board[i][j])
        print ""

