import turtle
tina=turtle.Turtle()
tina.shape("turtle")

# The magic of programming comes from easy automation of repeatable tasks. Introducing one of the basics of programming - loops!
while True:
    turtle.forward(20)
    turtle.right(13)

# Wow! we have introduced quite a bit of new concepts here!
# 1. Booleans! One more basic type present in most programming languages, along with string and int. True means a condition is correct, while its counterpart is False.
# for example, 5 > 2 will evaluate to True, while 3 > 4 will evaluate to False.
# 2. "while <smth>" keyword is a while cycle. Things keep happening while <"smth"> is True. In case of "while True", things will continue forever! Press "stop" to stop the trinket.
# 3. Code blocks! Notice how our turtle statements under while are indented. This is on purpose, and has meaning. In python, we use whitespaces to separate logical pieces of the code -
# just like paragraphs in natural language. You can create indentation by pressing `tab`

# lets play with it a bit more

# notice how there is nothing red in our drawing! 
while True:
    turtle.forward(20)
    turtle.right(120)
    turtle.color("blue")
turtle.color("red")

# nothing happens!
while False:
    turtle.forward(1000)

# come up with some cool pattern with while true here, let them play with it

# Here we will introduce another important concept in programming - variables!
# Imagine variables as buckets where you can store information. 
distance = 5

while True:
    tina.forward(distance)
    tina.right(90)
    # you can modify variables using for example, your expected mathematical operators, + - * / 
    # note how the distance will increase with each pass of the cycle!
    distance = distance + 5 


# its important to initialize variables before we actually use them!
# this would give us an error because we dont know what length is currently
length = length - 3 # length could be 0 or -1000 or 5689023? This will cause an error

# with varialbes, you can also finally make your porgrams have an end:
distance = 5

while distance < 60:
    tina.forward(distance) 
    tina.right(90)
    distance = distance + 5 

# task! 
# draw a "shell" made of circles!
radius = 5
while radius < 60:
    tina.circle(radius) 
    radius = radius + 5 

# You can also mix and match all that we learned. Also you can put cicles inside a cycles!
# lets walk through this code together
while True:
    radius = 5
    tina.color("red")
    while radius < 40
        tina.circle(radius)
        radius = radius + 5

    tina.right(60)
    tina.color("block")

    radius = 10
    while radius < 60
        tina.circle(radius)
        radius = radius + 10

    tina.right(60)

# this already looks more interesting!! Lets see what else can we imagine here:
while True:
    tina.color("black")

    side = 50
    while side > 5:
        tina.forward(side)
        tina.right(90)
        tina.forward(side)
        tina.right(90)
        tina.forward(side)
        tina.right(90)

        side = side / 2

    tina.color("red")

    while side < 60:
        tina.forward(side)
        tina.left(90)
        tina.forward(side)
        tina.left(90)
        tina.forward(side)

        tina.left(90)

        side = side * 2


## free form task!
