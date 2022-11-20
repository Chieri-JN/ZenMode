#################################################
# screens.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################
 
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

def distance(x1, y1, x2, y2): # DONE
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    return math.sqrt(x + y)

def circlesIntersect(x1, y1, r1, x2, y2, r2): # DONE
    if (r1 + r2) < distance(x1, y1, x2, y2):
        return False
    return True

##########################################
# Spalsh Screen / Start Mode
##########################################

def startScreen_redrawAll(app,canvas):
    font = ''


    pass

##########################################
# Quiz Screens / Start Mode
##########################################

# Colour Wheel
def moodWheel_redrawAll(app,canvas):
    pass

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

