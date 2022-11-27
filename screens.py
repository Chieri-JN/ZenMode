#################################################
# screens.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################

from cmu_112_graphics import *
import classes as cl
import dictionaries as dict
import random 
import string
import math

##########################################
# Helper Functions
##########################################

def randomHexGenerator():
    colour = ''
    HexAlpha = string.digits + 'ABCDEF'
    for i in range(6):
        colour += random.choice(HexAlpha)
    return '#' + colour

# Taken from hw1
def distance(x1, y1, x2, y2): 
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    return math.sqrt(x + y)

# Taken from hw1
def circlesIntersect(x1, y1, r1, x2, y2, r2): 
    return not (r1 + r2) < distance(x1, y1, x2, y2)

# Perfect elsastic collision of two balls 
def elasticCollision():
    pass

def areaCircle():
    pass



##########################################
# Spalsh Screen / Start Mode
##########################################

def startScreen_redrawAll(app,canvas):
    font = ''
    canvas.create_rectangle()


def startScreen_timerFired(app):
    #moveBall(app)
    pass


# NOTE Use timerFired to have colour gradually change (cycle through colours
# cycle through RGB colours)
# Have circles, randomly generated and drifting across screen, slightly light/
# darker than actually bg colour()
# OR have bg be paler shade(pastel) of circle colour  
# scatter function/transition function for when I screen is changed


##########################################
# Quiz Screens / Start Mode
##########################################

# Colour Wheel
def moodWheel_redrawAll(app,canvas):
    pass

# NOTE USE DISCTANCE TO CALCULATE location from circumfrence of circle

# Word Selection
def wordSelectorScreen_redrawAll(app,canvas):
    pass

#Reflexes/Other
def reflexesScreen_redrawAll(app,canvas):
    pass

##########################################
# Pause/Help Screen 
##########################################

# Help/Menue
def helpScreen_redrawAll(app,canvas):
    pass

# Pause
def pauseScreen_redrawAll(app,canvas):
    pass

##########################################
# GameOver Screen / You Win
##########################################

def gameEndScreen_redrawAll(app,canvas):
    pass

##########################################
# Game Screen / Game Mode
##########################################

def gameScreen_redrawAll(app,canvas):
    pass

