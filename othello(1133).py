# Abdurahman Abdurahman
# Othello
import turtle
import random
def drawGrid():
    t1 = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setworldcoordinates(0,0,12,12)
    screen.tracer(0)
    t1.shape("square")
    t1.color("darkgreen")
    t1.shapesize(2.5)
    t1.pu()
    x = 2
    matrix = []
    while 10 > x:
        y = 2
        row = []
        while 10 > y:
            t1.goto(x,y)
            t1.stamp()
            row.append(0)
            y += 1
        x += 1
        matrix.append(row)
    t1.color("black")
    num = 7
    x = 1
    y = 2
    while y < 10:
        t1.goto(x,y)
        t1.write(num, move=False, align="center", font=("Arial", 12, "bold"))
        y += 1
        num -= 1
    num = 0
    x = 2
    y = 10
    while x < 10:
        t1.goto(x,y)
        t1.write(num, move=False, align="center", font=("Arial", 12, "bold"))
        x += 1
        num += 1
    return matrix
# pieces will be called after each turn to make and change the pieces
def pieces(board):
    x = 2
    y = 2
    t1 = turtle.Turtle()
    t1.shape("circle")
    t1.shapesize(2)
    for row in range(8):
        for col in range(8):
            if board[row][col] == 1:
                t1.pu()
                t1.goto(x+col,y+row)
                t1.color("white")
                t1.stamp()
                t1.pd()
            if board[row][col] == 2:
                t1.pu()
                t1.goto(x+col,y+row)
                t1.color("black")
                t1.stamp()
                t1.pd()
    for row in board:
        print(row, "\n")
    return board

def userPlay(board):
    screen = turtle.getscreen()
    x = screen.textinput("location","Enter row,col: ")
    row = int(x[0])
    col = int(x[2])
    print(row,col)
    return row,col

def lineEnd(color,rowdir,coldir,row,col,board):
    validMove = False
    if (0 < row < 8) and (0 < col < 8):
        if board[row][col] == color:
            validMove = True
        if ((row + rowdir < 0) or (row + rowdir > 7)):
            validMove = False
        if ((col + coldir < 0) or (col + coldir > 7)):
            validMove = False
    if validMove == True:
        return lineEnd(color,rowdir,coldir,row + rowdir,col + coldir,board)

def validMove(color,rowdir,coldir,row,col,board):
    color = 1
    other = 2
    validMove = True
    if color == 1:
        other = 2
    if color == 2:
        other = 1
    if (0 < row+rowdir < 8) and (0 < col+coldir < 8):
        if board[row + rowdir][col + coldir] != other:
            validMove = False
        if ((row + rowdir + rowdir < 0) or (row + rowdir + rowdir > 7)):
            validMove = False
        if ((col + coldir + coldir < 0) or (col + coldir +coldir > 7)):
            validMove = False
        return lineEnd(color,rowdir,coldir,row + rowdir + rowdir,col + coldir + coldir,board)
    return validMove,rowdir,coldir

def isValidMove(board,row,col,color):
    isValid = False
    if (row,col) in getValidMoves(board,color):
        isValid = True
    return isValid

def getValidMoves(board,color):
    validMoves = []
    for row in range(8):
        for col in range(8):
            if board[row][col] == 0:
                up = validMove(color,-1,0,row,col,board)
                upright = validMove(color,-1,1,row,col,board)
                right = validMove(color,0,1,row,col,board)
                downright = validMove(color,1,1,row,col,board)
                down = validMove(color,1,0,row,col,board)
                downleft = validMove(color,1,-1,row,col,board)
                left = validMove(color,0,-1,row,col,board)
                upleft = validMove(color,-1,-1,row,col,board)
                if not (up or upright or right or downright or down or downleft or left or upleft):
                    validMoves.append((row,col))
    print(validMoves)
    return validMoves

def gameIsOver(board):
    gameOver = False
    num = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == 1 or board[row][col] == 2:
                num += 1
    if num != 0:
        gameOver = False
    if userPlay(board) == "":
        gameOver = True
    return gameOver

def selectNextPlay(board):
    color = ""
    row,col = random.choice(getValidMoves(board,color))
    return row,col

def flip(board,row,col,color):
    flip = []
    validMoves,rowdir,coldir = getValidMoves(board,color)
    while (0 < row+rowdir < 8) and (0 < col+coldir < 8):
        row += rowdir
        col += coldir
        if (0 < row+rowdir < 8) and (0 < col+coldir < 8):
            if board[row+rowdir][col+coldir] == color:
                flip.append([row+rowdir,col+coldir])
    if flip != []:
        newrow = row + rowdir - rowdir
        newcol = col + coldir - coldir
        if newrow != row or newcol != col:
            board[row+rowdir][col+coldir] = color
            newrow -= rowdir
            newcol -= coldir
    return flip


def main():
    board = drawGrid()
    board[3][4] = 2
    board[3][3] = 1
    board[4][4] = 1
    board[4][3] = 2
    board = pieces(board)
    color = 1
    gameOver = gameIsOver(board)
    while gameOver == False:
        if color == 1:
            isValid = False
            while isValid == False:
                printmessage = "Move not valid. Please enter a new row, column: "
                validMoves = getValidMoves(board,1)
                if validMoves == []:
                    gameOver = True
                else:
                    gameOver = False
                row, col = userPlay(board)
                isValid = isValidMove(board,row,col,color)
            color += 1
        if color == 2:
            validMoves = getValidMoves(board,2)
            if validMoves == []:
                gameOver = True
            else:
                gameOver = False
            row,col = selectNextPlay(board)
            color -= 1
if __name__ == '__main__':
    main()

#my function is theoretically supposed to work but I have not figured out how to make the flip work, so it gets stuck and
#looks like its not even changing
