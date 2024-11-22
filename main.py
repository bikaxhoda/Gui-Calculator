import tkinter as tk 

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation +=str(symbol)
    Text_result.dalete(1.0,"end")
    Text_result.insert(1.0, calculation)
    
    ""
def evaluated_calculation():
    pass

def clear_field():
    pass


root = tk.Tk()
root.geometry("300*275")

Text_result = tk.Text(root, height=2, width=16, font=("Arial",24))
root.mainloop()