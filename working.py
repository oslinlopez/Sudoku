board = [
    [0,5,0,0,3,0,6,0,0],
    [6,0,3,0,0,4,9,0,0],
    [7,0,0,1,6,0,2,0,0],
    [0,0,0,5,0,0,4,2,0],
    [9,8,0,2,0,6,0,3,7],
    [0,7,4,0,0,1,0,0,0],
    [0,0,7,0,5,8,0,0,2],
    [0,0,8,4,0,0,7,0,9],
    [0,0,1,0,7,0,0,6,0]
]

def solve(bo):
    
    find = findEmptySpot(bo)
    if not find:
        return True # Completed the solution
    else:
        row, col = find

    for i in range(1,10): # Loop for values 1-9 
        if valid(bo, i, (row, col)): # Check if adding the values into the board will be a good solution
            bo[row][col] = i # Once its vaild it will actually add it to the board

            if solve(bo): # Recursively try to finish the solution (repeat the process) until a solution was found
                return True
            
            bo[row][col] = 0 # Use a different value so it can repeat the process with the new value
    
    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: # Check each element in the row to see if it equals to the number that was added in the baord AND ignores the number that was added before
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != 1: # Same thing but checks the element in each column instead of row
            return False

    # Check rectangle we are in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def printBoard(bo):

    for i in range(len(bo)): 
        if i % 3 == 0 and i != 0: # If the remainder is 0 and i != 0 then the statement is true
            print("------------------------") # This will print out a horizontal line every 3 rows

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0: 
                print(" | ", end="") # Every 3 columns a vertical line will print, 'end' code will make it stay on the row it recently printed the line

            if j == 8: # Checking if at the last position
                print(bo[i][j]) # This will go to the next line
            else:
                print(str(bo[i][j]) + " ", end="")


def findEmptySpot(bo): # Find empty spaces
    for i in range(len(bo)): 
        for j in range(len(bo[0])):
            if bo [i][j] == 0:
                return (i, j) # (row, col)

    return None

printBoard(board)
solve(board)
print("___________________________________")
printBoard(board)
