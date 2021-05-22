import pyttsx3,time,random,sys
engine = pyttsx3.init()
voices = engine.getProperty('voices')
number=["0"]
lst_loc=["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

# ITS HAPPENING TOO SLOW SO REAL TYPE FEELING IS NOT COMING BETTER USE SIMPLE PRINT STATEMENT ONE
'''lst=[]
msg = "Let's see who is gonna win, well well well!, no worries i am pro at this."
a=msg.split()
for i in msg.split():
    lst.append(i)
for char in a:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.00000000000009)
    richard(char)'''


'''                 **************************************** CHARACTERS IN THE GAME ********************************************                      '''

# index 0 is for DAVID
# index 1 is for RICHARD (narrator MALE)
# index 2 is for MARK (OPPONENT 1 MALE)
# index 3 is for LINDA (OPPONENT 2 FEMALE)
# index 4 is for ZIRA (narrator FEMALE)

#MALE NARRATOR RICHARD
def richard(line):
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 195) #190
    engine.say(line)
    engine.runAndWait()
#FEMALE NARRATOR ZIRA
def zira(line):
    engine.setProperty('voice', voices[4].id)
    engine.setProperty('rate', 180)
    engine.say(line)
    engine.runAndWait()
#OPPONENT 1 MALE: MARK
def mark(line):
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 170) #170
    engine.say(line)
    engine.runAndWait()
#OPPONENT 2 FEMALE: LINDA
def linda(line):
    engine.setProperty('voice', voices[3].id)
    engine.setProperty('rate', 170)
    engine.say(line)
    engine.runAndWait()




'''  ************ INTRODUCTORY PART: WHERE NAME IS ASKED ND SELECTION OF OPPONENTS IS DONE WITH VARIOUS INSTRUCTIONS ARE GIVEN ABT GAME ************  '''

# RICHARD IS SPEAKING IN WELCOME
def welcome(lst_loc,number):
    width=180
    print("| HELLO |".center(180))
    l_1=("HELLO !")
    richard(l_1)

    print("| WELCOME TO TICTACTOE |".center(180))
    l_2 = ("WELCOME TO TICTACTOE")
    richard(l_2)
    print()

    print("Press S for opening game settings.")
    l_3 = ("Press S for opening game settings.")
    richard(l_3)

    print("Or Press enter to skip.")
    l_4 = ("Or Press enter to skip.")
    richard(l_4)
    ch=input("=> ")

    if ch in ["S","s"]:
        print("Directing you to GAME SETTINGS", end=" ")
        l_5 = ("Directing you to GAME SETTINGS")
        richard(l_5)
        for i in range(4):
            time.sleep(0.50)
            print(".", end="")
        print()
        settings(lst_loc,number)
    elif ch=="":
        askname(lst_loc,number)

# ZIRA IS SPEAKING IN SETTINGS
def settings(lst_loc,number):
    width=180
    print("| HELLO WELCOME TO TICTACTOE SETTINGS. |".center(width))
    l_1 = ("HELLO WELCOME TO TICTACTOE SETTINGS.")
    zira(l_1)

    print("| There will be 3x3 matrix in the game. |".center(width))
    l_2 = ("There will be 3 cross 3 matrix in the game.")
    zira(l_2)

    print("| You have to select O OR X as per ur choice. |".center(width))
    l_3 = ("You have to select O OR X as per your choice.")
    zira(l_3)

    print("| And then enter ur choice in the specified row and column. |".center(width))
    l_4 = ("And then enter your choice in the specified row and column.")
    zira(l_4)

    print("| TOSS WILL BE THERE IN ORDER TO DECIDE WHOSE TURN IS FIRST. | ".center(width))
    l_5 = ("TOSS WILL BE THERE IN ORDER TO DECIDE WHOSE TURN IS FIRST.")
    zira(l_5)

    print("| Easy right? Ik it is, WISH YA LUCK. |".center(width))
    l_5 = ("Easy right? I know it is, WISH YA LUCK.")
    zira(l_5)
    print()

    print("Press B to go back:")
    back = ("Press B to go back:")
    zira(back)
    back=input("=> ")

    if back in ["B","b"]:
        pass
        askname(lst_loc,number)
    else:
        print("OK, continue reading settings.")
        l_6 = ("OK, continue reading settings.")
        zira(l_6)

        print("Press D when you are done with reading.")
        l_7 = ("Press D when you are done with reading.")
        zira(l_7)
        ch = input("=> ")         #asking again
        if ch in ["D", "d"]:
            pass
            askname(lst_loc,number)
        else:
            print("Come when you want to play, BYE!")
            l_8 = ("Come when you want to play, BYE!")
            zira(l_8)

# RICHARD IS SPEAKING IN ASKNAME
def askname(lst_loc,number):
    print()
    print("Enter your user name before starting the game:")
    l_1 = ("Enter your user name before starting the game:")
    richard(l_1)
    name = input("=> ")
    opponent_ch(lst_loc,name,number)

# RICHARD, MARK, LINDA, IS SPEAKING IN OPPONENT_CH  # REPLAY FUNCTION STARTS FRM HERE AGAIN
def opponent_ch(lst_loc,name,number):

    # without replay
    if len(number)==1:
        print("| With whom do you want to play the game? |".center(180))
        l_2=("| With whom do you want to play the game? |")
        richard(l_2)
        print()

        print("To play with Mark, press M!")
        l_3=("To play with Mark, press M!")
        richard(l_3)
        print("To play with Linda, press L!")
        l_4=("To play with Linda, press L!")
        richard(l_4)

        oppo = input("=> ")
        # MARK IS SPEAKING HIS GREATNESS
        if oppo in ["m", "M"]:
            oppo = "Mark"
            print("Mark: ", end="")
            print("Hello " + name + ", Thanks for choosing me.")
            l_1 = ("Hello " + name + ", Thanks for choosing me.")
            mark(l_1)

            print("Mark: ", end="")
            print("Let's see who is gonna win, well well well!, no worries i am pro at this.")
            l_2 = ("Let's see who is gonna win, well well well!, no worries i am pro at this.")
            mark(l_2)
            introduction(lst_loc, name, oppo, number)

        # LINDA IS FLEXING HER STYLE
        elif oppo in ["l", "L"]:
            oppo="Linda"
            print("Linda: ", end="")
            print("Ohh Hi there " + name + ", Thanks a lot for choosing me, I have been waiting since a long time.")
            l_1 = ("Ohh Hi there " + name + ", Thanks a lot for choosing me, I have been waiting since a long time.")
            linda(l_1)

            print("Linda: ", end="")
            print("But yeah, I am not a bad player for real.")
            l_2 = ("But yeah, I am not a bad player for real.")
            linda(l_2)

            print("Linda: ",end="")
            print("Well! Let's see who is gonna win.")
            l_3=("Well! Let's see who is gonna win.")
            linda(l_3)

            introduction(lst_loc, name, oppo, number)

    # with replay
    elif len(number)%2!=0 and len(number)>1:
        print("| With whom do you want to play the game again? |".center(180))
        l_2 = ("| With whom do you want to play the game again? |")
        richard(l_2)
        print()

        print("To play with Mark again, press M!")
        l_3 = ("To play with Mark again, press M!")
        richard(l_3)
        print("To play with Linda again, press L!")
        l_4 = ("To play with Linda again, press L!")
        richard(l_4)

        oppo = input("=> ")
        # MARK IS SPEAKING HIS GREATNESS AGAIN
        if oppo in ["m", "M"]:
            oppo = "Mark"
            print("Mark: ", end="")
            print("OHH hey " + name + ", Thanks for choosing me in the new game.")
            l_1 = ("OHH hey " + name + ", Thanks for choosing me in the new game.")
            mark(l_1)

            print("Mark: ", end="")
            print("Well without any further talks, Let's see who is gonna win this time.")
            l_2 = ("Well without any further talks, Let's see who is gonna win this time.")
            mark(l_2)

            print("Are you ready to toss for the new game? (press y or n)")
            ready = ("Are you ready to toss for the new game?")
            richard(ready)
            ch = input("=> ")
            if ch in ["Y", "y"]:
                playrps(lst_loc, name, oppo, number)  # opponent ch will come

            elif ch in ["N", "n"]:
                print("Come when you want to play, BYE")
                l = ("Come when you want to play, BYE")
                richard(l)

        # LINDA IS FLEXING HER STYLE AGAIN
        elif oppo in ["l", "L"]:
            oppo = "Linda"
            print("Linda: ", end="")
            print("AHHA Hi there " + name + ", you are here again, right? Btw thanks for choosing me in the new game.")
            l_1 = ("AHHA Hi there " + name + ", you are here again, right? By the way thanks for choosing me in the new game.")
            linda(l_1)

            print("Linda: ", end="")
            print("I am so excited for the the new game, let's play it.")
            l_2 = ("I am so excited for the the new game, let's play it.")
            linda(l_2)


            print("Are you ready to toss for the new game?(press y or n) ")
            ready = ("Are you ready to toss for the new game?")
            richard(ready)
            ch = input("=> ")
            if ch in ["Y", "y"]:
                playrps(lst_loc, name,oppo, number)  # opponent ch will come

            elif ch in ["N", "n"]:
                print("Come when you want to play, BYE")
                l = ("Come when you want to play, BYE")
                richard(l)

# RICHARD IS SPEAKING IN INTRO...# Defining function which says some basic starting things and then calling ins_rps function i.e. directing to TOSS MANUAL.
def introduction(lst_loc,name,oppo,number):

    print()
    print("| OK NOW...IT'S TIME FOR THE TOSS |".center(180))
    l_2=("OK NOW...IT'S TIME FOR THE TOSS:")
    richard(l_2)

    print("Press t for opening toss settings.")
    l_2 = ("Press t for opening toss settings.")
    richard(l_2)

    print("Or Press enter to skip.")
    l_2 = ("Or Press enter to skip.")
    richard(l_2)

    strt = input("=> ")

    def opentoss(strt,name):

        if strt in ["T","t"]:
            print("Directing you to TOSS MANUAL",end=" ")
            l_3 = ("Directing you to TOSS MANUAL")
            richard(l_3)
            for i in range(4):
                time.sleep(0.75)
                print(".",end="")
            inst_rps(lst_loc,name,oppo,number)

        elif strt=="":
            # HERE RICHARD WILL ASK FOR TOSS...
            print("Are you ready to toss " + name + "? (press y or n) ")
            ready = ("Are you ready to toss " + name + "?")
            richard(ready)
            ch = input("=> ")

            if ch in ["Y", "y"]:
                playrps(lst_loc,name,oppo,number)
            else:
                print("Come when you want to play, BYE!")
                l_8 = ("Come when you want to play, BYE!")
                richard(l_8)

        else:
            print("SORRY try again! Do you want to skip?")
            l_3 = ("SORRY try again! Do you want to skip?")
            richard(l_3)
            restrt=input("=> ")


            opentoss(restrt,name)

    opentoss(strt,name)

# ZIRA IS SPEAKING IN TOSS MANUAL...# Defining function which tells the instructions for the rps toss game i.e.TOSS MANUAL(it is being called in introduction function)...which directs to playrps function.
def inst_rps(lst_loc,name,oppo,number):
    width=180
    print()
    print("| TOSS MANUAL |".center(width))
    l_1 = ("TOSS MANUAL")
    zira(l_1)

    print("| We will be playing ROCK-PAPER-SCISSORS for the toss. |".center(width))
    l_2 = ("We will be playing ROCK-PAPER-SCISSORS for the toss.")
    zira(l_2)

    print("| Press R for Rock. |".center(width))
    l_3 = ("Press R for Rock.")
    zira(l_3)

    print("| Press P for Paper. |".center(width))
    l_4 = ("Press P for Paper.")
    zira(l_4)

    print("| Press S for Scissors. |".center(width))
    print()
    l_5 = ("Press S for Scissors.")
    zira(l_5)

    print("| LET'S HOPE, YOU WILL WIN THE TOSS. |".center(width))
    print()
    l_5 = ("LET'S HOPE, YOU WILL WIN THE TOSS.")
    zira(l_5)

    # HERE RICHARD WILL ASK FOR TOSS...
    print("Are you ready to toss "+name+"? (press y or n) ")
    ready = ("Are you ready to toss "+name+"? ")
    richard(ready)
    ch=input("=> ")

    if ch in ["Y","y"]:
        playrps(lst_loc,name,oppo,number)

    elif ch in ["N","n"]:
        print("OK, continue reading toss manual.")
        l_6 = ("OK, continue reading toss manual.")
        zira(l_6)

        print("Press D when you are done with reading.")
        l_7 = ("Press D when you are done with reading.")
        zira(l_7)
        ch2 = input("=> ")  # asking again
        if ch2 in ["D", "d"]:
            playrps(lst_loc,name,oppo,number)
        else:
            print("Come when you want to play, BYE!")
            l_8 = ("Come when you want to play, BYE!")
            zira(l_8)




