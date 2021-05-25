# To make a calculator in python using GUI

# import GUI library named Tkinter
from tkinter import *

# create a tkinter container
root = Tk()
width = 400
height = 342
root.geometry(f"{width}x{height}")
root.resizable(0,0)
root.title('C A L C U L A T O R')

# Tkinter widget functions
input_text = StringVar()
expression = ""

# fn to make a click on operators
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# fn to use '='
def btn_equal():
    try:
        global expression
        total = str(eval(expression))
        input_text.set(total)
        expression = ""
    except:
        input_text.set("error")
        expression = ""

# Fn to clear the screen
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Design the Application
 # Step A making frame for display screen
input_frame = Frame(root,width=350,height=45,bd=2,highlightbackground='green',highlightcolor='red',highlightthickness=8)
input_frame.pack(side=TOP,padx=0,pady=0)

# Step B  making display screen
input_field = Entry(input_frame,font='majestica 18 bold', textvariable= input_text, width = 50, bg = "teal", bd = 0, justify = RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

# Step C  making frame for all buttons
btns_frame = Frame(root, width = 300, height = 200, bg = "grey")
btns_frame.pack()

# Step D  making clear, equal buttons
clear = Button(btns_frame, text ="Clear", fg = "white", width = 35, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 0, pady = 0)
equals = Button(btns_frame, text = "=", fg = "white", width = 23, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_equal()).grid(row = 0, column = 3, padx = 1, pady = 1)

# Step E making 7,8,9,divide(/) buttons
seven = Button(btns_frame, text = "7", fg = "white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 0, pady = 0)
divide = Button(btns_frame, text = "/", fg = "white", width = 23, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 1, column = 3, padx = 0, pady = 0)

# Step F making 4,5,6,multiply(*) buttons
four = Button(btns_frame, text = "4", fg = "white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg ="white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "white", width = 23, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 2, column = 3, padx = 1, pady = 1)

# Step G making 1,2,3,plus(+) buttons
one = Button(btns_frame, text = "1", fg = "white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "white", width = 23, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

# Step H making 0,point(.),minus(-)
zero = Button(btns_frame, text = "0", fg = "white", width = 23, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "white", width = 11, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "white", width = 23, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()
