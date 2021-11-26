#Screen Resolution = 1280 x 720
from os import kill
from tkinter import *
import random
from tkinter import ttk


window = Tk()
window.title("Watch Your Step")
window.geometry("1280x720")
width = 1200
height = 700
canvas = Canvas(window, bg="black", width=width, height=height)
safe = TRUE
cheat = FALSE

def begin():
    global error_tag
    global score_tag
    canvas.pack()
    canvas.create_line(100,350,1150,350, fill="white", width=2)
    error_tag= canvas.create_text(220, 10, fill = "white", font = "Times 12 bold", text="If the game does not begin after you press <p>, press <TAB> before pressing <p>")


def placeSignals():
    global red
    global green
    global red_light
    red = PhotoImage(file="red-light-2.png")# https://www.subpng.com/png-y62091/download.html
    red_light = canvas.create_image(width/2,150, image = red)


def greenSignals():
    global green
    global green_light
    my_label.config(text="Go on!")
    green = PhotoImage(file="green-light-2.png")# https://www.subpng.com/png-y62091/download.html
    green_light = canvas.create_image(width/2,150, image = green)


def label_stop():
    global red_light
    global w
    my_label.config(text="STOP!")
    w,v = canvas.coords(place3)
    placeSignals()


def red_kill():
    canvas.delete(red_light)


def label_go():
    my_label.config(text="Go on!")
    greenSignals()

def score_update():
    score = 0
    score = score + 1

my_label = Label(window,text="Press P to begin")

def kill_green():
    canvas.delete(green_light)

def delete_cheat_text():
    canvas.delete(cheat_act1)
    canvas.delete(cheat_act2)

def cKey(event):
    activate_cheat()
    global cheat_act1, cheat_act2
    cheat_act1 = canvas.create_text(width/2, height*(3/4)+120, fill = "white", font = "Times 18 bold", text="Cheat code activated, red traffic signal can not detect you")
    cheat_act2 = canvas.create_text(width/2, height*(3/4)+150, fill = "white", font = "Times 15 bold", text="Your score will not be recorded because you chose the easy way out")

def activate_cheat():
    global cheat
    cheat = TRUE

def reset():
    global loser, final_score, regame
    loser = canvas.create_text(width/2, height/3, fill = "white", font = "Times 30 bold", text="YOU LOST!")
    final_score = canvas.create_text(width/2, height/3 + 200, fill = "white", font = "Times 15 bold", text="Your score: "+str(score))
    regame = canvas.create_text(width/2, height/3+50, fill = "white", font = "Times 20 bold", text="Press <r> to Restart")

def rKey(event):
    my_label.after(2000,delete_restart_info)
    global label_r1, label_r2, label_r3
    label_r1 = canvas.create_text(width/2, height/4 + 340, fill = "white", font = "Times 18 bold", text=" -> Press <p> to Play")
    label_r2 = canvas.create_text(width/2, height/4 + 370, fill = "white", font = "Times 18 bold", text=" -> Press <i> to View Instructions")
    label_r3 = canvas.create_text(width/2, height/4 + 400, fill = "white", font = "Times 18 bold", text=" -> Press <e> to Exit")
    restart_game()
    delete_restart_info()

def current_pos():
    global place3
    global safe, loser, final_score, regame
    safe = TRUE
    a,c = canvas.coords(place3)
    if cheat == FALSE:
        if a > w:
            safe = FALSE
            red_kill()
            kill_green()
            reset()
            my_label.after(2000,kill_green)
            my_label.after(2000,red_kill)
            canvas.delete(place3)
    elif cheat == TRUE:
        my_label.config(text="Cheat code activated")
        my_label.after(3000,delete_cheat_text)


def begin_timer():
    global safe
    label_go()
    stopTime()

def begin_second():
    if safe == 1:
        second_round()
    else:
        my_label.after(1000,kill_green)

def second_round():
    #Second red light
    my_label.after((x+x+z)*1000,label_stop) # second red signal comes
    my_label.after((x+x+z+z)*1000,red_kill) # after x+x+z+z, red goes away
    my_label.after((x+x+z+z)*1000,label_go) # after red signal goes away, label is updated to go on
    my_label.after((x+x+z+2)*1000,current_pos) # if detection noticed on red, you lose
    my_label.after((x)*1000,begin_third)
    #End of second signal

def begin_third():
    if safe == 1:
        third_round()
    else:
        my_label.after(1000,kill_green)

def third_round():
    #Third red light
    my_label.after((x+x+z+z)*1000,label_stop) # third red signal comes
    my_label.after((x+x+z+z+y)*1000,red_kill) # after x+x+z+z, red goes away
    my_label.after((x+x+z+z+y)*1000,label_go) # after red signal goes away, label is updated to go on
    my_label.after((x+x+z+z+y+2)*1000,current_pos) # if detection noticed on red, you lose
    my_label.after((x)*1000,begin_fourth)
    #End of third signal

