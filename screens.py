#################################################
# screens.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################

from cmu_112_graphics import *
import classes as cl
import drawings as dr
import texts as tx
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

def drawCircle(canvas,cx,cy,r,colour):
    canvas.create_ovale(cx-r, cy-r, cx+r, cy+r,fill=colour)

def drawShape():
    pass

# NOTE MODIDY PARAMETERS IF NEEDED
def drawRandomShapes(shape,rate,bounds):
    pass
##########################################
# Main App
##########################################

testText = cl.Word(tx.helpText1)
# for buttons
def switchMode(app,mode,colour):
    app.screenColour = colour
    app.mode = mode
    

def appStarted(app):
    app.mode = 'startScreen'

    app.gameStarted = False # prevents going from help to pause without staring the game
    app.gameOver = False
    app.screenColour = "#c8eed5"
    app.centerx = app.width/2
    app.centery = app.height/2
    app.selectedWord = None

    # startScreen unique App values
    app.Startbuttons = []
    # NOTE WIll not respond when mouse hovers over txt
    app.startButton = cl.Button(app.centerx, 500, 85, 220,'#85daa2','#a9e5bd',5,
                            'white','Start','Krungthep 50')
    app.helpButton = cl.Button(app.centerx, 650, 85, 200,'#85daa2','#a9e5bd',5,
                            'white','Help','Krungthep 50')
    app.Startbuttons.extend([app.startButton,app.helpButton])

    # quiz Screen unique App values
    app.quizButtons = []

    # help screen unique App values
    app.helpButtons = []
    
    app.text1 = cl.Word(tx.helpText1)
    app.text2 = cl.Word(tx.helpText2)
    app.text3 = cl.Word(tx.helpText3)
    app.helpText= testText

    # pause screen unique App values
    # NOTE CHANGE LOCATION VALUES
    app.pauseButtons = []
    # help button 
    app.pauseHelpButton = cl.Button(app.centerx, 650, 85, 200,'#85daa2',
                                    '#a9e5bd',5,'white','Help','Krungthep 50')
    # exit button 
    app.exitGameButton = cl.Button(app.centerx, 650, 85, 200,'#85daa2',
                                    '#a9e5bd',5,'white','Exit Game',
                                    'Krungthep 50')
    # resume button
    app.resumeGameButton = cl.Button(app.centerx, 650, 85, 200,'#85daa2',
                                    '#a9e5bd',5,'white','Resume Game',
                                    'Krungthep 50')
    app.pauseButtons.extend([app.pauseHelpButton,app.exitGameButton,
                             app.resumeGameButton])


##########################################
# Spalsh Screen / Start Mode
##########################################
def startScreen_appStarted(app): 
    pass

def startScreen_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
    title1 = cl.Word('Zen')
    title2 = cl.Word('Mode')

    for button in app.Startbuttons:
        button.draw(canvas)

    # NOTE draw tree in between words 
    # Title
    title1.drawWord(canvas,app.centerx-263,200,'K2D 220','grey64') #shadow
    title1.drawWord(canvas,app.centerx-270,200,'K2D 220','white')
    title2.drawWord(canvas,app.centerx+217,200,'K2D 220','grey64') #shadow
    title2.drawWord(canvas,app.centerx+210,200,'K2D 220','white') 
 
def startScreen_keyPressed(app,event):
    if event.key == 'Return':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreen1'
    elif event.key == 'Space':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreen1'
    if event.key == 'h':
        app.screenColour = '#96c9a6'
        app.mode = 'helpScreen'
    else: # NOTE remove
        print('None')

def startScreen_mousePressed(app,event):
    if app.startButton.inBounds(event.x, event.y):
        app.startButton.buttonPressed(switchMode(app,'quizScreen1','#ffbe60'))
        print('Start button pressed!')

    if app.helpButton.inBounds(event.x, event.y):
        app.startButton.buttonPressed(switchMode(app,'helpScreen','#96c9a6'))
        print('Help button pressed!')

    # app.setSize(newWidth, newHeight) NOTE use to change canvas size
    pass

def startScreen_timerFired(app):
    #moveBall(app)
    pass

