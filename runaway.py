#ashikag
#######################################
#######################################

import pygame, random, sys
from pygame.locals import *
#use pygame to run the program and using the local functions from pygame

WINDOWWIDTH = 600
#set the window width and height to a standard 600x600 screen
WINDOWHEIGHT = 600

TEXTCOLOR = (255, 255, 255)
#prints text in black

BACKGROUNDCOLOR = (20, 20, 100)
#sets the backgrgound color to blue

timer = 40
#sets the clock to go at 50 millisecond intervals for the score

#during the villain drops, various sizes of villains are dropped
#ranging from 10 t0 40
villainMINSIZE = 10
villainMAXSIZE = 40

#the speeds that the villains are being dropped at range from 1 to 9
villainMINSPEED = 1
villainMAXSPEED = 9

#these values act as global values later used in the program
ADDNEWvillainRATE = 6

heroMOVERATE = 6
#the hero moves at a rate of 5 via the arrow keys and the aswd combo
#if the mouse is used, the move rate is up to the user


def endGame():
    pygame.quit()
    sys.exit()
    #the end game function allows the python game to quit and exit


def waitForheroToPressKey():
    #after the key is pressed to atart the game
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                endGame()
                # in the case of a force quit, then quit the game via the end game command

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits the program and exits pygame
                    endGame() #calls the end game function to quit
                return

def heroHasHitvillain(heroRect, villains):
    for b in villains:
        #for every villain that is created
        if heroRect.colliderect(b['rect']):
            #pygames colliderect tool tests to see if two rectangles overlap
            #this tests to see when the hero and the villain meet and ends the game
            return True
            #will return true if they do not touch and will continue
            #otherwise, will return false and show a flashscreen of text for how to continue
    return False

def drawText(text, font, surface, x, y):
    #the drawText function helps to create the text that is presented on the flashscreen and score menus
    temp = font.render(text, 1, TEXTCOLOR)
    #color is set to the original TEXTCOLOR as it is stated at the start of the code
    tempRect = temp.get_rect()
    #Returns a new rectangle covering the entire surface. This rectangle 
    #will always start at x, y with a width. and height the same size as the image.
    tempRect.topleft = (x, y)
    #sets the text to the x,y coordinate
    surface.blit(temp, tempRect)
    #pygames blit functions helps to draw one image onto another



# set up pygame, the window, and the mouse cursor
pygame.init()
mainTimer = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Run Away')
pygame.mouse.set_visible(False)

# set up fonts
font = pygame.font.SysFont(None, 45)



# set up images
heroImage = pygame.image.load('hero.png')
heroRect = heroImage.get_rect()
#loads in the immages
villainImage = pygame.image.load('villain.png')

windowSurface.fill(BACKGROUNDCOLOR)
#fills the background of the surface for the window to a blue based on the colors for BACKGROUND above