def begin_fourth():
    if safe == 1:
        fourth_round()
    else:
        my_label.after(1000,kill_green)

def fourth_round():
        #Fourth red light
    my_label.after((x+x+z+z+y)*1000,label_stop) # fourth red signal comes
    my_label.after((x+x+z+z+y+y)*1000,red_kill) # after x+x+z+z, red goes away
    my_label.after((x+x+z+z+y+y)*1000,label_go) # after red signal goes away, label is updated to go on
    my_label.after((x+x+z+z+y+y+3)*1000,current_pos) # if detection noticed on red, you lose
        #End of Fourth signal

def stopTime():
    global x,y,z, x1
    a,c = canvas.coords(place3)
    x = random.randint(3,4)
    y = random.randint(4,6)
    z = random.randint(2,3)
    x1 = random.randint(3,4)
    my_label.after(x*1000,label_stop) # first red signal comes
    my_label.after((x+x)*1000,red_kill) # for the same duration x + x, red signal goes away
    my_label.after((x+x)*1000,label_go) # after red signal goes away, label is updated to go on
    my_label.after((x+2)*1000,current_pos)#if detected motion on first red, you lose
    my_label.after((x)*1000,begin_second)

# Main Menu
label1 = canvas.create_text(width/2, height/4, fill = "white", font = "Times 30 bold", text="Watch your Step!")
label2 = canvas.create_text(width/2, height/4 + 250, fill = "white", font = "Times 18 bold", text=" -> Press <p> to Play")
label3 = canvas.create_text(width/2, height/4 + 280, fill = "white", font = "Times 18 bold", text=" -> Press <i> to View Instructions")
label4 = canvas.create_text(width/2, height/4 + 310, fill = "white", font = "Times 18 bold", text=" -> Press <e> to Exit")
label5 = canvas.create_text(width/2, height/4 + 500, fill = "white", font = "Times 15 bold", text="2021 © Copyright Ali Lakho (University of Manchester)")
# End of Main Menu

def welcome_text_delete():# Deletes menu texts once p is pressssed
    canvas.delete(label1)
    canvas.delete(label2)
    canvas.delete(label3)
    canvas.delete(label4)
    canvas.delete(label5)

def placeDoll():# Import pictures of character
    global place1, place2, char_Size, char_Size, char, char_walking,char_still_Size, char_walking, char_walking_Size
    char_still = PhotoImage(file="doll.png")# https://www.vecteezy.com/vector-art/131116-walk-cycle-cartoon-free-vector
    char_still_Size = char_still.subsample(6,6)
    char = PhotoImage(file="cartoon-standing-cutout.png")# https://www.vecteezy.com/vector-art/131116-walk-cycle-cartoon-free-vector
    char_Size = char.subsample(2,2)
    char_walking = PhotoImage(file="cartoon-walking-cutout.png")# https://www.vecteezy.com/vector-art/131116-walk-cycle-cartoon-free-vector
    char_walking_Size = char_walking.subsample(2,2)
    place2 = canvas.create_image(130,310, image=char_Size)

def placingObjects():# Place visual objects e.g. firesticks and flag
    global firestick
    global firestick_compressed
    global fire1
    global finalPost
    global comp_flag
    global finalflag
    firestick = PhotoImage(file="firestick.png") #https://www.vecteezy.com/vector-art/373945-fire-on-wooden-stick
    firestick_compressed = firestick.subsample(100)
    fire1 = canvas.create_image(250,180, image=firestick_compressed)
    fire2 = canvas.create_image(410,180, image=firestick_compressed)
    fire3 = canvas.create_image(800,180, image=firestick_compressed)
    fire4 = canvas.create_image(960,180, image=firestick_compressed)
    finishPost = PhotoImage(file="flag.png") #https://www.vecteezy.com/vector-art/109091-dive-flag-set
    comp_flag = finishPost.subsample(3)
    finalflag = canvas.create_image(1100,315, image=comp_flag)

def picture_delete():# Deletes character that is standing to replace with walking character
    canvas.delete(place2)
    walk_setup()

def walk_setup():# Places character at 130,310
    global place3
    place3 = canvas.create_image(130,310, image=char_walking_Size)

def delete_regame():# To delete restart text once you have won
    canvas.delete(regame)

def did_you_win():# Performs tasks when you win the game / reach the flag
    global a, winning_label,winning_score, regame
    a,c = canvas.coords(place3)
    if a == 1100 and safe == TRUE:
        cheat = FALSE
        winning_label = canvas.create_text(width/2, height/3, fill = "white", font = "Times 30 bold", text="YOU WIN!")
        winning_score = canvas.create_text(width/2, height/3 + 200, fill = "white", font = "Times 15 bold", text="Your score: 275")
        my_label.after(3000,delete_winning_labels)
        regame = canvas.create_text(width/2, height/3+50, fill = "white", font = "Times 20 bold", text="Press <r> to Restart")
        my_label.after(3000,delete_regame)

