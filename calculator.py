import tkinter as tk

app = tk.Tk()
app.title("Basic Calculator")

e = tk.Entry(app, width=70, border=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_clicked(number):
    e.insert("end", number)


def button_clear():
    e.delete(0, "end")


def button_add():
    first_number = e.get()
    global num
    global function
    function = "addition"
    num = first_number
    e.delete(0, "end")


def button_substract():
    first_number = e.get()
    global num
    global function
    function = "substraction"
    num = first_number
    e.delete(0, "end")


def button_times():
    first_number = e.get()
    global num
    global function
    function = "multiplication"
    num = first_number
    e.delete(0, "end")


def button_divide():
    first_number = e.get()
    global num
    global function
    function = "division"
    num = first_number
    e.delete(0, "end")


def button_equal():
    second_number = e.get()
    if function == "addition":
        ans = int(num) + int(second_number)

    elif function == "substraction":
        ans = int(num) - int(second_number)

    elif function == "multiplication":
        ans = int(num) * int(second_number)

    elif function == "division":
        ans = int(num) / int(second_number)
        ans = float(ans)

    e.delete(0, "end")
    e.insert(0, ans)


b1 = tk.Button(
    app,
    text="1",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(1),
)
b2 = tk.Button(
    app,
    text="2",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(2),
)
b3 = tk.Button(
    app,
    text="3",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(3),
)
b4 = tk.Button(
    app,
    text="4",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(4),
)
b5 = tk.Button(
    app,
    text="5",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(5),
)
b6 = tk.Button(
    app,
    text="6",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(6),
)
b7 = tk.Button(
    app,
    text="7",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(7),
)
b8 = tk.Button(
    app,
    text="8",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(8),
)
b9 = tk.Button(
    app,
    text="9",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(9),
)
b0 = tk.Button(
    app,
    text="0",
    height=2,
    width=5,
    padx=40,
    pady=20,
    command=lambda: button_clicked(0),
)
clear = tk.Button(
    app,
    text="clear",
    font=("Arial", 9),
    height=2,
    width=5,
    padx=30,
    pady=20,
    bg="yellow",
    command=lambda: button_clear(),
)
equal = tk.Button(
    app,
    text="=",
    font=("Arial", 9),
    height=2,
    width=5,
    padx=30,
    pady=20,
    bg="red",
    command=lambda: button_equal(),
)
plus_btn = tk.Button(
    app, text="+", height=2, width=5, padx=30, pady=20, command=lambda: button_add()
)
minus_btn = tk.Button(
    app,
    text="-",
    height=2,
    width=5,
    padx=30,
    pady=20,
    command=lambda: button_substract(),
)
multiply_btn = tk.Button(
    app, text="X", height=2, width=5, padx=40, pady=20, command=lambda: button_times()
)
divide_btn = tk.Button(
    app, text="/", height=2, width=5, padx=40, pady=20, command=lambda: button_divide()
)

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)
b0.grid(row=4, column=0)
clear.grid(row=1, column=3)
equal.grid(row=4, column=3)

plus_btn.grid(row=2, column=3)
minus_btn.grid(row=3, column=3)
multiply_btn.grid(row=4, column=1)
divide_btn.grid(row=4, column=2)


app.mainloop()