# show the "Start" screen
drawText(' Run Away', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('By: Ashika Ganesh', font, windowSurface, (WINDOWWIDTH / 3) - 60, (WINDOWHEIGHT / 3) + 50)

#gives a quick splash screen of information to continue the game with
drawText('Press space key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 90, (WINDOWHEIGHT / 3) + 100)
drawText("Use the arrow keys, mouse, or awsd keys", font, windowSurface, (WINDOWWIDTH / 3) - 200, (WINDOWHEIGHT / 3) + 150)
drawText("Continue to run away from the ghosts", font, windowSurface, (WINDOWWIDTH / 3) - 180, (WINDOWHEIGHT / 3) + 200)
drawText("to score points", font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3) + 250)

pygame.display.update()
waitForheroToPressKey()
#call the first function and wait til a key is pressed


topScore = 0
#set the initial score to 0

while True:
    # set up the start of the game
    villains = []
    score = 0
    heroRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    #this places the hero on the middle of the screen to begin with

    moveLeft = moveRight = moveUp = moveDown = False
    #set the keys posisble for the arrows

    reverseCheat = slowCheat = False
    #the reverse and slow cheat are implemented for the programmer to use cheat codes and test for errors
    villainAddCounter = 0
    #this sets up the initial villain count on the screen
    
    while True: # the game loop runs while the game part is playing
        score += 1 # increase score
        #the score increases by 1 constantly as the game continues

        for event in pygame.event.get():
            if event.type == QUIT:
                endGame()
                #if the escape key is pressed, the game will quit and exit pygame

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                    #this programmer hack is used to test for reverseing the motion of the ghosts/villains
                if event.key == ord('x'):
                    slowCheat = True
                    #this programmer hack is used to test for slowing down the motion of the ghosts/villains

                #these events allow for control via the arrow keys and the aswd keys

                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        endGame()
                #this allows the command of escape key to signal a quit

                #the following events move the keys accordingly
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            if event.type == MOUSEMOTION:
                # If the mouse moves, move the hero where the cursor is.
                heroRect.move_ip(event.pos[0] - heroRect.centerx, event.pos[1] - heroRect.centery)
                #this pygame feature lets the user use the mouse and control the hero
                #the hero will thus move at the speed of the mosue rather than the standared
                #speed of the control keys

        # Add new villains at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            #the if/not says that villains are added as long as there is no cheat being used at the moment
            villainAddCounter += 1

        if villainAddCounter == ADDNEWvillainRATE:
            #villains are added into the board are random sizes ranging from 10 to 40
            #the speeds of them are also varied
            villainAddCounter = 0
            #the initial counter is set to 0 to set up the adding counter for villains
            villainSize = random.randint(villainMINSIZE, villainMAXSIZE)
            #the above statement lets the size be selected at random via pygames randint function

            #each new villain is implemented by the following code below
            newvillain = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-villainSize), 0 - villainSize, villainSize, villainSize),
                        'speed': random.randint(villainMINSPEED, villainMAXSPEED),
                        'surface':pygame.transform.scale(villainImage, (villainSize, villainSize)),
                        }

            villains.append(newvillain)
            #this adds the villain into the initial list of villains and continues to fall on the screen

        # Move the hero around.
        #the following commands are with pygames move_ip function which moves the rectangle, in place

        #the up/down/right/left is marked and moved on the board respective to the rate of the hero
        #which is initialized to be 6
        if moveLeft and heroRect.left > 0:
            heroRect.move_ip(-1 * heroMOVERATE, 0)
        if moveRight and heroRect.right < WINDOWWIDTH:
            heroRect.move_ip(heroMOVERATE, 0)
        if moveUp and heroRect.top > 0:
            heroRect.move_ip(0, -1 * heroMOVERATE)
        if moveDown and heroRect.bottom < WINDOWHEIGHT:
            heroRect.move_ip(0, heroMOVERATE)


        # Move the mouse cursor to match the hero.
        # This also re sets the position of the mouse to the position of the hero at the start of the game
        # to allow for no errors and a fair game
        pygame.mouse.set_pos(heroRect.centerx, heroRect.centery)


        # This moves the villains down.
        for b in villains:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
                #the speeds are at random and are moved down in a  vertical fashion
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

         # Delete villains that have fallen past the bottom.
        for b in villains[:]: #checks the entire villains list
            if b['rect'].top > WINDOWHEIGHT:
                villains.remove(b)
                #the villain is removed as soon as it exceeds the bottom of the window height

        # create the game backdrop on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # print the score and top score.
        font1 = pygame.font.SysFont(None, 30)

        drawText('Score: %s' % (score), font1, windowSurface, 410, 0)
        drawText('High Score: %s' % (topScore), font1, windowSurface, 410, 40)

        # create the hero's rectangle
        windowSurface.blit(heroImage, heroRect)


        # create each villain
        for b in villains:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # this will check to see if any of the villains have hit the hero
        if heroHasHitvillain(heroRect, villains):
            if score > topScore:
                topScore = score # set new top score
                #this allows us to keep a running track per game of the top score
                #the new top scores are added each time a new game is created 
                #within a session
            break

        mainTimer.tick(timer)
        #the mainTimer function lets the timer to tick and keep track of the score 

    # Stop the game and show "You Lost!" screen.

    drawText('   You Lost!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press "R" key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 90, (WINDOWHEIGHT / 3) + 50)
    #pressing the key will allow a replay as well as diplaying the old "top score"
    drawText('Press escape to quit.', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3) + 100)
    # if escape is pressed, the game will exit and pygame will quit


    pygame.display.update()
    waitForheroToPressKey()
    #initialize the game and BEGIN!
