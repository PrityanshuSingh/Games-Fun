import turtle
import time
import os
import sys
from tkinter import simpledialog
from tkinter import messagebox


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HELLO START
game=turtle.Turtle()
style = ('Courier', 60, 'bold')                                # SETTING HELLO FILTER
game.write('!PS HUB!', font=style, align='center')
game.goto(0,-2)
style = ('Courier', 13, 'italic','bold')                       # SETTING HELLO FILTER
game.write('publications', font=style, align='center')

game.penup()
game.forward(250)
game.left(90)                       #positioning game
game.pendown()
game.speed(3)

game.color("black")
game.pensize(5)
for i in range(2):                  # making black box
    game.forward(100)
    game.left(90)
    game.forward(500)
    game.left(90)
game.color("white","black")
game.begin_fill()
for i in range(2):
    game.forward(100)
    game.left(90)                   # making white box and resulting in black bg
    game.forward(500)
    game.left(90)
game.end_fill()
game.getscreen().bgcolor("black")

'''game.speed(100)
game.color("black")
game.pensize(10)
for i in range(2):                  # making black bg
    game.forward(100)
    game.left(90)
    game.forward(500)
    game.left(90)'''
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HELLO END


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX SCRIB START
scrib=turtle.Turtle()
scrib.speed(15)
scrib.penup()                              # POSITIONING SCRIBBLE
scrib.goto(-250,25)
scrib.pendown()

scrib.pensize(20)
scrib.color("red")
scrib.left(70)
for i in range(30):
    scrib.forward(100)                     # JUST A LITTLE SCRIBBLE
    scrib.right(170)
    scrib.forward(97)
    scrib.left(170)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX SCRIB END



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX WELCOME START
welcome=turtle.Turtle()
welcome.penup()                                       # POSITIONING WELCOME
welcome.color('white')
welcome.backward(200)


style = ('Courier', 60, 'bold')                       # SETTING WELCOME FILTER and writing heading
welcome.write("W",font=style,align='center')
welcome.forward(50)
welcome.write("E", font=style, align='center')
welcome.forward(50)
welcome.write("L",font=style,align='center')
welcome.forward(50)
welcome.write("C", font=style, align='center')
welcome.forward(50)
welcome.write("O",font=style,align='center')
welcome.forward(50)
welcome.write("M", font=style, align='center')
welcome.forward(50)
welcome.write("E",font=style,align='center')
welcome.forward(100)
welcome.write("T", font=style, align='center')
welcome.forward(50)
welcome.write("O",font=style,align='center')
welcome.forward(600)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX WELCOME END



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ROCK PAPER SCISSORS START
rps=turtle.Turtle()
rps.speed(5)
rps.color("cyan")
rps.pensize(15)                                            #POSITIONING RPS
rps.penup()
rps.goto(-300,-100)

style = ('Comic sans MS', 50, 'bold')
rps.write("ROCK,",font=style,align='center')
rps.forward(200)
rps.write("PAPER",font=style,align='center')
rps.forward(350)                                            # SETTING RPS FILTER and writing heading
rps.write("SCISSORS",font=style,align='center')
rps.backward(210)
style = ('Times new roman', 90, 'italic')
rps.color("orange")
rps.write("&",font=style,align='center')
rps.right(90)
rps.forward(20)
rps.left(90)
rps.pendown()

rps.speed(6)
rps.color("orange")
rps.pensize(10)
rps.forward(410)
for i in range(2):                                            # making first loading box
    rps.left(90)
    rps.forward(275)
    rps.left(90)
    rps.forward(870)

rps.backward(410)
rps.color("black","orange")
rps.begin_fill()
rps.pensize(10)
rps.forward(410)
for i in range(2):                                            # closing the white box resulting in orange background
    rps.left(90)
    rps.forward(275)
    rps.left(90)
    rps.forward(870)
rps.end_fill()

