import random

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def get_user_input(prompt, data_type, max):
    if data_type == "string":
        return input(prompt)
    elif data_type == "int":
        try:
            output = int(input(prompt))
            if output <= max or max == 0:
                return output
            else:
                print(f"Please input an integer between 0 and {max}")
                return get_user_input(prompt, data_type, max)
        except ValueError:
            print("Please input integer and try again")
            return (get_user_input(prompt, data_type, max))
    elif data_type == "float":
        try:
            output = float(input(prompt))
            return output
        except ValueError:
            print("Please input float and try again")
            return (get_user_input(prompt, data_type, max))

def determine_winner(grid):
    for i in grid:
        if i[0] == i[1] == i[2]:
            if i[0] != " ":
                return i[0]
        
    for i in range(len(grid)):
        if grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] != " ":
                return grid[0][i]

    if grid[0][0] == grid[1][1] == grid[2][2]:
            if grid[0][0] != " ":
                return grid[0][0]

    if grid[2][0] == grid[1][1] == grid[0][2]:
            if grid[2][0] != " ":
                return grid[2][0]


def display_list(list):
    for i, item in enumerate(list):
        print(f"{item[0]} | {item[1]} | {item[2]}")
        if i != len(list) - 1:
            print("---------")

turn = random.choice(["X", "O"])
while True:
    display_list(board)

    print(f"Turn: {turn}")
    while True: 
        row = get_user_input("Row: ", "int", 2)
        column = get_user_input("Column: ", "int", 2)
        if board[row][column] == " ":
            board[row][column] = turn
            break
        else:
            print("That place on the board is taken silly")

    if determine_winner(board) != None:
        print(f"{determine_winner(board)} is the winner, game over")
        break


    if turn == "X":
        turn = "O"
    else:
        turn = "X"