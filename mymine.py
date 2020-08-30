#Kamal Chahrour - 101162518 COMP 1405 ASSIGNMENT 5
import random
MINE_CHANCE = 10
GRID_SIZE = 9
  
def placeMines():#Places mine in board, 1 in GRID_SIZE chance
    board = []
    row = []
    for y in range(GRID_SIZE):
        row = []
        for x in range(GRID_SIZE):
            num = random.randint(1,MINE_CHANCE)
            if num != MINE_CHANCE:
                row.append('')
            else:
                row.append('x')
        board.append(row)
    return board

def makeBoard():#Makes a 2D list for a board filled with #'s
    board = []
    row = []
    for y in range(GRID_SIZE):
        row = []
        for x in range(GRID_SIZE):
            row.append('#')
        board.append(row)
    return board

def showBoard(lis):#Prints out board
    output = " |"#Start of the first line
    for x in range(GRID_SIZE):
        output+=str(x) #Adds the Column numbers
    print(output)
    print("---"+"-"*GRID_SIZE) #Seperates top numbers from the grid
    for x in range(len(lis)):
        output2 = ""
        output2+=str(x) + "|" #Seperation between columns and rows
        for y in range(len(lis[x])):
            if lis[x][y] == '':
                output2+= " "
            elif lis[x][y] == 'x':
                output2+= lis[x][y]
            else:
                output2+= lis[x][y]
        print(output2)

def countHiddenCells(lis):#Counts #'s in board.
    total = 0
    for x in range(len(lis)):
        for y in range(len(lis[x])):
            if lis[x][y] == "#":
                total+=1
    return total

def countAllMines(lis):#Counts all mines in board.
    total = 0
    for x in range(len(lis)):
        for y in range(len(lis[x])):
            if lis[x][y] == "x":
                total+=1
            else:
                continue
    return total

def isMineAt(lis,row,col):#Checks if a mine is at a given cell
    try:
        if lis[row][col] == 'x':
            return True
        else:
            return False
    except:
        return False

def countAdjacentMines(lis,row,col):#Validates input around the given cell to make sure it does not overlap the list and returns a number
    total = 0
    while isMineAt(lis,row,col) is False:
        if ((row > 0 and col > 0) and lis[row-1][col-1] == 'x'):
            total+=1               
        if  (row > 0 and lis[row-1][col] == 'x'):
            total+=1
        if ((row > 0 and col < len(lis)-1) and lis[row-1][col+1] == 'x'):
            total+=1
        if (col > 0 and lis[row][col-1] == 'x'):
            total+=1 
        if (col < len(lis)-1 and lis[row][col+1] == 'x'):
            total+=1
        if ((row < len(lis)-1 and col > 0) and lis[row+1][col-1] == 'x'):
            total+=1
        if (row < len(lis)-1 and lis[row+1][col] == 'x'):
            total+=1
        if ((row < len(lis)-1 and col < len(lis)-1) and lis[row+1][col+1] == 'x'):
            total+=1
        return total

def main():#Game loop
    board = makeBoard()
    mines = placeMines()
    move = []
    showBoard(board)#Shows first empty board
    while True:
        while move == []:
            try:
                move = [int(s) for s in input("Select a cell (row,col) > ").split(",")] #Gets input of 2 integers in form x,y
                x = move[0]#Integer 1
                y = move[1]#Integer 2
            except:
                move = []
        
        if isMineAt(mines,x,y) is True: #If you hit a mine entire board is revealed and you lose
            for i in range(len(mines)):
                for n in range(len(mines)):
                    if mines[i][n] == 'x':#Goes through board and replaces hidden mines with an x
                        board[i][n] = 'x'
            showBoard(board)
            print("Game Over!")
            break
        reveal(board,mines,x,y)

        if countAllMines(mines) == countHiddenCells(board): #Checks if you won, hidden cells is the same number as mines
            print("You Win!!")
            break
        move = []
        showBoard(board)
        
def reveal(board,mines,x,y):#reveals cells if they haven't hit a MINE
    #input validation to see if x and y are in range
    gameboard = board
    mineboard = mines
    if x < 0 or x > GRID_SIZE - 1 or y > GRID_SIZE - 1 or y < 0:
        return

    #If a cell is empty, it means its already checked
    if gameboard[x][y] == " ": 
        return

    numMines = countAdjacentMines(mineboard,x,y)#Counts number of mines around the cell
    
    if numMines > 0:#Mines are present
        gameboard[x][y] = str(numMines)#Mutates cell to be the numMines

    else:#Mines are not present
        gameboard[x][y] = ' '#Mutates to an empty cell
        reveal(gameboard,mines,x+1,y)
        reveal(gameboard,mines,x-1,y)#Goes through the left,right,up and down of the (nest line)
        reveal(gameboard,mines,x,y-1)#cell to check for empty spaces/mines
        reveal(gameboard,mines,x,y+1)

main()