rps.speed(100)
rps.getscreen().bgcolor("orange")
rps.backward(410)
rps.color("orange")
rps.pensize(10)
rps.forward(410)
for i in range(2):                                            # making the bg orange
    rps.left(90)
    rps.forward(275)
    rps.left(90)
    rps.forward(870)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ROCK PAPER SCISSORS END



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX STARTING THE REAL GAME NOW
inst=turtle.Turtle()
sc = turtle.Screen()
inst.penup()
inst.goto(0,150)                                               # POSITIONING INST heading

inst.color("white")
style = ('Monotype Corsiva', 100, 'bold','underline')
inst.write("INSTRUCTIONS",font=style,align='center')

inst.goto(-300,40)
inst.speed(1)
inst.color("black")
style = ('Comic sans MS', 30, 'italic')
inst.write("1.",font=style,align='right')                     #telling instructions
inst.forward(40)
inst.write("PRESS 'R' FOR ROCK",font=style,align='left')

inst.goto(-300,-40)
inst.write("2.",font=style,align='right')
inst.forward(40)
inst.write("PRESS 'P' FOR PAPER",font=style,align='left')

inst.goto(-300,-120)
inst.write("3.",font=style,align='right')
inst.forward(40)
inst.write("PRESS 'S' FOR SCISSORS",font=style,align='left')

def hello():
    inst.speed(5)
    inst.goto(0,-250)
    style = ('Comic sans MS', 20, 'italic','underline')
    for i in range(2):
        inst.color("orange")
        inst.write("PRESS SPACE TO CONTINUE", font=style, align='center')
        time.sleep(0.3)                                                          # making function for space
        inst.color("red")
        inst.write("PRESS SPACE TO CONTINUE", font=style, align='center')
        time.sleep(0.3)
hello()                                       #running th function


def fxn():                                    #defining func for space
    inst.color("red")
    inst.goto(0,-300)                         #positioning box
    inst.speed(10)
    inst.pensize(10)

    inst.pendown()
    inst.forward(500)
    inst.left(90)
    for i in range(2):
        inst.forward(650)                      #making red box
        inst.left(90)
        inst.forward(1000)
        inst.left(90)

    inst.color("orange","red")
    inst.begin_fill()
    for i in range(2):
        inst.forward(650)                       #filling red box
        inst.left(90)
        inst.forward(1000)
        inst.left(90)
    inst.end_fill()

    sc.bgcolor("red")

    inst.speed(100)
    inst.color("red")
    for i in range(2):
        inst.forward(650)                        #making screen red
        inst.left(90)
        inst.forward(1000)
        inst.left(90)
    inst.penup()
    inst.goto(900,0)
    inst.pendown()

time.sleep(3)
sc.onkey(fxn,"space")                            #pressing space for continue
sc.listen()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ENDING THE REAL GAME



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ASKING PLAYER FOR COLOURS ( PART 1 )
colour= turtle.Turtle()

sc = turtle.Screen()

scrib=turtle.Turtle()
scrib.penup()
scrib.goto(1000,0)
scrib.pendown()

colour.penup()
colour.speed(10)
colour.goto(0,250)                                                # positioning heading (before u start
colour.color("black")
style = ('Times new roman', 70, 'bold','underline')
colour.write("BEFORE YOU START",font=style,align='center')

colour.goto(0,50)
colour.pendown()
colour.color("yellow")
colour.speed(10)                                                   # positing name table
colour.pensize(10)
colour.forward(500)
colour.left(90)
for i in range(2):
    colour.forward(100)
    colour.left(90)                                                # making table
    colour.forward(1000)
    colour.left(90)

colour.color("black")
colour.pensize(5)
colour.penup()                                                     # directing the user to dialogue box
colour.goto(0,80)
style = ('Comic sans MS', 28, 'italic')
colour.write("ENTER YOUR USERNAME IN THE DIALOGUE BOX",font=style,align='center')
colour.color("red")
colour.goto(1000,0)


