import tkinter as tk
from tkinter import Entry
from tkinter import messagebox
from speech import HiddenMarkovModel

class SpeechGUI():

    def __init__(self):
        self.phone_numbers = []
        self.m = tk.Tk() 
        self.m.title("Dr. Speech")
        #widgets are added here
        self.e = Entry(self.m, width=55, borderwidth=5)
        self.e.pack()
        self.w=tk.Button(self.m, activebackground='green', text='Speek', width=55, command=self.popup)
        self.w.pack() 
        self.m.mainloop()
    
    def popup(self):
        self.phone_numbers.append(self.e.get())
        speech_obj = HiddenMarkovModel()
        text, details = speech_obj.recognize(mobile_number=self.phone_numbers[-1])
        message = "Text: " + text +"\n" + "Details:\n" + details + "\nMessage sent to: " + self.phone_numbers[-1]
        messagebox.showinfo("Message", message)
    

if __name__ == '__main__':
    gui_obj = SpeechGUI()
    #gui_obj.main_window()