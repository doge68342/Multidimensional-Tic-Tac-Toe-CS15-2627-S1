grid_1 = [
    ["X", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]

grid_2 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "O", "X"]
]

grid_3 = [
    ["X", "O", "O"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]

grid_4 = [
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]

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

    tie = True
    for i in grid:
        if " " in i:
            tie = False
    if tie:
        return "Tie"


def display_grid(grid):
    for i, item in enumerate(grid):
        print(f"{item[0]} | {item[1]} | {item[2]}")
        if i != len(grid) - 1:
            print("---------")




print("Board 1: ")
display_grid(grid_1)
print("winner:", determine_winner(grid_1))
print("")

print("Board 2: ")
display_grid(grid_2)
print("winner:", determine_winner(grid_2))
print("")

print("Board 3: ")
display_grid(grid_3)
print("winner:", determine_winner(grid_3))
print("")

print("Board 4: ")
display_grid(grid_4)
print("winner:", determine_winner(grid_4))
print("")