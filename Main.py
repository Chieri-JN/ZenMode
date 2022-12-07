#################################################
# Main.py
#
# Your name: Chieri Nnadozi
# Your andrew id: cnnadozi
#################################################
# imports
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
def perfElasticCollision(x1,y1,x2,y2):
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
    app.circlex = app.centerx-300
    app.circley = 550
    
def appStarted(app):
    app.mode = 'startScreen'
    app._title = 'ZenMode'
    # NOTE ORIGINAL #c8eed5
    app.screenColour = "#c8eed5"
    app.timerDelay = 100 
    app.tick = 0

    app.gameStarted = False # stops player from going from help to pause without staring the game
    app.gameOver = False 
    app.gameOutcome = 'None'
    app.riskOfLoss = False
    
    app.centerx = app.width/2
    app.centery = app.height/2
    
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
    app.currMood = 'white'
    app.circlex = app.centerx-300
    app.circley = 550
    app.circle1 = cl.Circle(app.circlex,app.circley, 20,'white',0,'')
    # cx,cy,r, colour,width,outline
    app.circle2 = cl.Circle(app.centerx+200,510,50,app.currMood,6,'grey44')
    app.followMouse = False
    # switch to colour
    app.cwCirclePos = (app.circlex,app.circley)
    app.quiz1Buttons = []
    # buttons
    app.selectMoodButton = cl.Button(app.centerx+200, 650, 80, 150,'#e68800','#ffa11a',5,
                            'white','Select','Krungthep 30')
    app.quiz1Buttons.extend([app.selectMoodButton])

    # quiz2 Screen unique App values    
    app.selectedWord = cl.Word('happy') # Default is happy
    app.selectedColour = 'white'

    # wordbubble values
    app.wbx = app.centerx - 469
    app.wby = 335
    app.wbr = 40
    app.wbw = 7
    app.wbo = 'grey25'
    app.wbcolour = random.choices(col.pastelColoursTwoList,k=6)

    app.dx = 2.4
    app.dy = 3.3

    app.wordBubbleList = []
    for word in dict.dictonaryMood:
        wordbubble = cl.WordBubble(word)
        app.wordBubbleList.append(wordbubble)
    app.selectedWBList = random.choices(app.wordBubbleList,k=6)

    for wb in app.selectedWBList:
        wb.cx = app.wbx
        wb.cy = app.wby
    # buttons
    app.quiz2Buttons = []
    app.chooseWordButton = cl.Button(app.centerx+340, 500, 80, 150,'#a89fe0','#cbc5ec',5,
                            'white','Choose','Krungthep 30')
    app.refreshWordButton = cl.Button(app.centerx+340, 650, 80, 150,'#a89fe0','#cbc5ec',5,
                            'white','Refresh','Krungthep 30')
    app.quiz2Buttons.extend([app.chooseWordButton,app.refreshWordButton])

    # quiz3 Screen unique App values
    app.dotColour = random.choice(col.coloursTwoList)
    app.dotCount = 5 # default is 0
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

    # gamescreen unique App values
    # world boundries
    app.ground = 720 
    app.WorldWidthLeft =  -400
    app.WorldWidthRight = app.width + 400
    app.PcurrDistfromWR = app.width
    app.PcurrDistfromWL = 0
    app.WorldMargine = 50
    app.worldShift = 0

    # Player
    app.pColour = "red"
    app.px,app.py = app.centerx, app.ground
    app.pxB = app.px
    app.player = cl.Player(app,app.px,app.py)
    app.spriteCounter = 0 
    app.spriteState = 'idle'
    app.prevIdle = 'idle'

    app.jumpState = False
    app.jumpCounter = 0
    app.JumpComp = 0
   
   # Tree
    app.tree = cl.Tree(app.currMood)
    app.treeAngle = 90
    app.treeDepth = 0
    app.treeHeight = 10
    app.maxTreeHeight = 200
    app.maxDepth = 7

    # game play 
    app.playerTime = 1
    app.fastestTime = 1
    app.checkCount = 0
    app.speedScaling = app.fastestTime / app.playerTime
    app.fallSpeed = +10.8 * app.speedScaling 
    app.pM = 10
    app.wordM = 10
    app.drawWordType = True
    app.decounter = 0
    app.Points = 0
    app.CounterPoints = 0
    app.Score = 0 

    # word bubbles
    app.gameWordBubbleList  = []
    app.Synonymes = app.selectedWord.getSynonymes()
    app.Antonymes = app.selectedWord.getAntonymes()
    app.WordCheck = True
    app.gameWBr = 50
    app.list = list(app.Synonymes)
    app.WBshift = 0
    

    # for wb in app.gameWordBubbleList:
    #     wb.cy = 0
    #     wb.cx = random.randrange(app.WorldWidthLeft + app.WorldMargine,app.WorldWidthRight - app.WorldMargine)
    # random.randrange(app.WorldWidthLeft+20,app.WorldWidthRight-20)
    # NOTE change to a little over the width of world bubbles
    # NOTE TEMPORY VARIABLE
    app.wordPos = random.randrange(app.WorldWidthLeft+20,app.WorldWidthRight-20)

