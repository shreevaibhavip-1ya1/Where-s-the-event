from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handlekeypress(event):
    print(event.char)

window.bind("<Key>", handlekeypress)

def handleclick(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handleclick)

window.mainloop()