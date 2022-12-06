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

# NOTE MODIDY PARAMETERS IF NEEDED
def drawRandomShapes(shape,rate,bounds):
    pass

##########################################
# Background Trees
##########################################
def drawTree(app,canvas,width,y1):
    
    pass

def drawBackgroundTrees(app,canvas,width,y1):
    
    pass

##########################################
# Ground
##########################################

def drawGround(canvas,x0,y0,width,y1):
    dirtSpecs = 20
    #dirt
    canvas.create_rectangle(x0,y0+20,width,y1,fill="#372826",width=0)
    #
    
    # grass
    grassBlades = width // 40

    canvas.create_rectangle(x0,y0+20,width,y0+50,fill='#267326' ,width=0)
    canvas.create_rectangle(x0,y0-20,width,y0+20,fill="#39ac39",width=0)
    for grass in range(grassBlades):
        if grass % 4 == 0:
            #                   (x0,y0,x1,y1,x2,y2,x3,y3)
            canvas.create_line((30+50*grass)+x0,y0+5 , (30+50*grass)+x0,y0-7 , (33+50*grass)+x0,y0-14, 
                              (40+50*grass)+x0,y0-6,joinstyle='bevel',fill='#194d19',width=4,
                               capstyle='round')
        if grass % 4 == 2: 
            canvas.create_line((40+50*grass)-x0,y0-6 , (33+50*grass)-x0,y0-14 , (30+50*grass)-x0,y0-7, 
                              (30+50*grass)-x0,y0+5,joinstyle='bevel',fill='#2c872c',width=4,
                               capstyle='round')
    
##########################################
# Branch
##########################################
def drawBranch(canvas,x0,y0,x1,y1,h,step,lcolour):
    # if step < 5:
    #     colour = "#674119"
    # elif 5 < step < 8:
    #     colour = "#FFB6C1" 
    # else: 
    #     colour = "#FFB6C1"
    if step >= 7:
        colour = lcolour
        cap = 'round'
    else:
        colour = "#674119" 
        cap = 'projecting'

    canvas.create_line(x0,y0,x1,y1, fill=colour,width=5*h/15,capstyle=cap)
    # capstyle='round'


##########################################
# Player Sprites
##########################################
# Sprite sheets retrieved from https://godotmarketplace.com/shop/2d-pixel-slime-set/
def PlayerSprites(app):
    app.image1 = app.loadImage('slimeSprites/slimeIdle.png')
    slimeIdle = app.scaleImage(app.image1, 6)

    app.image2 = app.loadImage('slimeSprites/slimeRIdle.png')
    slimeIdleR = app.scaleImage(app.image2, 6)

    app.image3 = app.loadImage('slimeSprites/slimeJump.png')
    slimeJump = app.scaleImage(app.image3, 6)

    app.image4 = app.loadImage('slimeSprites/slimeMoveRight.png')
    slimeMRight = app.scaleImage(app.image4, 6)

    app.image5 = app.loadImage('slimeSprites/slimeMoveLeft.png')
    slimeMLeft = app.scaleImage(app.image5, 6)

    idle = []
    idleR = []
    jump = []
    right = []
    left = []

    for i in range(2):
        # sprite = slimeIdle.crop((80*i, 0, 40+80*i, 44))
        sprite = slimeIdle.crop((480*i, 96, 240+480*i, 264))
        idle.append(sprite)

    for i in range(2):
        # sprite = slimeIdle.crop((80*i, 0, 40+80*i, 44))
        sprite = slimeIdleR.crop((10+480*i, 96, 320+480*i, 264))
        idleR.append(sprite)

    for i in range(11):
        # use conditional to case on vertical crop
        # sprite = slimeJump.crop((78*i, 0, 78+78*i, 79))
        sprite = slimeJump.crop((40+480*i, 90, 180+480*i, 360))
        jump.append(sprite)

    for i in range(7):
        # sprite = slimeMRight.crop((11+80*i, 0, 34+80*i, 54))
        sprite = slimeMRight.crop((66+480*i, 126, 204+480*i, 331))
        right.append(sprite)

    for i in range(7):
        sprite = slimeMLeft.crop((66+480*i, 126, 212+480*i, 331))
        left.append(sprite)

    return {0:idle,1:idleR,2:jump,3:right,4:left}



"""TEST CODE"""

# def appStarted(app):
#     # app.timerDelay = 1000
#     app.spriteCounter  = 0
#     app.playerSprites = PlayerSprites(app)[3]
#     app.spriteCounter2  = 0
#     app.playerSprites2 = PlayerSprites(app)[2]
#     pass

# def redrawAll(app,canvas):
#     sprite = app.playerSprites[app.spriteCounter]
#     sprite2 = app.playerSprites2[app.spriteCounter2]
#     canvas.create_image(app.width/2, app.height/2+200, image=ImageTk.PhotoImage(sprite))
#     canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(sprite2))
#     pass


# def timerFired(app):
#     app.spriteCounter = (1 + app.spriteCounter) % len(app.playerSprites)
#     app.spriteCounter2 = (1 + app.spriteCounter2) % len(app.playerSprites2)
#     # print(len(PlayerSprites(app)[1]))
# #      drawBranch(canvas,app.width/2,780,app.width/2,700,5)
#     pass


# runApp(width=800, height=800)

