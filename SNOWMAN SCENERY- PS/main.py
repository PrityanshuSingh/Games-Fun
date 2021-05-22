import turtle
import math

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START BG COLOR
bg=turtle.Turtle()
bg.color("#000E22")
bg.getscreen().bgcolor("#000E22") #dark background
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END BG COLOR



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START STARS
star=turtle.Turtle()
star.color("white","white")
star.begin_fill()
star.speed(50)
star.pensize(2.5)

star.penup()
star.goto(500,20)
star.pendown()
for i in range(5):
    star.left(216)             # 1
    star.forward(10)

star.penup()
star.goto(-500,20)
star.pendown()
for i in range(5):
    star.left(216)             # 1
    star.forward(10)

star.penup()
star.goto(270,270)
star.pendown()
for i in range(5):               # 2
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-270,270)
star.pendown()
for i in range(5):               # 2
    star.left(216)
    star.forward(10)

star.penup()
star.goto(600,250)
star.pendown()                  # 3
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-600,250)
star.pendown()                  # 3
for i in range(5):
    star.left(216)
    star.forward(10)


star.penup()
star.goto(550,100)
star.pendown()
for i in range(5):                # 4
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-550,100)
star.pendown()
for i in range(5):                # 4
    star.left(216)
    star.forward(10)

star.penup()
star.goto(300,150)
star.pendown()
for i in range(5):               # 5
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-300,150)
star.pendown()
for i in range(5):               # 5
    star.left(216)
    star.forward(10)

star.penup()
star.goto(90,90)
star.pendown()
for i in range(5):                # 6
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-20,200)
star.pendown()
for i in range(5):                # 6
    star.left(216)
    star.forward(10)

star.penup()
star.goto(90,500)
star.pendown()
for i in range(5):                  #7
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-110,500)
star.pendown()
for i in range(5):                  #7
    star.left(216)
    star.forward(10)

star.penup()
star.goto(45,300)
star.pendown()                       #8
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-90,350)
star.pendown()                       #8
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(700,30)
star.pendown()
for i in range(5):                  #9
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-700,30)
star.pendown()
for i in range(5):                  #9
    star.left(216)
    star.forward(10)

star.penup()
star.goto(700,300)
star.pendown()                        #10
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-700,300)
star.pendown()                        #10
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(150,150)
star.pendown()                   #11
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-150,150)
star.pendown()                   #11
for i in range(5):
    star.left(216)
    star.forward(10)


star.penup()
star.goto(450,250)
star.pendown()                     #12
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-450,250)
star.pendown()                     #12
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(500,350)
star.pendown()                         #13
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-500,350)
star.pendown()                         #13
for i in range(5):
    star.left(216)
    star.forward(10)


star.penup()
star.goto(250,10)
star.pendown()
for i in range(5):                       #14
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-250,10)
star.pendown()
for i in range(5):                       #14
    star.left(216)
    star.forward(10)

star.penup()
star.goto(400,100)
star.pendown()                           #15
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-400,100)
star.pendown()                           #15
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(150,300)
star.pendown()                           #16
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-140,300)
star.pendown()                           #16
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(350,325)
star.pendown()                           #17
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-50,50)
star.pendown()                           #17
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-300,350)
star.pendown()                           #18
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(300,375)
star.pendown()                           #18
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-650,375)
star.pendown()                           #19 (last star)
for i in range(5):
    star.left(216)
    star.forward(10)

star.penup()
star.goto(-600,0)
star.pendown()                           # making it go away
for i in range(5):
    star.left(216)
    star.forward(10)


