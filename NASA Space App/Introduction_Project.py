from tkinter import *

root = Tk()
root.title("NASA Space App GUI Model for Materials Science & Quantum Model of Atoms, Compounds ")
root.iconbitmap("NASA.ico")


# İSİM GİRME
name_entry = Entry(root, width=60, borderwidth=5, fg="black", bg="white")
name_entry.grid(row=0, column=0)
name_entry.insert(0, "Please Enter your name: ")

# İSİM YÜKLEME BUTONU - YAZI
def buttonClick():
    greeting = Label(root, text="Hello" + name_entry.get()[23:] + "!" + """
    Welcome to UFULET's Graphical User Interface! In this GUI; you will gain advanced experience about Background History
    of Atoms, Classical & Quantum Models of Atoms, Structure & Features of Periodic Table, Bounds of Compounds and much more
    in a simple but educative way!

Because our platform has variety of choices; you can pick whatever you want to learn our practice.
To learn about the history of atom models; select "History".
To learn more about Bohr Atom Model and it's features; select "Bohr".
To learn more about first 20 elements and it's advanced properties; select "20".
To learn about exciting Quantum Models of Atom; select "Quantum".
To make exercises about Quantum Model of Atom using our own made calculator; select "Exercise".
To learn advanced topics About Material Science and get access to huge data; select "Material Science".""")
    greeting.grid(row=1, column=0)

name_buton = Button(root, text="Submit Your Name", command=buttonClick, fg="black", bg="white")
name_buton.grid(row=0, column=5, columnspan=1)





root.mainloop()



