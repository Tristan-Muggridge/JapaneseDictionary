import tkinter as tk
from tkinter.constants import DISABLED, END, INSERT, WORD
from functions import *
from classes import *
from fetcher import *
from functools import partial

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.url = tk.Entry(self)
        self.url.grid(row=0,column=1, pady=10)

        self.submit = tk.Button(self, text="Submit", command=self.submit)
        self.submit.grid(row=1,column=1, padx=20,pady=20)

    def submit(self):
        entries = parse_search(search(self.url.get()))

        for entry in range(5):
            frame = tk.LabelFrame(self, text=f"{entries[entry].kanji}・{entries[entry].hiragana}", pady=1,padx=5)
            frame.grid(row=entry+3, column=1, pady=10,padx=30)
            
            def_ = tk.Label(frame, text="Definition")
            def_.grid(row=1, column=0)
            
            text = tk.Text(frame, width=100, height=5, wrap=WORD, yscrollcommand=True)
            text.insert(INSERT, entries[entry].meanings)
            text.grid(row=2, column=0)
    
        

root = tk.Tk()
root.geometry("1920x1080")
root.title("凄い辞書")
app = Application(master=root)
app.mainloop()