def bossPic():
    global boss
    global enable_boss
    boss = PhotoImage(file="boss-key-pic.png") #Excel screenshot taken from personal spreadsheet
    enable_boss = canvas.create_image(width/2,height/2, image=boss)
    f,g = canvas.coords(enable_boss)

def delBosspic(): #To delete boss pic
    canvas.delete(enable_boss)

# Attempt to create a pausing screen
# def oKey(event):
    #global a
    #pause_rect = canvas.create_rectangle(width/2,height/3,width/2+200,height/3+100, fill="black")
    #pause_screen = canvas.create_text(width/2, height/3, fill = "white", font = "Times 30 bold", text="The game is paused, press i to resume the game")
    #a=canvas.coords(place3)
    #place3 = canvas.coords(a)

#def unpause():
    #canvas.move(place3,2,0)

#def iKey(event):
    #canvas.move(place3,2,0)

#Attempt to save game

#def sKey(event):
    #pause_screen = canvas.create_text(width/2, height/3, fill = "white", font = "Times 30 bold", text="The game is paused, press i to resume the game")
    #s = file(open="Game_Saved.txt,w")
#Initializiation of keybinds

def bKey(event):
    bossPic()

def qKey(event):
    delBosspic()

def pKey(event):# Begins the game as user presses p
    welcome_text_delete()
    canvas.delete(error_tag)
    picture_delete()
    begin_timer()


def delete_restart_info():
    canvas.delete(loser)
    canvas.delete(final_score)
    canvas.delete(regame)

score = 0
def rightKey(event):
    global score
    global a
    score = score + 0.25
    a,c = canvas.coords(place3)
    canvas.move(place3,2,0)
    did_you_win()

def iKey(event):# Viewing instructions
    global inst
    global inst1
    global inst2
    global inst3
    global inst4
    global inst5
    global inst_boss, inst_boss2
    global rect
    rect = canvas.create_rectangle(width/2 - 300, height/3 - 100,width/2 + 300, height/3 + 300, fill = "white")
    inst = canvas.create_text(width/2, height/3, fill = "black", font = "Times 30 bold", text="Instructions:")
    inst1 = canvas.create_text(width/2, height/3 + 100, fill = "black", font = "Times 15 bold", text="This is a simple game where your character has to cross the map")
    inst2 = canvas.create_text(width/2, height/3 + 120, fill = "black", font = "Times 15 bold", text="You need to be careful not to walk when the signal turns red, or you will lose")
    inst3 = canvas.create_text(width/2, height/3 + 140, fill = "black", font = "Times 15 bold", text="If you lose, the game is over")
    inst5 = canvas.create_text(width/2, height/3 + 160, fill = "black", font = "Times 15 bold", text="The level of difficulty increases as you cross each traffic light, so be careful")
    inst_boss = canvas.create_text(width/2, height/3 + 180, fill = "black", font = "Times 15 bold", text="Psst - if your boss is watching you, just type <b> to hide the game")
    inst_boss2 = canvas.create_text(width/2, height/3 + 200, fill = "black", font = "Times 15 bold", text="And <q> to return back to your game")
    inst4 = canvas.create_text(width/2, height/3 + 240, fill = "black", font = "Times 20 bold", text="Press <m> to go back to the Main Menu")


def delete_inst():# To delete instructions
    canvas.delete(rect)
    canvas.delete(inst)
    canvas.delete(inst1)
    canvas.delete(inst2)
    canvas.delete(inst3)
    canvas.delete(inst4)
    canvas.delete(inst5)
    canvas.delete(inst_boss)
    canvas.delete(inst_boss2)

def mKey(event):
    delete_inst()

def eKey(event):
    quit()

def quit():# To exit the code
    window.destroy()


def restart_game():# Restarts the loop =
    placeDoll()
    begin()
    delete_restart_info()

def delete_winning_labels():# To delete winning text after you win
    canvas.delete(winning_label)
    canvas.delete(winning_score)



canvas.bind("<Right>", rightKey) # Move characeter to the right
canvas.bind("<p>", pKey) # Play game
canvas.bind("<b>", bKey) # Boss key
canvas.bind("<i>", iKey) # View Instructions
canvas.bind("<m>", mKey) # Close Instructions
canvas.bind("<c>", cKey) # Cheat code
canvas.bind("<q>", qKey) # Quit Boss Key
canvas.bind("<e>", eKey) # Quit game
canvas.bind("<r>", rKey) # Restart game
#Attempt to pause and unpause the game
#canvas.bind("<o>", oKey) # Pause game
#canvas.bind("<i>", iKey) # Unpause game
#Attempt to save game
#canvas.bind("<s>", sKey) # Save game


canvas.focus_set

begin()
placingObjects()
placeDoll()
window.mainloop()