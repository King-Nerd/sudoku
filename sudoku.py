import time
#making a random change
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

indexed_points = []

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
                    
def verify_empty(bo):
    location_y = 0
    for i in bo:
        location_x = 0
        for j in i:
            if j == 0:
                indexed_points.append((location_y, location_x))
            location_x += 1
        location_y += 1


verify_empty(board)

def valid_num(coord):
    test_num = board[coord[0]][coord[1]]
    row_list = board[coord[0]]
    column = []
    box = []
    for row in board:
        column.append(row[coord[1]])
    
    box_coord_row = (coord[1] // 3) * 3
    box_coord_column = (coord[0] // 3) * 3
    
    for x in range(box_coord_row, box_coord_row+3):
        for y in range(box_coord_column,box_coord_column+3):
#            print(f"{x},{y}")
            box.append(board[y][x])
          
    while True:
        if test_num == 0:
            test_num += 1
            continue
        elif test_num in row_list:
            test_num += 1
            continue
        elif test_num in column:
            test_num += 1
            continue
        elif test_num in box:
            test_num += 1
            continue
        else:
            break
    
    if test_num > 9:
        board[coord[0]][coord[1]] = 0
        return False
    else: 
        board[coord[0]][coord[1]] = test_num
        return True
                
def solve_puzzle(board):
    pointer = 0
    while pointer < len(indexed_points) and pointer > -1:
        if valid_num(indexed_points[pointer]):
            pointer += 1
            print_board(board)
            print("\n")
            time.sleep(.5)

        else:
            pointer -= 1
            print_board(board)
            print("\n")
            time.sleep(.5)


    
#solve_puzzle(board)
solve_puzzle(board)
print_board(board)
#for index, coord in enumerate(indexed_points):
#    print(index)