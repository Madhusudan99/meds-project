import tkinter as tk
from speech import GSpeech

def create_diag():
    m = tk.Tk() 
    #widgets are added here 
    speech_obj = GSpeech()
    w=tk.Button(m, activebackground='green', text='Speek', width=25, command=speech_obj.recognize)
    w.pack() 
    m.mainloop()
    print(speech_obj.text) 

if __name__ == '__main__':
    create_diag()