##########################################
# Start Screen
##########################################

def startScreen_redrawAll(app,canvas):
    bgColourChange(app)
    canvas.create_rectangle(0,0,app.width,app.height,fill=bgColourChange(app))
    title1 = cl.Word('Zen')
    title2 = cl.Word('Mode')    

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

def startScreen_mousePressed(app,event):
    if app.startButton.inBounds(event.x, event.y):
        app.startButton.buttonPressed(switchMode(app,'quizScreenOne','#ffbe60','quizScreen1'))
        print('Start button pressed!')

    if app.helpButton.inBounds(event.x, event.y):
        app.helpButton.buttonPressed(switchMode(app,'helpScreen','#96c9a6','helpScreen'))
        print('Help button pressed!')

def bgColourChange(app):
    # NOTE Switch to Dictionary 
    return col.pastelColoursList[app.tick%len(col.pastelColoursList)]

def startScreen_timerFired(app):
    #moveBall(app):
    app.tick +=1 

# NOTE Have balls, randomly generated and drifting across screen, slightly light/
# darker than actually bg colour() in sinusoidal pattern
# OR have bg be paler shade(pastel) of circle colour  

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
    header2 = cl.Word('What colour are you feeling today?')
    header3 = cl.Word('Current Mood:')

    for button in app.quiz1Buttons:
        button.draw(canvas)

    header1.drawWord(canvas,app.centerx-370,100,'K2D 120','grey54') #shadow
    header1.drawWord(canvas,app.centerx-375,100,'K2D 120','white')
    header2.drawWord(canvas,app.centerx-12,200,'K2D 65','grey54') #shadow
    header2.drawWord(canvas,app.centerx-17,200,'K2D 65','white')

    header3.drawWord(canvas,app.centerx+205,370,'K2D 70','grey54')
    header3.drawWord(canvas,app.centerx+200,370,'K2D 70','white')

    # will change when ball is moved
    drawMood(app,canvas)
    # canvas.create_line(app.centerx+85,560, app.centerx+330,560, app.centerx+330,
    #                    500, app.centerx+85,500, app.centerx+85,560, 
    #                    fill='gray65',width=8)
def drawCircle(app, canvas):
    app.circle1.Drag(app.circlex,app.circley)
    app.circle1.draw(canvas)

def drawMood(app,canvas):
    app.circle2.draw(canvas)

# NOTE gets stuck if collides with border, try and shift pos or prevent collision # if not equal to zero set to zero
def quizScreenOne_mouseDragged(app,event):
    if app.mood1.inBounds(app.circlex,app.circley):
    #     if app.circle1.inBounds(event.x,event.y):
        if app.followMouse == True:
            app.circlex,app.circley = event.x, event.y
    # elif not app.mood1.inBound

def quizScreenOne_mouseReleased(app,event):
    if app.mood1.inBounds(event.x,event.y):
        # if app.circle1.inBounds(event.x,event.y):
        app.followMouse = False
        app.cwCirclePos = (app.circlex,app.circley)
        app.currMood = app.mood1.getColour(app.circlex,app.circley)
        app.circle2.colour = app.mood1.getColour(app.circlex,app.circley)
        
