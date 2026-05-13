import tkinter      # GUI library.


# This is where the inputs to the calculator are stored.
calculation = ""


# The functions affect the text field 'text_result'. The functions do not affect the buttons.

# User can add numbers and symbols to the text field to eventually be evaluated.
def add_to_calculation(symbol):
    global calculation                      # Use 'global' so that we can manipulate the 'calculation' variable (i.e. the place where the inputs to the calculator are stored) inside the function.
    calculation += str(symbol)
    text_result.delete(1.0, "end")          # Delete the content of the text result...
    text_result.insert(1.0, calculation)    # ...and insert the updated version of the 'calculation' string to be evaluated in the place that we deleted.
    # It seems that every time the user adds a symbol, the text field is wiped and replaced with the new [longer] 'calculation' string.


# Compute mathematical expressions inputted by the user. 
def evaluate_calculation():
    global calculation                              # "10 + 4 * 2"
    try:                                            # Use try for error handling, such as trying to divide by zero.
        # For division, we want to make the special character '÷' work.
        calculation = calculation.replace('÷', '/')
        
        calculation = str(eval(calculation))        # Evaluate the user input, then turn it into a string.
        text_result.delete(1.0, "end")              # We don't use the clear_field() function here, since we don't want to clear everything in the 'calculation' string. We just want to update it with the calculated result.
        text_result.insert(1.0, calculation)
        # Evaluate the 'calculation' string, delete the 'calculation' string from the text result, and display the new calculati
    except:
        clear_field()                       # Similar to 'text_result.delete(1.0, "end")'.
        text_result.insert(1.0, "Error")    # Print "Error"


# Clear the text field.
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# We need a basic GUI window.
# We want a text field.
# We want the values from the text field [so that we can calculate them].
# We want to clear the values in the text field.


# Start endpoint...
root = tkinter.Tk(className="akiva's calculator")


#...GUI in the middle...

# Dimensions of the window.
root.geometry("312x300")


# Add a text field for the result.
# 'root' parameter = Part of the root window
text_result = tkinter.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
# 1 row span and 5 column spaces are being occupied by the text result box.


# Now, we need to manually add each button.
# 'text' = Text on the button
# 'command' = What the button does
# In general, we use lambda functions so that we can pass arguments easily.
button_1 = tkinter.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))    # 'command=add_to_calculation(1)' would actually immediately call the function. However, we don't want to do that. We just want to reference it to 'button_1'.
# Now, we'll specify where we want the button to go.
# Row 1 and all 5 column spaces are occupied by the text box. The '1' button will go in row 2 and column space 1.
button_1.grid(row=2, column=1)

# Repeat for all buttons.

button_2 = tkinter.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
button_2.grid(row=2, column=2)

button_3 = tkinter.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
button_3.grid(row=2, column=3)

# We want the '+' button to be in column 4 of this row. So, the next button will go in the next row.

button_4 = tkinter.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
button_4.grid(row=3, column=1)      

button_5 = tkinter.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
button_5.grid(row=3, column=2)

button_6 = tkinter.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
button_6.grid(row=3, column=3)

button_7 = tkinter.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
button_7.grid(row=4, column=1)

button_8 = tkinter.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
button_8.grid(row=4, column=2)

button_9 = tkinter.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
button_9.grid(row=4, column=3)

button_0 = tkinter.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
button_0.grid(row=5, column=2)

# Add operators.

button_plus = tkinter.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
button_plus.grid(row=2, column=4)

button_minus = tkinter.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
button_minus.grid(row=3, column=4)

button_mult = tkinter.Button(root, text="x", command=lambda: add_to_calculation("x"), width=5, font=("Arial", 14))
button_mult.grid(row=4, column=4)

button_div = tkinter.Button(root, text="÷", command=lambda: add_to_calculation("÷"), width=5, font=("Arial", 14))
button_div.grid(row=5, column=4)

# Add parenthesis.

button_open_par = tkinter.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
button_open_par.grid(row=5, column=1)

button_close_par = tkinter.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
button_close_par.grid(row=5, column=3)

# Add clear.

button_clear = tkinter.Button(root, text="C", command=clear_field, width=15, font=("Arial", 14))       # On every row, we have four buttons. There are only two buttons left to place in the last row. So, we elongate the buttons. 
# We don't need lambda here. There are no parameters for this function. We remove the parenthesis because if we leave them, it will call the function instead of passing it as a reference to 'button_clear'.
button_clear.grid(row=6, column=1, columnspan=2) 

# Add equals.

button_equals = tkinter.Button(root, text="=", command=evaluate_calculation, width=15, font=("Arial", 14))       # On every row, we have four buttons. There are only two buttons left to place in the last row. So, we elongate the buttons. 
button_equals.grid(row=6, column=3, columnspan=2)       # If we don't update the columnspan, the program will accomodate the size 11 width by making the columns to be of size 11. Now, we've set the button to extend over two columns instead of causing the first column to stretch.


#...End endpoint.
root.mainloop()




# IMPROVEMENTS:
# How to name the window starting with a capital letter.
# Support more types of calculations.
# When the result of a division is a whole number, return an integer instead a float.