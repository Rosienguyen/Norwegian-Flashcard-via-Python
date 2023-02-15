import pandas

BACKGROUND_COLOR = "#B1DDC6"
import random
from tkinter import *
import pandas as pd
to_learn = {}
current_card = {}

lesson = random.choice(range(2,17))

try: # try running this line of code
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    # If for the first time we are running it
    # the words_to_learn.csv file might not be present
    # and FileNotFoundError might pop up
    
    original_data = pandas.read_csv(f"output/lesson{lesson}.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# data = pd.read_csv("./data/words_to_learn.csv")
# word_dict = {row.Norsk:row.English for (index, row) in df.iterrows()}
# spits out a list of dictionaries containing Norsk word and english translation
# print(word_dict)

#------------------------ Generating a Norsk word ----------

def next_card():
    global current_card #, flip_timer
    # window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # Norsk_word = random_pair['Norsk']

    # choose random language
    cur_text = random.choice(["EN", 'NO'])
    canvas.itemconfig(card_title, text = cur_text, fill="black")
    canvas.itemconfig(card_word, text=current_card[cur_text], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # flip_timer = window.after(30000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text = "EN", fill = "black")
    canvas.itemconfig(card_word, text=current_card["EN"], fill = "black")
    canvas.itemconfig(card_background, image=card_back_img)
    # canvas.itemconfig()

def flip_card_again():
    canvas.itemconfig(card_title, text = "NO", fill = "black")
    canvas.itemconfig(card_word, text=current_card["NO"], fill = "black")
    canvas.itemconfig(card_background, image=card_back_img)
    # canvas.itemconfig()

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("output/words_to_learn.csv", index=False)
    # index = false discrads the index numbers
    next_card()
#------------------------ FlashCard UI Setup -------------------------------

window = Tk()
window.title(f"Flashcard for Lesson {lesson}")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# flip_timer = window.after(3000, func=flip_card) # 3000 milliseocnds = 3 seconds

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 20, "italic"))
# Positions are related to canvas so 400 will be halfway in width
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 20, "bold"), tags="word")
# canvas should go in the middle
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, command = next_card)
unknown_button.grid(row=1, column=0, sticky="W")

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, command=flip_card_again)
known_button.grid(row=1, column=2, sticky="E")


flip_image = PhotoImage(file='./images/tomato_resized.png')
flip_button = Button(image = flip_image, text = 'flip', command=flip_card)
flip_button.grid(row = 1, column = 1, sticky = 'E' )

next_card()
window.mainloop()