def quizScreenOne_mousePressed(app,event):
    if app.selectMoodButton.inBounds(event.x, event.y): 
        if app.cwCirclePos != (app.centerx-300,550):
            app.selectMoodButton.buttonPressed(switchMode(app,'quizScreenTwo','#d8d4f1','quizScreen2'))
            print('Select Mood button pressed!')
        else:
            print('Please choose your mood')
    if app.circle1.inBounds(event.x,event.y):
        app.followMouse = True

# NOTE USED TO move across screens, will remove later
def quizScreenOne_keyPressed(app,event):
    # Shortcut commands
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

    redrawWords(app,canvas)
    
    for button in app.quiz2Buttons:
        button.draw(canvas)

def drawH3(app,canvas):
    header3 = cl.Word(f'Chosen Word:')
    header4 = cl.Word(f'{app.selectedWord.getWord()}')
    header3.drawWord(canvas,app.centerx+340,300,'K2D 50','grey44') #shadow
    header3.drawWord(canvas,app.centerx+336,300,'K2D 50','white')
    header4.drawWord(canvas,app.centerx+340,360,'K2D 50','grey44') #shadow
    header4.drawWord(canvas,app.centerx+336,360,'K2D 50',app.selectedColour)
    
def redrawWords(app,canvas):
    for i in range(len(app.selectedWBList)):# app.wordBubbleList: 
        wb = app.selectedWBList[i]
        if len(app.selectedWBList[i].getWord()) > 8: 
            app.selectedWBList[i].draw(canvas,('Baloo Bhaijaan','12'),app.wbx + 108*i, app.wby + 65*i, 
                                     app.wbr, app.wbcolour[i],app.wbw, app.wbo)
        else:
            app.selectedWBList[i].draw(canvas,('Baloo Bhaijaan','15'),app.wbx+ 108*i, app.wby + 65*i, 
                            app.wbr, app.wbcolour[i],app.wbw, app.wbo)

def refreshWords(app):
    app.selectedWBList = random.choices(app.wordBubbleList,k=6)
    app.selectedWBList = list(app.selectedWBList)
    app.wbcolour = random.choices(col.pastelColoursTwoList,k=6)

def quizScreenTwo_timerFired(app):
    # for wb in app.selectedWBList:
    #     #wb.setSpeed(app.dx,app.dy)
    #     wb.Move(app.dx,app.dy)
    #     if wb.cx - wb.r < app.centerx-525 or wb.cx + wb.r > app.centerx + 125:
    #         # wb.setSpeed(-wb.speedx,)
    #         wb.speedx = -wb.speedx
    #     if wb.cy - wb.r < 275 or wb.cy + wb.r > 725:
    #         wb.speedy = -wb.speedy

    # for wb in app.selectedWBList:
    #     for wb2 in app.selectedWBList:
    #         # check check check wb2.cx+wb.r
    #         if wb != wb and wb.inBounds(wb2.cx,wb2.cy):
    #             wb.collision(wb2)
    pass

def quizScreenTwo_mousePressed(app,event):
    if app.chooseWordButton.inBounds(event.x, event.y):
        if app.selectedWord.getWord != 'None':
            app.chooseWordButton.buttonPressed(switchMode(app,'quizScreenThree','#ff8c95','quizScreen3'))
            print('Choose word button pressed!')
        else:
            print('Please select a word')

    if app.refreshWordButton.inBounds(event.x, event.y):
        app.refreshWordButton.buttonPressed(refreshWords(app))
        print('Refresh word button pressed!')

    for wb in app.selectedWBList:
        if wb.inBounds(event.x,event.y):
            app.selectedWord.setWord(wb.getWord())
            app.selectedColour = wb.getColour()
    

def quizScreenTwo_keyPressed(app,event):
    # Shortcut commands
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
# incomplete screen
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

# calculates time betweent the apperance 

def drawDots(app,canvas):
    for dot in app.dots: 
        dot.draw()
    pass