########################################## DEFINING FUNCTION FOR UPPER STARS
star.speed(100)
for i in range(1):
    def tara(star):
        star.color("#000E22")
        star.penup()
        star.goto(-90, 350)
        star.pendown()  # 8
        for i in range(5):
            star.left(216)
            star.forward(10)

        star.penup()
        star.goto(-700, 300)
        star.pendown()  # 10
        for i in range(5):
            star.left(216)
            star.forward(10)

        star.penup()
        star.goto(450, 250)
        star.pendown()  # 12
        for i in range(5):
            star.left(216)
            star.forward(10)

        star.penup()
        star.goto(-450, 250)
        star.pendown()  # 12
        for i in range(5):
            star.left(216)
            star.forward(10)

        star.penup()
        star.goto(350, 325)
        star.pendown()  # 17
        for i in range(5):
            star.left(216)
            star.forward(10)

        star.penup()
        star.goto(-300, 350)
        star.pendown()  # 18
        for i in range(5):
            star.left(216)
            star.forward(10)

        star.penup()
        star.goto(300, 375)
        star.pendown()  # 18
        for i in range(5):
            star.left(216)
            star.forward(10)

        star.penup()
        star.goto(-650, 375)
        star.pendown()  # 19 (last star)
        for i in range(5):
            star.left(216)
            star.forward(10)

        star.penup()
        star.goto(45, 300)
        star.pendown()  # 8
        for i in range(5):
            star.left(216)
            star.forward(10)

        def tara1(star):
            star.color("white")
            star.penup()
            star.goto(-90, 350)
            star.pendown()  # 8
            for i in range(5):
                star.left(216)
                star.forward(10)

            star.penup()
            star.goto(-700, 300)
            star.pendown()  # 10
            for i in range(5):
                star.left(216)
                star.forward(10)

            star.penup()
            star.goto(450, 250)
            star.pendown()  # 12
            for i in range(5):
                star.left(216)
                star.forward(10)

            star.penup()
            star.goto(-450, 250)
            star.pendown()  # 12
            for i in range(5):
                star.left(216)
                star.forward(10)

            star.penup()
            star.goto(350, 325)
            star.pendown()  # 17
            for i in range(5):
                star.left(216)
                star.forward(10)

            star.penup()
            star.goto(-300, 350)
            star.pendown()  # 18
            for i in range(5):
                star.left(216)
                star.forward(10)

            star.penup()
            star.goto(300, 375)
            star.pendown()  # 18
            for i in range(5):
                star.left(216)
                star.forward(10)

            star.penup()
            star.goto(-650, 375)
            star.pendown()  # 19 (last star)
            for i in range(5):
                star.left(216)
                star.forward(10)

            star.penup()
            star.goto(45, 300)
            star.pendown()  # 8
            for i in range(5):
                star.left(216)
                star.forward(10)









            def tara2(star):
                star.color("#000E22")

                star.penup()
                star.goto(-500, 350)
                star.pendown()  # 13
                for i in range(5):
                    star.left(216)
                    star.forward(10)

                star.penup()
                star.goto(150, 300)
                star.pendown()  # 16
                for i in range(5):
                    star.left(216)
                    star.forward(10)

                star.penup()
                star.goto(-140, 300)
                star.pendown()  # 16
                for i in range(5):
                    star.left(216)
                    star.forward(10)

                star.penup()
                star.goto(270, 270)
                star.pendown()
                for i in range(5):  # 2
                    star.left(216)
                    star.forward(10)

                star.penup()
                star.goto(-270, 270)
                star.pendown()
                for i in range(5):  # 2
                    star.left(216)
                    star.forward(10)

                star.penup()
                star.goto(-600, 250)
                star.pendown()  # 3
                for i in range(5):
                    star.left(216)
                    star.forward(10)

                star.penup()
                star.goto(90, 500)
                star.pendown()
                for i in range(5):  # 7
                    star.left(216)
                    star.forward(10)

                star.penup()
                star.goto(-110, 500)
                star.pendown()
                for i in range(5):  # 7
                    star.left(216)
                    star.forward(10)


                def tara3(star):
                    star.color("white")

                    star.penup()
                    star.goto(-500, 350)
                    star.pendown()  # 13
                    for i in range(5):
                        star.left(216)
                        star.forward(10)

                    star.penup()
                    star.goto(150, 300)
                    star.pendown()  # 16
                    for i in range(5):
                        star.left(216)
                        star.forward(10)

                    star.penup()
                    star.goto(-140, 300)
                    star.pendown()  # 16
                    for i in range(5):
                        star.left(216)
                        star.forward(10)

                    star.penup()
                    star.goto(270, 270)
                    star.pendown()
                    for i in range(5):  # 2
                        star.left(216)
                        star.forward(10)

                    star.penup()
                    star.goto(-270, 270)
                    star.pendown()
                    for i in range(5):  # 2
                        star.left(216)
                        star.forward(10)

                    star.penup()
                    star.goto(-600, 250)
                    star.pendown()  # 3
                    for i in range(5):
                        star.left(216)
                        star.forward(10)

                    star.penup()
                    star.goto(90, 500)
                    star.pendown()
                    for i in range(5):  # 7
                        star.left(216)
                        star.forward(10)

                    star.penup()
                    star.goto(-110, 500)
                    star.pendown()
                    for i in range(5):  # 7
                        star.left(216)
                        star.forward(10)



                tara3(star)
            tara2(star)
        tara1(star)
    tara(star)
