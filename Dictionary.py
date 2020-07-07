# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:03:27 2020

@author: IMPOSSIBLE
"""


def dummy():
    pass


from tkinter import Tk, IntVar
from tkinter import Label
from tkinter import BOTH
from tkinter import Entry
from tkinter import Button
from tkinter import Message
from tkinter import Frame

import json
import sys
import os
import time
from difflib import get_close_matches

data = json.load(open("data.json"))

root = Tk()
root.title("DICTIONARY")
root.geometry("600x500")

var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

label1 = Label(root, text="WELCOME TO THE BEST DICTIONARY", bg="black", fg="red", font=("arial", 20, "bold"))
label1.pack(fill=BOTH, padx=3, pady=23)

label2 = Label(root, text="Enter the Word: ", font=("arial", 10))
label2.place(x=100, y=140)

entry1 = Entry(root, width=40)
entry1.place(x=200, y=142)

entry1.after(100, entry1.focus())


def restart():
    root.destroy()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def create_search_interface():
    label1_ = Label(root, text="WELCOME TO THE BEST DICTIONARY", bg="black", fg="red", font=("arial", 20, "bold"))
    label1_.pack(fill=BOTH, padx=3, pady=23)

    label2_ = Label(root, text="Enter the Word: ", font=("arial", 10))
    label2_.place(x=100, y=140)

    entry1_ = Entry(root, width=40)
    entry1_.place(x=200, y=142)

    entry1_.after(100, entry1.focus())
    submit_ = Button(root, text="SUBMIT", bg="red", fg='white', font=('arial', 10),
                     command=button_action)

    submit_.place(x=240, y=210)


def check_choice(choice, func=dummy):
    if (choice.lower() == 'y' or choice.lower() == 'n'):
        pass
    else:
        print("Invalid Choice! Please Enter Again")
        func()


def get_meaning(word):
    return data[word]


def close_words(word, i):
    return get_close_matches(word, data.keys[i])


def check_close_words(word):
    check1 = input("Did you mean: {}. Type 'y' for Yes / 'n' for No".format(close_words(word, 0)))
    check_choice(check1, func=check_close_words)
    if check1.lower() == 'y':
        return get_meaning(close_words(word, 0)), close_words(word, 0)
    check2 = input("Did you mean: {}. Type 'y' for Yes / 'n' for No".format(close_words(word, 1)))
    check_choice(check2, func=check_close_words)
    if check2.lower() == 'y':
        return get_meaning(close_words(word, 1)), close_words(word, 1)
    invalid = "Invalid Word! Please Try Again!"
    return invalid


def yes_button(label3, label4, new_word, yes, no):
    out = get_meaning(new_word)
    label3.after(25, label3.destroy())
    label4.after(25, label4.destroy())
    yes.after(50, yes.destroy())
    no.after(25, no.destroy())

    label5 = Label(root, text=new_word, bg='black', fg='white', font=("arial", 18, "bold"))
    label5.place(x=50, y=100)

    label6 = Message(root, text=out, fg='blue', font=('arial', 14), width=500)
    label6.place(x=50, y=150)

    btn_exit = Button(root, text="EXIT", bg='red', fg='white', font=('arial', 13),
                      command=lambda: [func2, root.destroy(), if_button])
    btn_exit.place(x=30, y=400)

    btn_search_again = Button(root, text="SEARCH ANOTHER", bg='red', fg='white', font=('arial', 13),
                              command=lambda: [func3, restart(), if_search_button])
    btn_search_again.place(x=390, y=400)
    if if_button():
        btn_exit.wait_variable(var)
    if if_search_button():
        btn_exit.wait_variable(var1)


def no_button(label3, label4, new_word, yes, no):
    label3.after(25, label3.destroy())
    label4.after(25, label4.destroy())
    yes.after(25, yes.destroy())
    no.after(50, no.destroy())

    label_invalid = Label(root, text="Invalid Word! Please Check Again!", fg='red', font=('arial', 18, "bold"))
    label_invalid.place(x=80, y=100)

    btn_exit = Button(root, text="EXIT", bg='red', fg='white', font=('arial', 13),
                      command=lambda: [func2, root.destroy(), if_button])
    btn_exit.place(x=30, y=400)

    btn_search_again = Button(root, text="SEARCH ANOTHER", bg='red', fg='white', font=('arial', 13),
                              command=lambda: [func3, restart(), if_search_button])
    btn_search_again.place(x=390, y=400)
    if if_button():
        btn_exit.wait_variable(var)
    if if_search_button():
        btn_exit.wait_variable(var1)


def button_action():
    word = entry1.get()
    if word in data:
        main_word = word
        out = get_meaning(word)

        label2.destroy()
        entry1.destroy()
        submit.destroy()

        label3 = Label(root, text=main_word, bg='black', fg='white', font=("arial", 18, "bold"))
        label3.place(x=50, y=100)

        label4 = Message(root, text=out, fg='blue', font=('arial', 14), width=500)
        label4.place(x=50, y=150)

        btn_exit = Button(root, text="EXIT", bg='red', fg='white', font=('arial', 13),
                          command=lambda: [func2, root.destroy(), if_button])
        btn_exit.place(x=30, y=400)

        btn_search_again = Button(root, text="SEARCH ANOTHER", bg='red', fg='white', font=('arial', 13),
                                  command=lambda: [func3, restart(), if_search_button])
        btn_search_again.place(x=390, y=400)
        if if_button():
            btn_exit.wait_variable(var)
            raise SystemExit
        if if_search_button():
            btn_exit.wait_variable(var1)



    else:
        label2.destroy()
        entry1.destroy()
        submit.destroy()

        main_word = word
        label3 = Label(root, text=main_word, bg='black', fg='white', font=("arial", 18, "bold"))
        label3.place(x=51, y=100)

        alt_word = get_close_matches(main_word, data.keys())[0]

        label4 = Label(root, text="Did you mean: {}".format(get_close_matches(main_word, data.keys())[0]),
                       fg='blue', font=("arial", 18, "bold"))
        label4.place(x=50, y=160)

        yes = Button(root, text='YES', bg='red', fg='white', font=('arial', 10, 'bold'),
                     command=lambda: [func1(), yes_button(label3, label4, alt_word, yes, no), yes_wait()])

        yes.place(x=220, y=240)
        no = Button(root, text='NO', bg='red', fg='white', font=('arial', 10, 'bold'),
                    command=lambda: [func2, no_button(label3, label4, alt_word, yes, no)])
        no.place(x=300, y=240)

        if yes_wait():
            yes.wait_variable(var)
        else:
            no.wait_variable(var1)


def func1():
    var.set(1)


def func2():
    var1.set(1)


def func3():
    var2.set(1)


def func4():
    var3.set(1)


def yes_wait():
    return True


def if_button():
    return True


def if_search_button():
    return True


def enter(event):
    button_action()


submit = Button(root, text="SUBMIT", bg="red", fg='white', font=('arial', 10),
                command=button_action)

submit.place(x=240, y=210)

root.mainloop()
