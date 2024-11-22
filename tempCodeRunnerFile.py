import tkinter as tk
from tkinter import messagebox

def click(event):
    global entry_value
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry_value.get())
            entry_value.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            entry_value.set("")
    elif text == "C":
        entry_value.set("")
    else:
        entry_value.set(entry_value.get() + text)

# Creating the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry widget for the calculator
entry_value = tk.StringVar()
entry = tk.Entry(root, textvar=entry_value, font="Arial 20", bd=5, relief=tk.SUNKEN, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame
frame = tk.Frame(root)
frame.pack()

# Button layout
button_texts = [
    "c", "/", "*", "-",
    "7", "8", "9", "+",
    "4", "5", "6", "",
    "1", "2", "3", ""
    "0",  "", ".", ""
]

# Adding buttons to the frame
for i, text in enumerate(button_texts):
    button = tk.Button(frame, text=text, font="Arial 18", relief=tk.RAISED, width=5, height=2)
    button.grid(row=i//4, column=i%4, padx=5, pady=5)
    button.bind("<Button-1>", click)

# Run the application
root.mainloop()
