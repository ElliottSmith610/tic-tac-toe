from tkinter import *

FONT = ('Arial', 18, 'bold')
HEIGHT = 2
WIDTH = 4
TURN = ""
TURN_COUNT = 0
SCORE = {'X': 0, 'O': 0}

window = Tk()
window.title("Tic Tac Toe")
window.config(padx=50, pady=25, bg="aliceblue")

row_1 = [' ', ' ', ' ']
row_2 = [' ', ' ', ' ']
row_3 = [' ', ' ', ' ']
playspace = [row_1, row_2, row_3]
valid_moves = ['1.1', '1.2', '1.3',
               '2.1', '2.2', '2.3',
               '3.1', '3.2', '3.3']
tile_dict = {}

for i in range(len(valid_moves)):
    def func(move=valid_moves[i]):
        tile_dict[move].config(state=DISABLED)
        return place_tile(move)

    tile_dict[valid_moves[i]] = Button(window, text=" ", width=WIDTH, height=HEIGHT,
                                       font=FONT, command=func)
    if i < 3:
        tile_dict[valid_moves[i]].grid(row=0+1, column=i, padx=(1, 1), pady=(1, 1))
    elif i < 6:
        tile_dict[valid_moves[i]].grid(row=1+1, column=i-3, padx=(1, 1), pady=(1, 1))
    else:
        tile_dict[valid_moves[i]].grid(row=2+1, column=i-6, padx=(1, 1), pady=(1, 1))

    # TODO: Score list
    # score_O = Label(text="2", font=FONT)
    # score_O.grid(row=0, column=0, pady=(0,10))
    # score_X = Label(text="3", font=FONT)
    # score_X.grid(row=0, column=2)


def reset():
    global row_1, row_2, row_3, playspace
    row_1 = [' ', ' ', ' ']
    row_2 = [' ', ' ', ' ']
    row_3 = [' ', ' ', ' ']
    playspace = [row_1, row_2, row_3]

    for (tile, button) in tile_dict.items():
        tile_dict[tile].config(text=" ", state=NORMAL)

    winner['text'] = ""


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
            game_over('X')
        elif row == "OOO" or column == "OOO" or diag_upward == "OOO" or diag_downward == "OOO":
            print("Player O wins")
            game_over('O')


def game_over(player):
    for (tile, button) in tile_dict.items():
        if button['text'] == " ":
            tile_dict[tile].config(state=DISABLED)
    winner['text'] = f"Player {player} wins!"


def place_tile(tile):
    global TURN, TURN_COUNT

    if TURN_COUNT % 2 == 0:
        TURN = "X"
    else:
        TURN = "O"

    tile_dict[tile].config(text=TURN)

    x = int(tile[0]) - 1
    y = int(tile[2]) - 1

    playspace[x][y] = TURN
    check_winner()
    TURN_COUNT += 1


winner = Label(text="", font=FONT, bg="aliceblue")
winner.grid(row=4, columnspan=4, pady=(25, 25))
reset_ = Button(text="Reset Board", font=('Arial', 12, 'normal'), command=reset)
reset_.grid(row=5, columnspan=4)
reset()

window.mainloop()

    # if check_winner():
    #     continue_playing = False
    # elif turn_count > 8:
    #     print("Game over, it's a draw!")
    #     continue_playing = False

# button_one_one = Button(text=row_1[0], width=WIDTH, height=HEIGHT, font=FONT, command=place_tile)
# button_one_one.grid(row=0, column=0)
# button_one_two = Button(text=row_1[1], width=WIDTH, height=HEIGHT, font=FONT, command=place_tile)
# button_one_two.grid(row=0, column=1)
# button_one_three = Button(text=row_1[2], width=WIDTH, height=HEIGHT, font=FONT, command=place_tile)
# button_one_three.grid(row=0, column=2)
#
# button_two_one = Button(text=row_2[0], width=WIDTH, height=HEIGHT, font=FONT, command=place_tile)
# button_two_one.grid(row=1, column=0)
# button_two_two = Button(text=row_2[1], width=WIDTH, height=HEIGHT, font=FONT, command=place_tile)
# button_two_two.grid(row=1, column=1)
# button_two_three = Button(text=row_2[2], width=WIDTH, height=HEIGHT, font=FONT, command=place_tile)
# button_two_three.grid(row=1, column=2)
#
# button_three_one = Button(text=row_3[0], width=WIDTH, height=HEIGHT, font=FONT, command=place_tile)
# button_three_one.grid(row=2, column=0)
# button_three_two = Button(text=row_3[1], width=WIDTH, height=HEIGHT, font=FONT, command=place_tile)
# button_three_two.grid(row=2, column=1)
# button_three_three = Button(text=row_3[2], width=WIDTH, height=HEIGHT, font=FONT, command=place_tile)
# button_three_three.grid(row=2, column=2)
