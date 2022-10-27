import os

from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.iconbitmap(os.path.dirname(__file__) + "/images/python.ico")

my_img1 = ImageTk.PhotoImage(Image.open("images/IBM.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/DB2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/NETEZZA.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/PYTHON.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/JAVA.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img4)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<")
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>")

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

#common
root.mainloop()
