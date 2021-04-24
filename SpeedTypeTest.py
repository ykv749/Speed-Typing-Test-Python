import random
from tkinter import *
import tkinter.font as tkFont
import time

#CREATING TKINTER WINDOW
root = Tk(className=" Speed Type Test")
root.geometry("750x500")

#BACKGROUND OF THE WINDOW 
root.configure(background = "#e7d9ea")

#ICON FOR THE PROJECT
ico = PhotoImage(file='icon1.png')
root.iconphoto(False, ico)
root.iconbitmap("icon1.ico")

#TITLE FOR THE PROJECT
title = Label(root, text="TYPING SPEED TEST", anchor=CENTER, font="Elephant 35 bold", bg="#350b40", fg='#F2BC94', relief="solid")
title.place(x=65, y=8)

#INPUT BOX
input_font = ('Centaur',30)
input_box = Entry(root, width='31', bg="#f3bda1", fg="#687980",font=input_font)
input_box.place(x=63, y=300)
input_box.focus()

#Clear ENTRY
def clearfunc():
    input_box.delete(0, 'end')

#RESET BUTTON
reset_btn = Button(root, text="RESET", bg="#114e60", fg="#114e60", font="Garamond 15", padx=15, pady=7, relief=RAISED,
               command=clearfunc)
reset_btn.place(x=90, y=380)

#SENTENCES
fontStyle = tkFont.Font(family="Perpetua", size=18)
text = Label(root, height='7', width='51', fg='#16c79a', bg='#11698e', font=fontStyle, wraplength=500, anchor=CENTER,
             justify=LEFT)
text.place(x='62', y='88')

def randomTXT():
    f = open('Sentence.txt').read()
    sentences = f.split('\n')
    display = random.choice(sentences)
    text.config(text=display)
randomTXT()

#NEW TEXT BUTTON
new_text_btn = Button(root, text="NEW TEXT", bg='#687980', fg='#114e60', font="Garamond 15", padx=15, pady=7, relief=RAISED, command=randomTXT)
new_text_btn.place(x=300, y=380)

# CALCULATE TIME TAKEN,TOTAL WORDS,SPEED
t0 = time.time()
def calculate(*args,**kwargs):
    t1 = time.time()
    st = input_box.get()
    w_count = len(st.split())
    mylabel = Label(root, text="TOTAL WORDS: " + str(w_count))
    mylabel.place(x=85, y=435)
    mylabel = Label(root, text="TIME TAKEN: " + str(round(t1 - t0)))
    mylabel.place(x=315, y=435)
    if (t1 - t0) >= 60:
        mylabel = Label(root, text="SPEED: POOR")
        mylabel.place(x=533, y=435)
    elif(t1 - t0) >= 30 and (t1 - t0) <= 60    :
        mylabel = Label(root, text="SPEED: AVERAGE")
        mylabel.place(x=533, y=435)
    else:
        mylabel = Label(root, text="SPEED: EXCELLENT")
        mylabel.place(x=533, y=435)

calculate()
result_btn = Button(root, text="RESULT", bg="#93329e", fg="#440a67",font="Garamond 15", padx=1, pady=7, relief=RAISED, command=calculate).place(x=550,y=380)
root.mainloop()