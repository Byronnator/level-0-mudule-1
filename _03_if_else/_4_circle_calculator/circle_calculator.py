# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
import math
import turtle
from tkinter import simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    bob = turtle.Turtle()
    radius = simpledialog.askinteger(title=None, prompt='give me a radius')
    question = simpledialog.askstring(title=None, prompt='do you want area or circumference')
    if question == 'area':
        area = (math.pi * radius * radius)
        bob.write(arg="area = " + str(area), move=True, align='left', font=('Arial', 8, 'normal'))
    if question == 'circumference':
        circumference = (math.pi * math.pi * radius)
        bob.write(arg="circumference = " + str(circumference), move=True, align='left', font=('Arial', 8, 'normal'))
    bob.hideturtle()
    turtle.done()
    window.mainloop()