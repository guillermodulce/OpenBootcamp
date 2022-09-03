from tkinter import *

master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Rusia",
             "Canadá", 
             "Estados Unidos", 
             "China", 
             "Brasil", 
             "Australia", 
             "India", 
             "Argentina",
             "Kazajistán",
             "Argelia"]:
             
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Los países más grandes del mundo")

label.pack()
master.mainloop()