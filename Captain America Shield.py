import turtle
from turtle import *

t=turtle.Turtle()
wn=Screen()

wn.bgcolor("white")
t.pensize(30)
t.hideturtle()

#outer circle
t.setposition(0,-270)
t.pendown()
t.begin_fill()
t.color("white")
t.pencolor("red")
t.circle(270)
t.end_fill()
t.penup()

#inner circle
t.pensize(2)
t.setposition(0,-210)
t.pendown()
t.begin_fill()
t.color("red")
t.circle(210)
t.end_fill()
t.penup()

#inner-inner circle
t.pensize(2)
t.setposition(0,-160)
t.pendown()
t.begin_fill()
t.color("#000066")
t.circle(160)
t.end_fill()
t.penup()

#draw star
t.pensize(2)
t.setposition(-155,50)
t.pendown()
t.begin_fill()
t.color("white")
for i in range(5):
    t.fd(310)
    t.rt(144)
t.end_fill()
t.penup()

turtle.done()