'''                      ************************* TOSSING PART: WHERE WHO WILL INPUT FIRST WILL DECIDE ***************************                     '''

# Defining function which marks the beginning of the rps toss game (it is being called after TOSS MANUAL i.e inst_rps function.
# ZIRA WILL SAY RPS AND RICHARD WILL CALL OUT THE RESULTS
def playrps(lst_loc,name,oppo,number):
    lst=["Rock","Paper","Scissors"]
    print("OK", end=" ")
    ok=("ok")
    zira(ok)

    for i in range(3):
        time.sleep(0.000000009)
        print(lst[i], end=":")
        l_1=(lst[i])
        zira(l_1)

    print("=>",end="")
    shoot=("shoot")
    zira(shoot)
    rpsu = str(input(""))  # taking user rps choice

    rpsc = random.choice(lst)  # taking comp. rps choice
    print()

    # Printing the entered value
    print("You: ", end="")
    if rpsu in ["R", "r"]:
        print("Rock")
    if rpsu in ["P", "p"]:
        print("Paper")
    if rpsu in ["S", "s"]:
        print("Scissors")
    print(oppo+": ", rpsc)
    print()

    # Checking who won the match:
    # if user choose rock
    if rpsu in ["R", "r"] and rpsc == "Scissors":  # user won
        print("Uk You just WON the toss...right?")
        rpsu = ("You know YOU just WON the toss...right?")
        richard(rpsu)
        loadmatrix(lst_loc,name,oppo,number, win="rpsu")

    elif rpsu in ["R", "r"] and rpsc == "Paper":  # computer won
        print("Uk "+oppo+" just WON the toss...right?")
        rpsc = ("You know "+oppo+" just WON the toss...right?")
        richard(rpsc)
        loadmatrix(lst_loc,name,oppo,number, win="rpsc")

    elif rpsu in ["R", "r"] and rpsc == "Rock":  # draw
        print("Bruh DRAW...try again.")
        draw = ("Bruh DRAW...try again.")
        richard(draw)
        print()
        playrps(lst_loc,name,oppo,number)


    # if user choose paper
    if rpsu in ["P", "p"] and rpsc == "Rock":  # user won
        print("Uk You just WON the toss...right?")
        rpsu = ("You know YOU just WON the toss...right?")
        richard(rpsu)
        loadmatrix(lst_loc,name,oppo,number, win="rpsu")

    elif rpsu in ["P", "p"] and rpsc == "Scissors":  # computer won
        print("Uk "+oppo+" just WON the toss...right?")
        rpsc = ("You know "+oppo+" just WON the toss...right?")
        richard(rpsc)
        loadmatrix(lst_loc,name,oppo,number, win="rpsc")

    elif rpsu in ["P", "p"] and rpsc == "Paper":  # draw
        print("Bruh DRAW...try again.")
        draw = ("Bruh DRAW...try again.")
        richard(draw)
        print()
        playrps(lst_loc,name,oppo,number)


    # if user choose scissors
    if rpsu in ["S", "s"] and rpsc == "Paper":  # user won
        print("Uk You just WON the toss...right?")
        rpsu = ("You know YOU just WON the toss...right?")
        richard(rpsu)
        loadmatrix(lst_loc,name,oppo,number, win="rpsu")

    elif rpsu in ["S", "s"] and rpsc == "Rock":  # computer won
        print("Uk "+oppo+" just WON the toss...right?")
        rpsc = ("You know "+oppo+" just WON the toss...right?")
        richard(rpsc)
        loadmatrix(lst_loc,name,oppo,number, win="rpsc")

    elif rpsu in ["S", "s"] and rpsc == "Scissors":  # draw
        print("Bruh DRAW...try again.")
        draw = ("Bruh DRAW...try again.")
        richard(draw)
        print()
        playrps(lst_loc,name,oppo,number)




'''                         ********************** TICTACTOE INTRO PART : TELLING ABT MATRIX STUFF ***************************                           '''

# Defining function which marks the intro of the MAIN TICTACTOE game (it is called frm playrps function after the toss).
# RICHARD IS SPEAKING IN LOADMATRIX
def loadmatrix(lst_loc,name,oppo,number,win):
    print("Now we know whose chance is first.")
    l_1=("Now we know whose chance is first.")
    richard(l_1)

    print("Press enter to start the game:")
    l_2=("Press enter to start the game:")
    richard((l_2))
    play=input("=> ")
    print()

    print("LOADING 3X3 MATRIX",end=" ")
    l_3 = ("LOADING 3 cross 3 MATRIX")
    richard(l_3)

    for i in range(4):
        time.sleep(0.5)
        print(".",end="")

    print("Sry for wait.")
    l_4 = ("Sorry for wait.")
    richard(l_4)
    print()
    gen_matrix(lst_loc,name,oppo,number,win)

# Defining function which provides the general matrix for player to understand.
# RICHARD IS SPEAKING IN GENERAL MATRIX
def gen_matrix(lst_loc,name,oppo,number,win):
    col = 3
    row = 3
    dic_gen = {}
    user_ch = "x"  # user choice
    lst_gen = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
               "w", "x", "y", "z"]
    for i in range(row):
        i = lst_gen[i]
        for j in range(1, col + 1):
            dict = {str(i) + str(j): user_ch}
            dic_gen.update(dict)
            if j == col:
                print("|", str(i) + str(j), "|")
            else:
                print("|", str(i) + str(j), end=" ")
        print()
    print()


    if len(number)==1:
        print("This is what an initial matrix looks like. Enter the block location as per your choice in order to win the game.")
        l_1 = ("This is what an initial matrix looks like. Enter the block location as per your choice in order to win the game.")
        richard(l_1)

    elif len(number) % 2 != 0 and len(number) > 1:
        print("You already know this is the initial matrix.")
        l_1=("You already know this is the initial matrix.")
        richard(l_1)

    makingchoice(lst_loc,name,oppo,number,win)


# Defining function in order to check who won RPS game AND THEN SPECIFING THE LOOP (called frm gen_matrix func).
# RICHARD IS SPEAKING IN HERE ABOUT VALUES.
def makingchoice(lst_loc,name,oppo,number,win):

    #WHEN USER WON THE TOSS.......
    if win == "rpsu":

        print("As...'You' will be the first one to make a move. ")
        l_1 = ("As...'You' will be the first one to make a move. ")
        richard(l_1)

        print("Select the value for the game: X or O - ")
        l_2 = ("Select the value for the game:")
        richard(l_2)
        ch = input("=> ")

        print("You selected: ", ch)
        l_3 = ("You selected " + ch)
        richard(l_3)

        # TAKING X OR O VALUES OF USER AND COMPUTER IN MATRIX
        if ch in ["X", "x"]:
            comp_chvalue = "O"
            print("So, "+oppo+" got: ", comp_chvalue)
            l_4 = ("So, "+oppo+" got " + comp_chvalue)
            richard(l_4)
        else:
            comp_chvalue = "X"
            print("So, "+oppo+" got: ", comp_chvalue)
            l_4 = ("So, "+oppo+" got: "+ comp_chvalue)
            richard(l_4)

        main1,a, us_a, a_, ad,CU1,CC1 = userwon(lst_loc,oppo,ch,comp_chvalue,number, comp_chloc="", user_chloc="", len_ch=[], dic={}, CU=["ku"],CC=["kc"],n="1st")
        if (len(str(a)) == 20 or len(str(a)) == 21 or len(str(a)) == 35) and len(us_a) in [1,2,3] and a_ == None and ad == None and CU1 ==None and CC1 ==None:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_a)
            return bye

        main2,b, us_b, b_, bd,CU2,CC2 = userwon(main1,oppo,ch,comp_chvalue,number, comp_chloc=a, user_chloc=us_a, len_ch=a_, dic=ad,CU=CU1,CC=CC1,n="2nd")
        if len(str(b)) == 20 or len(str(b)) == 21 or len(str(b)) == 35 and len(us_b) in [1,2,3]:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_b)
            return bye

        main3,c, us_c, c_, cd,CU3,CC3 = userwon(main2,oppo,ch,comp_chvalue,number, comp_chloc=b, user_chloc=us_b, len_ch=b_, dic=bd,CU=CU2,CC=CC2, n="3rd")
        if len(str(c)) == 20 or len(str(c)) == 21 or len(str(c)) == 35 and len(us_c) in [1,2,3]:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_c)
            return bye

        main4,d, us_d, d_, dd,CU4,CC4 = userwon(main3,oppo,ch,comp_chvalue,number,  comp_chloc=c, user_chloc=us_c, len_ch=c_, dic=cd,CU=CU3,CC=CC3, n="4th")
        if len(str(d)) == 20 or len(str(d)) == 21 or len(str(d)) == 35 and len(us_d) in [1,2,3]:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_d)
            return bye

        main5,e, us_e, e_, ed,CU5,CC5 = userwon(main4,oppo,ch,comp_chvalue,number, comp_chloc=d, user_chloc=us_d, len_ch=d_, dic=dd,CU=CU4,CC=CC4, n="5th")
        if len(str(e)) == 20 or len(str(e)) == 21 or len(str(e)) == 35 and len(us_e) in [1,2,3]:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_e)
            return bye


    #WHEN COMPUTER WON THE TOSS.....
    elif win == "rpsc":

        print("As..."+oppo+" will be the first one to make a move.")
        l_1 = ("As..."+oppo+" will be the first one to make a move.")
        richard(l_1)

        ch = random.choice(["X","O"])

        print(oppo+" is selecting value for the game: X or O")
        l_2 = (oppo+" is selecting value for the game:")
        richard(l_2)

        print(oppo+" selected: ", ch)
        l_3=(oppo+" selected:"+ch)
        richard(l_3)

        if ch in ["X", "x"]:
            u_ch = "O"
            print("So, you got: ", u_ch)
            l_4=("So, you got "+u_ch)
            richard(l_4)
        else:
            u_ch = "X"
            print("So, you got: ", u_ch)
            l_4=("So, you got "+u_ch)
            richard(l_4)


        main1,a, us_a, a_, ad, CU1, CC1 = compwon(lst_loc,oppo,ch,u_ch,number, comp_chloc="", user_chloc="", len_ch=[], dic={}, CU=["ku"], CC=["kc"],n="1st")
        if (len(str(a)) == 20 or len(str(a)) == 21 or len(str(a)) == 35) and len(us_a) in [1,2,3] and a_ == None and ad == None:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_a)
            return bye

        main2,b, us_b, b_, bd, CU2, CC2 = compwon(main1,oppo,ch,u_ch,number, comp_chloc=a, user_chloc=us_a, len_ch=a_, dic=ad, CU=CU1, CC=CC1,n="2nd")
        if len(str(b)) == 20 or len(str(b)) == 21 or len(str(b)) == 35 and len(us_b) in [1,2,3]:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_b)
            return bye

        main3,c, us_c, c_, cd, CU3, CC3 = compwon(main2,oppo,ch,u_ch,number, comp_chloc=b, user_chloc=us_b, len_ch=b_, dic=bd, CU=CU2, CC=CC2, n="3rd")
        if len(str(c)) == 20 or len(str(c)) == 21 or len(str(c)) == 35 and len(us_c) in [1,2,3]:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_c)
            return bye

        main4,d, us_d, d_, dd, CU4, CC4 = compwon(main3,oppo,ch,u_ch,number, comp_chloc=c, user_chloc=us_c, len_ch=c_, dic=cd, CU=CU3, CC=CC3, n="4th")
        if len(str(d)) == 20 or len(str(d)) == 21 or len(str(d)) == 35 and len(us_d) in [1,2,3]:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_d)
            return bye

        main5,e, us_e, e_, ed, CU5, CC5 = compwon(main4,oppo,ch,u_ch,number, comp_chloc=d, user_chloc=us_d, len_ch=d_, dic=dd, CU=CU4, CC=CC4, n="5th")
        if len(str(e)) == 20 or len(str(e)) == 21 or len(str(e)) == 35 and len(us_e) in [1,2,3]:
            # calling replay(name)
            bye = replay(lst_loc,name,number,oppo,what=us_e)
            return bye




'''                            ************** CALCULATIONS PART : WHERE DIFFERENT ALGORITHEMS ARE USED ********************************                       '''

'''  ************ FROM HERE REAL GAME STARTS I.E. TAKING INPUTS FROM USER AND THEN MAKING MATRIX ACCORDING TO IT AND THEN PRINTING THE RESULT ************   '''

                                                  # COMMON FUNCTION BETWEEN USER AND OPPONENT #
                                            # FROM HERE THEY DIVERGE INTO THIER SPECIFIED FUNCTIONS #