#################################### END DEFINING FUNCTION FOR UPPER STARS
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END STARS



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START MOON
moon=turtle.Turtle()
moon.color("white","white")
moon.pensize(10)

moon.speed(25)
moon.penup()
moon.goto(-600, 300)
moon.pendown()
moon.begin_fill()
for i in range(50):
    moon.forward(10)
    moon.left(100)
    moon.forward(2)                  # moon
    moon.right(50)
    moon.forward(20)
moon.end_fill()

moon.left(95)
moon.forward(72)                      # positioning circle
moon.left(90)

moon.color("#000E22","#000E22")
moon.begin_fill()
moon.circle(30)                       # circle diminishing moon
moon.end_fill()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END MOON




#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START BACK MOUNTAINS
bmount=turtle.Turtle()
bmount.pensize(3)
bmount.color("#3575B5","#8cbaba") #light white green
bmount.begin_fill()
bmount.speed(5)

bmount.penup()
bmount.right(90)                              #positioning back mountain
bmount.forward(30)
bmount.right(90)
bmount.forward(770)
bmount.right(90)
bmount.forward(300)
bmount.right(110)
bmount.pendown()

bmount.forward(350)
bmount.backward(50)
bmount.left(45)
bmount.forward(200)
bmount.right(45)                               #making 1st back mountain
bmount.forward(300)
bmount.backward(100)
bmount.left(45)
bmount.forward(100)
bmount.right(45)
bmount.forward(100)

bmount.right(120)
bmount.forward(150)
bmount.backward(300)                           #making 2nd back mountain
bmount.left(110)
bmount.forward(250)
bmount.backward(50)
bmount.left(60)
bmount.forward(100)
bmount.right(45)
bmount.forward(350)

bmount.penup()
bmount.right(75)
bmount.forward(177)                             #joing back mountains
bmount.right(90)
bmount.pendown()
bmount.forward(1580)
bmount.right(90)
bmount.forward(300)
bmount.end_fill()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END BACK MOUNTAINS



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START FRONT MOUNTAINS
mount=turtle.Turtle()
mount.pensize(3)
mount.color("#3575B5","#197575") #light fade green
mount.begin_fill()
mount.speed(10)
mount.penup()
mount.right(90)                              #positioning front mountain
mount.forward(30)
mount.right(90)
mount.forward(770)
mount.right(90)
mount.forward(25)
mount.right(70)
mount.pendown()

mount.forward(800)
mount.right(45)
mount.forward(550)                              #making  1st mountain
mount.backward(100)

mount.left(80)
mount.forward(300)
mount.right(80)
mount.forward(50)
mount.left(80)                                  #making 2nd mountain
mount.backward(100)
mount.forward(200)
mount.right(100)
mount.forward(200)

mount.penup()
mount.right(45)
mount.forward(275)                             #joing front mountains
mount.right(90)
mount.pendown()
mount.forward(1580)
mount.right(90)
mount.forward(25)
mount.end_fill()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END FRONT MOUNTAINS





#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START SNOW ON MOUNTAIN
snow=turtle.Turtle()
snow.color("white","white")
snow.pensize(10)
snow.speed(50)

snow.penup()
snow.left(90)
snow.forward(300)
snow.left(90)
snow.forward(773)                              #positioning snow for leftmost mountain
snow.left(90)
snow.forward(100)
snow.left(90)
snow.pendown()

snow.begin_fill()
for i in range(5):
    snow.forward(15)
    snow.left(100)
    snow.forward(2)
    snow.right(90)
    snow.forward(5)                            # making snow on leftmost back mountain
snow.left(110)
snow.forward(100)
snow.left(110)
snow.forward(75)
snow.end_fill()


snow.penup()
snow.left(90)                                 #positioning snow for middle front mountain
snow.forward(595)
snow.pendown()
snow.pensize(20)

snow.begin_fill()
for i in range(7):
    snow.forward(20)
    snow.right(91)                         # making snow on middle front mountain
    snow.forward(5)
    snow.left(90)
    snow.forward(5)

