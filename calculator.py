def click(event):
text = event.widget.cget("text")
if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, font="Arial 20")
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    b = tk.Button(root, text=button, font="Arial 18", width=4, height=2)
    b.grid(row=row_val, column=col_val, padx=5, pady=5)
    b.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
