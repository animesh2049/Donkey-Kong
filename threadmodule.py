import threading
import time
from random import randint

class myThread(threading.Thread):
    def __init__(self,threadId,name):
        self.__threadId = threadId
        self.__name = name
    def getThreadName(self):
        return self.__name
    def run(self,board,donkey):
        move = randint(0,1)
        present_pos = donkey.getPosition()
        if move == 0:
            board[present_pos[0]][present_pos[1]] = donkey.showPrevious()
            donkey.setPrevious(board[present_pos[0]][present_pos[1] + 1])
            donkey.setPositon(board[present_pos[0]][present_pos[1] + 1])
                
        
    
