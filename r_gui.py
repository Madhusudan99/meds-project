import tkinter as tk
from tkinter import messagebox
from speech import HiddenMarkovModel

def popup():
    speech_obj = HiddenMarkovModel()
    text, details = speech_obj.recognize()
    message = "Text: " + text +"\n" + "Details:\n" + details
    messagebox.showinfo("Message", message)
    
def create_diag():
    m = tk.Tk() 
    m.title("Dr. Speech")
    #widgets are added here
    speech_obj = HiddenMarkovModel()
    w=tk.Button(m, activebackground='green', text='Speek', width=55, command=popup)
    w.pack() 
    m.mainloop()

if __name__ == '__main__':
    create_diag()
