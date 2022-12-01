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
import time
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
    app.mode = 'gameScreen'
    app._title = 'ZenMode'
    # NOTE ORIGINAL #c8eed5
    app.screenColour = "#c8eed5"
    app.timerDelay = 200
    app.tick = 0
    app.mouseMovedDelay = -10
    app.gameStarted = False # prevents going from help to pause without staring the game
    app.gameOver = False 
    # SET to NONE
    app.gameOutcome = 'Loss'
    
    app.centerx = app.width/2
    app.centery = app.height/2
    app.selectedWord = 'None'
    app.mass = 10

    # startScreen unique App values
    app.Startbuttons = []
    # NOTE WIll not respond when mouse hovers over txt
    app.startButton = cl.Button(app.centerx, 500, 85, 220,'#85daa2','#a9e5bd',5,
                            'white','Start','Krungthep 50')
    app.helpButton = cl.Button(app.centerx, 650, 85, 200,'#85daa2','#a9e5bd',5,
                            'white','Help','Krungthep 50')
    app.Startbuttons.extend([app.startButton,app.helpButton])

    # quiz1 Screen unique App values
    app.mood1 = cl.MoodWheel(app.centerx-300,550,190)
    app.circlex = app.centerx-300
    app.circley = 550
    app.circle1 = cl.Circle(app.circlex,app.circley, 20,'white',0,'')
    app.currMood = 'Neutral'
    app.mood = cl.Word(app.currMood)
    app.cwCirclePos = (app.circlex,app.circley)
    app.quiz1Buttons = []
    # buttons
    app.selectMoodButton = cl.Button(app.centerx+200, 650, 80, 150,'#e68800','#ffa11a',5,
                            'white','Select','Krungthep 30')
    app.quiz1Buttons.extend([app.selectMoodButton])

    # quiz2 Screen unique App values
    app.WordList = []
    # for word in dict.dictonaryMood:
    #     wordbubble = cl.WordBubble(word,)
    #     app.WordList.append(wordbubble)

    # buttons
    app.quiz2Buttons = []
    app.chooseWordButton = cl.Button(app.centerx+340, 500, 80, 150,'#a89fe0','#cbc5ec',5,
                            'white','Choose','Krungthep 30')
    app.refreshWordButton = cl.Button(app.centerx+340, 650, 80, 150,'#a89fe0','#cbc5ec',5,
                            'white','Refresh','Krungthep 30')
    app.quiz2Buttons.extend([app.chooseWordButton,app.refreshWordButton])

    # quiz3 Screen unique App values
   
    app.dotColour = random.choice(col.coloursTwoList)
    app.dotCount = 0
    app.dots = []

    app.quiz3Buttons = []
    app.quiz3StartButton = cl.Button(app.centerx, app.centery, 115, 250,'#ff4d5a','#ffb3b8',5,
                            'white','Start','Krungthep 70')
    app.quiz3Buttons.extend([app.quiz3StartButton])

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

    # game screen unique App values

    app.player = cl.Player(app.centerx,700)

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
        app.helpButton.buttonPressed(switchMode(app,'helpScreen','#96c9a6','helpScreen'))
        print('Help button pressed!')

    # app.setSize(newWidth, newHeight) NOTE use to change canvas size

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
    app.mood1.drawColourWheel(canvas)

    drawCircle(app,canvas)

    header1 = cl.Word('Hello,')
    header2 = cl.Word('How are you feeling today?')
    header3 = cl.Word('Current Mood:')


    for button in app.quiz1Buttons:
        button.draw(canvas)

    header1.drawWord(canvas,app.centerx-370,100,'K2D 120','grey54') #shadow
    header1.drawWord(canvas,app.centerx-375,100,'K2D 120','white')
    header2.drawWord(canvas,app.centerx-20,200,'K2D 80','grey54') #shadow
    header2.drawWord(canvas,app.centerx-25,200,'K2D 80','white')

    header3.drawWord(canvas,app.centerx+205,370,'K2D 70','grey54')
    header3.drawWord(canvas,app.centerx+200,370,'K2D 70','white')

    # will change when ball is moved
    app.mood.drawWord(canvas,app.centerx+205,510,'K2D 70','gray65')
    app.mood.drawWord(canvas,app.centerx+200,510,'K2D 70','gray99')
    canvas.create_line(app.centerx+85,560,app.centerx+330,
                       560,fill='gray65',width=8, smooth=True)
    canvas.create_line(app.centerx+80,555,app.centerx+325,
                       555,fill='grey99',width=8, smooth=True)

def drawCircle(app, canvas):
    app.circle1.Drag(app.circlex,app.circley)
    app.circle1.draw(canvas)


# NOTE gets stuck if collides with border, try and shift pos or prevent collision
def quizScreenOne_mouseDragged(app,event):
    if app.mood1.inBounds(app.circlex,app.circley):
        if app.circle1.inBounds(event.x,event.y):
            app.circlex,app.circley = event.x, event.y

