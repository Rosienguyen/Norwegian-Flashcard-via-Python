import pandas as pd
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS

BACKGROUND_COLOR = "#B1DDC6"
import random
from tkinter import *
to_learn = {}
current_card = {}
source = input("Choose between (pavei, stein): ")

# if you like to have it random, you can use this code
# lesson = random.choice(range(2,17))

# if you like to have it selected, you should use this code
lesson = input("Lesson to study:")


try: # try running this line of code
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    
    original_data = pd.read_csv(f"{source}/lesson{lesson}.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#------------------------ Generating a Norsk word ----------
index = -1

def next_card():
    
    global current_card, index, cur_text
    index += 1
    if index >= len(to_learn):
        # End the game if all cards have been shown
        window.quit()
        return

    current_card = to_learn[index]

    # choose random language
    cur_text = random.choice(["EN", 'NO'])
    canvas.itemconfig(card_title, text =  f"{cur_text}_{index}", fill="black")
    canvas.itemconfig(card_word, text=current_card[cur_text], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
   

def flip_to_en():
    global index

    canvas.itemconfig(card_title, text = f"EN_{index}", fill = "black")
    canvas.itemconfig(card_word, text=current_card["EN"], fill = "black")
    canvas.itemconfig(card_background, image=card_front_img)
    # canvas.itemconfig()

def flip_to_no():
    global index 
    canvas.itemconfig(card_title, text = f"NO_{index}", fill = "black")
    canvas.itemconfig(card_word, text=current_card["NO"], fill = "black")
    canvas.itemconfig(card_background, image=card_front_img)
    # canvas.itemconfig()

def play_sound():
    global index
    cur_text = "NO"
    # Create a gTTS object
    tts = gTTS(current_card[cur_text], lang = cur_text.lower())

    # Save the audio as a byte array in memory using BytesIO
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)

    # Load the audio from the byte array using AudioSegment
    audio = AudioSegment.from_file(audio_bytes, format="mp3")

    # Play the audio using pydub
    play(audio)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("pavei/words_to_learn.csv", index=False)
    # index = false discrads the index numbers
    next_card()


#------------------------ FlashCard UI Setup -------------------------------

window = Tk()
window.title(f"Flashcard from {source} for Lesson {lesson}")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# flip_timer = window.after(3000, func=flip_card) # 3000 milliseocnds = 3 seconds

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 80, text="Title", font=("Ariel", 20, "italic"))
# Positions are related to canvas so 400 will be halfway in width
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 20, "bold"), tags="word", width=700, justify="center")

# canvas should go in the middle
canvas.grid(row=0, column=0, columnspan=4)

left_image = PhotoImage(file="./images/speaker.png")
unknown_button = Button(image=left_image, command = play_sound)
unknown_button.grid(row=1, column=0, sticky="W")

right_image = PhotoImage(file="./images/arrow_right_resized.png")
known_button = Button(image = right_image, command = next_card)
known_button.grid(row=1, column=3, sticky="E")

no_image = PhotoImage(file="./images/Norway_resized.png")
known_button = Button(image=no_image, command = flip_to_no)
known_button.grid(row=1, column=1, sticky="E")

en_image = PhotoImage(file='./images/USA_resized.png')
flip_button = Button(image = en_image, text = 'flip', command = flip_to_en)
flip_button.grid(row = 1, column = 2, sticky = 'W' )

next_card()
# prev_card()
window.mainloop()


