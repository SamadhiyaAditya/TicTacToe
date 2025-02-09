import random

def Board(brd):
    for row in brd:
        print(" | ".join(row))
        print("-" * (len(brd) * 4 - 1))


def winner(brd, size):
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


def full(brd):
    for row in brd:
        if " " in row:
            return False
    return True


def Turn(brd, size):
    while True:
        row_input = input(f"Enter the row (0-{size - 1}): ")
        col_input = input(f"Enter the column (0-{size - 1}): ")

        if row_input.isdigit() and col_input.isdigit():
            row, col = int(row_input), int(col_input)
            if 0 <= row < size and 0 <= col < size:
                if brd[row][col] == " ":
                    return row, col
                else:
                    print("That spot is already taken. Try again.")
            else:
                print(f"Invalid row or column. Please choose between 0 and {size - 1}.")
        else:
            print("Invalid input. Please enter numbers only.")


def computer_turn(brd, size):
    empty_cells = [(r, c) for r in range(size) for c in range(size) if brd[r][c] == " "]
    return random.choice(empty_cells)


print("Welcome to Tic Tac Toe!")
size = 3
brd = [[" " for _ in range(size)] for _ in range(size)]
players = ["Player", "Computer"]
player_symbol = "X"
computer_symbol = "O"
current_player = 0

Board(brd)

while True:
    if current_player == 0:
        print("Your turn!")
        row, col = Turn(brd, size)
        brd[row][col] = player_symbol
    else:
        print("Computer's turn!")
        row, col = computer_turn(brd, size)
        brd[row][col] = computer_symbol

    Board(brd)

    Winner = winner(brd, size)
    if Winner:
        if Winner == player_symbol:
            print("Congratulations! You win!")
        else:
            print("Computer wins! Better luck next time.")
        break

    if full(brd):
        print("It's a draw!")
        break

    current_player = 1 - current_player