# NOTE USE DISCTANCE TO CALCULATE location from circumfrence of circle
def quizScreenOne_mouseReleased(app,event):
    if app.mood1.inBounds(event.x,event.y):
        if app.circle1.inBounds(event.x,event.y):
            app.cwCirclePos = (event.x,event.y)
        # USE COORDINATE TO ASSIGN MOOD/COLOUR
        print(app.cwCirclePos)
        

def quizScreenOne_mousePressed(app,event):
    if app.selectMoodButton.inBounds(event.x, event.y): 
        if app.cwCirclePos != (app.centerx-300,550):
            app.selectMoodButton.buttonPressed(switchMode(app,'quizScreenTwo','#d8d4f1','quizScreen2'))
            print('Select Mood button pressed!')
        else:
            print('Please choose your mood')

# NOTE will change mood
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

    header1 = cl.Word('What word best\ndescribes your mood?')
    
    header1.drawWord(canvas,app.centerx,100,'K2D 80','grey44') #shadow
    header1.drawWord(canvas,app.centerx-5,100,'K2D 80','white')

    drawH3(app,canvas)

    box = cl.Box(app.centerx-200, 500, 450, 650, '#8578d3', 10, '#6252c7')
    box.draw(canvas)

    for button in app.quiz2Buttons:
        button.draw(canvas)

def drawH3(app,canvas):
    header3 = cl.Word(f'Chosen Word:\n {app.selectedWord}')
    header3.drawWord(canvas,app.centerx+340,320,'K2D 50','grey44') #shadow
    header3.drawWord(canvas,app.centerx+336,320,'K2D 50','white')

def quizScreenTwo_timerFired(app):

    pass

def chooseWords():
    # choose 6 words from list at random
    pass

def quizScreenTwo_mousePressed(app,event):
    if app.chooseWordButton.inBounds(event.x, event.y):
        app.chooseWordButton.buttonPressed(switchMode(app,'quizScreenThree','#ff8c95','quizScreen3'))
        print('Choose word button pressed!')

    if app.refreshWordButton.inBounds(event.x, event.y):
        app.refreshWordButton.buttonPressed(chooseWords())
        print('Refresh word button pressed!')


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

# Reflexes
##########################################

# NOTE this screen will determine the overall speed of the player and falling word
# will use time.time to calc start and end time through how quickly player can click on
# 5 appearing points of a specfic colour . This time gotten will be the denominator for object
# speeds
# TODO # circles will appear on screen, different colours
# count of correct clicks (need to store and match colour)
# once 5 points obtained, display start button

def quizScreenThree_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.screenColour)

    if app.dotCount < 5:
        header1 = cl.Word(f'Click 5 {app.dotColour.capitalize()} dots!')
        header1.drawWord(canvas,app.centerx,100,'K2D 80','grey44') #shadow
        header1.drawWord(canvas,app.centerx-5,100,'K2D 80','white')

        drawDots(app,canvas)
        
    elif app.dotCount >= 5:
        drawStartButton(app,canvas)

def drawStartButton(app,canvas):
    for button in app.quiz3Buttons:
        button.draw(canvas)

def drawDots(app,canvas):
    pass

def quizScreenThree_mousePressed(app,event):
    if app.quiz3StartButton.inBounds(event.x, event.y):
        app.quiz3StartButton.buttonPressed(switchMode(app,'gameScreen','pink','gameScreen'))
        print('Game start button pressed!')
    else:
        app.dotCount += 1
        print(app.dotCount)

def quizScreenThree_timerFired(app):
    pass

# NOTE WILL REMOVE LATER
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
    dr.drawGround(canvas,0,740,app.width,app.height)

def gameScreen_appStarted(app):
    pass


def gameScreen_keyPressed(app,event):
    if (event.key == "Left"):    app.player.movePlayer(-10, 0)
    elif (event.key == "Right"): app.player.movePlayer(+5, 0)
    elif (event.key == "Up"):    app.player.movePlayer(0, +10)
    elif event.key == 'p':
        app.screenColour = 'grey74'
        app.mode = 'pauseScreen'
        app._title = 'pauseScreen'


    if event.key == 'r':
        app.screenColour = '#ff8c95'
        app.mode = 'quizScreenThree'
        app._title = 'quizScreen3'
    elif event.key == 'n':
        # include different colours based on weither player won or not
        if app.gameOutcome == 'Win':
            app.screenColour = '#eac4bb'
        elif app.gameOutcome == 'Loss':
            app.screenColour = 'cornsilk3'
        else:
            app.screenColour = 'lawn green'
        app.mode = 'endGame'
        app._title = 'endGame'
    



def spawnItem():
    pass
def spawnWord():
    pass


def gameScreen_timerFired(app):
    pass
def gameScreen_mousePressed(app,event):
    pass

runApp(width=1200, height=820, title = 'ZenMode')