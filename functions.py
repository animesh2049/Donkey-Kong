def checkWall(board,position,move):
    if move == "left":
        if position[1] - 1 <= 0 or board[position[0]][position[1] - 1] == "X":
            return True
        else:
            return False
    elif move == "right":
        if position[1] + 1 >= 79 or board[position[0]][position[1] + 1] == "X":
            return True
        else:
            return False
    elif move == "up":
        if position[0] - 1 <= 0:
            return True
        else:
            return False


def checkBase(board,position,move):
    if move == "left":
        if board[position[0] + 1][position[1] - 1] == "X" or board[position[0] + 1][position[1] - 1] == "H":
            return True
        else:
            return False
    elif move == "right":
        if board[position[0] + 1][position[1] + 1] == "X" or board[position[0] + 1][position[1] + 1]  == "H":
            return True
        else:
            return False

def getchar():
    import tty, termios, sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def move_left():
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




    
def check_coin(board, position_to_go):
    if board[position_to_go[0]][position_to_go[1]] == "C":
        return True
    else:
        return False
