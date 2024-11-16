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
 pop_up = messagebox.showinfo("Alert!", "Do you wish to continue with the denomination counting?")
 if pop_up == "ok":
  topwin()

atm=Button(window, text="Lets get started!", bg="black", fg="white", command=msg)
atm.pack()

#function for opening the top window
def topwin():
 top = Toplevel()
 top.configure(bg="black")
 top.geometry("400x450")
 top.title("Denominations calculator")

 label= Label(top, text="enter the total ammount", fg="yellow", bg="Black")
 label.place(x=150 ,y=20)
 entry= Entry(top, bg="white")
 entry.place(x=155 ,y=50)

 button = Button(top , text="calculate" , bg="red")
 
 button.place(x=185, y=75)
 label11 = Label(top, text="here are the number of notes for each denomination", fg="yellow", bg="black")
 label11.place(x=70,y=150)
 label33= Label(top, text="10000",fg="yellow", bg="black")
 label33.place(x=70,y=180)
 entry33=Entry(top)
 entry33.place(x=120,y=180)


 label55= Label(top, text="5000",fg="yellow", bg="black")
 label55.place(x=70,y=205)
 entry55=Entry(top)
 entry55.place(x=120,y=205)

 label77= Label(top, text="1000",fg="yellow", bg="black")
 label77.place(x=70,y=230)
 entry77=Entry(top)
 entry77.place(x=120,y=230)


 top.mainloop()


window.mainloop()