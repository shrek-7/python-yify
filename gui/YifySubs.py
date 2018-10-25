from tkinter import *

from subs import search_subtitles

window = Tk()
window.wm_title(string="Yify Subtitles")

def get_subs():
    search_subtitles(e1_value.get())


l1 = Label(window, text="Movie Name : ")
l1.grid(row=1, column=0,  padx=10, pady=10)

l2 = Label(window, text="Find your file in F:\subtitle.zip ")
l2.grid(row=3, column=0)

b1 = Button(window, text="Download Subtitle", command=get_subs, relief=RAISED, activebackground='lightgreen', pady=5)
b1.grid(row=2, column=0, columnspan=2, pady=10)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=30)
e1.grid(row=1, column=1, padx=10, pady=10)


window.mainloop()


