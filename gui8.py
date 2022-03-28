from tkinter import *

root = Tk()
def fun(event):
    print(f"The coordinates of x and y where u click on Button{event.x},{event.y}")

root.title('GUI')

root.geometry('644x344')

button = Button(root, text='click here')
button.pack()

button.bind('<Button-1>', fun)
button.bind('<Double-1>', quit)


root.mainloop()