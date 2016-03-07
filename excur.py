#!/usr/bin/env python
# _*_ coding: utf-8 _*_


from random import randint
from classes import *

new_player = Player("Animesh")
donkey = Donkey("donkey")

screen = curses.initscr()
screen.clear()
screen.border("X","X","X","X")
screen.addstr(7,40,"Level %d" % new_player.level)
screen.addstr(10,33,"Press 1 to play game!")
screen.addstr(11,33,"Press 2 to exit")
x = screen.getch()

if x == ord('1'):
    board = Board(1)
    board.printboard(donkey,new_player)
screen.refresh()
curses.endwin()
