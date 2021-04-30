import tkinter


window = tkinter.Tk(className="Random Number Generator!")
window.geometry("800x600")
window.configure(bg='black')

(tkinter.Message(window, aspect=200, text="What range would you like the number to be within?")).pack()

window.mainloop()