# Defining function in order to store the givepos function coz its so big tbh (called from userwon func or compwon func).
def ingame_matrix_check(oppo,user_chloc, user_chvalue,comp_chloc,comp_chvalue,lst_loc,dic,dic_u,dic_c,CU,CC,store):

    # Checking from who enter first value in order to determine which givepos func to call
    lst_user = []
    for i in dic.keys():
        lst_user.append(i)  # taking the keys of dic

    '''print(dic)
    print("u",CU)
    print("c",CC)
    print("list formed",lst_user)'''

    for i in range(len(lst_user)):

        if i % 2 == 0 and lst_user[i] in CU:
            #print("check givepos_user")
            if len(dic)<=10:
                retgive_user,what = givepos_user(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc, dic, dic_u, dic_c,
                                       store)  # calling the givepos_user function that give positions in matrix
                if len(str(retgive_user)) == 20 or len(str(retgive_user)) == 21 or len(str(retgive_user)) == 35:
                    #print("in here",retgive_user, what)
                    return retgive_user,what
                else:
                    return "check", "itup"

        elif i % 2 == 0 and lst_user[i] in CC:
            #print("check givepos_comp")
            if len(dic) <= 10:
                retgive_comp,what = givepos_comp(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc, dic, dic_u, dic_c,
                                            store)  # calling the givepos_comp function that give positions in matrix
                if len(str(retgive_comp)) == 20 or len(str(retgive_comp)) == 21 or len(str(retgive_comp)) == 35:
                    #print("in here", retgive_comp, what)
                    return retgive_comp,what
                else:
                    return "check", "itup"

        else:
            return "check", "itup"

#Defining function which is being called from userwon or usercomp frnc used to return value of opposition of comp
def callfrmfunc(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc, dic, store):


    lst_loc_dash=["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    key_list = list(dic.keys())
    val_list = list(dic.values())
    ind = val_list.index(comp_chvalue)

    lst_user = []
    for i in dic.keys():
        lst_user.append(i)  # taking the keys of dic

    # when user enters the first value i.e won the toss (calling user_firstturn func)
    if str(key_list[ind]) != str(lst_user[0]):
        storeuser = []  # list of user keys
        storecomp = []  # list of comp keys
        for i in range(1, len(lst_user) + 1):  # sorting which key is of user or of comp nd storing them lists
            if i % 2 != 0:
                storeuser.append(lst_user[i - 1])
            elif i % 2 == 0:
                storecomp.append(lst_user[i - 1])

        for i in storeuser:
            del lst_loc_dash[lst_loc_dash.index(i)]
        for i in storecomp:
            del lst_loc_dash[lst_loc_dash.index(i)]

        value_an = userfirst_turn(oppo,dic, storeuser, storecomp,lst_loc_dash)
        return value_an

    # when comp enters the first value i.e won the toss (calling comp_firstturn func)
    elif str(key_list[ind]) == str(lst_user[0]):
        storeuser = []  # list of user keys
        storecomp = []  # list of comp keys

        for i in lst_user:
            if i=='':
                del lst_user[lst_user.index('')]
        else:
            pass

        for i in range(1, len(lst_user) + 1):  # sorting which key is of user or of comp nd storing them lists
            if i % 2 != 0:
                storecomp.append(lst_user[i - 1])
            elif i % 2 == 0:
                storeuser.append(lst_user[i - 1])

        for i in storeuser:
            if i=='':
                del storeuser[storeuser.index('')]
        else:
            pass

        for i in storeuser:
            del lst_loc_dash[lst_loc_dash.index(i)]
        for i in storecomp:
            del lst_loc_dash[lst_loc_dash.index(i)]

        value_an = compfirst_turn(oppo,dic, storeuser, storecomp,lst_loc_dash)
        return value_an





'''                                                                  # USER SECTION #                                                           '''
                                                    # IT INCLUDES ALL USER RELATED CALC. ND RESULTS #

# Defining function when the USER WON THE RPS GAME (called frm makingchoice func). RICHARD SPEAKING
#lst_loc = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
def userwon(lst_loc,oppo,user_chvalue,comp_chvalue,number,comp_chloc,user_chloc, len_ch,dic,CU,CC,n):

    if len(number)==1:
        number.append("1")
        lst_loc = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    elif len(number)%2!=0 and len(number)>1 :
        number.append("1")
        lst_loc=["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

    # print(dic)
    # TAKING THE LOCATION VALUES OF USER AND COMPUTER IN MATRIX
    hello_else1=""
    while True:
        print()
        print("Enter your", n,"location in matrix: ", end="")  # USER TAKING LOCATION IN MATRIX
        if n=="1st":
            l_1=("Enter your first location in matrix: ")
            richard(l_1)

        elif n=="2nd":
            l_1=("Enter your second location in matrix: ")
            richard(l_1)

        elif n=="3rd":
            l_1=("Enter your third location in matrix: ")
            richard(l_1)

        elif n=="4th":
            l_1=("Enter your fourth location in matrix: ")
            richard(l_1)

        elif n=="5th":
            l_1=("Enter your fifth location in matrix: ")
            richard(l_1)




        user_chloc = str(input(""))
        dic[user_chloc] = user_chvalue
        del lst_loc[lst_loc.index(user_chloc)]

        print("Wait! "+oppo+" is selecting its location ",end="")
        l_2=("Wait! "+oppo+" is selecting its location.")
        richard(l_2)
        for i in range(3):
            time.sleep(0.25)
            print(".",end="")
        print()


        dic_u = {}
        dic_c = {}
        dict_u = {(user_chloc): user_chvalue}  # UPDATING THE DICTIONARY FOR POSITIONS
        dic.update(dict_u)

        if comp_chloc in lst_loc:  # COMPUTER TAKING LOCATION IN MATRIX
            del lst_loc[lst_loc.index(comp_chloc)]
            #print("remiained list is",lst_loc)
            if len(len_ch) >= 1:
                hello = callfrmfunc(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,dic,store="")  # directing to callfrmfunc function in order to oppose the user or win the game
                comp_chloc = str(hello)         # giving diff names for ease
                dic_c = {(comp_chloc): comp_chvalue}
                dic.update(dic_c)

                len_ch.append("1")
                break

            else:
                hello = callfrmfunc(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,dic,store="")  # directing to callfrmfunc function in order to oppose the user or win the game

                hello_else1 = str(random.choice(lst_loc))
                comp_chloc = str(hello_else1)  # giving diff names for ease
                dict_c = {(comp_chloc): comp_chvalue}
                dic.update(dict_c)

                len_ch.append("1")
                break


        elif comp_chloc not in lst_loc:

            if len(len_ch)==0:
                hello_else1 = str(random.choice(lst_loc))
                comp_chloc = str(hello_else1)  # giving diff names for ease
                dict_c = {str(comp_chloc): comp_chvalue}
                dic.update(dict_c)

                len_ch.append("1")
                #len_ch.append("1") why two ?
                break

            elif len(dic)>=1:
                hello_else1 = callfrmfunc(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,dic,store="")  # directing to callfrmfunc function in order to oppose the user or win the game
                comp_chloc = str(hello_else1)  # giving diff names for ease
                dict_c = {comp_chloc: comp_chvalue}
                dic.update(dict_c)

                len_ch.append("1")
                #len_ch.append("1") why two ?
                break



    print("You chose:", user_chloc)
    print(oppo+" chose:", comp_chloc)
    print()

    print("Current game position: ")
    l_3=("Current game position: ")
    richard((l_3))
    print()

    CU.append(user_chloc) #collectuser
    CC.append(comp_chloc) #collectcomp
    #print(CU)
    #print(CC)

    reting,what=ingame_matrix_check(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc, dic, dic_u, dic_c,CU,CC,store="")  # CALLING THE ingame_matrix FUNCTION
    # Checking if the result condition is true
    if len(str(reting)) == 20 or len(str(reting)) == 21 or len(str(reting))==35:
        return None,reting,what,None,None,None,None
    else:
        #del lst_loc[lst_loc.index(comp_chloc)]
        return lst_loc,hello_else1,user_chloc, len_ch, dic,CU,CC

# Defining function in order to give the opposition value of comp (case of when the user won the toss)(called from callfrmfunc func).
def userfirst_turn(oppo,dic, storeuser, storecomp,lst_loc):

    # return "CHECK USERFIRST"
    # Defining conditions when the comp. will oppose
    inrow_a = [["a1", "a2", "a3"]]
    inrow_b = [["b1", "b2", "b3"]]
    inrow_c = [["c1", "c2", "c3"]]
    incol_1 = [["a1", "b1", "c1"]]
    incol_2 = [["a2", "b2", "c2"]]
    incol_3 = [["a3", "b3", "c3"]]
    diag_r = [["a1", "b2", "c3"]]
    diag_l = [["a3", "b2", "c1"]]

    to_oppose = inrow_a + inrow_b + inrow_c + incol_1 + incol_2 + incol_3 + diag_r + diag_l  # groupiing all condtions in one list

    # Defining "a" which will test who won the game by adding up by len of 1 if condition is true...
    # When the len of "a" reaches 2 i.e.( the len of elements inside ith element of to_oppose list), it tells which value to oppose.

    # Defining function to check opposition...
    def check(storeuser, storecomp, storeuser_main, removelater,lst_loc):

        # if storeuser len is not 2
        if len(storeuser) != 2:
            for i in to_oppose:
                a = ""  # a is defined
                for j in range(len(i)):
                    if i[j] in storeuser:  # checking if cond. is true to add len of 1 in "a"
                        a += "Y"
                else:
                    pass

                if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                    for j in range(len(i)):
                        # return check 1
                        if i[j] not in storeuser_main and i[j] not in storecomp:
                            oppose_value = i[j]
                            return oppose_value
                    else:
                        for i in to_oppose:
                            a = ""  # a is defined
                            for j in range(len(i)):
                                if i[j] in storecomp:  # checking if cond. is true to add len of 1 in "a"
                                    a += "Y"
                            else:
                                pass


                            if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                for j in range(len(i)):
                                    # return check 2
                                    if i[j] not in storeuser_main and i[j] not in storecomp:
                                        oppose_value = i[j]
                                        return oppose_value

                        else:
                            oppose_value = random.choice(lst_loc)
                            return oppose_value

            else:  # if no one reaches len of 2.
                oppose_value = random.choice(lst_loc)
                return oppose_value


        # if storeuser len is 2

        elif len(storeuser) == 2:
            for i in to_oppose:
                a = ""  # a is defined
                for j in range(len(i)):
                    if i[j] in storeuser_main:  # checking if cond. is true to add len of 1 in "a"
                        a += "Y"
                else:
                    pass

                if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                    for j in range(len(i)):

                        # checking here another loop
                        if i[j] not in storeuser_main and i[j] not in storecomp:
                            #return 'check 3'
                            oppose_value = i[j]
                            return oppose_value

                        elif i[j] not in storeuser_main and i[j] in storecomp:

                            # DEFINIING LOOPS FUNCTION TO CHECK MORE POSSIBILITIES OF CANCELATION
                            def loops(storeuser, removelater,lst_loc):
                                for i in to_oppose:
                                    a = ""  # a is defined
                                    for j in range(len(i)):
                                        if i[j] in storeuser:  # checking if cond. is true to add len of 1 in "a"
                                            a += "Y"
                                    else:
                                        pass

                                    if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                        for j in range(len(i)):
                                            if i[j] not in storeuser and i[j] not in storecomp:
                                                #return "check4"
                                                oppose_value = i[j]
                                                return oppose_value
                                            else:
                                                pass
                                        else:
                                            pass
                                    else:
                                        pass

                                else:
                                    #return 'check 5'
                                    if len(removelater) > 1:
                                        #print("INSIDE FIRST CHOICE")
                                        removelater_ = list(removelater)
                                        del removelater_[tmax.index(tmax[1])]

                                        add = storeuser_main[-1]  # len(storeuser_main-1)]
                                        removelater_.append(add)  # SECOND TIME REMOVAL ()
                                        #print(removelater_)
                                        for i in to_oppose:
                                            a = ""  # a is defined
                                            for j in range(len(i)):
                                                if i[j] in removelater_:  # checking if cond. is true to add len of 1 in "a"
                                                    a += "Y"
                                            else:
                                                pass

                                            if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                                #return "check 6"
                                                for j in range(len(i)):
                                                    if i[j] not in storeuser_main and i[j] not in storecomp:
                                                            oppose_value = i[j]
                                                            return oppose_value

                                                    else:
                                                        pass
                                                else:
                                                    pass
                                            else:
                                                pass
                                        else:
                                            oppose_value = random.choice(lst_loc)
                                            return oppose_value

                                    elif len(removelater) == 1:
                                        #print("INSIDE SECOND CHOICE")
                                        removelater_ = list(removelater)
                                        add = storeuser_main[-1]  # len(storeuser_main-1)]
                                        removelater_.append(add)  # SECOND TIME REMOVAL ()

                                        del1 = removelater_
                                        del2 = removelater_
                                        #return removelater_ ,'check 7'

                                        # from here separately checking starts
                                        del del1[tmax.index(tmax[0])]
                                        add = "b2"  # len(storeuser_main-1)]
                                        del1.append(add)  # FIRST TIME REMOVAL ()

                                        for i in to_oppose:
                                            a = ""  # a is defined
                                            for j in range(len(i)):
                                                if i[j] in del1:  # checking if cond. is true to add len of 1 in "a"
                                                    a += "Y"
                                            else:
                                                pass

                                            if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                                #return 'check 8'
                                                for j in range(len(i)):
                                                    if i[j] not in del1 and i[j] not in storecomp:
                                                        oppose_value = i[j]
                                                        return oppose_value

                                                    else:
                                                        pass
                                                else:
                                                    pass
                                            else:
                                                pass

                                        else:
                                            #print("INSIDE FIRST CHOICE 2.0")
                                            del del2[tmax.index(tmax[0])]
                                            #return del2 ,'check 9'
                                            add = removelater[0]  # len(storeuser_main-1)]
                                            del2.append(add)  # SECOND TIME REMOVAL ()

                                            for i in to_oppose:
                                                a = ""  # a is defined
                                                for j in range(len(i)):
                                                    if i[j] in del2:  # checking if cond. is true to add len of 1 in "a"
                                                        a += "Y"
                                                else:
                                                    pass
                                                if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                                    #return 'check 10'
                                                    for j in range(len(i)):
                                                        if i[j] not in del1 and i[j] not in storecomp:
                                                            oppose_value = i[j]
                                                            return oppose_value

                                                        else:
                                                            pass
                                                    else:
                                                        pass
                                                else:
                                                    pass

                                            else:
                                                oppose_value = random.choice(lst_loc)
                                                return oppose_value

                                    else:
                                        #print("INSIDE THIRD CHOICE")
                                        oppose_value = random.choice(lst_loc)
                                        return oppose_value

                            # checking conditions when to call loops function
                            if len(storeuser) > 1:
                                #print("CHECK 11")
                                del storeuser[storeuser.index(storeuser[0])]
                                add = storeuser_main[-1]  # len(storeuser_main-1)]
                                storeuser.append(add)  # FIRST TIME REMOVAL (c2,a2)
                                loop_r = loops(storeuser, removelater,lst_loc)
                                return loop_r

                            elif len(storeuser) == 1:
                                #print("CHECK 12")
                                add = storeuser_main[-1]  # len(storeuser_main-1)]
                                storeuser.append(add)  # FIRST TIME REMOVAL (c2,a2)
                                loop_r = loops(storeuser, removelater,lst_loc)
                                return loop_r

                            else:
                                oppose_value = random.choice(lst_loc)
                                return oppose_value

                        '''else:
                            oppose_value = random.choice(lst_loc)
                            return oppose_value'''

                    else:
                        oppose_value = random.choice(lst_loc)
                        return oppose_value

                else:  # if no one reaches len of 2.
                    pass

            else:  # if no one reaches len of 2.
                oppose_value = random.choice(lst_loc)
                return oppose_value

        '''else:
            oppose_value = random.choice(lst_loc)
            return oppose_value'''

    # Defining function to check WINNING...
    def checkwin(storeuser, storecomp,lst_loc):

        #print("user",storeuser)
        #print("comp",storecomp)
        for i in to_oppose:
            # WHEN to win by the computer
            a = ""  # a is defined
            for j in range(len(i)):
                if i[j] in storecomp:  # checking if cond. is true to add len of 1 in "a"
                    a += "Y"
            else:
                pass

            if len(a) == 2:  # when the condition reaches len of 2 before that of user it printsvthat resp value in the line in order to win
                for j in range(len(i)):
                    if i[j] not in storeuser and i[j] not in storecomp:
                        win_value = i[j]
                        return win_value

                else:
                    return

        else:  # if no one reaches len of 2.
            return


    # CHECKING CONTIONS TO DECIDE WHICH FUNCTION TO CALL AT WHAT STOREUSER LENGTH

    # when len of storeuser is 2
    if len(storeuser) == 2:

        storeuser_main = []
        removelater = ()
        storeuser_main = storeuser
        r = check(storeuser, storecomp, storeuser_main, removelater,lst_loc)
        return r


    # when len of storeuser is 3
    elif len(storeuser) == 3:
        usersort_1 = []
        usersort_2 = []
        usersort_3 = []
        for i in storeuser:  # putting values together according to row number
            if i[1] == '1':
                usersort_1.append(i)
            elif i[1] == '2':
                usersort_2.append(i)
            elif i[1] == '3':
                usersort_3.append(i)
        else:
            pass

        tmax = []
        draw_lst = []
        if (len(usersort_1) > len(usersort_2)) and (len(usersort_1) > len(usersort_3)):  # checking whichrow elements r more entered by user
            tmax = usersort_1
            #print("CHECK 1 max", tmax)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = ()
                removelater = tuple(tmax)
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(usersort_2) > len(usersort_1)) and (len(usersort_2) > len(usersort_3)):
            tmax = usersort_2
            #print("CHECK 2 max", tmax)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = ()
                removelater = tuple(tmax)
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(usersort_3) > len(usersort_1)) and (len(usersort_3) > len(usersort_2)):
            tmax = usersort_3
            #print("CHECK 3 max", tmax)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = ()
                removelater = tuple(tmax)
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(usersort_1) == len(usersort_2)) and (len(usersort_1) == len(usersort_3)):
            #print("CHECK 4 max", storeuser)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = ()
                removelater = tuple(tmax)
                storeuser_main = storeuser
                r = check(storeuser, storecomp, storeuser_main, removelater,lst_loc)
                return r


    # when len of storeuser is 4
    elif len(storeuser) == 4:
        usersort_1 = []
        usersort_2 = []
        usersort_3 = []
        for i in storeuser:  # putting values together according to row number
            if i[1] == '1':
                usersort_1.append(i)
            elif i[1] == '2':
                usersort_2.append(i)
            elif i[1] == '3':
                usersort_3.append(i)
        else:
            pass

        if (len(usersort_1) > len(usersort_2)) and (len(usersort_1) > len(usersort_3)):  # checking whichrow elements r more entered by user
            tmax = usersort_1
            #print("check 1 max 2.0")

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = []
                removelater = tmax
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(usersort_2) > len(usersort_1)) and (len(usersort_2) > len(usersort_3)):
            tmax = usersort_2
            # print("check 2 max 2.0")

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = []
                removelater = tmax
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(usersort_3) > len(usersort_1)) and (len(usersort_3) > len(usersort_2)):
            tmax = usersort_3
            # print("check 3 max 2.0")

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = []
                removelater = tmax
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(usersort_1) == len(usersort_2)) and (len(usersort_1) == len(usersort_3)):
            compwin = checkwin(storeuser, storecomp, lst_loc)
            if compwin != None:
                return compwin
            else:
                draw_lst = storeuser
                oppose_value = random.choice(lst_loc)
                return oppose_value

        elif (len(usersort_1) == len(usersort_2)) or (len(usersort_2) == len(usersort_3)):
            compwin = checkwin(storeuser, storecomp, lst_loc)
            if compwin != None:
                return compwin
            else:
                draw_lst = storeuser
                print(lst_loc)
                oppose_value = random.choice(lst_loc)
                return oppose_value

    # when len of storeuser is 5
    elif len(storeuser) == 5:
        #print("check 1 max 3.0")
        compwin = checkwin(storeuser, storecomp, lst_loc)
        if compwin != None:
            return compwin
        else:
            if len(lst_loc)==0:
                return "None"
            else:
                r = random.choice(lst_loc)
                if r in storeuser or r in storecomp:
                    del lst_loc[lst_loc.index(r)]
                    r= random.choice(lst_loc)
                    #print("here", r)
                    return r
                else:
                    #print("here", r)
                    return r

