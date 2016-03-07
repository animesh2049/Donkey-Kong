from classes import *
from board import *
from functions import *
import time
import curses

############################################## Variable Initialization ######################################################

new_player = Player("Animesh")
donkey = Donkey("donkey")
board = generateBoard(1)

########################################## For Starting Screen ##############################################################

screen = curses.initscr()
screen.clear()
screen.border("X","X","X","X")
screen.addstr(7,40,"Level 1")
screen.addstr(10,33,"Press 1 to play game!")
screen.addstr(11,33,"Press 2 to exit")
x = screen.getch()
curses.endwin()

##################################################### Game Starts ###########################################################

if x == ord('1'):
    printBoard()
    move = " "
    while move != "q":
        move = getchar()
        if move == "a":
            present_pos = new_player.getPosition()
            if checkWall(board,present_pos,"left"):
                pass
            elif not checkBase(board,present_pos,"left"):
                x = present_pos[0] + 1
                y = present_pos[1] - 1
                down_count = 0
                while board[x][y] != "X":
                    x = x + 1
                    down_count = down_count + 1
                board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                if board[present_pos[0]][present_pos[1] - 1] == "C":
                    new_player.Increase_score()
                    new_player.setPrevious(" ")
                    board[present_pos[0]][present_pos[1] - 1 ] = new_player.sym()
                else:
                    new_player.setPrevious(board[present_pos[0]][present_pos[1] - 1])
                    board[present_pos[0]][present_pos[1] - 1] = new_player.sym()
                new_player.setPositon([present_pos[0],present_pos[1] - 1])
                printBoard()
                for i in xrange(0,down_count):
                    present_pos = new_player.getPosition()
                    board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                    new_player.setPrevious(board[present_pos[0] + 1][present_pos[1]])
                    new_player.setPositon([present_pos[0] + 1,present_pos[1]])
                    board[present_pos[0] + 1][present_pos[1]] = new_player.sym()
                    printBoard()
                    time.sleep(0.1)
            else:
                board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                if board[present_pos[0]][present_pos[1] - 1] == "C":
                    new_player.Increase_score()
                    new_player.setPrevious(" ")
                    board[present_pos[0]][present_pos[1] - 1 ] = new_player.sym()
                else:
                    new_player.setPrevious(board[present_pos[0]][present_pos[1] - 1])
                    board[present_pos[0]][present_pos[1] - 1] = new_player.sym()
                new_player.setPositon([present_pos[0],present_pos[1] - 1])
                printBoard()
        elif move == "d":
            present_pos = new_player.getPosition()
            if checkWall(board,present_pos,"right"):
                pass
            elif not checkBase(board,present_pos,"right"):
                x = present_pos[0] + 1
                y = present_pos[1] + 1
                count_down = 0
                while board[x][y] != "X":
                    x = x + 1
                    count_down = count_down + 1
                board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                if board[present_pos[0]][present_pos[1] + 1] == "C":
                    new_player.Increase_score()
                    new_player.setPrevious(" ")
                    board[present_pos[0]][present_pos[1] + 1] = new_player.sym()
                else:
                    new_player.setPrevious(board[present_pos[0]][present_pos[1] + 1])
                    board[present_pos[0]][present_pos[1] + 1] = new_player.sym()
                new_player.setPositon([present_pos[0],present_pos[1] + 1])
                printBoard()
                for i in xrange(0,count_down):
                    present_pos = new_player.getPosition()
                    board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                    if board[present_pos[0] + 1][present_pos[1]] == "C":
                        new_player.Increase_score()
                        new_player.setPrevious(" ")
                        board[present_pos[0] + 1][present_pos[1]] = new_player.sym()
                    else:
                        new_player.setPrevious(board[present_pos[0] + 1][present_pos[1]])
                        new_player.setPositon([present_pos[0] + 1,present_pos[1]])
                        board[present_pos[0] + 1][present_pos[1]] = new_player.sym()
                    printBoard()
                    time.sleep(0.1)
            else:
                board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                if board[present_pos[0]][present_pos[1] + 1] == "C":
                    new_player.Increase_score()
                    new_player.setPrevious(" ")
                    board[present_pos[0]][present_pos[1] + 1] = new_player.sym()
                else:
                    new_player.setPrevious(board[present_pos[0]][present_pos[1] + 1])
                    board[present_pos[0]][present_pos[1] + 1] = new_player.sym()
                new_player.setPositon([present_pos[0],present_pos[1] + 1])
                printBoard()
        elif move == "w":
            present_pos = new_player.getPosition()
            if checkWall(board,present_pos,"up"):
                pass
            else:
                if new_player.showPrevious() == "H":
                    board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                    if board[present_pos[0] - 1][present_pos[1]] == "C":
                        new_player.Increase_score()
                        new_player.setPrevious(" ")
                        board[present_pos[0] - 1][present_pos[1]] = " "
                    new_player.setPrevious(board[present_pos[0] - 1][present_pos[1]])
                    new_player.setPositon([present_pos[0]-1,present_pos[1]])
                    board[present_pos[0] - 1][present_pos[1]] = new_player.sym()
                    printBoard()
                else:
                    pass
        elif move == "s":
            present_pos = new_player.getPosition()
            if checkWall(board,present_pos,"down"):
                pass
            else:
                if  board[present_pos[0] + 1][present_pos[1]] == "H":
                    board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                    new_player.setPrevious(board[present_pos[0] + 1][present_pos[1]])
                    new_player.setPositon([present_pos[0] + 1,present_pos[1]])
                    board[present_pos[0] + 1][present_pos[1]] = new_player.sym()
                    printBoard()
                else:
                    pass
        elif move == " ":
            present_pos = new_player.getPosition()
            if (board[present_pos[0] + 1][present_pos[1]] == "X" or (board[present_pos[0] + 1][present_pos[1]] == "H" and new_player.showPrevious() == " " and board[present_pos[0] - 1][present_pos[1]] != "H")) and new_player.showPrevious() == " ":
                x = present_pos[0]
                y = present_pos[1]
                count_up = 0
                while board[x][y] != "X" and count_up < 3:
                    x = x - 1
                    count_up = count_up + 1
                for i in xrange(0,count_up - 1):
                    present_pos = new_player.getPosition()
                    board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                    if board[present_pos[0] - 1][present_pos[1]] == "C":
                        new_player.Increase_score()
                        new_player.setPrevious(" ")
                        board[present_pos[0] - 1][present_pos[1]] = " "
                    new_player.setPrevious(board[present_pos[0] - 1][present_pos[1]])
                    new_player.setPositon([present_pos[0]-1,present_pos[1]])
                    board[present_pos[0] - 1][present_pos[1]] = new_player.sym()
                    printBoard()
                    time.sleep(0.1)
                for i in xrange(0,count_up - 1):
                    present_pos = new_player.getPosition()
                    board[present_pos[0]][present_pos[1]] = new_player.showPrevious()
                    new_player.setPrevious(board[present_pos[0] + 1][present_pos[1]])
                    new_player.setPositon([present_pos[0] + 1,present_pos[1]])
                    board[present_pos[0] + 1][present_pos[1]] = new_player.sym()
                    printBoard()
                    time.sleep(0.1)
                    
            
