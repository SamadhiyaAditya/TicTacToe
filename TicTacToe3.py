def brd_layout(brd):
    for row in brd:
        print(" | ".join(row))
        print("-" * (len(brd) * 4 - 1))

def Winner(brd, size):

    for row in brd:
        if row.count(row[0]) == size and row[0] != " ":
            return row[0]
    for col in range(size):
        column = [brd[row][col] for row in range(size)]
        if column.count(column[0]) == size and column[0] != " ":
            return column[0]

    diagonal1 = [brd[i][i] for i in range(size)]
    if diagonal1.count(diagonal1[0]) == size and diagonal1[0] != " ":
        return diagonal1[0]
    diagonal2 = [brd[i][size - i - 1] for i in range(size)]
    if diagonal2.count(diagonal2[0]) == size and diagonal2[0] != " ":
        return diagonal2[0]

    return None


def draw(brd):
    for row in brd:
        if " " in row:
            return False
    return True


def Turn(brd, size, symbol):
    while True:
        row_input = input(f"Enter the row (0-{size - 1}): ")
        col_input = input(f"Enter the column (0-{size - 1}): ")

        if row_input.isdigit() and col_input.isdigit():
            row, col = int(row_input), int(col_input)
            if 0 <= row < size and 0 <= col < size:
                if brd[row][col] == " ":
                    brd[row][col] = symbol
                    return
                else:
                    print("That spot is already taken. Try again.")
            else:
                print(f"Invalid row or column. Please choose between 0 and {size - 1}.")
        else:
            print("Invalid input. Please enter numbers only.")



print("Welcome to 2-Player Tic Tac Toe!")
while True:
    size_input = input("Enter the brd size (odd number between 3 and 100): ")
    if size_input.isdigit():
        size = int(size_input)
        if 3 <= size <= 100 and size % 2 == 1:
            break
        else:
            print("Please enter an odd number between 3 and 100.")
    else:
        print("Invalid input. Please enter a number.")

brd = [[" " for _ in range(size)] for _ in range(size)]
symbols = ["X", "O"]
current_player = 0

brd_layout(brd)

while True:
    print(f"Player {current_player + 1}'s turn ({symbols[current_player]}).")
    Turn(brd, size, symbols[current_player])
    brd_layout(brd)

    winner = Winner(brd, size)
    if winner:
        print(f"Player {symbols.index(winner) + 1} ({winner}) wins!")
        break

    if draw(brd):
        print("It's a draw!")
        break

    current_player = 1 - current_player