#################################################
# screens.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################

from cmu_112_graphics import *
import classes as cl
import drawings as dr
import texts_colours as tx
import texts_colours as col
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
def perfElasticCollision():
    pass

def areaCircle():
    pass

# NOTE MODIDY PARAMETERS IF NEEDED
def drawRandomShapes(shape,rate,bounds):
    pass

##########################################
# Main App
##########################################

# for buttons
def switchMode(app,mode,colour,title):
    app.screenColour = colour
    app.mode = mode
    app._title = title
    app.tick = 0
    

def appStarted(app):
    app.timerDelay = 200
    app.mode = 'quizScreenOne'
    app._title = 'ZenMode'
    app.tick = 0
    app.gameStarted = False # prevents going from help to pause without staring the game
    app.gameOver = False 
    # SET to NONE
    app.gameOutcome = 'None'
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

    # quiz1 Screen unique App values
    app.quiz1Buttons = []
    app.mood = 'Neutral'

    app.quiz1Buttons.extend([])

    # quiz2 Screen unique App values
    app.quiz2Buttons = []

    app.quiz2Buttons.extend([])

    # quiz3 Screen unique App values
    app.quiz3Buttons = []

    app.quiz3Buttons.extend([])

    # help screen unique App values
    #text
    app.text1 = cl.Word(tx.helpText1)
    app.text2 = cl.Word(tx.helpText2)
    app.text3 = cl.Word(tx.helpText3)
    app.helpText = 1


    # pause screen unique App values
    app.pauseButtons = []
    # resume button
    app.resumeGameButton = cl.Button(app.centerx, 400, 90, 200,'gray61',
                                    'gray81',5,'white','Resume\n   Game',
                                    'Krungthep 35')
    # help button 
    app.pauseHelpButton = cl.Button(app.centerx, 525, 90, 200,'gray51',
                                    'gray81',5,'white','Help','Krungthep 40')
    # exit button 
    app.exitGameButton = cl.Button(app.centerx, 650, 90, 200,'gray41',
                                    'gray81',5,'white','  Exit\nGame',
                                    'Krungthep 35')
    app.pauseButtons.extend([app.pauseHelpButton,app.exitGameButton,
                             app.resumeGameButton])


##########################################
# Start Screen
##########################################
def startScreen_appStarted(app): 
    pass

def startScreen_redrawAll(app,canvas):
    #canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
    canvas.create_rectangle(0,0,app.width,app.height,fill=bgColourChange(app))
    title1 = cl.Word('Zen')
    title2 = cl.Word('Mode')
    bgColourChange(app)
    for button in app.Startbuttons:
        button.draw(canvas)

    # NOTE draw tree in between words 
    # Title
    title1.drawWord(canvas,app.centerx-263,200,'K2D 220','grey54') #shadow
    title1.drawWord(canvas,app.centerx-270,200,'K2D 220','white')
    title2.drawWord(canvas,app.centerx+217,200,'K2D 220','grey54') #shadow
    title2.drawWord(canvas,app.centerx+210,200,'K2D 220','white') 
 
def startScreen_keyPressed(app,event):
    if event.key == 'Return':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreenOne'
        app._title = 'quizScreen1' # test
    elif event.key == 'Space':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreenOne'
        app._title = 'quizScreen1'
    elif event.key == 'h':
        app.screenColour = '#96c9a6'
        app.mode = 'helpScreen'
        app._title = 'helpScreen'
    elif event.key == 'q':
        app.quit()
    else: # NOTE remove
        print('None')

def startScreen_mousePressed(app,event):
    if app.startButton.inBounds(event.x, event.y):
        app.startButton.buttonPressed(switchMode(app,'quizScreenOne','#ffbe60','quizScreen1'))
        print('Start button pressed!')

    if app.helpButton.inBounds(event.x, event.y):
        app.startButton.buttonPressed(switchMode(app,'helpScreen','#96c9a6','helpScreen'))
        print('Help button pressed!')

    # app.setSize(newWidth, newHeight) NOTE use to change canvas size
    pass

def bgColourChange(app):
    return col.pastelColoursList[app.tick%len(col.pastelColoursList)]

