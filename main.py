from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
#--------------------CREATING NEW CARDS--------------------------#
data=pandas.read_csv("data/french_words.csv")

to_learn=data.to_dict(orient="records")

new_random_pair=random.choice(to_learn)
french_word=new_random_pair["French"]
translation_word=new_random_pair["English"]


def tick_button():
    global new_random_pair,flip_timer,french_word,translation_word
    window.after_cancel(flip_timer)
    to_learn.remove(new_random_pair)
    new_random_pair=random.choice(to_learn)
    french_word=new_random_pair["French"]
    translation_word=new_random_pair["English"]
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text,text=f"{french_word}",fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer=window.after(3000,func=flip_card)

def cross_button():
    global new_random_pair,flip_timer,french_word,translation_word
    window.after_cancel(flip_timer)
    new_random_pair = random.choice(to_learn)
    random_pair=new_random_pair
    french_word = new_random_pair["French"]
    translation_word = new_random_pair["English"]
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{french_word}",fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer=window.after(3000, func=flip_card)


#--------------------CARD FLIP FUNCTIONALITY---------------#
def flip_card():
    canvas.itemconfig(lang_text,text="English",fill="white")
    canvas.itemconfig(word_text,text=f"{translation_word}",fill="white")
    canvas.itemconfig(canvas_image,image=card_back_image)




#--------------------- UI SETUP ----------------------------------#
window=Tk()
window.title("Flashcard App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)


canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_image=PhotoImage(file="images/card_front.png")
card_back_image=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400,263,image=front_image)
lang_text=canvas.create_text(400,150,text="French",fill="black",font=("Ariel",40,"italic"))
word_text=canvas.create_text(400,263,text=f"{french_word}",fill="black",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

wrong_img=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_img,highlightthickness=0,bg=BACKGROUND_COLOR,relief=GROOVE,command=cross_button)
wrong_button.grid(row=1,column=0)

right_img=PhotoImage(file="images/right.png")
right_button=Button(image=right_img,highlightthickness=0,bg=BACKGROUND_COLOR,relief=GROOVE,command=tick_button)
right_button.grid(row=1,column=1)




window.mainloop()