def quizScreenThree_mousePressed(app,event):
    if app.quiz3StartButton.inBounds(event.x, event.y):
        app.quiz3StartButton.buttonPressed(switchMode(app,'gameScreen','#c8e5ee','gameScreen'))
        print('Game start button pressed!')
    else:
        app.dotCount += 1
        print(app.dotCount)
    for dot in app.dots:
        if dot.inBounds(event.x,event.y):
            if dot.getColour == app.dotColour:
                app.dotCount += 1
            else:
                if app.dotCount > 0: 
                    app.dotCount -=1

def drawNewDot(app):
    newDot = cl.Dot()
    app.dots.append(newDot)
    if newDot.getColour == app.dotColour:
        app.checkCount +=1
    pass

def quizScreenThree_timerFired(app):
    app.tick += 1
    if app.dotCount < 5:
        if app.tick % 10 == 0:
            drawNewDot(app)
    if app.dotCount >= 1 and app.dotCount < 5:
        app.playerTime += 1
    if app.checkCount < 5:
        app.fastestTime += 1
        # get players time and divide this by that


def quizScreenThree_keyPressed(app,event):
    # Shortcut commands
    if event.key == 'Left':
        app.screenColour = '#d8d4f1'
        app.mode = 'quizScreenTwo'
        app._title = 'quizScreen2'
    elif event.key == 'Right':
        app.screenColour = '#c8e5ee'
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
        app.screenColour = '#c8e5ee'
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
        app.startButton.buttonPressed(switchMode(app,'gameScreen','#c8e5ee','gameScreen'))
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
        app.screenColour = '#c8e5ee' 
        app.mode = 'gameScreen'
        app._title = 'gameScreen'
        app.Points = 0
        app.CounterPoints = 0
        app.Score = 0
        app.gameOver == False

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
def gameScreen_appStarted(app):
    app.timerDelay = 100
    pass

def gameScreen_redrawAll(app,canvas):
    drawBackground(app,canvas)
    drawTree(app,canvas,app.treeDepth)
    drawWorld(app,canvas)
    drawPlayer(app,canvas)
    if app.drawWordType: 
        drawWordType(app,canvas)
    drawScore(app,canvas)
    drawWords(app,canvas)

def drawScore(app,canvas):
    header1 = cl.Word(f'Score: {app.Score}')
    header1.drawWord(canvas,145,50,'K2D 60','grey45') #shadow
    header1.drawWord(canvas,140,50,'K2D 60',app.selectedColour)
    pass

def drawWordType(app,canvas):
    if app.selectedWord.checkType() == 'Negative':
        type = 'Antonymes'
    elif app.selectedWord.checkType() == 'Positive':
        type = 'Synonymes'
    else:
        type = 'Nothing'
    header1 = cl.Word(f'Goal: Collect {type} for {app.selectedWord.getWord()}!')
    header1.drawWord(canvas,app.centerx,150,'K2D 60','grey45') #shadow
    header1.drawWord(canvas,app.centerx-5,150,'K2D 60',app.selectedColour)
    
def drawPlayer(app,canvas):
    app.player.drawPlayer(canvas,app.spriteState,app.spriteCounter)

def drawTree(app,canvas,depth):
    # note there is a max recursion error at depth 7
    app.tree.leafColour =  app.currMood
    app.tree.drawBranch(canvas,app.treeDepth,app.centerx,app.ground,app.treeHeight,app.treeAngle)

def drawBackground(app,canvas):
    # Add clouds
    canvas.create_rectangle(app.WorldWidthLeft+app.worldShift ,0, app.WorldWidthRight+app.worldShift
                            ,app.height, fill=app.screenColour)

def drawWorld(app,canvas):
    dr.drawGround(canvas,app.WorldWidthLeft+app.worldShift,app.ground,
                  app.WorldWidthRight+app.worldShift, app.height)

def drawWords(app,canvas):
    #  draw(self,canvas,font,cx,cy,r,colour,width,outline)
    for wb in  app.gameWordBubbleList:
        wb.draw(canvas,('Baloo Bhaijaan','16'),wb.cx + app.WBshift,wb.cy,app.gameWBr,wb.colour,10,'grey40')