for i in range(6):
    snow.forward(20)
    snow.left(93)                         # making snow on middle front mountain
    snow.forward(5)
    snow.right(90)
    snow.forward(5)
snow.left(143)
snow.forward(160)
snow.left(45)
snow.forward(165)
snow.end_fill()


snow.penup()
snow.left(168)                                 #positioning snow for 1st right front mountain
snow.forward(715)
snow.right(30)
snow.pendown()
snow.pensize(6)

snow.begin_fill()
for i in range(5):
    snow.forward(10)
    snow.left(100)
    snow.forward(2)
    snow.right(90)
    snow.forward(2)                         # making snow on 1st right front mountain
snow.left(125)
snow.forward(40)
snow.left(85)
snow.forward(30)
snow.end_fill()

snow.penup()
snow.left(90)                                #positioning snow for 2nd right front mountain
snow.forward(50)
snow.right(30)
snow.pendown()
snow.begin_fill()
snow.pensize(10)


for i in range(6):
    snow.forward(10)
    snow.left(93)                         # making snow on 2nd right front mountain
    snow.forward(5)
    snow.right(90)
    snow.forward(5)
for i in range(10):
    snow.forward(5)
    snow.left(93)
    snow.forward(5)
    snow.right(90)
    snow.forward(5)
snow.left(85)                                # making snow on 2nd right front mountain
snow.forward(40)
snow.left(60)
snow.forward(180)
snow.left(100)
snow.forward(140)
snow.end_fill()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END SNOW ON MOUNTAIN


tara(star)


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START HILL
hill=turtle.Turtle()
hill.speed(25)

hill.penup()
hill.right(90)
hill.forward(30)
hill.right(90)
hill.forward(770)                           # positioning hill
hill.right(90)
hill.forward(30)
hill.right(40)
hill.pendown()

hill.pensize(3)
hill.color("#4d1800","#383300")  #green brown
hill.begin_fill()
for i in range(10):
    hill.forward(10)
    hill.right(100)                         # making left small hill
    hill.forward(2)
    hill.left(90)
    hill.forward(10)

hill.left(45)
hill.forward(20)
hill.left(70)                               #positioning middle small hill
hill.forward(10)

for i in range(12):
    hill.forward(10)
    hill.right(100)
    hill.forward(2)                         #making middle small hill
    hill.left(90)
    hill.forward(60)

hill.left(45)
hill.forward(20)
hill.left(70)                               #positioning 2nd middle small hill
hill.forward(20)

for i in range(8):
    hill.forward(10)
    hill.right(100)
    hill.forward(2)                         #making 2nd middle small hill
    hill.left(90)
    hill.forward(30)

hill.forward(20)                              #positioning 3rd middle small hill
hill.forward(20)

for i in range(3):
    hill.forward(10)
    hill.left(100)
    hill.forward(2)                         #making 3rd middle small hill
    hill.right(80)
    hill.forward(30)

hill.forward(20)                              #positioning right small hill
hill.forward(20)

for i in range(5):
    hill.forward(10)
    hill.right(100)
    hill.forward(2)                         #making right small hill
    hill.left(80)
    hill.forward(60)

hill.penup()
hill.right(30)
hill.forward(52)
hill.right(90)
hill.pendown()                               #joining hill
hill.forward(1745)
hill.right(90)
hill.forward(30)
hill.end_fill()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END HILL





#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START FIELD
field=turtle.Turtle()
field.pensize(5)
field.penup()
field.right(90)                          #positioning field
field.forward(230)
field.right(90)
field.forward(770)
field.right(180)
field.pendown()

field.color("#55B61C","#55B61C")          #light green color
field.begin_fill()
field.forward(1540)
field.left(90)
field.forward(200)                        #making light green field
field.left(90)
field.forward(1540)
field.left(90)
field.forward(200)
field.end_fill()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END FIELD





#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START HOUSE
house=turtle.Turtle()
house.speed(5)

house.penup()
house.goto(400,-80)                    # positioning house
house.left(90)
house.pendown()

house.color("orange","orange")
house.pensize(3)
house.begin_fill()
house.forward(100)
house.right(90)
house.forward(150)
house.right(90)                        # front wall
house.forward(100)
house.right(90)
house.forward(150)
house.right(90)
house.forward(100)

