import tkinter as tk
from tkinter import ttk

def handle_button_click(clicked_button_text):
    current_text = result_var.get()

    if clicked_button_text == "=":
        try:

            expression = current_text.replace("÷", "/").replace("x", "*")
            result = eval(expression)

            if result.is_integer():
                result = int(result)

                result_var.set(result)
        except Exception as e:
            result_var.set("Error")

    elif clicked_button_text == "C":
            result_var.set("")
    elif clicked_button_text == "%":
         
         try:
              current_number = float(current_text)
              result_var.set(current_number / 100)
         except  ValueError:
              result_var.set("Error")

    elif clicked_button_text == '±':
         try:
              current_number = float(current_text)
              result_var.set(-current_number)
         except ValueError:
              result_var.set("Error")
    else:
         result_var.set(current_text + clicked_button_text)


    root = tk.Tk()
    root.title("Calculator")

    result_var = tk.StringVar()
    result_entry = ttk.Entry(root, textvariable=result_var,
    font=("Helvetica", 24), justify='right')
    result_entry.grid(row=0, column=0, columnspan=4,
    sticky="nsew")

    buttons = [
         ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
         ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("x", 2, 3),
         ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
         ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
         ("0", 5, 0), (".", 5, 1), ("=", 5, 2)
    ]

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Tbutton", font=("Helvetica", 16), width=10, height=4)

    for button_info in buttons:
         button_text, row, col = button_info[:3]
         colspan = button_info[3] if len(button_info) > 3 else 1
         button = ttk.Button(root, text=button_text,
    command=lambda text=button_text: handle_button_click(text),
    style="TButton")
         button.grid(row=row, column=col, columnspan=colspan, 
    sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)
         
    for i in range(6):
         root.grid_rowconfigure(i, weight=1)

    for i in range(4):
         root.grid_columnconfigure(i, weight=1)

    width = 500
    height = 700
    root.geometry(f"{width}x{height}")

    root.resizable(False, False)

    