time.sleep(1)
player = sc.textinput(" ", " ! Enter username (<= 6 ch) !")            # making dialogue box appear

thanks=turtle.Turtle()
thanks.color("red")
thanks.penup()                                                # positioning thanks
thanks.speed(100)
thanks.goto(-625,275)
for i in range(2):
    thanks.color("yellow")
    thanks.write("THANKS:)", font=style, align='center')
    time.sleep(0.3)                                           # making thanks blink
    thanks.color("red")
    thanks.write("THANKS:)", font=style, align='center')
    time.sleep(0.3)
    thanks.clear()
thanks.speed(10)
thanks.goto(-1000,0)


name=turtle.Pen()
name.penup()                                                   # positioning paragraph
name.pensize(20)
name.goto(-60,-50)

style = ('Comic sans MS', 40,'bold')
name.color("black")
name.write("HEY ",font=style,align="center")                    # WRITING CONTENTS

def length6():                                                  # DEFINING FUNCTION IF NAME LENGTH<=6
    style = ('Comic sans MS', 40, 'underline','bold')
    name.forward(140)
    name.pensize(100)
    for i in range(4):
        name.color("white")
        name.write(player.capitalize(),font=style,align="center")
        time.sleep(0.1)                                                # making name to blink fast
        name.color("black")
        name.write(player.capitalize(), font=style, align="center")
        time.sleep(0.1)

    for i in range(3):
        name.color("white")
        name.write(player.capitalize(),font=style,align="center")
        time.sleep(0.2)                                                # making name to blink medium
        name.color("black")
        name.write(player.capitalize(), font=style, align="center")
        time.sleep(0.2)

    for i in range(2):
        name.color("white")
        name.write(player.capitalize(),font=style,align="center")
        time.sleep(0.3)                                                # making name to blink slow
        name.color("black")
        name.write(player.capitalize(), font=style, align="center")
        time.sleep(0.3)


def length6M():                                                         # DEFINING FUNCTION IF NAME LENGTH>6
    style = ('Comic sans MS', 40, 'underline', 'bold')
    name.forward(200)
    name.pensize(100)
    for i in range(4):
        name.color("white")
        name.write(player.capitalize(), font=style, align="center")
        time.sleep(0.1)                                               # making name to blink fast
        name.color("black")
        name.write(player.capitalize(), font=style, align="center")
        time.sleep(0.1)

    for i in range(3):
        name.color("white")
        name.write(player.capitalize(), font=style, align="center")
        time.sleep(0.2)                                               # making name to blink medium
        name.color("black")
        name.write(player.capitalize(), font=style, align="center")
        time.sleep(0.2)

    for i in range(2):
        name.color("white")
        name.write(player.capitalize(), font=style, align="center")
        time.sleep(0.3)                                                # making name to blink slow
        name.color("black")
        name.write(player.capitalize(), font=style, align="center")
        time.sleep(0.3)

if len(player) <= 6:                                                   # calling function accord to condition
    length6()
else:
    length6M()

name.color("red")                                                      # making name invisible
name.goto(1000,0)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END ASKING PLAYER FOR COLOURS ( PART 1 )




#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx DEFINING FUNCTIONS FOR BOY MOVEMENT TO BE USED IN NEXT SECTION (START)
boy =turtle.Pen()
road=turtle.Turtle()

'''road.penup()
road.color("orange")
road.pensize(15)
road.speed(10)                           # temporary for beta
road.goto(-800,20)
road.pendown()
road.forward(1800)'''

boy.speed(10000)
boy.pensize(26)
boy.penup()                              # imp conditions for boy
boy.left(90)
boy.pendown()