# Defining function in order to fill the positions when user won the toss in matrix (called from ingamematrix_check func func).
def givepos_user(oppo,user_chloc, user_chvalue,comp_chloc,comp_chvalue,lst_loc,dic,dic_u,dic_c,store):
    row = 3
    col = 3
    lst = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    for i in range(row):
        i = lst[i]
        for j in range(1, col + 1):
            dic_u = {str(user_chloc): user_chvalue}  # UPDATING THE DICTIONARY FOR POSITIONS
            dic_c = {str(comp_chloc): comp_chvalue}
            dic.update(dic_u)
            dic.update(dic_c)
            a = list(dic.keys())  # list of keys of dic

            # checking if the value x or o is given in certain position and storing it in "store" so as it doesnt show initial position again
            for k in range(1, len(a) + 1):
                if k % 2 != 0 and a[k - 1] == (str(i) + str(j)):  # checking user's value if it is given in certain pos
                    if j == col:  # checking 3rd column
                        print("| ", dic[user_chloc], "|")
                    else:
                        print("| ", dic[user_chloc], end=" ")
                    store = (str(i) + str(j))
                elif k % 2 == 0 and a[k - 1] == (str(i) + str(j)):  # checking comp.'s value if it is given in certain pos
                    if j == col:  # checking 3rd column
                        print("| ", dic[comp_chloc], "|")
                    else:
                        print("| ", dic[comp_chloc], end=" ")
                    store = (str(i) + str(j))

            # Printing positions in matrix
            if j == col:  # checking if it is 3rd coloumn  or not
                if store != (str(i) + str(j)) and (user_chloc == (str(i) + str(j)) or comp_chloc == (str(i) + str(j))):  # printing x or 0 positions
                    if user_chloc == (str(i) + str(j)):
                        print("| ", dic[user_chloc], "|")
                    elif comp_chloc == (str(i) + str(j)):
                        print("| ", dic[comp_chloc], "|")
                elif store == (str(i) + str(j)):  # passing away
                    pass
                elif store != (str(i) + str(j)):  # printing remaining positions
                    print("|", str(i) + str(j), "|")

            else:  # if not the 3rd column
                if store != (str(i) + str(j)) and (user_chloc == (str(i) + str(j)) or comp_chloc == (str(i) + str(j))):  # printing x or 0 positions
                    if user_chloc == (str(i) + str(j)):
                        print("| ", dic[user_chloc], end=" ")
                    elif comp_chloc == (str(i) + str(j)):
                        print("| ", dic[comp_chloc], end=" ")
                elif store == (str(i) + str(j)):  # passing away
                    pass
                elif store != (str(i) + str(j)):  # printing remaining positions
                    print("|", str(i) + str(j), end=" ")

        print()

    #print("check dic when user",dic)
    # Checking from who enter first value in order to determine which result func to call

    lst_user = []
    for i in dic.keys():
        lst_user.append(i)  # taking the keys of dic

    key_list = list(dic.keys())
    val_list = list(dic.values())
    ind = val_list.index(comp_chvalue)

    if str(key_list[ind]) != str(lst_user[0]):
        #print("Check result_userwon_t")
        result,what = result_userwon_t(oppo,dic, user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,
                                  store='')  # giving diff names for ease to the result
        resultstr = str(result)
        if len(resultstr) == 20 or len(resultstr) == 21 or len(resultstr) == 35:
            return result,what
        else:
            return "check", "itup"


    elif str(key_list[ind]) == str(lst_user[0]):
        #print("Check result_compwon_t")
        result,what = result_compwon_t(oppo,dic, user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,
                                  store='')  # giving diff names for ease to the result
        resultstr = str(result)
        if len(resultstr) == 20 or len(resultstr) == 21 or len(resultstr) == 35:
            return result,what
        else:
            return "check", "itup"

    #ALTERNATIVE METHOD
    '''storeuser = []  # list of user keys
    storecomp = []  # list of comp keys
    for i in lst_user:  # sorting which key is of user or of comp nd storing them lists
        if i[0] in user_chloc:
            result = result_userwon_t(dic, user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,store='')  # giving diff names for ease to the result
            resultstr = str(result)
            print(result)
            if len(resultstr) == 24 or len(str(resultstr)) == 35:
                return result
            else:
                pass
            print(dic)
        else:
            result = result_compwon_t(dic, user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,store='')  # giving diff names for ease to the result
            resultstr = str(result)
            print(result)
            if len(resultstr) == 24 or len(str(resultstr)) == 35:
                return result
            else:
                pass
            print(dic)'''

