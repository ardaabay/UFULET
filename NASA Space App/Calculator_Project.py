# Importing and Naming Tkinter.
from tkinter import *
root = Tk()
root.title("NASA Space App Calculator")
root.iconbitmap(r"NASA.ico")

# Creating the Imput Part
numberEntry = Entry(root, width=35, borderwidth=10)
numberEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#numberEntry.insert(0, "Enter your number: ")

# Defining our functions
def button_click(number):
    current = numberEntry.get()
    numberEntry.delete(0, END)
    numberEntry.insert(0, str(current) + str(number))

def button_clear():
    numberEntry.delete(0, END)
    #numberEntry.insert(0, "Enter your number: ")

def button_add():
    first_number = numberEntry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    numberEntry.delete(0, END)


def button_equal():
    second_number = numberEntry.get()
    numberEntry.delete(0, END)
    if math == "addition":
        numberEntry.insert(0, f_num + int(second_number))

    if math == "subtraction":
        numberEntry.insert(0, f_num - int(second_number))

    if math == "multiplication":
        numberEntry.insert(0, f_num * int(second_number))

    if math == "division":
        numberEntry.insert(0, f_num / int(second_number))



def button_subtract():
    first_number = numberEntry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    numberEntry.delete(0, END)

def button_multiply():
    first_number = numberEntry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    numberEntry.delete(0, END)

def button_divide():
    first_number = numberEntry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    numberEntry.delete(0, END)


# Creating buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
button_10 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))
button_quit = Button(root, text="Exit", padx=34, pady=20, command=root.quit)

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="x", padx=41, pady=20, command=button_multiply)
button_divide = Button(root, text="÷", padx=39, pady=20, command=button_divide)

button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(root, text="AC", padx=96, pady=20, command=button_clear)

#Sorting the buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_10.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=6, column=0)
button_divide.grid(row=6, column=1)


button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=2)
button_quit.grid(row=6, column=2)


root.mainloop()