def boyp1():
    boy.penup()
    boy.forward(50)                         # positioning legs
    boy.left(150)
    boy.pendown()

    boy.color("black")
    boy.forward(50)
    boy.backward(50)
    boy.left(60)                            # making first pair legs
    boy.color("grey")
    boy.forward(50)
    boy.backward(50)

    boy.color("black")
    boy.left(150)
    boy.forward(75)
    boy.backward(15)
    boy.left(130)                           # making first second hands
    boy.color("grey")
    boy.forward(50)
    boy.backward(50)
    boy.penup()
    boy.left(80)
    boy.pendown()
    boy.color("black")
    boy.forward(50)
    boy.backward(50)

    boy.right(210)
    boy.right(90)
    boy.penup()                              # positioning face
    boy.forward(30)
    boy.left(90)
    boy.forward(55)
    boy.pendown()

    boy.color("black")
    boy.begin_fill()
    boy.circle(34)
    boy.end_fill()
    time.sleep(0.1)
    boy.clear()

def boyp2():
    boy.penup()
    boy.forward(50)                          # positioning legs
    boy.left(150)
    boy.pendown()

    boy.color("grey")
    boy.forward(50)
    boy.backward(50)
    boy.left(60)                             # making first pair legs
    boy.color("black")
    boy.forward(50)
    boy.backward(50)

    boy.color("black")
    boy.left(150)
    boy.forward(75)
    boy.backward(15)
    boy.left(160)                            # making first second hands
    boy.color("black")
    boy.forward(50)
    boy.backward(50)
    boy.penup()
    boy.left(70)
    boy.pendown()
    boy.color("grey")
    boy.forward(50)
    boy.backward(50)

    boy.right(220)
    boy.right(100)
    boy.penup()                                # positioning face
    boy.forward(30)
    boy.left(90)
    boy.forward(55)
    boy.pendown()

    boy.color("black")
    boy.begin_fill()
    boy.circle(34)
    boy.end_fill()
    time.sleep(0.1)
    boy.clear()

def respl():                               #MAKING THE BOY MOVE
    for i in range(500,0,-40):
        boy.penup()
        boy.goto(-i, 20)                 #calling func of boy 2
        boy.pendown()
        boyp2()

        boy.penup()
        boy.right(90)
        boy.forward(50)                  #positioning boy 1
        boy.left(90)

        boy.backward(150)
        boy.goto(-i + 30, 20)            #calling func of boy 1
        boy.pendown()
        boyp1()




c_boy =turtle.Pen()

c_boy.speed(10000)
c_boy.pensize(26)
c_boy.penup()                              # imp conditions for c_boy
c_boy.left(90)
c_boy.pendown()

def boyc1():
    c_boy.penup()
    c_boy.forward(50)                         # positioning legs
    c_boy.left(150)
    c_boy.pendown()

    c_boy.color("white")
    c_boy.forward(50)
    c_boy.backward(50)
    c_boy.left(60)                            # making first pair legs
    c_boy.color("grey")
    c_boy.forward(50)
    c_boy.backward(50)

    c_boy.color("white")
    c_boy.left(150)
    c_boy.forward(75)
    c_boy.backward(15)
    c_boy.left(80)                           # making first second hands
    c_boy.color("grey")
    c_boy.forward(50)
    c_boy.backward(50)
    c_boy.penup()
    c_boy.left(130)
    c_boy.pendown()
    c_boy.color("white")
    c_boy.forward(50)
    c_boy.backward(50)

    c_boy.right(210)
    c_boy.right(90)
    c_boy.penup()                              # positioning face
    c_boy.forward(30)
    c_boy.left(90)
    c_boy.forward(55)
    c_boy.pendown()

    c_boy.color("white")
    c_boy.begin_fill()
    c_boy.circle(35)
    c_boy.end_fill()
    time.sleep(0.1)
    c_boy.clear()