def gameScreen_keyPressed(app,event):
    # LEFT Key commands
    if (event.key == "Left"):    
        if app.PcurrDistfromWL >= app.WorldWidthLeft:
            app.spriteState = 'left'
            app.spriteCounter = (1 + app.spriteCounter) % 7 
            app.player.movePlayer(-10,0)
            app.PcurrDistfromWR -= 10
            app.PcurrDistfromWL -= 10
            # gameScreen_timerFired(app)
        else:
            if app.worldShift + app.WorldWidthLeft < 0:
                app.worldShift +=10
                app.spriteState = 'left'
                app.spriteCounter = (1 + app.spriteCounter) % 7
                app.WBshift += 5
            else: # should allow player to collide with window edge
                if app.px >= app.pxB-120:
                    app.player.movePlayer(-10,0)
                    app.px -= 10
                    app.spriteState = 'left'
                    app.spriteCounter = (1 + app.spriteCounter) % 7

    # RIGHT Key commands      
    elif (event.key == "Right"): 
        if app.PcurrDistfromWR <= app.WorldWidthRight:
            app.spriteState = 'right'
            app.spriteCounter = (1 + app.spriteCounter) % 7 # change later
            app.player.movePlayer(10,0)
            app.PcurrDistfromWR += 10
            app.PcurrDistfromWL += 10
        else:
            if app.WorldWidthRight + app.worldShift > app.width:
                app.worldShift -=10
                app.spriteState = 'right'
                app.spriteCounter = (1 + app.spriteCounter) % 7
                app.WBshift -= 5
            else:
                if app.px <= app.pxB+100:
                    app.player.movePlayer(10,0)
                    app.px += 10
                    app.spriteState = 'right'
                    app.spriteCounter = (1 + app.spriteCounter) % 7
        
    elif (event.key == "Space"):    
        app.spriteState = 'jump'
        app.spriteCounter = 1 # change later
    elif event.key == 'p':
        app.screenColour = 'grey74'
        app.mode = 'pauseScreen'
        app._title = 'pauseScreen'

    # Shortcut commands
    if event.key == 'r':
        app.screenColour = '#ff8c95'
        app.mode = 'quizScreenThree'
        app._title = 'quizScreen3'
    elif event.key == 'n':
        if app.gameOutcome == 'Win':
            app.screenColour = '#eac4bb'
        elif app.gameOutcome == 'Loss':
            app.screenColour = 'cornsilk3'
        else:
            app.screenColour = 'lawn green'
        app.mode = 'endGame'
        app._title = 'endGame' 
    elif event.key == 'Up':
        # NOTE MAX DEPTH IS 8
        if app.treeDepth <= 7:
            app.Points +=1
            app.Score += 1
    elif event.key == 'Down':
        if app.treeDepth > 0:
            app.treeDepth -=1
    elif not event.key:
        gameScreen_timerFired(app)
    
def gameScreen_keyReleased(app,event):
    if event.key == 'Space':
        app.jumpState = True
        gameScreen_timerFired(app) # app.?
        # app.player.movePlayer(0,-40)
        # app.py -=40
        app.spriteState == 'jump'
    elif event.key == 'Right':
        app.spriteState = 'idle'
        app.prevIdle = 'idle'
        app.WBshift = 0
    elif event.key == 'Left':
        app.spriteState = 'idleL'
        app.prevIdle = 'idleL'
        app.WBshift = 0
    elif not event.key:
        gameScreen_timerFired() # app.?

