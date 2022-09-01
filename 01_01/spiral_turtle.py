"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""
import turtle

MAX_LENGTH = 150
INCREMENT = 20


def draw_spiral(a_turtle, line_length):
    if line_length > MAX_LENGTH:
        return
    a_turtle.forward(line_length)
    a_turtle.right(90)
    draw_spiral(a_turtle, line_length + INCREMENT)


charlie = turtle.Turtle(shape="turtle")
charlie.pensize(5)
charlie.color("green")
draw_spiral(charlie, 5)
turtle.done()