def boyc2():
    c_boy.penup()
    c_boy.forward(50)                          # positioning legs
    c_boy.left(150)
    c_boy.pendown()

    c_boy.color("grey")
    c_boy.forward(50)
    c_boy.backward(50)
    c_boy.left(60)                             # making first pair legs
    c_boy.color("white")
    c_boy.forward(50)
    c_boy.backward(50)

    c_boy.color("white")
    c_boy.left(150)
    c_boy.forward(75)
    c_boy.backward(15)
    c_boy.left(140)                            # making first second hands
    c_boy.color("white")
    c_boy.forward(50)
    c_boy.backward(50)
    c_boy.penup()
    c_boy.left(90)
    c_boy.pendown()
    c_boy.color("grey")
    c_boy.forward(50)
    c_boy.backward(50)

    c_boy.right(220)
    c_boy.right(100)
    c_boy.penup()                                # positioning face
    c_boy.forward(30)
    c_boy.left(90)
    c_boy.forward(55)
    c_boy.pendown()

    c_boy.color("white")
    c_boy.begin_fill()
    c_boy.circle(35)
    c_boy.end_fill()
    time.sleep(0.1)
    c_boy.clear()

def rescomp():                               #MAKING THE C_BOY MOVE
    for i in range(500,0,-40):
        c_boy.penup()
        c_boy.goto(i, 20)                 #calling func of c_boy 2
        c_boy.pendown()
        boyc2()

        c_boy.penup()
        c_boy.right(90)
        c_boy.forward(50)                  #positioning c_boy 1
        c_boy.left(90)

        c_boy.backward(150)
        c_boy.goto(i - 30, 20)            #calling func of c_boy 1
        c_boy.pendown()
        boyc1()


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ENDING BOY MOVEMENT FUNCTIONS


# make the user to choose colour of boy                              (in the end if necessary)
'''sc = turtle.Screen()
sc.bgcolor("lime")'''

def respl_():
    housep=turtle.Pen()
    housep.speed(100)

    housec=turtle.Pen()
    housec.speed(100)


    round=turtle.Turtle()
    round.penup()
    style = ('Comic sans MS', 45,'bold')
    round.goto(0,200)
    round.pendown()
    round.write("SELECT THE NUMBER OF ROUNDS",font=style, align="center")

    round.penup()
    round.pensize(7)
    round.color("black","white")
    round.goto(-250,-250)                                     # positioning white round
    round.shape("circle")
    round.shapesize(3)
    round.pendown()
    round.begin_fill()
    round.circle(45)                                       # making circle
    round.end_fill()
    style = ('Comic sans MS', 45)
    round.write("3", font=style, align="center")


    round.penup()
    round.pensize(7)
    round.color("black","white")
    round.goto(0,-250)                                     # positioning white round
    round.shape("circle")
    round.shapesize(3)
    round.pendown()
    round.begin_fill()
    round.circle(45)                                       # making circle
    round.end_fill()
    style = ('Comic sans MS', 45)
    round.write("5", font=style, align="center")


    round.penup()
    round.pensize(7)
    round.color("black","white")
    round.goto(250,-250)                                     # positioning white round
    round.shape("circle")
    round.shapesize(3)
    round.pendown()
    round.begin_fill()
    round.circle(45)                                         # making circle
    round.end_fill()
    style = ('Comic sans MS', 45)
    round.write("7", font=style, align="center")

    # DEFINING FUNC FOR HOUSES
    def house_pl():
        housep.goto(-250,250)
        housep.right(90)                                    # player house
        housep.forward(300)

    def house_comp():
        housec.goto(250,250)
        housec.right(90)                                    # comp house
        housec.forward(300)


    import threading

    threading.Thread(target=house_pl).start()               # CALLING BOTH THE FUNCTIONS TOGETHER of houses
    threading.Thread(target=house_comp).start()

    threading.Thread(target=respl).start()                  # CALLING BOTH THE FUNCTIONS TOGETHER of boiss
    threading.Thread(target=rescomp).start()



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START ASKING PLAYER FOR COLOURS ( PART 2 )
scrib.speed(100)
scrib.penup()                              # POSITIONING SCRIBBLE 2
scrib.goto(-450,-200)
scrib.pendown()

