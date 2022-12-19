# TODO: Board dictionary
# TODO: End game conditions: X/O win, run out of spaces (9)
# TODO: Tkinter?

row_1 = [' ', ' ', ' ']
row_2 = [' ', ' ', ' ']
row_3 = [' ', ' ', ' ']
playspace = [row_1, row_2, row_3]


def board():
    print(f"{row_1[0]} | {row_1[1]} | {row_1[2]}\n"
          f"- - - - -\n"
          f"{row_2[0]} | {row_2[1]} | {row_2[2]}\n"
          f"_ _ _ _ _\n"
          f"{row_3[0]} | {row_3[1]} | {row_3[2]}\n")


def turn(player):
    valid_moves = ['1.1', '1.2', '1.3',
                   '2.1', '2.2', '2.3',
                   '3.1', '3.2', '3.3']

    illegal_move = True
    while illegal_move:
        coords = input(f"{player}'s turn to place tile: ")
        while coords not in valid_moves:
            print("Invalid coordinate, please use the format (row).(column) for example 1.1 or 3.2")
            coords = input(f"{player}'s turn to place tile: ")

        x = int(coords[0]) - 1
        y = int(coords[2]) - 1

        if playspace[x][y] == ' ':
            playspace[x][y] = player
            illegal_move = False
        else:
            print("Tile already taken")


def check_winner():
    reversed_playspace = playspace[::-1]
    diag_downward = ""
    diag_upward = ""

    # check row winner
    for x in range(3):
        row = "".join(playspace[x])
        # print(f"row {row}")

    # check diagonal winner
        diag_downward += playspace[x][x]
        diag_upward += reversed_playspace[x][x]

    # check column winner
        column = ""
        for y in range(3):
            column += playspace[y][x]
        # print(f"column {column}")

        if row == "XXX" or column == "XXX" or diag_upward == "XXX" or diag_downward == "XXX":
            print("Player X wins")
            return True
        elif row == "OOO" or column == "OOO" or diag_upward == "OOO" or diag_downward == "OOO":
            print("Player O wins")
            return True

    # print(diag_downward)
    # print(diag_upward)

continue_playing = True
turn_count = 0
while continue_playing:
    board()

    if turn_count % 2 == 0:
        turn('X')
    else:
        turn('O')

    turn_count += 1
    if check_winner():
        continue_playing = False
    elif turn_count > 8:
        print("Game over, it's a draw!")
        continue_playing = False



