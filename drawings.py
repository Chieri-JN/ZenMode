#################################################
#drawings.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################

from cmu_112_graphics import *
import random 
import string
import math


##########################################
# Helper Functions
##########################################


def HextoRGB(hexColour):
    r,g,b = 0,0,0
    
    return(r,g,b)

##########################################
# Wave
##########################################

def drawWave(canvas,cx,cy,r):
    canvas.create_arc(cx-r,cy-r,cx+r,cy+r, 
                            fill="black", outline = '', style="pieslice", 
                            extent=180)

##########################################
# Ground
##########################################

def drawGround(canvas,x0,y0,width,height):

    dirtSpecs = 20

    #dirt
    canvas.create_rectangle(x0,y0,x0+width,height,fill="#372826",width=0)
    # grass
    grassBlades = width // 40
    margin = width / 40 % 1
    bladeW = 10
    bladeH = 7
    canvas.create_rectangle(x0,y0,x0+width,y0+20,fill="#39ac39",width=0)
    for grass in range(grassBlades):

        pass
        # canvas.create_polygon(x0*grass,y0+20, (x0)*(grass+1),y0+20, (x0+bladeW/2)*grass,
        #                        y0+bladeH+20,fill="#39ac39",width=0)


##########################################
# Branch
##########################################

def drawBranch(canvas,x0,y0,x1,y1,step,check):
    # if step < 5:
    #     colour = "#674119"
    # elif 5 < step < 8:
    #     colour = "#FFB6C1" 
    # else: 
    #     colour = "#FFB6C1"
    
    if check % 3 == 0:
        colour = "blue" 
    elif check % 3 == 1:
        colour = "#FFB6C1" 
    elif check % 3 == 2:
        colour = "red"
    else:
        colour = "#674119"

    canvas.create_line(x0,y0,x1,y1, fill=colour,width=(28/check))
    # capstyle='round'


##########################################
# Player Sprites
##########################################
# Sprite sheets retrieved from https://godotmarketplace.com/shop/2d-pixel-slime-set/
def PlayerSprites(app):

    app.image1 = app.loadImage('slimeIdle.png')
    slimeIdle = app.scaleImage(app.image1, 6)

    app.image2 = app.loadImage('slimeJump.png')
    slimeJump = app.scaleImage(app.image2, 6)
    # slimeJump = app.image2

    app.image3 = app.loadImage('slimeMoveRight.png')
    slimeMRight = app.scaleImage(app.image3, 6)
    # slimeMRight = app.image3

    app.image4 = app.loadImage('slimeMoveLeft.png')
    slimeMLeft = app.scaleImage(app.image4, 6)

    idle = []
    jump = []
    right = []
    left = []

    for i in range(2):
        # sprite = slimeIdle.crop((80*i, 0, 40+80*i, 44))
        sprite = slimeIdle.crop((480*i, 96, 240+480*i, 264))
        idle.append(sprite)

    for i in range(11):
        # use conditional to case on vertical crop
        # sprite = slimeJump.crop((78*i, 0, 78+78*i, 79))
        sprite = slimeJump.crop((40+480*i, 0, 180+480*i, 474))
        jump.append(sprite)

    for i in range(7):
        # sprite = slimeMRight.crop((11+80*i, 0, 34+80*i, 54))
        sprite = slimeMRight.crop((66+480*i, 96, 204+480*i, 240))
        right.append(sprite)

    for i in range(7):
        sprite = slimeMLeft.crop((66+480*i, 0, 212+480*i, 324))
        left.append(sprite)

    return {0:idle,1:jump,2:right,3:left}


"""TEST CODE"""

def appStarted(app):
    # app.timerDelay = 1000
    app.spriteCounter  = 0
    app.playerSprites = PlayerSprites(app)[0]
    pass

# def redrawAll(app,canvas):
#     sprite = app.playerSprites[app.spriteCounter]
#     canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(sprite))
#     pass


# def timerFired(app):
#     app.spriteCounter = (1 + app.spriteCounter) % len(app.playerSprites)
#     # print(len(PlayerSprites(app)[1]))
# #      drawBranch(canvas,app.width/2,780,app.width/2,700,5)
#     pass


# runApp(width=800, height=800)