# NOTE Use timerFired to have colour gradually change (cycle through colours
# cycle through RGB colours)
# Have circles, randomly generated and drifting across screen, slightly light/
# darker than actually bg colour()
# NOTE (maybe)if balls are pressed they will change shade
# OR have bg be paler shade(pastel) of circle colour  
# scatter function/transition function for when I screen is changed


##########################################
# Quiz Screens / Start Mode
##########################################

# Mood Wheel (colour wheel)
##########################################
# drawWord(self, canvas, x, y, font, colour)
def quizScreen1_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
    mood1 = cl.MoodWheel(app.centerx,500,200)
    mood1.drawColoutWheel(canvas)

    text1 = cl.Word('Hello')

def quizScreen1_mouseDragged(app,event):
    pass
def quizScreen1_mouseReleased(app,event):
    pass
def quizScreen1_mousePressed(app,event):
    pass

# NOTE USE DISCTANCE TO CALCULATE location from circumfrence of circle
def quizScreen1_timerFired(app):
    pass

# NOTE USED TO move across screens, will remove later
def quizScreen1_keyPressed(app,event):
    if event.key == 'Left':
        app.screenColour = "#c8eed5"
        app.mode = 'startScreen'
    elif event.key == 'Right':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreen2'

# Word Selection # for words generation
##########################################
def quizScreen2_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
def quizScreen2_timerFired(app):
    pass
def quizScreen2_mousePressed(app,event):
    pass


#NOTE remove Later
def quizScreen2_keyPressed(app,event):
    if event.key == 'Left':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreen1'
    elif event.key == 'Right':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreen3'

#Reflexes/Other
##########################################
def quizScreen3_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
def quizScreen3_timerFired(app):
    pass
def quizScreen3_mousePressed(app,event):
    pass

def quizScreen2_keyPressed(app,event):
    if event.key == 'Left':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreen2'
    elif event.key == 'Right':
        app.screenColour = '#ffbe60'
        app.mode = 'gameScreen'

##########################################
# Pause/Help Screen 
##########################################

# Help Screen
# drawWord(self, canvas, x, y, font, colour)
def helpScreen_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
    header1 = cl.Word('Help Menu')

    header1.drawWord(canvas,app.centerx,100,'K2D 170','grey64') #shadow
    header1.drawWord(canvas,app.centerx-5,100,'K2D 170','white')
    
    app.helpText.drawWord(canvas,app.centerx,app.centery,'K2D 30','white')

# NOTE Condisder having seperate draw function for info text
def helpScreen_keyPressed(app,event):
    if event.key == 'Escape':
        if app.gameStarted == False:
            app.screenColour = '#c8eed5'
            app.mode = 'startScreen'
        else:
            app.screenColour = 'grey64'
            app.mode = 'pauseScreen'
    elif event.key == 'H':
        app.helpText= app.text1
    elif event.key == 'C':
        app.helpText= app.text2
        appStarted(app)
    elif event.key == 'F':
        app.helpText= app.text3

def helpScreen_timerFired(app):
    pass

# Pause
def pauseScreen_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
    header1 = cl.Word('Game Paused')

    header1.drawWord(canvas,app.centerx,100,'K2D 170','grey64') #shadow
    header1.drawWord(canvas,app.centerx-5,100,'K2D 170','white')

    # exit button 
    # help button 
    # resume Game button

def pauseScreen_timerFired(app):
    pass
def pauseScreen_mousePressed(app,event):
    pass

##########################################
# GameOver Screen / You Win
##########################################

def endGame_redrawAll(app,canvas):
    pass
def endGame_timerFired(app):
    pass
def endGame_mousePressed(app,event):
    pass
def endGame_keyPressed(app,event):
    pass



##########################################
# Game Screen / Game Mode
##########################################

def gameScreen_redrawAll(app,canvas):
    pass
def gameScreen_appStarted(app):
    pass
def gameScreen_timerFired(app):
    pass
def gameScreen_mousePressed(app,event):
    pass
def quizScreen1_keyPressed(app,event):
    if event.key == 'Left':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreen1'
    elif event.key == 'Right':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreen3'
    elif event.ky == 'P':
        app.screenColour = 'grey64'
        app.mode = 'pauseScreen'


def spawnItem():
    pass
def spawnWord():
    pass

runApp(width=1200, height=820, title = 'ZenMode')