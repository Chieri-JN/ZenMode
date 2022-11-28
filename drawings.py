#################################################
#drawings.py
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


##########################################
# Wave
##########################################

def drawWave(canvas,cx,cy,r):
    canvas.create_arc(cx-r,cy-r,cx+r,cy+r, 
                            fill="black", outline = '', style="pieslice", 
                            extent=180)

def redrawAll(app, canvas):
    pass




# runApp(width=800, height=800)



