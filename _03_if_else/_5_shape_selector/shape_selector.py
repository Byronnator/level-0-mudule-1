import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # Make a new turtle
    bob = turtle.Turtle()
    bob.pendown()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title=None, prompt='do you want me to draw a triangle, square, or circle')
    if shape == 'circle':
        bob.circle(50)
    if shape == 'triangle':
        bob.forward(100)
        bob.left(120)
        bob.forward(100)
        bob.left(120)
        bob.forward(100)
    if shape == 'square':
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)


    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
    bob.hideturtle()
    turtle.done()