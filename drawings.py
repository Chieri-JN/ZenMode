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

def redrawAll(app, canvas):
    pass

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

def drawBranch(canvas,x0,y0,x1,y1,step):
    if step < 5:
        colour = "674119"
    elif 5 < step < 8:
        colour = "#FFB6C1" 
    else: 
        colour = "FFB6C1"

    canvas.create_line(x0,y0,x1,y1, fill='colour',
                       width=(x1-x0)*0.70, capstyle='round')



##########################################
# Player
##########################################

def drawPlayer(canvas):
    pass



# runApp(width=800, height=800)