def gameScreen_timerFired(app):
    app.tick += 1
    # Game State Conditions
    if app.Score >= 1:
        app.riskOfLoss = True

    if app.riskOfLoss:
        if app.Score == 0:
            app.gameOver = True 
            app.gameOutcome = 'Loss'
    if app.Score >= 14:
        app.gameOver = True 
        app.gameOutcome = 'Win'
    elif app.Score < 0:
        app.gameOver = True 
        app.gameOutcome = 'Loss'

    if app.gameOver == True:
        app.mode = 'endGame'
        app._title = 'endGame'
    if app.tick >= 50: 
        app.drawWordType = False

    # have app.treeDepth tick away in decimals or have counter
    # difficulty scaling will be how quickly the shrink rate is so how quickly will
    # the tree depth decrease
    # Point State Conditions: 
    if app.gameOver == False:
        if app.Points % 2 == 0 and app.Points != 0: 
            app.Points = 0
            app.treeDepth += 1

        if app.CounterPoints % 2 == 0 and app.CounterPoints != 0:
            app.CounterPoints = 0
            app.treeDepth -= 1
        # Tree State Conditions
        app.decounter = app.treeDepth -  0.05*(app.tick%20) * (app.speedScaling*0.6)
        if app.treeDepth > 0:
            if abs(app.treeDepth - app.decounter) == 1-0.5*(app.speedScaling*0.6):
                app.treeDepth -= 1
                app.Score -= 3
        if app.treeHeight <= app.treeDepth*(app.maxTreeHeight/app.maxDepth):
            app.treeHeight += 1
        elif app.treeHeight > app.treeDepth*(app.maxTreeHeight/app.maxDepth):
            app.treeHeight -= 1

        # Player State Conditions
        if app.spriteState == 'idle':
                app.spriteCounter = (1 + app.spriteCounter) % 2
        elif app.spriteState == 'idleL':
                app.spriteCounter = (1 + app.spriteCounter) % 2
        # if app.jumpState=='False':
        #     if app.spriteState == 'idle':
        #         app.spriteCounter = (1 + app.spriteCounter) % 2
        #     elif app.spriteState == 'idleL':
        #             app.spriteCounter = (1 + app.spriteCounter) % 2
        if app.jumpState:
            app.spriteCounter = (1 + app.spriteCounter) % 11
            app.jumpCounter += 1
            app.JumpComp = 50
            if app.jumpCounter == 10:
                app.jumpCounter = 0
                app.spriteCounter = 0
                app.spriteState = app.prevIdle 
                app.jumpState = False
                app.JumpComp = 0

        # WordBubble State Conditions
        if app.tick % 20 == 0:
            spawnWord(app)
        for wb in app.gameWordBubbleList:
            wb.Move(0,app.fallSpeed)
            if wb.inBounds(wb.cx,app.ground):
                app.gameWordBubbleList.remove(wb)
            if wb.inBounds(app.player.px,app.ground-40):
                # if type == 'Synonymes':
                if app.selectedWord.checkType() == 'Negative':
                    if wb.getWord() in app.selectedWord.getAntonymes():
                        app.Score += 1
                        app.Points += 1
                        if wb in app.gameWordBubbleList:
                            app.gameWordBubbleList.remove(wb)
                    else:
                        app.Score -= 1
                        app.CounterPoints += 1
                        if wb in app.gameWordBubbleList:
                            app.gameWordBubbleList.remove(wb)
                elif app.selectedWord.checkType() == 'Positive':
                    if wb.getWord() in app.selectedWord.getSynonymes():
                        app.Score += 1
                        app.Points += 1
                        if wb in app.gameWordBubbleList:
                            app.gameWordBubbleList.remove(wb)
                    else:
                        app.Score -= 1
                        app.CounterPoints += 1
                        if wb in app.gameWordBubbleList:
                            app.gameWordBubbleList.remove(wb)

def spawnWord(app):
    if app.WordCheck == True:
        app.list = list(app.Antonymes)
        app.WordCheck = False
    else:
        app.list = list(app.Synonymes)
        app.WordCheck = True
    newWB = cl.WordBubble(random.choice(app.list))
    newWB.cy = 0
    newWB.colour = random.choice(col.pastelColoursTwoList)
    newWB.cx = random.randrange(app.WorldWidthLeft + app.WorldMargine,app.WorldWidthRight - app.WorldMargine)
    app.gameWordBubbleList.append(newWB)

def gameScreen_mousePressed(app,event):
    pass

runApp(width=1200, height=820, title = 'ZenMode')