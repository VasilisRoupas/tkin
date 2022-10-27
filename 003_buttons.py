from tkinter import *

root = Tk()

#1
# myButton = Button(root, text="Click Me!")

#2
# myButton = Button(root, text="Click Me!", state=DISABLED)

#3
# myButton = Button(root, text="Click Me!", padx=50)

#4
# myButton = Button(root, text="Click Me!", padx=50, pady=50)

#5
# myButton = Button(root, text="Click Me!", pady=50)

#6
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!")

#7
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick)

#8
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick())

#9
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick, fg='blue')

#10
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick, fg='blue', bg='red')

#11
# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!")
#     myLabel.pack()
#
# myButton = Button(root, text="Click Me!", command=myClick, fg='blue', bg='#ffffff')

#12
def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg='blue', bg='#000000')


#common
myButton.pack()

root.mainloop()
