from tkinter import *

root = Tk()

#1
# e = Entry(root)
# e.pack()
#
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick)

#2
# e = Entry(root, width=50)
# e.pack()
#
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick)

#3
# e = Entry(root, width=50, bg='blue')
# e.pack()
#
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick)

#4
# e = Entry(root, width=50, bg='blue', fg='white')
# e.pack()
#
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick)

#5
# e = Entry(root, width=50, borderwidth=5)
# e.pack()
#
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick)

#6
# e = Entry(root, width=50)
# e.pack()
#
# def myClick():
#     myLabel = Label(root, text=e.get())
#     myLabel.pack()
#
# myButton = Button(root, text="Entrer Your Name", command=myClick)

#7
# e = Entry(root, width=50)
# e.pack()
#
# def myClick():
#     myLabel = Label(root, text="Hello " + e.get())
#     myLabel.pack()
#
# myButton = Button(root, text="Entrer Your Name", command=myClick)

#8
# e = Entry(root, width=50)
# e.pack()
#
# def myClick():
#     hello = "Hello " + e.get()
#     myLabel = Label(root, text=hello)
#     myLabel.pack()
#
# myButton = Button(root, text="Entrer Your Name", command=myClick)

#9
e = Entry(root, width=50)
e.pack()
e.insert(0, "Entrer Your Name:")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Entrer Your Name", command=myClick)

#common
myButton.pack()

root.mainloop()
