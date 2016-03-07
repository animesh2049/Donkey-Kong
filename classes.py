from os import system
import curses
from random import randint

class Person:
    def __init__(self, name):
        self.__name = name
        self.crt()
        self.__level = 1

class Player(Person):
    def crt(self):
        self.__symbol = 'P'
        self.__score = 0
        self.__life = 3
        self.__position = [28, 1]
        self.__previousthing = " "
    def sym(self):
        return self.__symbol
    def Player_score(self):
        return self.__score
    def Increase_score(self):
        self.__score = self.__score + 1;
    def Player_life(self):
        return self.__life
    def Decrease_life(self):
        self.__life = self.__life - 1;
    def Game_status(self):
        if self.Player_life():
            return 1
        else:
            return 0
    def getPosition(self):
        return self.__position
    def showPrevious(self):
        return self.__previousthing
    def setPrevious(self, holder):
        self.__previousthing = holder
    def setPositon(self, position):
        self.__position = [position[0], position[1]]

class Donkey(Person):
    def crt(self):
        self.__symbol = "D"
        self.__position = [4, 1]
        self.__previousthing = " "
    def sym(self):
        return self.__symbol
    def getPosition(self):
        return self.__position
    def setPositon(self, position):
        self.__position = position
    def showPrevious(self):
        return self.__previousthing
    def setPrevious(self, holder):
        self.__previousthing = holder