run=["r"]
# Defining function in order to give the final results of game (case of when the user won the toss)(called from givepos_user func).
def result_userwon_t(oppo,dic,user_chloc, user_chvalue,comp_chloc,comp_chvalue,lst_loc,store):#dictionary from givepos function


    def initial_run(oppo,dic):

        #Defining conditions when the user or the computer will win
        inrow = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"]]
        incol = [["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"]]
        diagnol = [["a1", "b2", "c3"], ["a3", "b2", "c1"]]

        to_win = inrow + incol + diagnol         #groupiing all condtions in one list
        lst_user=[]
        for i in dic.keys():
            lst_user.append(i)                    #taking the keys of dic

        storeuser=[] #list of user keys
        storecomp=[] #list of comp keys
        for i in range(1,len(lst_user)+1):         #sorting which key is of user or of comp nd storing them lists
            if i%2!=0:
                storeuser.append(lst_user[i-1])
            elif i%2==0:
                storecomp.append(lst_user[i-1])

        # DRAW BETWEEN USER AND COMPUTER
        if len(dic) == 10:
            print("BRUHH...IT TURNS OUT TO BE A DRAW!".center(180))
            draw = ("Bruh.....it TURNS OUT TO BE A DRAW!")  # 35
            zira(draw)
            d = ["5"]
            return draw, d

        # Defining "a" which will test who won the game by adding up by len of 1 if condition is true...
        # When the len of "a" reaches 3 i.e.( the len of elements inside ith element of to_win list), it tells whther match is won or not.

        for i in to_win:
            # WHEN USER IS WON
            a = ""  # a is defined
            for j in range(len(i)):
                if i[j] in storeuser:  # checking if cond. is true to add len of 1 in "a"
                    a += "Y"
            else:
                pass
            if len(a) == 3:  # when the condition reaches len of 3 before that of comp. it prints user wins
                print("YOU WON! ".center(180))
                print("".center(84) + oppo + " LOOSE!")
                won = ("YOU WON! "+oppo+" LOOSE!") # 20 or 21
                zira(won)
                w=["1","2","3"]
                return won,w


            # WHEN COMP IS WON
            a = ""  # a is defined
            for j in range(len(i)):
                if i[j] in storecomp:  # checking if cond. is true to add len of 1 in "a"
                    a += "Y"
            else:
                pass
            if len(a) == 3:  # when the condition reaches len of 3 before that of user it prints comp wins
                print("".center(84) + oppo + " WON!")
                print("YOU LOOSE! ".center(180))
                loose = (oppo+" WON, YOU LOOSE!")  # 20 or 21
                zira(loose)
                l=["9","8"]
                return loose,l

        else:  # if no one reaches len of 3 it prints draw
            return "check","itup"

    #calling the defined function the return the main value
    val,what=initial_run(oppo,dic)
    return val,what





'''                                                                   # OPPONENT SECTION #                                                        '''
                                                    # IT INCLUDES ALL OPPONENT RELATED CALC. ND RESULTS #

# Defining function when the COMPUTER WON THE RPS GAME (called frm makingchoice func).  RICHARD SPEAKING
#lst_loc = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
def compwon(lst_loc,oppo,comp_chvalue,user_chvalue,number, comp_chloc, user_chloc, len_ch,dic,CU,CC,n):

    if len(number)==1:
        number.append("1")
        lst_loc = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    elif len(number) % 2 != 0 and len(number) > 1:
        number.append("1")
        lst_loc=["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

    # print(dic)
    # TAKING THE LOCATION VALUES OF USER AND COMPUTER IN MATRIX
    hello_else1 = ""
    while True:

        print()
        print("Wait! "+oppo+" is selecting its location ", end="")
        l_1=("Wait! "+oppo+" is selecting its location.")
        richard(l_1)
        for i in range(3):
            time.sleep(0.25)
            print(".", end="")
        print()

        dic_u = {}
        dic_c = {}
        if comp_chloc in lst_loc:  # COMPUTER TAKING LOCATION IN MATRIX
            del lst_loc[lst_loc.index(comp_chloc)]
            #print("remiained list is", lst_loc)

            if len(len_ch) >= 2:
                hello = callfrmfunc(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc, dic,store="")  # directing to callfrmfunc function in order to oppose the user or win the game
                comp_chloc = str(hello)  # giving diff names for ease
                dic_c = {(comp_chloc): comp_chvalue}
                dic.update(dic_c)

                print(oppo+" chose: ",comp_chloc)

                len_ch.append("1")
                break

            else:
                hello = callfrmfunc(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc, dic,store="")  # directing to callfrmfunc function in order to oppose the user or win the game

                hello_else1 = str(random.choice(lst_loc))
                comp_chloc = str(hello_else1)  # giving diff names for ease
                dict_c = {(comp_chloc): comp_chvalue}
                dic.update(dict_c)

                print(oppo+" chose: ", comp_chloc)

                len_ch.append("1")
                break


        elif comp_chloc not in lst_loc:

            if len(len_ch) in [0,1]:
                hello_else1 = str(random.choice(lst_loc))
                comp_chloc = str(hello_else1)  # giving diff names for ease
                dict_c = {str(comp_chloc): comp_chvalue}
                dic.update(dict_c)

                print(oppo+" chose: ", comp_chloc)

                len_ch.append("1")
                break

            elif len(dic) >= 2:
                hello_else1 = callfrmfunc(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc, dic,store="")  # directing to comp_oppose function in order to oppose the user or win the game
                comp_chloc = str(hello_else1)  # giving diff names for ease
                dict_c = {comp_chloc: comp_chvalue}
                dic.update(dict_c)

                print(oppo+" chose: ", comp_chloc)

                len_ch.append("1")
                # len_ch.append("1") why two ?
                break


    print()
    print("Current game position: ")
    l_2=("Current game position: ")
    richard(l_2)
    print()

    CC.append(comp_chloc)  # collectcomp
    #print(CU)
    #print(CC)

    reting,what = ingame_matrix_check(oppo,user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc, dic, dic_u, dic_c, CU, CC,store="")

    # Checking if the result condition is true
    if len(str(reting)) == 20 or len(str(reting)) == 21 or len(str(reting)) == 35:
        return None,reting,what,None,None,None,None

    else:
        print()
        print("Enter your", n, "location in matrix: ", end="")  # USER TAKING LOCATION IN MATRIX
        if n == "1st":
            l_1 = ("Enter your first location in matrix: ")
            richard(l_1)

        elif n == "2nd":
            l_1 = ("Enter your second location in matrix: ")
            richard(l_1)

        elif n == "3rd":
            l_1 = ("Enter your third location in matrix: ")
            richard(l_1)

        elif n == "4th":
            l_1 = ("Enter your fourth location in matrix: ")
            richard(l_1)

        elif n == "5th":
            l_1 = ("Enter your fifth location in matrix: ")
            richard(l_1)

        user_chloc = str(input(""))
        dic[user_chloc] = user_chvalue
        dict_u = {(user_chloc): user_chvalue}  # UPDATING THE DICTIONARY FOR POSITIONS
        dic.update(dict_u)
        del lst_loc[lst_loc.index(user_chloc)]

        print("You chose: ", user_chloc)
        CU.append(user_chloc)  # collectuser

        return lst_loc,hello_else1,user_chloc, len_ch, dic,CU,CC

# Defining function in order to give the opposition value of comp (case of when the comp won the toss)(called from callfrmfunc func).
def compfirst_turn(oppo,dic, storeuser, storecomp,lst_loc):

    #return COMPFIRST
    # Defining conditions when the comp. will oppose
    inrow_a = [["a1", "a2", "a3"]]
    inrow_b = [["b1", "b2", "b3"]]
    inrow_c = [["c1", "c2", "c3"]]
    incol_1 = [["a1", "b1", "c1"]]
    incol_2 = [["a2", "b2", "c2"]]
    incol_3 = [["a3", "b3", "c3"]]
    diag_r = [["a1", "b2", "c3"]]
    diag_l = [["a3", "b2", "c1"]]

    to_oppose = inrow_a + inrow_b + inrow_c + incol_1 + incol_2 + incol_3 + diag_r + diag_l  # groupiing all condtions in one list

    # Defining "a" which will test who won the game by adding up by len of 1 if condition is true...
    # When the len of "a" reaches 3 i.e.( the len of elements inside ith element of to_win list), it tells whther match is won or not.

    # Defining function to check opposition (addition of winning later)...
    def check(storeuser, storecomp, storeuser_main, removelater,lst_loc):

        # if comp len is not 2
        if len(storecomp) != 2:
            #print("inside fisrt")
            for i in to_oppose:
                # WHEN to oppose the user
                a = ""  # a is defined
                for j in range(len(i)):
                    if i[j] in storeuser:  # checking if cond. is true to add len of 1 in "a"
                        a += "Y"
                else:
                    pass

                if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                    for j in range(len(i)):
                        # return CHECK 1
                        if i[j] not in storeuser_main and i[j] not in storecomp:
                            oppose_value = i[j]
                            return oppose_value
                    else:
                        for i in to_oppose:
                            a = ""  # a is defined
                            for j in range(len(i)):
                                if i[j] in storecomp:  # checking if cond. is true to add len of 1 in "a"
                                    a += "Y"
                            else:
                                pass

                            if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                for j in range(len(i)):
                                    #print ("CHECK 2")
                                    if i[j] not in storeuser_main and i[j] not in storecomp:
                                        oppose_value = i[j]
                                        return oppose_value

                                else:
                                    pass
                        else:
                            oppose_value = random.choice(lst_loc)
                            return oppose_value

            else:  # if no one reaches len of 2.
                oppose_value = random.choice(lst_loc)
                return oppose_value


        # if comp len is 2
        elif len(storecomp) == 2:
            #print("inside when is 2")

            for i in to_oppose:
                # WHEN to oppose the user
                a = ""  # a is defined
                for j in range(len(i)):
                    if i[j] in storeuser_main:  # checking if cond. is true to add len of 1 in "a"
                        a += "Y"
                else:
                    pass
                if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                    for j in range(len(i)):

                        # checking here another loop
                        if i[j] not in storeuser_main and i[j] not in storecomp:
                            #return "CHECK 3"
                            oppose_value = i[j]
                            return oppose_value

                        elif i[j] not in storeuser_main and i[j] in storecomp:

                            # DEFINIING LOOPS FUNCTION TO CHECK MORE POSSIBILITIES OF CANCELATION
                            def loops(storeuser, removelater,lst_loc):
                                for i in to_oppose:
                                    # WHEN to oppose the user
                                    a = ""  # a is defined
                                    for j in range(len(i)):
                                        if i[j] in storeuser:  # checking if cond. is true to add len of 1 in "a"
                                            a += "Y"
                                    else:
                                        pass

                                    if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                        #return "CHECK 4"
                                        for j in range(len(i)):
                                            if i[j] not in storeuser and i[j] not in storecomp:
                                                oppose_value = i[j]
                                                return oppose_value
                                            else:
                                                pass
                                        else:
                                            pass
                                    else:
                                        oppose_value = random.choice(lst_loc)
                                        return oppose_value

                                else:
                                    #return "CHECK 5"
                                    if len(removelater) > 1:
                                        removelater_ = list(removelater)
                                        del removelater_[tmax.index(tmax[1])]

                                        add = storeuser_main[-1]  # len(storeuser_main-1)]
                                        removelater_.append(add)  # SECOND TIME REMOVAL ()

                                        for i in to_oppose:
                                            a = ""  # a is defined
                                            for j in range(len(i)):
                                                if i[j] in storeuser:  # checking if cond. is true to add len of 1 in "a"
                                                    a += "Y"
                                            else:
                                                pass

                                            if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                                #return "CHECK 6"
                                                for j in range(len(i)):
                                                    if i[j] not in storeuser_main and i[j] not in storecomp:
                                                        oppose_value = i[j]
                                                        return oppose_value
                                                    else:
                                                        pass
                                                else:
                                                    pass
                                            else:
                                                pass
                                        else:
                                            oppose_value = random.choice(lst_loc)
                                            return oppose_value


                                    elif len(removelater) == 1:
                                        removelater_ = list(removelater)
                                        add = storeuser_main[-1]  # len(storeuser_main-1)]
                                        removelater_.append(add)  # SECOND TIME REMOVAL ()

                                        del1 = removelater_
                                        del2 = removelater_
                                        #return removelater_,233

                                        # from here separately checking starts
                                        del del1[tmax.index(tmax[0])]
                                        add = "b2"  # len(storeuser_main-1)]
                                        del1.append(add)  # FIRST TIME REMOVAL ()

                                        for i in to_oppose:
                                            a = ""  # a is defined
                                            for j in range(len(i)):
                                                if i[j] in del1:  # checking if cond. is true to add len of 1 in "a"
                                                    a += "Y"
                                            else:
                                                pass

                                            if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                                #return "CHECK 8"
                                                for j in range(len(i)):
                                                    if i[j] not in del1 and i[j] not in storecomp:
                                                        oppose_value = i[j]
                                                        return oppose_value

                                                    else:
                                                        pass
                                                else:
                                                    pass
                                            else:
                                                pass


                                        else:
                                            del del2[tmax.index(tmax[0])]
                                            #return del2, 54
                                            add = removelater[0]  # len(storeuser_main-1)]

                                            for i in to_oppose:
                                                # WHEN to oppose the user
                                                a = ""  # a is defined
                                                for j in range(len(i)):
                                                    if i[j] in del2:  # checking if cond. is true to add len of 1 in "a"
                                                        a += "Y"
                                                else:
                                                    pass

                                                if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                                                    #return "CHECK 10"
                                                    for j in range(len(i)):
                                                        if i[j] not in del1 and i[j] not in storecomp:
                                                            oppose_value = i[j]
                                                            return oppose_value

                                                        else:
                                                            pass
                                                    else:
                                                        pass
                                                else:
                                                    pass

                                            else:
                                                oppose_value = random.choice(lst_loc)
                                                return oppose_value


                                    else:
                                        oppose_value = random.choice(lst_loc)
                                        return oppose_value

                            # checking conditions when to call loops function
                            if len(storeuser) > 1:
                                del storeuser[storeuser.index(storeuser[0])]
                                add = storeuser_main[-1]  # len(storeuser_main-1)]
                                storeuser.append(add)  # FIRST TIME REMOVAL (c2,a2)
                                loop_r = loops(storeuser, removelater,lst_loc)
                                return loop_r

                            elif len(storeuser) == 1:
                                add = storeuser_main[-1]  # len(storeuser_main-1)]
                                storeuser.append(add)  # FIRST TIME REMOVAL (c2,a2)
                                loop_r = loops(storeuser, removelater,lst_loc)
                                return loop_r

                            else:
                                oppose_value = random.choice(lst_loc)
                                return oppose_value

                        '''else:
                            oppose_value = random.choice(lst_loc)
                            return oppose_value'''

                    else:
                        oppose_value = random.choice(lst_loc)
                        return oppose_value

                else:  # if no one reaches len of 2.
                    pass

            else:  # if no one reaches len of 2.
                oppose_value = random.choice(lst_loc)
                return oppose_value

        '''else:
            oppose_value = random.choice(lst_loc)
            return oppose_value'''

    # Defining function to check WINNING...
    def checkwin(storeuser, storecomp,lst_loc):
        #print("check win")
        #print(storecomp)

        for i in to_oppose:
            # WHEN to win by the computer
            a = ""  # a is defined
            for j in range(len(i)):
                if i[j] in storecomp:  # checking if cond. is true to add len of 1 in "a"
                    a += "Y"
            else:
                pass

            if len(a) == 2:  # when the condition reaches len of 2 before that of user it printsvthat resp value in the line in order to win
                for j in range(len(i)):
                    if i[j] not in storeuser and i[j] not in storecomp:
                        win_value = i[j]
                        return win_value

                else:
                    return

        else:  # if no one reaches len of 2.
            return


    # print(lst_loc)
    # CHECKING CONTIONS TO DECIDE WHICH FUNCTION TO CALL AT WHAT STOREUSER LENGTH

    # when len of storecomp is 2
    if len(storecomp) == 2:
        storeuser_main = []
        removelater = ()
        storeuser_main = storeuser
        r = check(storeuser, storecomp, storeuser_main, removelater,lst_loc)
        return r

    # when len of storecomp is 3
    elif len(storecomp) == 3:
        compsort_1 = []
        compsort_2 = []
        compsort_3 = []
        for i in storecomp:  # putting values together according to row number
            if i[1] == '1':
                compsort_1.append(i)
            elif i[1] == '2':
                compsort_2.append(i)
            elif i[1] == '3':
                compsort_3.append(i)
        else:
            pass

        tmax = []
        draw_lst = []
        if (len(compsort_1) > len(compsort_2)) and (len(compsort_1) > len(compsort_3)):  # checking whichrow elements r more entered by user
            tmax = compsort_1
            #print("CHECK 1 max", tmax)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = ()
                removelater = tuple(tmax)
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(compsort_2) > len(compsort_1)) and (len(compsort_2) > len(compsort_3)):
            tmax = compsort_2
            #print("CHECK 2 max", tmax)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = ()
                removelater = tuple(tmax)
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(compsort_3) > len(compsort_1)) and (len(compsort_3) > len(compsort_2)):
            tmax = compsort_3
            #print("CHECK 3 max", tmax)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = ()
                removelater = tuple(tmax)
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(compsort_1) == len(compsort_2)) and (len(compsort_1) == len(compsort_3)):
            #print("CHECK 4 max", tmax)
            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = ()
                removelater = tuple(tmax)
                storeuser_main = storeuser
                r = check(storeuser, storecomp, storeuser_main, removelater,lst_loc)
                return r

    # when len of storecomp is 4
    elif len(storecomp) == 4:

        compsort_1 = []
        compsort_2 = []
        compsort_3 = []
        for i in storecomp:  # putting values together according to row number
            if i[1] == '1':
                compsort_1.append(i)
            elif i[1] == '2':
                compsort_2.append(i)
            elif i[1] == '3':
                compsort_3.append(i)
        else:
            pass

        tmax = []
        draw_lst = []
        if (len(compsort_1) > len(compsort_2)) and (len(compsort_1) > len(compsort_3)):  # checking whichrow elements r more entered by user
            tmax = compsort_1
            #print("CHECK 5 max 2.0", tmax)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = []
                removelater = tmax
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(compsort_2) > len(compsort_1)) and (len(compsort_2) > len(compsort_3)):
            tmax = compsort_2
            #print("CHECK 6 max2.0", tmax)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = []
                removelater = tmax
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(compsort_3) > len(compsort_1)) and (len(compsort_3) > len(compsort_2)):
            tmax = compsort_3
            #print("CHECK 7 max2.0", tmax)

            compwin = checkwin(storeuser, storecomp,lst_loc)
            if compwin != None:
                return compwin
            else:
                storeuser_main = []
                removelater = []
                removelater = tmax
                storeuser_main = storeuser
                r = check(tmax, storecomp, storeuser_main, removelater,lst_loc)
                return r

        elif (len(compsort_1) == len(compsort_2)) and (len(compsort_1) == len(compsort_3)):
            compwin = checkwin(storeuser, storecomp, lst_loc)
            if compwin != None:
                return compwin
            else:
                #print("CHECK 8 max2.0", tmax)
                draw_lst = storecomp
                oppose_value = random.choice(lst_loc)
                return oppose_value

        elif (len(compsort_1) == len(compsort_2)) or (len(compsort_2) == len(compsort_3)):
            compwin = checkwin(storeuser, storecomp, lst_loc)
            if compwin != None:
                return compwin
            else:
                draw_lst = storeuser
                #print("check 5 max 2.0")
                oppose_value = random.choice(lst_loc)
                return oppose_value

    # when len of storecomp is 5
    elif len(storecomp) == 5:
        compwin = checkwin(storeuser, storecomp, lst_loc)
        if compwin != None:
            return compwin
        else:
            #print("CHECK 9 max 3.0")
            if len(lst_loc)==0:
                return "None"
            else:
                r = random.choice(lst_loc)
                if r in storeuser or r in storecomp:
                    del lst_loc[lst_loc.index(r)]
                    r= random.choice(lst_loc)
                    #print("here", r)
                    return r
                else:
                    #print("here", r)
                    return r

