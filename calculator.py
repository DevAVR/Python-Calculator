from tkinter import *
from tkinter import messagebox

# Funtion for Performing Button Operations.
def insert_text(text):
    """
    A Button Listener which inserts the Values to Input Field.
    """
    if text_field.get() == "0":
        text_field.set("")
    text_field.set(text_field.get() + text)


def back_text():
    """
    A Funtion for Backspace Funtionality.
    """
    text_field.set(text_field.get()[:-1])
    if text_field.get() == "":
        text_field.set("0")


def clear_text():
    """
    A Funtion for Clearing Input Field.
    """
    text_field.set("0")


def calculate():
    """
    A Funtion for Arithmetic Calculation.
    """
    try:
        result = eval(text_field.get())
        text_field.set(result)
    except:
        messagebox.showerror("Error", "Error : Inavlid Operation")
        text_field.set("0")


# GUI Settings
screen = Tk()
screen.geometry("500x500")
screen.title("Calculator")
screen.configure(bg="#dd29e3")

text_field = StringVar()
text_field.set("0")

# Input Field and Buttons.
input_field = Entry(
    screen,
    state=DISABLED,
    justify=RIGHT,
    textvariable=text_field,
    font=("Calibri", 22, "bold"),
    width=30,
    cursor="pirate",
)
button7 = Button(
    text="7",
    width=4,
    height=2,
    command=lambda: insert_text("7"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
button8 = Button(
    text="8",
    width=4,
    height=2,
    command=lambda: insert_text("8"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
button9 = Button(
    text="9",
    width=4,
    height=2,
    command=lambda: insert_text("9"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonDiv = Button(
    text="/",
    width=4,
    height=2,
    command=lambda: insert_text("/"),
    bd=4,
    bg="#fc6203",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonBrace1 = Button(
    text="(",
    width=4,
    height=2,
    command=lambda: insert_text("("),
    bd=4,
    bg="#fc6203",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonBrace2 = Button(
    text=")",
    width=4,
    height=2,
    command=lambda: insert_text(")"),
    bd=4,
    bg="#fc6203",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
button4 = Button(
    text="4",
    width=4,
    height=2,
    command=lambda: insert_text("4"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
button5 = Button(
    text="5",
    width=4,
    height=2,
    command=lambda: insert_text("5"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
button6 = Button(
    text="6",
    width=4,
    height=2,
    command=lambda: insert_text("6"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonMul = Button(
    text="*",
    width=4,
    height=2,
    command=lambda: insert_text("*"),
    bd=4,
    bg="#fc6203",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonBack = Button(
    text="Back",
    width=10,
    height=2,
    command=back_text,
    bd=4,
    bg="#0339fc",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
button1 = Button(
    text="1",
    width=4,
    height=2,
    command=lambda: insert_text("1"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
button2 = Button(
    text="2",
    width=4,
    height=2,
    command=lambda: insert_text("2"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
button3 = Button(
    text="3",
    width=4,
    height=2,
    command=lambda: insert_text("3"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonDif = Button(
    text="-",
    width=4,
    height=2,
    command=lambda: insert_text("-"),
    bd=4,
    bg="#fc6203",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonClear = Button(
    text="Clear",
    width=10,
    height=2,
    command=clear_text,
    bd=4,
    bg="#0339fc",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonDot = Button(
    text=".",
    width=4,
    height=2,
    command=lambda: insert_text("."),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
button0 = Button(
    text="0",
    width=4,
    height=2,
    command=lambda: insert_text("0"),
    bd=4,
    bg="orange",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonEqual = Button(
    text="=",
    width=4,
    height=2,
    command=calculate,
    bd=4,
    bg="black",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonAdd = Button(
    text="+",
    width=4,
    height=2,
    command=lambda: insert_text("+"),
    bd=4,
    bg="#fc6203",
    fg="white",
    font=("Helvetica", 15, "bold"),
)
buttonExit = Button(
    text="Exit",
    width=10,
    height=2,
    bd=4,
    bg="red",
    fg="white",
    font=("Helvetica", 15, "bold"),
    command=lambda: screen.quit(),
)

# Placement of Input Field and Buttons
input_field.place(x=23, y=20, height=40)
button7.place(x=25, y=80)
button8.place(x=100, y=80)
button9.place(x=175, y=80)
buttonDiv.place(x=255, y=80)
buttonBrace1.place(x=335, y=80)
buttonBrace2.place(x=415, y=80)
button4.place(x=25, y=180)
button5.place(x=100, y=180)
button6.place(x=175, y=180)
buttonMul.place(x=255, y=180)
buttonBack.place(x=338, y=180)
button1.place(x=25, y=280)
button2.place(x=100, y=280)
button3.place(x=175, y=280)
buttonDif.place(x=255, y=280)
buttonClear.place(x=338, y=280)
buttonDot.place(x=25, y=380)
button0.place(x=100, y=380)
buttonEqual.place(x=175, y=380)
buttonAdd.place(x=255, y=380)
buttonExit.place(x=338, y=380)

# Run
screen.mainloop()
