# Function Plotter
A GUI program that plots arbitrary user-entered function.

### Project Description

The program takes the function expression to be plotted, and the  min-max values of x. It validates the input and shows a graph of the function if all input was valid, othewise prints an error message.

### Technologies Used

- python
- matplotlib and numpy
- unittest
- tkinter

#### Function Expression Validation Criteria

- Allowed characters are : 'x' , operators (+,-,*,/,^), numbers, spaces
- Operands (variables and numbers) are seperated by operators
- Operators must have two operands
- No spaces inside a number (like: 2 5)
- Brackets must be in pairs and in order
	