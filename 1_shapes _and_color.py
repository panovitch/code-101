"""
Here we introduce the concepts of statements and basic types: strings and integers.
WE talk about how a program is a list of senteses exuted from top to bottom, and
that some commands can result in a change of state, and some commands are just actions to execute.
We also explain what comments are :D

"""

# here we talk about how all programming languages are made of modules - and we are going to be using a turtle module!
# but we also say they shouldnt worry about it for now. 
import turtle
tina=turtle.Turtle()
tina.shape("turtle")

# this is a statement that makes turtle go forward!
tina.forward(90)

# this is a statement that makes turtle turn!
tina.right(50)


# this is a statement that doesnt seem to do anything.
# notice how the argument to this command is different - we provide the color name instead of a numerical value
# in programming, we usually call text values "strings"
tina.color("blue")

# however, now see what happens when we draw!
tina.forward(20)

tina.reset()

# lets draw a square!
tina.forward(20)
tina.right(90)
tina.forward(20)
tina.right(90)
tina.forward(20)
tina.right(90)
tina.forward(20)

tina.reset()


# ====== task! ======
# draw a green triangle! 
# advanced! draw a black circle surrounding the triangle (doesnt have to be centred, unless you are big on geometry)

# ====== expected result ======

import turtle
tina=turtle.Turtle()
tina.shape("turtle")


tina.color("green")

tina.forward(50)
tina.left(120)
tina.forward(50)
tina.left(120)
tina.forward(50)