# Defining function in order to fill the positions when comp won the toss in matrix (called from ingamematrix_check func func).
def givepos_comp(oppo,user_chloc, user_chvalue,comp_chloc,comp_chvalue,lst_loc,dic,dic_u,dic_c,store):

    row = 3
    col = 3
    lst = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
    for i in range(row):
        i = lst[i]
        for j in range(1, col + 1):
            dic_u = {str(user_chloc): user_chvalue}  # UPDATING THE DICTIONARY FOR POSITIONS
            dic_c = {str(comp_chloc): comp_chvalue}
            dic.update(dic_u)
            dic.update(dic_c)

            a = list(dic.keys())  # list of keys of dic
            #print("before ",a)
            if '' in a:
                del a[(a.index(''))]
            #print(("after",a))

            # checking if the value x or o is given in certain position and storing it in "store" so as it doesnt show initial position again

            for k in range(1, len(a) + 1):
                if k % 2 != 0 and a[k - 1] == (str(i) + str(j)):  # checking user's value if it is given in certain pos
                    if j == col:  # checking 3rd column
                        print("| ", dic[comp_chloc], "|")
                    else:
                        print("| ", dic[comp_chloc], end=" ")
                    store = (str(i) + str(j))
                elif k % 2 == 0 and a[k - 1] == (
                        str(i) + str(j)):  # checking comp.'s value if it is given in certain pos
                    if j == col:  # checking 3rd column
                        print("| ", dic[user_chloc], "|")
                    else:
                        print("| ", dic[user_chloc], end=" ")
                    store = (str(i) + str(j))

            # Printing positions in matrix
            if j == col:  # checking if it is 3rd coloumn  or not
                if store != (str(i) + str(j)) and (user_chloc == (str(i) + str(j)) or comp_chloc == (
                        str(i) + str(j))):  # printing x or 0 positions
                    if user_chloc == (str(i) + str(j)):
                        print("| ", dic[comp_chloc], "|")
                    elif comp_chloc == (str(i) + str(j)):
                        print("| ", dic[user_chloc], "|")
                elif store == (str(i) + str(j)):  # passing away
                    pass
                elif store != (str(i) + str(j)):  # printing remaining positions
                    print("|", str(i) + str(j), "|")

            else:  # if not the 3rd column
                if store != (str(i) + str(j)) and (user_chloc == (str(i) + str(j)) or comp_chloc == (
                        str(i) + str(j))):  # printing x or 0 positions
                    if user_chloc == (str(i) + str(j)):
                        print("| ", dic[comp_chloc], end=" ")
                    elif comp_chloc == (str(i) + str(j)):
                        print("| ", dic[user_chloc], end=" ")
                elif store == (str(i) + str(j)):  # passing away
                    pass
                elif store != (str(i) + str(j)):  # printing remaining positions
                    print("|", str(i) + str(j), end=" ")

        print()

    #print("check dic when comp",dic)
    # Checking from who enter first value in order to determine which result func to call

    lst_user = []
    for i in dic.keys():
        lst_user.append(i)  # taking the keys of dic

    key_list = list(dic.keys())
    val_list = list(dic.values())
    ind = val_list.index(comp_chvalue)

    if str(key_list[ind]) != str(lst_user[0]):
        # print("Check result_userwon_t")
        result,what = result_userwon_t(oppo, dic, user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,
                                  store='')  # giving diff names for ease to the result
        resultstr = str(result)
        if len(resultstr) == 20 or len(resultstr) == 21 or len(resultstr) == 35:
            return result,what
        else:
            return "check", "itup"


    elif str(key_list[ind]) == str(lst_user[0]):
        # print("Check result_compwon_t")
        result,what = result_compwon_t(oppo, dic, user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,
                                  store='')  # giving diff names for ease to the result
        resultstr = str(result)
        if len(resultstr) == 20 or len(resultstr) == 21 or len(resultstr) == 35:
            return result,what
        else:
            return "check", "itup"

    # ALTERNATIVE METHOD
    '''storeuser = []  # list of user keys
    storecomp = []  # list of comp keys
    for i in lst_user:  # sorting which key is of user or of comp nd storing them lists
        if i in user_chloc:
            result = result_userwon_t(dic, user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,store='')  # giving diff names for ease to the result
            resultstr = str(result)
            print(result)
            if len(resultstr) == 24 or len(resultstr) == 35:
                return result
            else:
                pass
            print(dic)
        else:
            result = result_compwon_t(dic, user_chloc, user_chvalue, comp_chloc, comp_chvalue, lst_loc,store='')  # giving diff names for ease to the result
            resultstr = str(result)
            print(result)
            if len(resultstr) == 24 or len(resultstr) == 35:
                return result
            else:
                pass
            print(dic)'''

