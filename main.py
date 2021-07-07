# --------------------IMPORTING ALL MODULES-------------------- #
import tkinter
from PIL import ImageTk, Image
import pandas
import random
# --------------------DECLARING VARIABLES-------------------- #
card_front_tf = True
dicty = {}

# --------------------IMPORTING CSV-------------------- #
try:
    french_words = pandas.read_csv('data/data.csv', header=None, index_col=0, squeeze=True).to_dict()
except FileNotFoundError:
    french_words = pandas.read_csv('data/french_words.csv', header=None, index_col=0, squeeze=True).to_dict()
random_word = random.choice((list(french_words)))
# --------------------DEFINING FUNCTIONS-------------------- #


def flip_card():
    global card_front_tf, french_words
    global random_word

    if card_front_tf:
        del french_words[random_word]
        random_word = random.choice((list(french_words)))
        canvas.create_image(300, 200, anchor="center", image=card_back)
        card_front_tf = False
        canvas.create_text(300, 150, fill="white", font="Times 20 italic", text="French")
        canvas.create_text(300, 200, fill="white", font="Times 20 bold", text=random_word)
    else:
        canvas.create_image(300, 200, anchor="center", image=card_front)
        card_front_tf = True
        canvas.create_text(300, 150, fill="black", font="Times 20 italic", text="English")
        canvas.create_text(300, 200, fill="black", font="Times 20 bold", text=french_words[random_word])


def timed_flip(tf):
    global dicty
    if not tf:
        dicty[random_word] = french_words[random_word]
        df = pandas.DataFrame(list(dicty.items()))
        df.to_csv("data/data.csv", header=False, index=False)
    flip_card()
    window.after(3000, flip_card)



# --------------------DECLARING ALL VARIABLES-------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# --------------------CREATING WINDOW-------------------- #
window = tkinter.Tk()
window.configure(bg=BACKGROUND_COLOR, padx=0, pady=50)
window.title("Flash Cards")

# -----setting icon----- #
icon = tkinter.PhotoImage(file="icon.png")
window.iconphoto(False, icon)

# --------------------CREATING ALL IMAGES-------------------- #

# -----back of card----- #
card_back_img = Image.open("images/card_back.png")  # reference path
card_back_img = card_back_img.resize((500, 300), Image.ANTIALIAS)  # resizing and anti-aliasing
card_back = ImageTk.PhotoImage(card_back_img)  # turning into tkinter photo class

# -----front of card----- #
card_front_img = Image.open("images/card_front.png")  # reference path
card_front_img = card_front_img.resize((500, 300), Image.ANTIALIAS)  # resizing and anti-aliasing
card_front = ImageTk.PhotoImage(card_front_img)  # turning into tkinter photo class

# -----right button----- #
right_button_img = Image.open("images/right.png")  # reference path
right_button_img = right_button_img.resize((100, 100), Image.ANTIALIAS)  # resizing and anti-aliasing
right_button = ImageTk.PhotoImage(right_button_img)  # turning into tkinter photo class

# -----wrong button----- #
wrong_button_img = Image.open("images/wrong.png")  # reference path
wrong_button_img = wrong_button_img.resize((100, 100), Image.ANTIALIAS)  # resizing and anti-aliasing
wrong_button = ImageTk.PhotoImage(wrong_button_img)  # turning into tkinter photo class

# TODO: Make this DRY

# --------------------CREATING CANVAS-------------------- #
canvas = tkinter.Canvas(width=600, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)  # setting canvas size

# --------------------LAYING IMAGE ON CANVAS-------------------- #
timed_flip(True)

# --------------------CREATING BUTTONS-------------------- #
rb = tkinter.Button(image=right_button, highlightthickness=0, borderwidth=0, bd=0, bg=BACKGROUND_COLOR,
                    command=lambda: timed_flip(True))
wb = tkinter.Button(image=wrong_button, highlightthickness=0, borderwidth=0, bd=0, bg=BACKGROUND_COLOR,
                    command=lambda: timed_flip(False))

# --------------------LAYING OUT OBJECTS-------------------- #
canvas.grid(row=1, column=0, columnspan=2)
rb.grid(row=2, column=0)
wb.grid(row=2, column=1)

# --------------------MAIN LOOP-------------------- #
tkinter.mainloop()

# --------------------END-------------------- #
