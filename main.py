from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox

#setting up the main window

window=Tk()
window.title("Denomination counter")
window.config(bg="light blue")
window.geometry("500x500")

#adding the image in the main window

counter=Image.open("app_img.jpg")

#resizing the image

counter=counter.resize((200,200))

cregister=ImageTk.PhotoImage(counter)
label=Label(window, image=cregister, bg="black")
label.pack()
#adding text

intro=Label(window,text="Hey user! Welcome to the denomination counter application!", bg="light blue")
intro.pack()

#button
def msg():
 messagebox.showinfo("Alert!", "Do you wish to continue with the denomination counting?")
atm=Button(window, text="Lets get started!", bg="black", fg="white", command=msg)
atm.pack()



window.mainloop()