# Defining function in order to give the final results of game (case of when the user won the toss)(called from givepos_comp func).
def result_compwon_t(oppo,dic,user_chloc, user_chvalue,comp_chloc,comp_chvalue,lst_loc,store):#dictionary from givepos function


    def initial_run(oppo,dic):
        #Defining conditions when the user or the computer will win
        inrow = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"]]
        incol = [["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"]]
        diagnol = [["a1", "b2", "c3"], ["a3", "b2", "c1"]]

        to_win = inrow + incol + diagnol         #groupiing all condtions in one list

        a = list(dic.keys())  # list of keys of dic
        # print("before ",a)
        if '' in a:
            del a[(a.index(''))]
        # print(("after",a))

        lst_user=[]
        for i in a:
            lst_user.append(i)                    #taking the keys of dic

        storeuser=[] #list of user keys
        storecomp=[] #list of comp keys
        for i in range(1,len(lst_user)+1):         #sorting which key is of user or of comp nd storing them lists
            if i%2!=0:
                storecomp.append(lst_user[i-1])
            elif i%2==0:
                storeuser.append(lst_user[i-1])

        if len(dic)==10:
            empty={}
            empty['last']='None'
            dic.update(empty)

        # DRAW BETWEEN USER AND COMPUTER
        if len(dic) == 11:
            print("BRUHH...IT TURNS OUT TO BE A DRAW!".center(180))
            draw = ("Bruh.....it TURNS OUT TO BE A DRAW!")  # 35
            zira(draw)
            d = ["5"]
            return draw, d
        # Defining "a" which will test who won the game by adding up by len of 1 if condition is true...
        # When the len of "a" reaches 3 i.e.( the len of elements inside ith element of to_win list), it tells whther match is won or not.

        for i in to_win:

            #WHEN USER IS WON
            a = ""  # a is defined
            for j in range(len(i)):
                if i[j] in storeuser:      # checking if cond. is true to add len of 1 in "a"
                    a += "Y"
            else:
                pass
            if len(a) == 3:                 # when the condition reaches len of 3 before that of user it prints comp wins
                print("YOU WON! ".center(180))
                print("".center(84) + oppo + " LOOSE!")
                won = ("YOU WON! " + oppo + " LOOSE!")  # 20 or 21
                zira(won)
                w=["1","2","3"]
                return won,w

            # WHEN COMPUTER IS WON
            a = ""  # a is defined
            for j in range(len(i)):
                if i[j] in storecomp:  # checking if cond. is true to add len of 1 in "a"
                    a += "Y"
            else:
                pass
            if len(a) == 3:  # when the condition reaches len of 3 before that of comp. it prints user wins
                print("".center(84) + oppo + " WON!")
                print("YOU LOOSE! ".center(180))
                loose = (oppo + " WON, YOU LOOSE!")  # 20 or 21
                zira(loose)
                l=["9","8"]
                return loose,l

        else:  # if no one reaches len of 3 it prints draw
            return "check", "itup"


    val, what = initial_run(oppo, dic)
    return val, what




'''                   ************** REPLAYING PART : WHERE REPLAY FUNCTION IS BEING CALLED WHICH THEN GO BACK TO STARTING ***********************                  '''

# Defining function to ask to replay or not (it is being called in the end in makingchoice function only).
def replay(lst_loc,name,number,oppo,what):
    #name="Prityanshu"
    print()

    if len(oppo)==4:

        if len(what)==3:
            print(oppo+": ",end="")
            print("Ok...next time i am gonna win the game.")
            l_1=("Ok...next time i am gonna win the game")
            mark(l_1)

        elif len(what)==2:
            print(oppo + ": ",end="")
            print("I told you...i am gonna win the game.")
            l_2 = ("I told you...i am gonna win the game.")
            mark(l_2)

        elif len(what)==1:
            print(oppo + ": ",end="")
            print("No worries...let's see in the next game.")
            l_3 = ("No worries...let's see in the next game.")
            mark(l_3)

    elif len(oppo)==5:

        if len(what) == 3:
            print(oppo + ": ",end="")
            print("Ok...next time i am gonna win the game.")
            l_1 = ("Ok...next time i am gonna win the game")
            linda(l_1)

        elif len(what) == 2:
            print(oppo + ": ",end="")
            print("I told you...i am gonna win the game.")
            l_2 = ("I told you...i am gonna win the game.")
            linda(l_2)

        elif len(what) == 1:
            print(oppo + ": ",end="")
            print("No worries...let's see in the next game.")
            l_3 = ("No worries...let's see in the next game.")
            linda(l_3)


    print()
    print("Wanna play again "+name+" ? (press y or n) ")
    l_1=("Wanna play again "+name+"?")
    richard(l_1)
    replay = input("=> ")
    if replay in ["Y", "y"]:
        print("Directing you to the NEW GAME", end=" ")
        l_2=("Directing you to the NEW GAME")
        richard(l_2)
        for i in range(4):
            time.sleep(0.75)
            print(".", end="")
        print()
        print("| WELCOME TO THE NEW GAME |".center(180))
        l_3=("WELCOME TO THE NEW GAME")
        zira(l_3)
        print()
        another_one(lst_loc,name,number) # has to also include toss first in this okkkkkkkkkkkkkkk

    elif replay in ["N", "n"]:
        print("".center(78)+"| THANKS FOR PLAYING "+name+" .|")
        bye = "THANKS FOR PLAYING " + name
        zira(bye)
        return bye

