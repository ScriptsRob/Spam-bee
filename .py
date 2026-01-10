import customtkinter as ctk
import pyautogui as pg
import time
from PIL import Image
import os, sys

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

bee_img = resource_path("Bee.png")
bee_ico = resource_path('bee.ico')

root = ctk.CTk()
root.iconbitmap(bee_ico)
root.geometry('300x400')
root.resizable(0,0)
root.config(bg='lightyellow')
root.title('SpamBee')

bee = ctk.CTkImage(
    Image.open(bee_img),
    size=(60, 60)
)

def only_numbers(new_value):
    return new_value.isdigit() or new_value == ""

def spam_func():
    entered_number = count.get()
    entered_text = word.get()
    if not entered_number:
        pg.alert("Write a number!")
        return
    elif not entered_text:
        pg.alert('Write a word!')
        return
    entered_number = int(entered_number)
    if entered_number > 1000:
        pg.alert("Max number is 1000!")
        return
    pg.alert('Switch to the window you want to spam.\nSpam starts in 2 seconds')
    time.sleep(2)
    for i in range(entered_number):
        pg.write(entered_text)
        pg.press('enter')

vcmd = root.register(only_numbers)

bee_ = ctk.CTkLabel(root,
                    width=20,
                    height=50,
                    text='',
                    image=bee,
                    fg_color='Lightyellow',
                    corner_radius=15,
                    bg_color='Lightyellow'
)
bee_.place(x=225,y=340)

name = ctk.CTkLabel(root,
                    width=60,
                    height=40,
                    fg_color='Black',
                    text='SpamBee',
                    text_color='Yellow',
                    corner_radius=15,
                    font=('Cooper black',17),
                    bg_color='Lightyellow'
)
name.place(x=100,y=10)

count = ctk.CTkEntry(root,
                     width=220,
                     height=60,
                     font=('Cooper black', 18),
                     corner_radius=15,
                     fg_color='yellow',
                     text_color='Black',
                     placeholder_text_color='Black',
                     validate="key",
                     validatecommand=(vcmd, "%P"),
                     placeholder_text='Write a num(max 1000)',
                     bg_color='Lightyellow'
)
count.place(x=40,y=70)

word = ctk.CTkEntry(root,
                    width=220,
                    height=60,
                    placeholder_text='Write a word',
                    font=('Cooper black', 18),
                    corner_radius=15,
                    fg_color='yellow',
                    text_color='Black',
                    placeholder_text_color='Black',
                    bg_color='Lightyellow'
)
word.place(x=40,y=140)

spam = ctk.CTkButton(root,
                     width=220,
                     height=60,
                     text='Spam',
                     corner_radius=15,
                     fg_color='Black',
                     bg_color='Lightyellow',
                     text_color='Yellow',
                     font=('Cooper black', 18),
                     command=spam_func
)
spam.place(x=40,y=280)

root.mainloop()