house.right(45)
house.forward(105)
house.right(90)
house.forward(105)                       # front top yellow terrace
house.right(135)
house.forward(150)
house.right(90)

house.end_fill()

house.color("white","white")
house.pensize(10)
house.right(45)
house.backward(20)
house.forward(125)                     # front top white line terrace
house.right(90)
house.forward(125)
house.backward(125)

def back_top(house):
    house.color("white","white")
    house.pensize(10)
    house.begin_fill()
    house.left(60)
    house.forward(150)
    house.right(60)                        # back top  terrace
    house.forward(125)
    house.backward(20)
    house.right(120)
    house.forward(150)
    house.end_fill()
back_top(house)

house.color("red","red")
house.pensize(3)
house.begin_fill()
house.left(75)
house.forward(100)
house.left(105)                        # back wall
house.forward(150)
house.left(75)
house.forward(100)
house.end_fill()

house.penup()
house.backward(100)
house.right(75)
house.backward(150)                    # positioning gate
house.left(165)
house.forward(50)
house.right(90)
house.pendown()

house.color("black","black")
house.begin_fill()
for i in range(4):                     # gate
    house.forward(60)
    house.left(90)
house.end_fill()

house.penup()
house.right(90)
house.forward(50)
house.left(90)                         # positioning back top terrace to cover red
house.forward(100)
house.left(45)
house.pendown()

house.color("white","white")
house.pensize(10)
house.backward(25)
house.forward(125)                      # making again back top terrace
house.right(180)
back_top(house)


'''house.penup()
house.goto(470,40)
house.pendown()
house.pensize(3)
house.color("black","black")            # making hole
house.begin_fill()
house.circle(10)
house.right(90)
house.end_fill()'''
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END HOUSE





#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START WAY
way=turtle.Turtle()

way.penup()
way.goto(450,-80)
way.right(180)                             # positioning way
way.pendown()

way.speed(20)
way.color("#c2a370","#c2a370") #skin soil color
way.begin_fill()
way.pensize(5)
for i in range(5):
    way.forward(5)
    way.left(100)
    way.forward(2)                         #making left small way
    way.right(80)
    way.forward(7)

way.pensize(10)
for i in range(5):
    way.forward(5)
    way.right(100)
    way.forward(2)                         #making left big way
    way.left(80)
    way.forward(30)

way.pensize(10)
way.right(180)
way.forward(212)
way.left(45)

way.pensize(10)
for i in range(5):
    way.forward(5)
    way.left(100)
    way.forward(2)                         #making right big way
    way.right(80)
    way.forward(17)

way.pensize(5)
for i in range(5):
    way.forward(5)
    way.right(100)
    way.forward(2)                         #making right small way
    way.left(80)
    way.forward(5.8)

way.pensize(10)
way.left(135)
way.forward(57)
way.end_fill()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END WAY





#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START SNOWMAN
bob = turtle.Turtle()
bob.speed(100)
bob.pensize(3)                                #making BOB
bob.color("white","white")                  
bob.begin_fill()
for i in range(72):
    bob.forward(10)
    #bob.left(math.sin(i/10)*25)
    #bob.right(20)
    bob.left(355)
for i in range(62):
    bob.forward(10)
    bob.right(350)
bob.end_fill()

bob.color("black","black")
bob.begin_fill()
#sunglasses starts
bob.left(100)
bob.forward(20)
bob.right(90)
bob.forward(10)
bob.left(90)
bob.forward(20)
bob.left(90)                     #first lence
bob.forward(20)
bob.left(90)
bob.forward(20)
bob.left(90)
bob.forward(10)

bob.penup()
bob.left(90)
bob.forward(20)
bob.pendown()

bob.forward(30)
bob.right(90)
bob.forward(10)
bob.left(90)
bob.forward(20)
bob.left(90)                      #second lence
bob.forward(20)
bob.left(90)
bob.forward(20)
bob.left(90)
bob.forward(10)

bob.penup()
bob.left(90)
bob.forward(20)
bob.pendown()

bob.forward(20)

bob.end_fill()
#sun glasses finished

bob.penup()
bob.right(90)
bob.forward(20)
bob.right(90)                       #positioning nose
bob.forward(55)
bob.pendown()

#making nose
bob.color("red","red")
bob.begin_fill()
for i in range(52):
    bob.forward(1)
    bob.left(45)
    bob.forward(2)

bob.end_fill()
#making nose finished