scrib.pensize(20)
scrib.color("black")
scrib.left(70)
for i in range(50):
    scrib.forward(100)                     # JUST A LITTLE SCRIBBLE 2
    scrib.right(170)
    scrib.forward(97)
    scrib.left(170)
scrib.penup()                              # ending SCRIBBLE 2
scrib.goto(900,0)
scrib.pendown()

col = turtle.Turtle()
col.penup()
col.goto(0,-200)
col.color("yellow")                                                                    # writing statement for colour choice
style = ('Comic sans MS', 20, 'underline', 'italic')
col.write("CHOOSE A COLOUR OF YOUR CHOICE FOR BACKGROUND", font=style, align="center")
col.color("black")
col.goto(1000,0)


# MAKING USER TO CHOOSE COLOUR               STARTING CIRCLES
sc.bgcolor("white")
circle=turtle.Pen()
circle.speed(100)
circle.pensize(2)

circle.penup()
circle.goto(-650,1000)                                     # making colour circle appear

def red():
    circle.penup()
    circle.color("black","red")
    circle.goto(-650,250)                                     # making red circle
    circle.shape("circle")
    circle.shapesize(5)
    circle.pendown()
    circle.begin_fill()
    circle.circle(45)
    circle.end_fill()
    style = ('Comic sans MS', 45)
    circle.write("R", font=style, align="center")


def green():
    circle.penup()
    circle.color("black","green")
    circle.goto(-650,50)                                     # making green circle
    circle.shape("circle")
    circle.shapesize(5)
    circle.pendown()
    circle.begin_fill()
    circle.circle(45)
    circle.end_fill()
    style = ('Comic sans MS', 45)
    circle.write("G", font=style, align="center")

def pink():
    circle.penup()
    circle.color("black","pink")
    circle.goto(-650,-150)                                     # making pink circle
    circle.shape("circle")
    circle.shapesize(5)
    circle.pendown()
    circle.begin_fill()
    circle.circle(45)
    circle.end_fill()
    style = ('Comic sans MS', 45)
    circle.write("P", font=style, align="center")

def blue():
    circle.penup()
    circle.color("black","blue")
    circle.goto(-650,-350)                                     # making blue circle
    circle.shape("circle")
    circle.shapesize(5)
    circle.pendown()
    circle.begin_fill()
    circle.circle(45)
    circle.end_fill()
    style = ('Comic sans MS', 45)
    circle.write("B", font=style, align="center")

def yellow():
    circle.penup()
    circle.color("black","yellow")
    circle.goto(650,250)                                     # making yellow circle
    circle.shape("circle")
    circle.shapesize(5)
    circle.pendown()
    circle.begin_fill()
    circle.circle(45)
    circle.end_fill()
    style = ('Comic sans MS', 45)
    circle.write("Y", font=style, align="center")

def cyan():
    circle.penup()
    circle.color("black","cyan")
    circle.goto(650,50)                                     # making cyan circle
    circle.shape("circle")
    circle.shapesize(5)
    circle.pendown()
    circle.begin_fill()
    circle.circle(45)
    circle.end_fill()
    style = ('Comic sans MS', 45)
    circle.write("C", font=style, align="center")

def orange():
    circle.penup()
    circle.color("black","orange")
    circle.goto(650,-150)                                     # making orange circle
    circle.shape("circle")
    circle.shapesize(5)
    circle.pendown()
    circle.begin_fill()
    circle.circle(45)
    circle.end_fill()
    style = ('Comic sans MS', 45)
    circle.write("O", font=style, align="center")

def lime():
    circle.penup()
    circle.color("black","lime")
    circle.goto(650,-350)                                     # making grey circle
    circle.shape("circle")
    circle.shapesize(5)
    circle.pendown()
    circle.begin_fill()
    circle.circle(45)
    circle.end_fill()
    style = ('Comic sans MS', 45)
    circle.write("L", font=style, align="center")

#CALLING ALL FUNCTIONS
red()
green()
pink()
blue()
yellow()
cyan()
orange()
lime()

