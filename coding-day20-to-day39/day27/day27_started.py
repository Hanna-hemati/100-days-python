import tkinter

window = tkinter.Tk()

window.title("This is my Tk window")
window.minsize(width=500, height=500)
my_label = tkinter.Label(text= "LABEL", font= ("Arial", 20))
my_label.pack()







window.mainloop()