#making smile
bob.color("black","black")
bob.penup()
bob.left(180)
bob.forward(25)
bob.left(90)
bob.forward(10)
bob.pendown()

for i in range(3):
    bob.forward(10)
    bob.left(45)

bob.right(45)
bob.forward(15)

for i in range(3):
    bob.forward(10)
    bob.left(45)
#making smile finished

bob.color("black","black")
bob.pensize(15)
bob.penup()
bob.left(150)
bob.forward(100)                    #positioning right hand
bob.left(90)
bob.forward(45)
bob.pendown()

#right hand
bob.left(30)
bob.forward(100)
bob.left(30)
bob.forward(20)
bob.backward(20)
bob.right(60)
bob.forward(60)
#right hand finished

bob.penup()
bob.right(90)
bob.forward(50)
bob.right(97)                           #left hand positioning
bob.forward(340)
bob.pendown()

#left hand
bob.right(45)
bob.forward(100)
bob.right(30)
bob.forward(20)
bob.backward(20)
bob.left(60)
bob.forward(60)
#left hand finished
#MAKING SNOWMAN (BOB) FINISHED

bob.penup()
bob.left(30)
bob.forward(300)
bob.left(90)                          #positioning tree
bob.forward(132)
bob.right(203)
bob.pendown()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END SNOWMAN




#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START TREES
#BIG TREE
bob.speed(100)
bob.pensize(20)
bob.color("#551A00") #dark brown
bob.forward(300)                        #trunk


bob.color("green")                      #branches
bob.begin_fill()

#starting 2 small branches
bob.pensize(9)
bob.left(45)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3.25*l/5)
        bob.right(60)
        draw(3.25*l/5)
        bob.left(30)
        bob.backward(l)

draw(72)

bob.right(90)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3.25*l/5)
        bob.right(60)
        draw(3.25*l/5)
        bob.left(30)
        bob.backward(l)

draw(72)
#starting 2 small branches finished

bob.pensize(6)
bob.left(45)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/4)
        bob.right(60)             #middle main branch
        draw(3*l/4)
        bob.left(30)
        bob.backward(l)

draw(90)

#leftmost branch
bob.pensize(6)
bob.left(70)
bob.forward(100)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/4)
        bob.right(60)
        draw(3*l/4)
        bob.left(30)
        bob.backward(l)

draw(50)

#rightmost branch
bob.backward(100)
bob.right(140)
bob.forward(100)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/4)
        bob.right(60)
        draw(3*l/4)
        bob.left(30)
        bob.backward(l)

draw(50)

bob.end_fill()
bob.backward(100)
#BIG TREE finished

bob.penup()
bob.left(70)
bob.left(180)
bob.forward(300)
bob.left(90)                    #positioning right small tree
bob.forward(110)
bob.left(90)
bob.pendown()

#RIGHT SMALL TREE
bob.pensize(20)
bob.color("#551A00")
bob.forward(100)                 #trunk of right tree

bob.color("#004200")   #dark green            #branches
bob.begin_fill()

#starting 2 small branches
bob.pensize(9)
bob.left(45)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/5)
        bob.right(60)
        draw(3*l/5)
        bob.left(30)
        bob.backward(l)

draw(50)

bob.right(90)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/5)
        bob.right(60)
        draw(3*l/5)
        bob.left(30)
        bob.backward(l)

draw(50)
#starting 2 small branches finished


bob.pensize(7)
bob.color("green")
bob.left(45)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3.5*l/5)
        bob.right(60)             #middle main branch OF RIGHT SMALL TREE
        draw(3.5*l/5)
        bob.left(30)
        bob.backward(l)

draw(65)

#leftmost branch
bob.pensize(5)
bob.color("#004200")
bob.left(70)
bob.forward(2)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/4)
        bob.right(60)
        draw(3*l/4)
        bob.left(30)
        bob.backward(l)

draw(50)

#rightmost branch
bob.backward(2)
bob.right(140)
bob.forward(2)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/4)
        bob.right(60)
        draw(3*l/4)
        bob.left(30)
        bob.backward(l)

draw(50)

bob.end_fill()
bob.backward(2)
#RIGHT SMALL TREE FINISHED

bob.penup()
bob.left(70)
bob.left(180)
bob.forward(100)
bob.right(90)                    #positioning left small tree
bob.forward(250)
bob.right(90)
bob.pendown()