# Defining function which transfers value frm replay to opponent_ch function
def another_one(lst_loc,name,number):

    lst_loc=["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    number.append("1")
    opponent_ch(lst_loc,name,number)







# CALLING THE VERY FIRST WELCOME FUNCTION
welcome(lst_loc,number)





# CONTAINS TRASH
def useless():
    # lst_loc = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    '''def comp_oppose(dic):#dictionary from givepos function

        # Defining conditions when the comp. will oppose
        inrow_a = [["a1", "a2", "a3"]]
        inrow_b = [["b1", "b2", "b3"]]
        inrow_c = [["c1", "c2", "c3"]]
        incol_1 = [["a1", "b1", "c1"]]
        incol_2 = [["a2", "b2", "c2"]]
        incol_3 = [["a3", "b3", "c3"]]
        diag_r = [["a1", "b2", "c3"]]
        diag_l = [["a3", "b2", "c1"]]

        to_oppose = inrow_a + inrow_b + inrow_c + incol_1 + incol_2 + incol_3 + diag_r + diag_l  # groupiing all condtions in one list
        #dic = {'b2': 'x', 'a3': 'O', 'b3': 'x', 'b1': 'O', 'a1': 'x', "c3": "0", "c2": "x"}

        # Defining "a" which will test who won the game by adding up by len of 1 if condition is true...
        # When the len of "a" reaches 3 i.e.( the len of elements inside ith element of to_win list), it tells whther match is won or not.

        lst_user = []
        for i in dic.keys():
            lst_user.append(i)  # taking the keys of dic

        lst_loc_i = lst_loc
        print("thsis is list user",lst_user)

        storeuser = []  # list of user keys
        storecomp = []  # list of comp keys
        for i in range(1, len(lst_user) + 1):  # sorting which key is of user or of comp nd storing them lists
            if i % 2 != 0:
                storeuser.append(lst_user[i - 1])
            elif i % 2 == 0:
                storecomp.append(lst_user[i - 1])
        print("uuuuuuuuuuuuuuuuuu", storeuser)
        print("cccccccccccccccccc", storecomp)

        #print("userchlocccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",user_chloc)
        #print("compchlocccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc",comp_)
        if lst_user[0] in storeuser:
            retuser = userfirst_turn(storeuser, storecomp)
            return retuser

        else:
            retcomp = compfirst_turn(storeuser, storecomp)
            return retcom'''

    '''import random
    #Defining conditions when the comp. will oppose
    inrow_a = [["a1", "a2", "a3"]]
    inrow_b = [["b1", "b2", "b3"]]
    inrow_c = [["c1", "c2", "c3"]]
    incol_1 = [["a1", "b1", "c1"]]
    incol_2 = [["a2", "b2", "c2"]]
    incol_3 = [["a3", "b3", "c3"]]
    diag_r = [["a1","b2","c3"]]
    diag_l = [["a3", "b2", "c1"]]

    to_oppose = inrow_a + inrow_b + inrow_c + incol_1 + incol_2 + incol_3 + diag_r +diag_l         #groupiing all condtions in one list

    lst_user=[]
    for i in dic.keys():
        lst_user.append(i)                    #taking the keys of dic


    storeuser=[] #list of user keys
    storecomp=[] #list of comp keys
    for i in range(1,len(lst_user)+1):         #sorting which key is of user or of comp nd storing them lists
        if i%2!=0:
            storeuser.append(lst_user[i-1])
        elif i%2==0:
            storecomp.append(lst_user[i-1])

    print(dic)
    print(storeuser)
    # Defining "a" which will test who won the game by adding up by len of 1 if condition is true...
    # When the len of "a" reaches 3 i.e.( the len of elements inside ith element of to_win list), it tells whther match is won or not.

    for i in to_oppose:
        #WHEN to oppose the user
        a=""   # a is defined
        for j in range(len(i)):
            if i[j] in storeuser:    # checking if cond. is true to add len of 1 in "a"
                a+="Y"
        else:
            pass

        #print(a)
        if len(a)==2:                 # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
            for j in range(len(i)):
                del storeuser[storeuser.index[i[j]]]
                if i[j] not in storeuser:
                    if i[j] not in storecomp:
                        ''''''if i[j] in lst_loc:
                            oppose_value = i[j]
                            return oppose_value

                        else:
                            oppose_value = random.choice(lst_loc)
                            return oppose_value''''''


                        oppose_value=i[j]
                        return oppose_value
                    else:
                        if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                            for j in range(len(i)):
                                if i[j] not in storecomp:
                                    if i[j] not in lst_loc:
                                        oppose_value = i[j]
                                        return oppose_value

                                    else:
                                        oppose_value=random.choice(lst_loc)
                                        return oppose_value

        #WHEN to win by the computer
        a = ""  # a is defined
        for j in range(len(i)):
            if i[j] in storecomp:      # checking if cond. is true to add len of 1 in "a"
                a += "Y"
        else:
            pass

        #print(a)
        if len(a) == 2:                 # when the condition reaches len of 2 before that of user it printsvthat resp value in the line in order to win
            for j in range(len(i)):
                if i[j] not in storecomp:
                    if i[j] not in storeuser:
                        oppose_value=i[j]
                        return oppose_value

                    else:
                        if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                            for j in range(len(i)):
                                if i[j] not in storeuser:
                                    if i[j] not in lst_loc:
                                        win_value = i[j]
                                        return win_value

                                    else:
                                        win_value=random.choice(lst_loc)
                                        return win_value



    else:  # if no one reaches len of 3 it prints draw
        rand_value = random.choice(lst_loc)
        return rand_value'''

    '''print(to_oppose)
    print(storeuser)
    print(storecomp)'''

    '''elif len(storeuser) == 3:
            usersort_1 = []
            usersort_2 = []
            usersort_3 = []
            for i in storeuser:  # putting values together according to row number
                if i[1] == '1':
                    usersort_1.append(i)
                elif i[1] == '2':
                    usersort_2.append(i)
                elif i[1] == '3':
                    usersort_3.append(i)
            else:
                pass

            # print("max", tmax)
            print(usersort_1)
            print(usersort_2)
            print(usersort_3)

            tmax = []
            draw_lst = []
            if len(usersort_1) > (len(usersort_2) and len(usersort_1) > len(
                    usersort_3)):  # checking whichrow elements r more entered by user
                tmax = usersort_1
                print("max", tmax)
                compwin = checkwin(storeuser, storecomp)
                if compwin != None:
                    return compwin
                else:
                    storeuser_main = []
                    removelater = ()
                    removelater = tuple(tmax)
                    storeuser_main = storeuser
                    r= check(tmax, storecomp, storeuser_main, removelater)
                    return r

            elif len(usersort_2) > (len(usersort_1) and len(usersort_2) > len(usersort_3)):
                tmax = usersort_2
                print("max", tmax)
                compwin = checkwin(storeuser, storecomp)
                if compwin != None:
                    return compwin
                else:
                    storeuser_main = []
                    removelater = ()
                    removelater = tuple(tmax)
                    storeuser_main = storeuser
                    r= check(tmax, storecomp, storeuser_main, removelater)
                    return r

            elif len(usersort_3) > (len(usersort_1) and len(usersort_3) > len(usersort_2)):
                tmax = usersort_3
                print("max", tmax)
                compwin = checkwin(storeuser, storecomp)
                if compwin != None:
                    return compwin
                else:
                    storeuser_main = []
                    removelater = ()
                    removelater = tuple(tmax)
                    storeuser_main = storeuser
                    r= check(tmax, storecomp, storeuser_main, removelater)
                    return r

            elif len(usersort_1) == len(usersort_2) and len(usersort_1) == len(usersort_3):
                print("max", tmax)
                compwin = checkwin(storeuser, storecomp)
                if compwin != None:
                    return compwin
                else:
                    storeuser_main = []
                    removelater = ()
                    removelater = tuple(tmax)
                    storeuser_main = storeuser
                    r = check(storeuser, storecomp, storeuser_main, removelater)
                    return r





        # when len of storeuser is 4
        elif len(storeuser) == 4:
            print("4=>")
            print(storeuser)
            print(storecomp)
            compsort_1 = []
            compsort_2 = []
            compsort_3 = []
            for i in storecomp:  # putting values together according to row number
                if i[1] == '1':
                    compsort_1.append(i)
                elif i[1] == '2':
                    compsort_2.append(i)
                elif i[1] == '3':
                    compsort_3.append(i)
            else:
                pass

            tmax = []
            draw_lst = []
            if len(compsort_1) > len(compsort_2):  # checking whichrow elements r more entered by user
                tmax = compsort_1
                compwin = checkwin(storeuser, storecomp)
                if compwin != None:
                    return compwin
                else:
                    storeuser_main = []
                    removelater = []
                    removelater = tmax
                    storeuser_main = storeuser
                    r = check(tmax, storecomp, storeuser_main, removelater)
                    return r

            elif len(compsort_2) > len(compsort_1):
                tmax = compsort_2
                compwin = checkwin(storeuser, storecomp)
                if compwin != None:
                    return compwin
                else:
                    storeuser_main = []
                    removelater = []
                    removelater = tmax
                    storeuser_main = storeuser
                    r = check(tmax, storecomp, storeuser_main, removelater)
                    return r

            elif len(compsort_3) > (len(compsort_1) and len(compsort_2)):
                tmax = compsort_3
                compwin = checkwin(storeuser, storecomp)
                if compwin != None:
                    return compwin
                else:
                    storeuser_main = []
                    removelater = []
                    removelater = tmax
                    storeuser_main = storeuser
                    r = check(tmax, storecomp, storeuser_main, removelater)
                    return r

            elif len(compsort_1) == len(compsort_2) and len(compsort_1) == len(compsort_3):
                draw_lst = storecomp
                oppose_value = random.choice(lst_loc)
                return oppose_value

        # when len of storeuser is 5
        elif len(storeuser) == 5:
            return'''

    '''lst_loc = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    # Defining conditions when the comp. will oppose
    inrow_a = [["a1", "a2", "a3"]]
    inrow_b = [["b1", "b2", "b3"]]
    inrow_c = [["c1", "c2", "c3"]]
    incol_1 = [["a1", "b1", "c1"]]
    incol_2 = [["a2", "b2", "c2"]]
    incol_3 = [["a3", "b3", "c3"]]
    diag_r = [["a1", "b2", "c3"]]
    diag_l = [["a3", "b2", "c1"]]

    to_oppose = inrow_a + inrow_b + inrow_c + incol_1 + incol_2 + incol_3 + diag_r + diag_l  # groupiing all condtions in one list
    # example: dic = {'b2': 'X', 'b1': 'O', 'a2': 'X', 'c3':'O' , 'c1':'X','c2':'O', 'a3':'X'}#,'b3':'O','a3':'X' }

    lst_user = []
    for i in dic.keys():
        lst_user.append(i)  # taking the keys of dic

    print(lst_user)

    print("dic in compoppose: ",dic)
    storeuser = []  # list of user keys
    storecomp = []  # list of comp keys
    for i in range(1, len(lst_user) + 1):  # sorting which key is of user or of comp nd storing them lists
        if i % 2 != 0:
            storeuser.append(lst_user[i - 1])
        elif i % 2 == 0:
            storecomp.append(lst_user[i - 1])

    lst_loc_i=lst_loc

    print(storeuser)
    print(storecomp)

    for i in storeuser:  # deleting elements from main list which are already used
        del lst_loc_i[lst_loc_i.index(i)]
    else:
        for i in storecomp:
            del lst_loc_i[lst_loc_i.index(i)]

    print(lst_loc_i)
    print(dic)
    print("user is",storeuser)
    print("comp is", storecomp)


    # Defining "a" which will test who won the game by adding up by len of 1 if condition is true...
    # When the len of "a" reaches 3 i.e.( the len of elements inside ith element of to_win list), it tells whther match is won or not.

    # Defining function to check opposition (addition of winning later)...
    def check(storeuser, storecomp):

        # if comp len is not 2
        if len(storecomp) != 2:
            for i in to_oppose:
                # WHEN to oppose the user
                a = ""  # a is defined
                for j in range(len(i)):
                    if i[j] in storeuser:  # checking if cond. is true to add len of 1 in "a"
                        a += "Y"
                else:
                    pass

                print(a)
                if len(
                        a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                    for j in range(len(i)):
                        if i[j] not in storeuser and i[j] not in storecomp:
                            oppose_value = i[j]
                            # print("oppose",oppose_value)
                            return oppose_value
                    else:
                        oppose_value = random.choice(lst_loc_i)
                        # print("oppose", oppose_value)
                        return oppose_value

            else:  # if no one reaches len of 2.
                oppose_value = random.choice(lst_loc_i)
                return oppose_value


        # if comp len is 2
        elif len(storecomp) == 2:
            for i in to_oppose:
                # WHEN to oppose the user
                a = ""  # a is defined
                for j in range(len(i)):
                    if i[j] in storeuser:  # checking if cond. is true to add len of 1 in "a"
                        a += "Y"
                else:
                    pass

                print(a)
                if len(a) == 2:  # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                    for j in range(len(i)):
                        if i[j] not in storeuser and i[j] not in storecomp:
                            oppose_value = i[j]
                            print("oppose hello", oppose_value)
                            return oppose_value
                    else:
                        oppose_value = random.choice(lst_loc_i)
                        print("oppose yoooo", oppose_value)
                        # print("oppose", oppose_value)
                        return oppose_value

                ''''''else:  # if no one reaches len of 2.
                    oppose_value = random.choice(lst_loc)
                    return oppose_value''''''

                    # WHEN to win by the computer
                    a = ""  # a is defined
                    for j in range(len(i)):
                        if i[j] in storecomp:  # checking if cond. is true to add len of 1 in "a"
                            a += "Y"
                    else:
                        pass

                    print("yo", a)
                    if len(a) == 2:  # when the condition reaches len of 2 before that of user it printsvthat resp value in the line in order to win
                        for j in range(len(i)):
                            if i[j] not in storeuser and i[j] not in storecomp:
                                win_value = i[j]
                                print("oppose bruuhhhh", win_value)
                                # print("oppose",oppose_value)
                                return win_value
                        else:
                            oppose_value = random.choice(lst_loc_i)
                            print("oppose hellaaaa", oppose_value)
                            # print("oppose", oppose_value)
                            return oppose_value

                else:  # if no one reaches len of 2.
                    oppose_value = random.choice(lst_loc_i)
                    return oppose_value

        # Defining function to check WINNING...
        def checkwin(storecomp):
            print(storecomp)

            for i in to_oppose:
                # WHEN to win by the computer
                a = ""  # a is defined
                for j in range(len(i)):
                    if i[j] in storecomp:  # checking if cond. is true to add len of 1 in "a"
                        a += "Y"
                else:
                    pass

                print(a)
                if len(
                        a) == 2:  # when the condition reaches len of 2 before that of user it printsvthat resp value in the line in order to win
                    for j in range(len(i)):
                        if i[j] not in storeuser and i[j] not in storecomp:
                            win_value = i[j]
                            # print("oppose",oppose_value)
                            return win_value
                    else:
                        oppose_value = random.choice(lst_loc_i)
                        # print("oppose", oppose_value)
                        return oppose_value

            else:  # if no one reaches len of 2.
                oppose_value = random.choice(lst_loc_i)
                return oppose_value

        # when len of storeuser is 2
        if len(storeuser) == 2:
            print("yo")
            a = check(storeuser,storecomp)
            return a


        # when len of storeuser is 3
        elif len(storeuser) == 3:
            usersort_1 = []
            usersort_2 = []
            usersort_3 = []
            for i in storeuser:  # putting values together according to row number
                if i[1] == '1':
                    usersort_1.append(i)
                elif i[1] == '2':
                    usersort_2.append(i)
                elif i[1] == '3':
                    usersort_3.append(i)
            else:
                pass

            tmax = []
            draw_lst = []
            if len(usersort_1) > (len(usersort_2) and len(usersort_3)):  # checking whichrow elements r more entered by user
                tmax = usersort_1
                print("max", tmax)
                r = check(tmax, storecomp)
                return r
            elif len(usersort_2) > (len(usersort_1) and len(usersort_3)):
                tmax = usersort_2
                print("max", tmax)
                r = check(tmax, storecomp)
                return r
            elif len(usersort_3) > (len(usersort_1) and len(usersort_2)):
                tmax = usersort_3
                print("max", tmax)
                r = check(tmax, storecomp)
                return r
            elif len(usersort_1) == len(usersort_2) and len(usersort_1) == len(usersort_3):
                r = check(storeuser, storecomp)
                print("max", tmax)
                return r

            print("max", tmax)
            print(usersort_1)
            print(usersort_2)
            print(usersort_3)


        # when len of storeuser is 4
        elif len(storeuser) == 4:
            print("4=>")
            print(storeuser)
            print(storecomp)
            compsort_1 = []
            compsort_2 = []
            compsort_3 = []
            for i in storecomp:  # putting values together according to row number
                if i[1] == '1':
                    compsort_1.append(i)
                elif i[1] == '2':
                    compsort_2.append(i)
                elif i[1] == '3':
                    compsort_3.append(i)
            else:
                pass

            tmax = []
            draw_lst = []
            if len(compsort_1) > len(compsort_2):  # checking whichrow elements r more entered by user
                tmax = compsort_1
                r = checkwin(tmax)
                return r
            elif len(compsort_2) > len(compsort_1):
                tmax = compsort_2
                r = checkwin(tmax)
                return r
            elif len(compsort_3) > (len(compsort_1) and len(compsort_2)):
                tmax = compsort_3
                r = checkwin(tmax)
                return r
            elif len(compsort_1) == len(compsort_2) and len(compsort_1) == len(compsort_3):
                draw_lst = storecomp
                oppose_value = random.choice(lst_loc)
                return oppose_value

        # when len of storeuser is 5
        elif len(storeuser) == 5:
            return'''


    '''#Defining conditions when the comp. will oppose
        inrow_a = [["a1", "a2", "a3"]]
        inrow_b = [["b1", "b2", "b3"]]
        inrow_c = [["c1", "c2", "c3"]]
        incol_1 = [["a1", "b1", "c1"]]
        incol_2 = [["a2", "b2", "c2"]]
        incol_3 = [["a3", "b3", "c3"]]
        diag_r = [["a1","b2","c3"]]
        diag_l = [["a3", "b2", "c1"]]
    
        to_oppose = inrow_a + inrow_b + inrow_c + incol_1 + incol_2 + incol_3 + diag_r +diag_l         #groupiing all condtions in one list
    
        lst_user=[]
        for i in dic.keys():
            lst_user.append(i)                    #taking the keys of dic
    
    
        storeuser=[] #list of user keys
        storecomp=[] #list of comp keys
        for i in range(1,len(lst_user)+1):         #sorting which key is of user or of comp nd storing them lists
            if i%2!=0:
                storeuser.append(lst_user[i-1])
            elif i%2==0:
                storecomp.append(lst_user[i-1])
    
        print(dic)
        print(storeuser)
        # Defining "a" which will test who won the game by adding up by len of 1 if condition is true...
        # When the len of "a" reaches 3 i.e.( the len of elements inside ith element of to_win list), it tells whther match is won or not.
    
        for i in to_oppose:
            #WHEN to oppose the user
            a=""   # a is defined
            for j in range(len(i)):
                if i[j] in storeuser:    # checking if cond. is true to add len of 1 in "a"
                    a+="Y"
            else:
                pass
    
            #print(a)
            if len(a)==2:                 # when the condition reaches len of 2 before that of comp. it prints in that direction to oppose
                for j in range(len(i)):
                    if i[j] not in storeuser:
                        oppose_value=i[j]
                        return oppose_value
    
            #WHEN to win by the computer
            a = ""  # a is defined
            for j in range(len(i)):
                if i[j] in storecomp:      # checking if cond. is true to add len of 1 in "a"
                    a += "Y"
            else:
                pass
    
            #print(a)
            if len(a) == 2:                 # when the condition reaches len of 2 before that of user it printsvthat resp value in the line in order to win
                for j in range(len(i)):
                    if i[j] not in storecomp:
                        win_value=i[j]
                        return win_value
    
    
        else:  # if no one reaches len of 3 it prints draw
            pass
        print(to_oppose)
        print(storeuser)
        print(storecomp)'''