circle.penup()
circle.goto(650,-1000)                                     # making colour circle disappeae

#                                            ENDING CIRCLES

#DEFINING FUNCTION TO WHICH THE USER WILL GO ON PRESSING RES. KEY
bg = turtle.Screen()
finish= turtle.Pen()

bg.listen()
def r():
    bg.bgcolor("red")
    finish.speed(1000)
    finish.penup()
    finish.pensize(5)
    finish.goto(0, -600)
    finish.color("red", "red")
    for i in range(10, 1600, 100):
        finish.begin_fill()
        finish.circle(i)
        finish.pensize(i)
        finish.end_fill()
    respl_()
bg.onkey(r,"r")                              # making red bg
bg.listen()

def g():
    bg.bgcolor("green")
    finish.speed(1000)
    finish.penup()
    finish.pensize(5)
    finish.goto(0,-600)
    finish.color("green","green")
    for i in range(10,1600,100):
        finish.begin_fill()
        finish.circle(i)
        finish.pensize(i)
        finish.end_fill()
    respl_()
bg.onkey(g,"g")                              # making green bg
bg.listen()

def p():
    bg.bgcolor("pink")
    finish.speed(1000)
    finish.penup()
    finish.pensize(5)
    finish.goto(0, -600)
    finish.color("pink", "pink")
    for i in range(10, 1600, 100):
        finish.begin_fill()
        finish.circle(i)
        finish.pensize(i)
        finish.end_fill()
    respl_()
bg.onkey(p,"p")                              # making pink bg
bg.listen()

def b():
    bg.bgcolor("blue")
    finish.speed(1000)
    finish.penup()
    finish.pensize(5)
    finish.goto(0, -600)
    finish.color("blue", "blue")
    for i in range(10, 1600, 100):
        finish.begin_fill()
        finish.circle(i)
        finish.pensize(i)
        finish.end_fill()
    respl_()
bg.onkey(b,"b")                              # making blue bg
bg.listen()

def y():
    bg.bgcolor("yellow")
    finish.speed(1000)
    finish.penup()
    finish.pensize(5)
    finish.goto(0, -600)
    finish.color("yellow", "yellow")
    for i in range(10, 1600, 100):
        finish.begin_fill()
        finish.circle(i)
        finish.pensize(i)
        finish.end_fill()
    respl_()
bg.onkey(y,"y")                              # making yellow bg
bg.listen()

def c():
    bg.bgcolor("cyan")
    finish.speed(1000)
    finish.penup()
    finish.pensize(5)
    finish.goto(0, -600)
    finish.color("cyan", "cyan")
    for i in range(10, 1600, 100):
        finish.begin_fill()
        finish.circle(i)
        finish.pensize(i)
        finish.end_fill()
    respl_()
bg.onkey(c,"c")                              # making cyan bg
bg.listen()

def o():
    bg.bgcolor("orange")
    finish.speed(1000)
    finish.penup()
    finish.pensize(5)
    finish.goto(0, -600)
    finish.color("orange", "orange")
    for i in range(10, 1600, 100):
        finish.begin_fill()
        finish.circle(i)
        finish.pensize(i)
        finish.end_fill()
    respl_()
bg.onkey(o,"o")                              # making orange bg
bg.listen()

def l():
    bg.bgcolor("lime")
    finish.speed(1000)
    finish.penup()
    finish.pensize(5)
    finish.goto(0, -600)
    finish.color("lime", "lime")
    for i in range(10, 1600, 100):
        finish.begin_fill()
        finish.circle(i)
        finish.pensize(i)
        finish.end_fill()
    respl_()
bg.onkey(l,"l")                              # making lime bg
bg.listen()

finish.penup()
finish.goto(900,0)                           # ending circles functions
finish.pendown()


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ENDING ASKING PLAYER FOR COLOURS ( PART 2 )



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX MAKING USER SELECT NUMBER OF ROUNDS









turtle.done()