def startScreen_timerFired(app):
    #moveBall(app)

    app.tick +=1
    print(app.tick)

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
def quizScreenOne_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)

    mood1 = cl.MoodWheel(app.centerx-300,550,190)
    mood1.drawColourWheel(canvas)

    header1 = cl.Word('Hello')
    header2 = cl.Word('How are you feeling today?')
    header3 = cl.Word('Current Mood:')

    mood = cl.Word(app.mood)

    header1.drawWord(canvas,app.centerx-370,100,'K2D 120','grey54') #shadow
    header1.drawWord(canvas,app.centerx-375,100,'K2D 120','white')
    header2.drawWord(canvas,app.centerx-20,200,'K2D 80','grey54') #shadow
    header2.drawWord(canvas,app.centerx-25,200,'K2D 80','white')

    header3.drawWord(canvas,app.centerx+205,370,'K2D 70','grey54')
    header3.drawWord(canvas,app.centerx+200,370,'K2D 70','white')

    mood.drawWord(canvas,app.centerx+205,540,'K2D 70','gray65')
    mood.drawWord(canvas,app.centerx+200,540,'K2D 70','gray99')

# NOTE USE DISCTANCE TO CALCULATE location from circumfrence of circle
def quizScreenOne_mouseDragged(app,event):
    pass
def quizScreenOne_mouseReleased(app,event):
    pass
def quizScreenOne_mousePressed(app,event):
    pass


# NOTE will change modd
def moodChange(app):
    app.mood = 'New Mood'
    return app.mood

# NOTE USED TO move across screens, will remove later
def quizScreenOne_keyPressed(app,event):
    print('A key was pressed!')
    if event.key == 'Left':
        app.screenColour = "#c8eed5"
        app.mode = 'startScreen'
        app._title = 'ZenMode'
    elif event.key == 'Right':
        app.screenColour = '#d8d4f1'
        app.mode = 'quizScreenTwo'
        app._title = 'quizScreen2'

def quizScreenOne_timerFired(app):
    pass

# Word Selection # for words generation
##########################################
def quizScreenTwo_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
def quizScreenTwo_timerFired(app):
    pass
def quizScreenTwo_mousePressed(app,event):
    pass


#NOTE remove Later
def quizScreenTwo_keyPressed(app,event):
    if event.key == 'Left':
        app.screenColour = '#ffbe60'
        app.mode = 'quizScreenOne'
        app._title = 'quizScreen1'
    elif event.key == 'Right':
        app.screenColour = '#ff8c95'
        app.mode = 'quizScreenThree'
        app._title = 'quizScreen3'

#Reflexes/Other
##########################################
def quizScreenThree_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
def quizScreenThree_timerFired(app):
    pass
def quizScreenThree_mousePressed(app,event):
    pass

def quizScreenThree_keyPressed(app,event):
    if event.key == 'Left':
        app.screenColour = '#d8d4f1'
        app.mode = 'quizScreenTwo'
        app._title = 'quizScreen2'
    elif event.key == 'Right':
        app.screenColour = 'pink'
        app.mode = 'gameScreen'
        app._title = 'gameScreen'

##########################################
# Pause/Help Screen 
##########################################

# Help Screen
def helpScreen_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
    
    header1 = cl.Word('Help Menu')
    header1.drawWord(canvas,app.centerx,150,'K2D 170','grey64') #shadow
    header1.drawWord(canvas,app.centerx-5,150,'K2D 170','white')

    if app.helpText == 1 :
        app.text1.drawWord(canvas,app.centerx,app.centery+50,'K2D 30','white')
    elif app.helpText == 2 :
        app.text2.drawWord(canvas,app.centerx,app.centery+50,'K2D 30','white')
    elif app.helpText == 3 :
        app.text3.drawWord(canvas,app.centerx,app.centery+50,'K2D 30','white')

def helpScreen_keyPressed(app,event):
    if event.key == 'Escape':
        if app.gameStarted == False:
            app.screenColour = '#c8eed5'
            app.mode = 'startScreen'
            app._title = 'ZenMode'
        else:
            app.screenColour = 'grey74'
            app.mode = 'pauseScreen'
            app._title = 'pauseScreen'
    elif event.key == 'h':
        app.helpText = 1
    elif event.key == 'c':
        app.helpText = 2
    elif event.key == 'f':
        app.helpText = 3

def helpScreen_timerFired(app):
    pass

# Pause
def pauseScreen_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
    header1 = cl.Word('Game Paused')

    header1.drawWord(canvas,app.centerx,170,'K2D 120','grey45') #shadow
    header1.drawWord(canvas,app.centerx-5,170,'K2D 120','white')

    for button in app.pauseButtons:
        button.draw(canvas) 

def pauseScreen_keyPressed(app,event):
    if event.key == 'Return':
        app.screenColour = 'pink'
        app.mode = 'gameScreen'
        app._title = 'gameScreen'  
    elif event.key == 'Escape':
        app.screenColour = "#c8eed5"
        app.mode = 'startScreen'
        app._title = 'ZenMode'
    if event.key == 'h':
        app.screenColour = '#96c9a6'
        app.mode = 'helpScreen'
        app._title = 'helpScreen'
 
