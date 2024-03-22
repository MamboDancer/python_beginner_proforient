from tkinter import *
import random

root = Tk()

root.title("TicTacToe")
root.resizable(False, False)
buttons = []
activePlayer = True
game = True


def check_move(number):
    if buttons[number].cget('text') or not game:
        return
    mark = get_active_player()
    buttons[number].config(text=mark)
    if not check_win(mark):
        bot_move()
    else:
        show_winner(mark)


def get_active_player():
    global activePlayer
    if activePlayer:
        activePlayer = False
        mark = "X"
    else:
        activePlayer = True
        mark = "O"
    return mark


def check_win(mark):
    for i in range(0, 9, 3):
        if (buttons[i].cget('text') == mark
                and buttons[i + 1].cget('text') == mark
                and buttons[i + 2].cget('text') == mark):
            return mark

    for i in range(3):
        if (buttons[i].cget('text') == mark
                and buttons[i + 3].cget('text') == mark
                and buttons[i + 6].cget(
                'text') == mark):
            return mark

    if (buttons[0].cget('text') == mark
            and buttons[4].cget('text') == mark
            and buttons[8].cget('text') == mark):
        return mark

    if (buttons[2].cget('text') == mark
            and buttons[4].cget('text') == mark
            and buttons[6].cget('text') == mark):
        return mark


def bot_move():
    position = random.randint(0, 8)
    while buttons[position].cget("text"):
        position = random.randint(0, 8)
    mark = get_active_player()
    buttons[position].config(text=mark)
    if check_win(mark):
        show_winner(mark)


def show_winner(mark):
    global game
    window = Toplevel(root)
    Label(window, text=mark + " is winner!", font=("Arial", 50)).pack()
    game = False


def init_board():
    i = 0
    for row in range(3):
        for column in range(3):
            b = Button(root, width=5, font=("Arial", 50), command=lambda x=i: check_move(x))
            b.grid(row=row, column=column)
            buttons.append(b)
            i += 1


init_board()
root.mainloop()