#LEFT SMALL TREE
bob.pensize(20)
bob.color("#551A00")
bob.forward(150)                  #trunk of left tree


bob.color("#004200")                #branches
bob.begin_fill()

#starting 2 small branches
bob.pensize(9)
bob.left(45)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/5)
        bob.right(60)
        draw(3*l/5)
        bob.left(30)
        bob.backward(l)

draw(50)

bob.right(90)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/5)
        bob.right(60)
        draw(3*l/5)
        bob.left(30)
        bob.backward(l)

draw(50)
#starting 2 small branches finished

bob.pensize(7)
bob.color("green")
bob.left(45)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3.5*l/5)
        bob.right(60)             #middle main branch OF LEFT SMALL TREE
        draw(3.5*l/5)
        bob.left(30)
        bob.backward(l)

draw(60)

#leftmost branch
bob.pensize(5)
bob.color("#004200")
bob.left(70)
bob.forward(2)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/4)
        bob.right(60)
        draw(3*l/4)
        bob.left(30)
        bob.backward(l)

draw(40)

#rightmost branch
bob.backward(2)
bob.right(140)
bob.forward(2)
def draw(l):
    if(l<10):
        return
    else:
        bob.forward(l)
        bob.left(30)
        draw(3*l/4)
        bob.right(60)
        draw(3*l/4)
        bob.left(30)
        bob.backward(l)

draw(40)

bob.backward(2)
bob.end_fill()

bob.penup()
bob.left(70)
bob.left(180)
bob.forward(100)
bob.right(90)                    #removing bob
bob.forward(250)
bob.right(90)
bob.pendown()
#LEFT SMALL TREE FINISHED
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END TREES


tara(star)


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START ROAD
road=turtle.Turtle()
road.speed(5)
road.penup()
road.right(90)
road.forward(235)
road.right(90)                    #positioning ROAD
road.forward(770)
road.right(180)
road.pendown()

#Making road
road.color("black","black")
road.begin_fill()

road.pensize(10)
road.forward(1540)
road.right(90)
road.forward(160)
road.right(90)                    #making road black
road.forward(1540)
road.right(90)
road.forward(160)
road.end_fill()


road.right(180)
road.forward(65)
road.left(90)
road.pensize(5)
for i in range(16):                 #making white line strips
    road.color("white")
    road.forward(50)
    road.penup()
    road.forward(50)
    road.pendown()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END ROAD



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX START FENCES
road.penup()
road.right(90)
road.forward(100)                     #positioning fences
road.right(90)
road.pendown()

road.speed(100)
road.pensize(15)
road.color("brown")
road.forward(83)
road.right(90)                       #making fences
for i in range(32):
    road.forward(110)
    road.backward(110)
    road.left(90)
    road.forward(50)
    road.right(90)

road.pensize(5)
road.penup()
road.forward(30)                  #positioning small stripes
road.right(90)
road.pendown()


road.color("orange")
road.forward(1640)
road.left(90)                    #making small strips
road.forward(20)
road.left(90)
road.forward(1640)

road.penup
road.right(90)
road.forward(125)                  #positioning 2nd fence
road.right(90)
road.pendown()

road.pensize(15)
road.color("brown")
road.forward(80)                       #making 2nd fences
road.left(90)
for i in range(22):
    road.forward(110)
    road.backward(110)
    road.right(90)
    road.forward(50)
    road.left(90)

road.penup()
road.right(90)
road.forward(200)                       #giving gap for way
road.pendown()
road.forward(50)
road.left(90)

for i in range(5):
    road.forward(110)
    road.backward(110)
    road.right(90)                      #continuing 2nd fences
    road.forward(50)
    road.left(90)


road.pensize(5)
road.penup()
road.forward(30)                        #positioning 2nd small stripes
road.left(90)
road.pendown()


road.color("orange")
road.forward(255)                       #making 2nd small stripes

road.penup()
road.forward(290)                       #giving gap for way
road.pendown()

road.forward(1100)
road.right(90)                          #cotinuing 2nd small strips
road.forward(20)
road.right(90)
road.forward(1100)

road.penup()
road.forward(290)                       #giving gap for way
road.pendown()

road.forward(290)                       #finally finishing 2nd small stripes
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END FENCES


for i in range(10000):
    tara(star)                          #IN THE END MAKING THE STARS TWINKLE


turtle.done()