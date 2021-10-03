import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('300x220')
root.resizable(False, False)
root.title('UFULET')


def show_selected_size():
    showinfo(
        title='Information',
        message=selected_size.get()
    )


selected_size = tk.StringVar()
sizes = (('History', 'S'),
         ('Bohr', 'M'),
         ('20', 'L'),
         ('Quantum', 'bilgi'),
         ('Material Science', 'blgi'))



# label
label = ttk.Label(text="Which subject do you want to choose")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Submit",
    command=show_selected_size)

button.pack(fill='x', padx=5, pady=5)


root.mainloop()