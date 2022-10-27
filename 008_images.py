import os

from tkinter import *
from PIL import ImageTk, Image
#find path_used_for_python
# import os
# import sys
#
# print(os.path.dirname(sys.executable))
#run
#/path_used_for_python/used/python -m pip install pillow

root = Tk()

#1
# root.iconbitmap("c:/Users/067410726/PycharmProjects/pythonProject/tkin/images/python.ico")

#2
# root.iconbitmap("c:/Users/067410726/PycharmProjects/pythonProject/tkin/images/python.ico")
#
# button_quit = Button(root, text="Exit Program", command=root.quit)
# button_quit.pack()

#3
# root.iconbitmap(os.path.dirname(__file__) + "/images/python.ico")
#
# button_quit = Button(root, text="Exit Program", command=root.quit)
# button_quit.pack()

#4
root.iconbitmap(os.path.dirname(__file__) + "/images/python.ico")

my_img = ImageTk.PhotoImage(Image.open("images/IBM.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

#common
root.mainloop()