def pauseScreen_mousePressed(app,event):
    if app.pauseHelpButton.inBounds(event.x, event.y):
        app.gameStarted = True # NOTE REMOVE 
        app.startButton.buttonPressed(switchMode(app,'helpScreen','#96c9a6','helpScreen'))
        print('Help button pressed!')

    if app.exitGameButton.inBounds(event.x, event.y):
        app.gameStarted = False # set game state to false
        app.startButton.buttonPressed(switchMode(app,'startScreen',"#c8eed5",'ZenMode'))
        print('Exit Game button pressed!')
        
    if app.resumeGameButton.inBounds(event.x, event.y):
        app.startButton.buttonPressed(switchMode(app,'gameScreen','pink','gameScreen'))
        print('Resume Game button pressed!')

def pauseScreen_timerFired(app):
    pass
##########################################
# GameOver Screen / You Win
##########################################

def endGame_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)
    # drawWord(canvas, x, y, font, colour)
    if app.gameOutcome == 'Win':
        textSize = 120
        textSize2 = 100
        textSize3 = 50
        text1 = 'ZenTree complete!'
        text2 ='You won!'
        text3 = 'Congrats on reaching your Zen'
        T1colour1 = 'dark goldenrod'
        T1colour2 = 'gold'
        T2colour1 = 'grey56'
        T2colour2 = 'white'
    elif app.gameOutcome == 'Loss':
        textSize = 170
        textSize2 = 100
        textSize3 = 50
        text1 = 'Game Over'
        text2 = 'You lost...'
        text3 = 'Better luck next time'
        T1colour1 = 'red4'
        T1colour2 = 'firebrick3'
        T2colour1 = 'dark slate blue'
        T2colour2 = 'medium slate blue'
    else:
        textSize = 170
        textSize2 = 70
        textSize3 = 50
        text1 = 'Uh Oh!'
        text2 = "Seems like something's broken..."
        text3 = "You'll probably want to fix that"
        T1colour1 = 'grey60'
        T1colour2 = 'white'
        T2colour1 = 'dark slate blue'
        T2colour2 = 'medium slate blue'

    header1 = cl.Word(text1)
    header2 = cl.Word(text2)
    header3 = cl.Word(text3)

    header1.drawWord(canvas,app.centerx,150,f'K2D {textSize}',T1colour1) # shadow
    header1.drawWord(canvas,app.centerx-4,150,f'K2D {textSize}',T1colour2)

    # NOTE CHANGE FONT
    header2.drawWord(canvas,app.centerx,350,f'K2D {textSize2}',T2colour1)# shadow
    header2.drawWord(canvas,app.centerx-3,350,f'K2D {textSize2}',T2colour2)# shadow
    # NOTE CHANGE FONT
    header3.drawWord(canvas,app.centerx,550,f'K2D {textSize3}','black')

    text = cl.Word(tx.endGameText)
    text.drawWord(canvas,app.centerx-5,720,'K2D 20','black')
    
def endGame_keyPressed(app,event):
    if event.key == 'Return':
        app.screenColour = 'pink' 
        app.mode = 'gameScreen'
        app._title = 'gameScreen'
    elif event.key == 'Escape':
        app.screenColour = "#c8eed5"
        app.mode = 'startScreen'
        app._title = 'ZenMode'
    elif event.key == 'q':
        app.quit()
        print('You quit ZenMode! Hope you had fun! :)')

def endGame_mousePressed(app,event):
    pass

def endGame_timerFired(app):
    pass

##########################################
# Game Screen / Game Mode
##########################################

def gameScreen_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)

def gameScreen_appStarted(app):
    pass
def gameScreen_timerFired(app):
    pass
def gameScreen_mousePressed(app,event):
    pass


def gameScreen_keyPressed(app,event):
    if event.key == 'Left':
        app.screenColour = '#ff8c95'
        app.mode = 'quizScreenThree'
        app._title = 'quizScreen3'
    elif event.key == 'Right':
        # include different colours based on weither player won or not
        if app.gameOutcome == 'Win':
            app.screenColour = '#eac4bb'
        elif app.gameOutcome == 'Loss':
            app.screenColour = 'cornsilk3'
        else:
            app.screenColour = 'lawn green'
        app.mode = 'endGame'
        app._title = 'endGame'
    elif event.key == 'p':
        app.screenColour = 'grey74'
        app.mode = 'pauseScreen'
        app._title = 'pauseScreen'


def spawnItem():
    pass
def spawnWord():
    pass

runApp(width=1200, height=820, title = 'ZenMode')