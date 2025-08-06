'''
Jake Kostenko
Testing gui for voice recognition project
'''
import tkinter as tk

root = tk.Tk()
root.title("hamburger")

mainframe = tk.Frame(root, padx=0, pady=50)
mainframe.grid(column=0, row=0, sticky=tk.N)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text = tk.Label(mainframe, text="hamburger").grid(column=1, row=1, sticky=tk.N)

root.mainloop()