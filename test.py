import tkinter as tk

def test():
    root = tk.Tk()
    root.title("tkinter Test")
    label = tk.Label(root, text="tkinter is working!")
    label.pack()
    root.mainloop()

test()

