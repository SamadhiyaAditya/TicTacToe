import random

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


def Turn(brd, size):
    while True:
        row_input = input(f"Enter the row (0-{size - 1}): ")
        col_input = input(f"Enter the column (0-{size - 1}): ")

        if row_input.isdigit() and col_input.isdigit():
            row, col = int(row_input), int(col_input)
            if 0 <= row < size and 0 <= col < size:
                if brd[row][col] == " ":
                    brd[row][col] = "X"
                    return
                else:
                    print("That spot is already taken. Try again.")
            else:
                print(f"Invalid row or column. Please choose between 0 and {size - 1}.")
        else:
            print("Invalid input. Please enter numbers only.")


def computer_move(brd, size):
    empty_cells = [(r, c) for r in range(size) for c in range(size) if brd[r][c] == " "]
    move = random.choice(empty_cells)
    brd[move[0]][move[1]] = "O"
    print(f"Computer chose row {move[0]}, column {move[1]}.")



print("Welcome to Custom Tic Tac Toe (Player vs Computer)!")
while True:
    size_input = input("Enter the brd size (odd number between 3 and 99): ")
    if size_input.isdigit():
        size = int(size_input)
        if 3 <= size <= 99 and size % 2 == 1:
            break
        else:
            print("Please enter an odd number between 3 and 99.")
    else:
        print("Invalid input. Please enter a number.")

brd = [[" " for _ in range(size)] for _ in range(size)]

brd_layout(brd)

while True:
    print("Your turn!")
    Turn(brd, size)
    brd_layout(brd)
    winner = Winner(brd, size)
    if winner:
        print("Congratulations! You win!" if winner == "X" else "Computer wins! Better luck next time.")
        break

    if draw(brd):
        print("It's a draw!")
        break

    print("Computer's turn!")
    computer_move(brd, size)
    brd_layout(brd)

    winner = Winner(brd, size)
    if winner:
        print("Congratulations! You win!" if winner == "X" else "Computer wins! Better luck next time.")
        break

    if draw(brd):
        print("It's a draw!")
        break