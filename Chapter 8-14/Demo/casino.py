"""
Same code as the curriculum,except a couple of adjustments
Specifically we want to center the window and define its size
"""
import tkinter
from tkinter import messagebox
import random

secret = random.randint(1, 100)

window = tkinter.Tk()  # create a Tk root window

w = 300  # width for the Tk root
h = 200  # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth()  # width of the screen
hs = window.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window,
# (0,0) is top-left of screen,
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2))

# top-left of the window will be placed on position (x,y) on the screen
window.geometry(f"{w}x{h}+{x}+{y}")  # define starting size and position

# greeting text
greeting = tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

# guess entry field
guess = tkinter.Entry(window)
guess.pack()


# check guess
def check_guess():
    if int(guess.get()) == secret:
        result_text = "CORRECT!"
    elif int(guess.get()) > secret:
        result_text = "WRONG! Your guess is too high."
    else:
        result_text = "WRONG! Your guess is too low."

    messagebox.showinfo("Result", result_text)


# submit button
submit = tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()

window.mainloop()
