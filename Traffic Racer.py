#########################################
# File Name: Traffic Racer.py
# Description: This program is a Traffic Racer inspired game that incorporates racing and speeding past other cars on a highway
# Author: Marcus Ng
# Date: 2022/10/23
#########################################

import pygame
import random
pygame.init()

#initialized bool variables used for game section loops
repeatGame = True #game will repeat if True
startingMenu = True #starting menu will show if True
creditsMenu = False #credits menu won't show if False
startStartingSequence = False #starting sequence (countdown) won't show if False
gameRunning = False #actual game won't run if False
endMenu = False #end menu won't show if false

#length and width of screen 
length = 1008
width = 780

#variables used to make the screen turn a certain colour for a specific period of time (ex. 2s)
currentTime = 0
futureTime = 0

#initialized values for calculating score
score = 0
loopCounter = 0

#initialized bool values used to track player keybind controls
leftKeyPressed = False
rightKeyPressed = False
upKeyPressed = False
downKeyPressed = False

#initialized values used for the car that the player controls
playerCarImage1 = pygame.image.load("Player Car Image.png")
playerCarImage1Y = 400
playerCarImage1X = 220

#initialized values used for the random npc cars that spawn on the road
carImage1 = pygame.image.load("Car Image 1.png")
carImage2 = pygame.image.load("Car Image 2.png")
carImage3 = pygame.image.load("Car Image 3.png")
carImage1Y, carImage1Height = -780, 780
carImage2Y, carImage2Height = -780, 780
carImage3Y = -780
carImage4Y = -780
carImageShown = carImage1

#initialized random numbers below
randNumber = 1
secondRandNumber = 0
thirdRandNumber = 0
fourthRandNumber = 0
randNumberForCarPicture = random.randrange(1, 4)
secondrandNumberForCarPicture = 0
thirdrandNumberForCarPicture = 0
fourthrandNumberForCarPicture = 0

carScrollingSpeed = 4 #speed that the npc cars will drive at

#initialized values used for the scrolling background
defaultHighwayBackground1 = pygame.image.load("Default Highway Background.png")
defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground1Height = 0, 0, 780
defaultHighwayBackground2 = pygame.image.load("Default Highway Background.png") #for scrolling purposes
defaultHighwayBackground2X, defaultHighwayBackground2Y, defaultHighwayBackground2Height = 0, -780, 780
scrollingSpeed = 5 #speed at which the screen scrolls (also the speed at which the player's car starts at before speeding up)

font = pygame.font.Font(("Pricedown Font.otf"), 70) #font used for game
window = pygame.display.set_mode((length, width)) #sets window dimensions
gameOverScreen = pygame.image.load("Game Over.png") #game over screen
clock = pygame.time.Clock() #clock used for fps

#below are the music and sound FX used in game 
pygame.mixer.music.load('Traffic Racer Theme Song.wav') #background music for game
pygame.mixer.music.set_volume(0.4) #sets volume of music
pygame.mixer.music.play(-1) #loops the music
explosionFX = pygame.mixer.Sound('Explosion FX.wav') #sound played when player crashes
explosionFX.set_volume(1.5)

#initialized hitboxes for cars below
carImageShownRectangle1 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle2 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle3 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle4 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle5 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle6 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle7 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle8 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle9 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle10 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle11 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle12 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle13 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle14 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle15 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
carImageShownRectangle16 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)

#########################################
# The startingMenuFunc() function shows the starting menu
# Args: buttonType (used to return the type of button that was pressed)
# Returns: "playButtonType" or "creditsButtonType" (It's a type of button that can be pressed by player)
#########################################

def startingMenuFunc(buttonType):
    window.blit(font.render('Traffic Racer', False, (255, 255, 255)), (285, 75)) #creates the title for the main menu
    playButton = pygame.draw.rect(window, (255, 255, 255), (360, 250, 290, 150), 5) #creates an area for the player to press the button
    window.blit(font.render('Play', False, (255, 255, 255)), (435, 275)) #creates the play button for the main menu
    creditsButton = pygame.draw.rect(window, (255, 255, 255), (360, 450, 290, 150), 5) #creates an area for the player to press the button
    window.blit(font.render('Credits', False, (255, 255, 255)), (390, 480)) #creates the credits button for the main menu
    window.blit(font.render('ESC to Quit', False, (255, 255, 255)), (335, 640)) #prints information on how to quit game onto player's screen
    if buttonType == "playButtonType":
        return playButton
    elif buttonType == "creditsButtonType":
        return creditsButton

#########################################
# The startingSequence() function shows the countdown from 3, 2, 1, GO
# Args: startingMenu, repeatGame (if the player decides to quit the game during the countdown, these 2 booleans will return False back to the main program, which will quit the game)
# Returns: startingMenu, repeatGame (if the player decides to quit the game during the countdown, these 2 booleans will return False back to the main program, which will quit the game)
#########################################

def startingSequence(startingMenu, repeatGame):
    window.fill((0, 0, 0))
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    startingTimerCounter = 3
    runTimerLoop = True
    while runTimerLoop:
        for event in pygame.event.get(): #loops through all pygame events
            keyPressDetection = pygame.key.get_pressed() #function used to detect whether a key was pressed or not
            if event.type == pygame.QUIT or keyPressDetection[pygame.K_ESCAPE]: #if the python window is exited or ESC is pressed, exit the program
                startingMenu, repeatGame = False, False 
                return startingMenu, repeatGame
            if event.type == pygame.USEREVENT:
                startingTimerCounter -= 1
        if startingTimerCounter >= 1:
            window.blit(defaultHighwayBackground1, (0, 0))
            window.blit(font.render(str(startingTimerCounter), False, (255, 255, 255)), (485, 390))
            pygame.display.flip()
        elif startingTimerCounter == 0:
            window.blit(defaultHighwayBackground1, (0, 0))
            window.blit(font.render("GO", False, (255, 255, 255)), (470, 390))
            pygame.display.flip()
        elif startingTimerCounter == -1:
            window.blit(defaultHighwayBackground1, (0, 0))
            pygame.display.flip()
            runTimerLoop = False
        clock.tick(30)

#########################################
# The showCredits() function shows the credits menu
# Args: buttonType (used to return the type of button that was pressed)
# Returns: "backButton" (It's a type of button that can be pressed by player)
#########################################

def showCredits(buttonType):
    window.blit(defaultHighwayBackground1, (0, 0))
    window.blit(font.render('Credits', False, (255, 255, 255)), (380, 60)) #creates the title for the credits menu
    window.blit(font.render('Creator - Marcus Ng', False, (255, 255, 255)), (200, 300)) #shows marcus's name in credits menu
    window.blit(font.render('Back', False, (255, 255, 255)), (430, 550)) #creates the back button for the credits menu
    backButton = pygame.draw.rect(window, (255, 255, 255), (350, 545, 300, 100), 5)
    if buttonType == "backButton":
        return backButton #returns type of button pressed to main program
    pygame.display.flip()

#########################################
# The endMenuFunc() function shows the end menu
# Args: buttonType (It's a type of button that can be pressed by player), score (score of the player)
# Returns: "playAgainButtonType", "creditsButtonType" (It's a type of button that can be pressed by player)
#########################################

def endMenuFunc(buttonType, score):
    window.blit(font.render('Final Score: '+str(int(score)), False, (255, 255, 255)), (270, 75)) #creates the title for the main menu
    playAgainButton = pygame.draw.rect(window, (255, 255, 255), (300, 250, 400, 150), 5) #creates an area for the player to press the button
    window.blit(font.render('Play Again', False, (255, 255, 255)), (350, 275)) #creates the play button for the main menu
    creditsButton = pygame.draw.rect(window, (255, 255, 255), (300, 450, 400, 150), 5) #creates an area for the player to press the button
    window.blit(font.render('Credits', False, (255, 255, 255)), (380, 480)) #creates the credits button for the main menu
    window.blit(font.render('ESC to Quit', False, (255, 255, 255)), (335, 640)) #prints information on how to quit game onto player's screen
    if buttonType == "playAgainButtonType":
        return playAgainButton
    elif buttonType == "creditsButtonType":
        return creditsButton
    pygame.display.flip()

#########################################
# The movingBackgroundFunc() function is quintessentially the most important part of the program and is why the program functions. it is the working mechanism behind the moving background and moving cars
# Args: defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16
# Returns: defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16
#########################################

def movingBackgroundFunc(defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16):
    #block of code below essentially just moves 2 of the same picture on top of each other back and forth which creates an infinite scrolling effect
    window.blit(defaultHighwayBackground1, (defaultHighwayBackground1X, defaultHighwayBackground1Y)) #blits the first road picture onto the screen
    window.blit(defaultHighwayBackground2, (defaultHighwayBackground2X, defaultHighwayBackground2Y)) #blits the second road picture onto the screen
    defaultHighwayBackground1Y = defaultHighwayBackground1Y + scrollingSpeed #scrolls the first road picture down, keeping the screen scrolling speed in mind
    if defaultHighwayBackground1Y + scrollingSpeed > defaultHighwayBackground1Height: #if the first picture is not visible anymore, put it under the second picture
        defaultHighwayBackground1Y = -defaultHighwayBackground2Height #puts the first picture under the second picture
    defaultHighwayBackground2Y = defaultHighwayBackground2Y + scrollingSpeed #scrolls the second road picture down, keeping the screen scrolling speed in mind
    if defaultHighwayBackground2Y + scrollingSpeed > defaultHighwayBackground2Height: #if the second picture is not visible anymore, put it under the first picture
        defaultHighwayBackground2Y = -defaultHighwayBackground1Height #puts the second picture under the first picture
    
    #block of code below is responsible for the random spawning and movement of the npc cars on the screen.
    #NOTE: comments will be sparse since most of it is repetitive
    #this first block of code is responsible for cars specific to the first lane on the left
    if randNumber == 1: #first random number is initialized as 1 at the top of the program
        if randNumberForCarPicture == 1: #first random number for car picture is also initialized at top of program 
            carImageShown = carImage1 #sets the random car image to the car image 1
        elif randNumberForCarPicture == 2: #repeat of first if condition
            carImageShown = carImage2
        elif randNumberForCarPicture == 3: #repeat of first if condition
            carImageShown = carImage3
        window.blit(carImageShown,(220, carImage1Y)) #blits the car image in the first lane onto the screen
        carImageShownRectangle1 = carImageShown.get_rect(topleft = (220, carImage1Y)) #sets the hitbox for the car
        carImage1Y = carImage1Y + carScrollingSpeed #scrolls the car on the screen at a specific speed 
        if carImage1Y + carScrollingSpeed >= carImage1Height: #if the car isn't visible anymore, put it under the second car picture
            carImage1Y = -carImage2Height #puts the car picture under the second car picture
        if carImage1Y == -780: #if the first car's Y position is at -780, spawn another car
            randNumber = random.randrange(1,5) #picks a random number which decides which car should spawn in which lane (randomly)
            randNumberForCarPicture = random.randrange(1, 4) #picks a random number which decides what picture the car should be
        if carImage1Y == -392: #if the first car's Y position is at -392, spawn another car
            secondRandNumber = random.randrange(1,5) #picks a random number which decides where the second car will spawn
            secondrandNumberForCarPicture = random.randrange(1, 4) #picks a random number which decides what picture the car should be
        if carImage1Y == 0: #if the first car's Y position is at 0, spawn another car
            thirdRandNumber = random.randrange(1,5) #picks a random number which decides where the third car will spawn
            thirdrandNumberForCarPicture = random.randrange(1, 4) #picks a random number which decides what picture the car should be
        if carImage1Y == 392: #if the first car's Y position is at 392, spawn another car
            fourthRandNumber = random.randrange(1,5) #picks a random number which decides where the fourth car will spawn
            fourthrandNumberForCarPicture = random.randrange(1, 4) #picks a random number which decides what picture the car should be
    #the following 3 blocks of code are basically the same as the block of code above except with different variables
    elif randNumber == 2:
        if randNumberForCarPicture == 1:
            carImageShown = carImage1
        elif randNumberForCarPicture == 2:
            carImageShown = carImage2
        elif randNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(380, carImage1Y))
        carImageShownRectangle2 = carImageShown.get_rect(topleft = (380, carImage1Y))
        carImage1Y = carImage1Y + carScrollingSpeed
        if carImage1Y + carScrollingSpeed >= carImage1Height:
            carImage1Y = -carImage2Height
        if carImage1Y == -780:
            randNumber = random.randrange(1,5)
            randNumberForCarPicture = random.randrange(1, 4)
        if carImage1Y == -392:
            secondRandNumber = random.randrange(1,5)
            secondrandNumberForCarPicture = random.randrange(1, 4)
        if carImage1Y == 0:
            thirdRandNumber = random.randrange(1,5)
            thirdrandNumberForCarPicture = random.randrange(1, 4)
        if carImage1Y == 392:
            fourthRandNumber = random.randrange(1,5)
            fourthrandNumberForCarPicture = random.randrange(1, 4)

    elif randNumber == 3:
        if randNumberForCarPicture == 1:
            carImageShown = carImage1
        elif randNumberForCarPicture == 2:
            carImageShown = carImage2
        elif randNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(530, carImage1Y))
        carImageShownRectangle3 = carImageShown.get_rect(topleft = (530, carImage1Y))
        carImage1Y = carImage1Y + carScrollingSpeed
        if carImage1Y + carScrollingSpeed >= carImage1Height:
            carImage1Y = -carImage2Height
        if carImage1Y == -780:
            randNumber = random.randrange(1,5)
            randNumberForCarPicture = random.randrange(1, 4)
        if carImage1Y == -392:
            secondRandNumber = random.randrange(1,5)
            secondrandNumberForCarPicture = random.randrange(1, 4)
        if carImage1Y == 0:
            thirdRandNumber = random.randrange(1,5)
            thirdrandNumberForCarPicture = random.randrange(1, 4)
        if carImage1Y == 392:
            fourthRandNumber = random.randrange(1,5)
            fourthrandNumberForCarPicture = random.randrange(1, 4)

    elif randNumber == 4:
        if randNumberForCarPicture == 1:
            carImageShown = carImage1
        elif randNumberForCarPicture == 2:
            carImageShown = carImage2
        elif randNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(690, carImage1Y))
        carImageShownRectangle4 = carImageShown.get_rect(topleft = (690, carImage1Y))
        carImage1Y = carImage1Y + carScrollingSpeed
        if carImage1Y + carScrollingSpeed >= carImage1Height:
            carImage1Y = -carImage2Height
        if carImage1Y == -780:
            randNumber = random.randrange(1,5)
            randNumberForCarPicture = random.randrange(1, 4)
        if carImage1Y == -392:
            secondRandNumber = random.randrange(1,5)
            secondrandNumberForCarPicture = random.randrange(1, 4)
        if carImage1Y == 0:
            thirdRandNumber = random.randrange(1,5)
            thirdrandNumberForCarPicture = random.randrange(1, 4)
        if carImage1Y == 392:
            fourthRandNumber = random.randrange(1,5)
            fourthrandNumberForCarPicture = random.randrange(1, 4)

    #The next 3 blocks of code that starts with secondRandNumber, thirdRandNumber, and fourthRandNumber, are ALL repetitions of the block of code above
    #except that each block of code is specific to each lane. For example secondRandNumber block is responsible for the second lane from the left
    if secondRandNumber == 1:
        if secondrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif secondrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif secondrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(220, carImage2Y))
        carImageShownRectangle5 = carImageShown.get_rect(topleft = (220, carImage2Y))
        carImage2Y = carImage2Y + carScrollingSpeed
        if carImage2Y + carScrollingSpeed >= carImage1Height:
            secondRandNumber = 0
            carImage2Y = -carImage2Height
    elif secondRandNumber == 2:
        if secondrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif secondrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif secondrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(380, carImage2Y))
        carImageShownRectangle6 = carImageShown.get_rect(topleft = (380, carImage2Y))
        carImage2Y = carImage2Y + carScrollingSpeed
        if carImage2Y + carScrollingSpeed >= carImage1Height:
            secondRandNumber = 0
            carImage2Y = -carImage2Height
    elif secondRandNumber == 3:
        if secondrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif secondrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif secondrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(530, carImage2Y))
        carImageShownRectangle7 = carImageShown.get_rect(topleft = (530, carImage2Y))
        carImage2Y = carImage2Y + carScrollingSpeed
        if carImage2Y + carScrollingSpeed >= carImage1Height:
            secondRandNumber = 0
            carImage2Y = -carImage2Height
    elif secondRandNumber == 4:
        if secondrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif secondrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif secondrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(690, carImage2Y))
        carImageShownRectangle8 = carImageShown.get_rect(topleft = (690, carImage2Y))
        carImage2Y = carImage2Y + carScrollingSpeed
        if carImage2Y + carScrollingSpeed >= carImage1Height:
            secondRandNumber = 0
            carImage2Y = -carImage2Height

    if thirdRandNumber == 1:
        if thirdrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif thirdrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif thirdrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(220, carImage3Y))
        carImageShownRectangle9 = carImageShown.get_rect(topleft = (220, carImage3Y))
        carImage3Y = carImage3Y + carScrollingSpeed
        if carImage3Y + carScrollingSpeed >= carImage1Height:
            thirdRandNumber = 0
            carImage3Y = -carImage2Height
    elif thirdRandNumber == 2:
        if thirdrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif thirdrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif thirdrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(380, carImage3Y))
        carImageShownRectangle10 = carImageShown.get_rect(topleft = (380, carImage3Y))
        carImage3Y = carImage3Y + carScrollingSpeed
        if carImage3Y + carScrollingSpeed >= carImage1Height:
            thirdRandNumber = 0
            carImage3Y = -carImage2Height
    elif thirdRandNumber == 3:
        if thirdrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif thirdrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif thirdrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(530, carImage3Y))
        carImageShownRectangle11 = carImageShown.get_rect(topleft = (530, carImage3Y))
        carImage3Y = carImage3Y + carScrollingSpeed
        if carImage3Y + carScrollingSpeed >= carImage1Height:
            thirdRandNumber = 0
            carImage3Y = -carImage2Height
    elif thirdRandNumber == 4:
        if thirdrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif thirdrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif thirdrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(690, carImage3Y))
        carImageShownRectangle12 = carImageShown.get_rect(topleft = (690, carImage3Y))
        carImage3Y = carImage3Y + carScrollingSpeed
        if carImage3Y + carScrollingSpeed >= carImage1Height:
            thirdRandNumber = 0
            carImage3Y = -carImage2Height

    if fourthRandNumber == 1:
        if fourthrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif fourthrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif fourthrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(220, carImage4Y))
        carImageShownRectangle13 = carImageShown.get_rect(topleft = (220, carImage4Y))
        carImage4Y = carImage4Y + carScrollingSpeed
        if carImage4Y + carScrollingSpeed >= carImage1Height:
            fourthRandNumber = 0
            carImage4Y = -carImage2Height
    elif fourthRandNumber == 2:
        if fourthrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif fourthrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif fourthrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(380, carImage4Y))
        carImageShownRectangle14 = carImageShown.get_rect(topleft = (380, carImage4Y))
        carImage4Y = carImage4Y + carScrollingSpeed
        if carImage4Y + carScrollingSpeed >= carImage1Height:
            fourthRandNumber = 0
            carImage4Y = -carImage2Height
    elif fourthRandNumber == 3:
        if fourthrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif fourthrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif fourthrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(530, carImage4Y))
        carImageShownRectangle15 = carImageShown.get_rect(topleft = (530, carImage4Y))
        carImage4Y = carImage4Y + carScrollingSpeed
        if carImage4Y + carScrollingSpeed >= carImage1Height:
            fourthRandNumber = 0
            carImage4Y = -carImage2Height
    elif fourthRandNumber == 4:
        if fourthrandNumberForCarPicture == 1:
            carImageShown = carImage1
        elif fourthrandNumberForCarPicture == 2:
            carImageShown = carImage2
        elif fourthrandNumberForCarPicture == 3:
            carImageShown = carImage3
        window.blit(carImageShown,(690, carImage4Y))
        carImageShownRectangle16 = carImageShown.get_rect(topleft = (690, carImage4Y))
        carImage4Y = carImage4Y + carScrollingSpeed
        if carImage4Y + carScrollingSpeed >= carImage1Height:
            fourthRandNumber = 0
            carImage4Y = -carImage2Height
    #below is a return statement which returns all the variables that were modified in the movingBackgroundFunc() function
    return defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16

while repeatGame: #actual start of the program. if repeatGame is True, the whole program repeats
    while startingMenu: #startingMenu loop. if startingMenu is True, the starting menu is shown
        startingMenuFunc("null") #calls the startingMenuFunc() which shows the starting menu. parameter is null since nothing needs to be sent to the function
        pygame.display.flip() #updates the pygame screen
        #below are variables that are being fed into the movingBackgroundFunc() function, and also being received back from the movingBackgroundFunc() after being modified by the function
        defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16 = movingBackgroundFunc(defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16)
        for event in pygame.event.get(): #loops through all pygame events
            keyPressDetection = pygame.key.get_pressed() #function used to detect whether a key was pressed or not
            if event.type == pygame.QUIT or keyPressDetection[pygame.K_ESCAPE]: #if the python window is exited or ESC is pressed, exit the program
                startingMenu, repeatGame = False, False 
            if event.type == pygame.MOUSEBUTTONDOWN: #detects if the player pressed their mouse button
                if startingMenuFunc("playButtonType").collidepoint(event.pos): #if the player pressed play
                    startStartingSequence = True #start the countdown
                    startingMenu = False #hide starting menu
                    gameRunning = True #starts the actual game
                elif startingMenuFunc("creditsButtonType").collidepoint(event.pos): #if the player pressed the credits menu
                    startingMenu = False #hide the starting menu
                    creditsMenu = True #show the credits menu
                    showCredits("null") #calls the showCredits() menu which shows the credits menu
                    while creditsMenu: #while the credits menu is open, check if the back button is pressed
                        for event in pygame.event.get(): #loops through all pygame events
                            keyPressDetection = pygame.key.get_pressed() #function used to detect whether a key was pressed or not
                            if event.type == pygame.QUIT or keyPressDetection[pygame.K_ESCAPE]: #if the python window is exited or ESC is pressed, exit the program
                                startingMenu, creditsMenu, repeatGame = False, False, False
                            if event.type == pygame.MOUSEBUTTONDOWN: #if the player clicks the mouse left click, check if the mouse click collided with the back button hitbox
                                if showCredits("backButton").collidepoint(event.pos): #if the mouse click collided with the back button hitbox, hide the credits menu and call the showMenu() function which shows the main menu
                                    creditsMenu = False #hides the credits menu
                                    startingMenu = True #shows the starting menu again
                                    startingMenuFunc("null") #calls the startingMenuFunc() function which opens the main menu again
                        clock.tick(60) #sets the fps to 60
        clock.tick(60) #fps is 60

    #initialized variables for hitboxes and car heights and dimensions below
    carImage1Y, carImage1Height = -780, 780
    carImage2Y, carImage2Height = -780, 780
    carImage3Y = -780
    carImage4Y = -780
    carImageShown = carImage1
    carImageShownRectangle1 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle2 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle3 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle4 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle5 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle6 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle7 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle8 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle9 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle10 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle11 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle12 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle13 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle14 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle15 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)
    carImageShownRectangle16 = pygame.draw.rect(window, (255, 255, 255), (1, 1, 0, -780), 0)

    #initialized random numbers below
    randNumber = 1
    secondRandNumber = 0
    thirdRandNumber = 0
    fourthRandNumber = 0
    randNumberForCarPicture = random.randrange(1, 4)
    secondrandNumberForCarPicture = 0
    thirdrandNumberForCarPicture = 0
    fourthrandNumberForCarPicture = 0

    #initialized score and loopCounter below (used for calculating score)
    score = 0
    loopCounter = 0

    while gameRunning: #actual game loop. if the gameRunning is True, the actual game starts running
        if startStartingSequence == True: #boolean to determine if the countdown should start or not
            startingSequence(startingMenu, repeatGame) #calls the startingSequence function which displays the starting countdown to the player
            startStartingSequence = False #countdown won't start again
        #below are variables that are being fed into the movingBackgroundFunc() function, and also being received back from the movingBackgroundFunc() after being modified by the function
        defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16 = movingBackgroundFunc(defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16)
        window.blit(playerCarImage1,(playerCarImage1X, playerCarImage1Y)) #blits the player's car onto the screen
        playerCarImage1Rectangle = playerCarImage1.get_rect(topleft = (playerCarImage1X, playerCarImage1Y)) #sets the hitbox for the player's car
        #below is an if condition to determine if the player's car collided with one of the npc's cars
        if playerCarImage1Rectangle.colliderect(carImageShownRectangle1) or playerCarImage1Rectangle.colliderect(carImageShownRectangle2) or playerCarImage1Rectangle.colliderect(carImageShownRectangle3) or playerCarImage1Rectangle.colliderect(carImageShownRectangle4) or playerCarImage1Rectangle.colliderect(carImageShownRectangle5) or playerCarImage1Rectangle.colliderect(carImageShownRectangle6) or playerCarImage1Rectangle.colliderect(carImageShownRectangle7) or playerCarImage1Rectangle.colliderect(carImageShownRectangle8) or playerCarImage1Rectangle.colliderect(carImageShownRectangle9) or playerCarImage1Rectangle.colliderect(carImageShownRectangle10) or playerCarImage1Rectangle.colliderect(carImageShownRectangle11) or playerCarImage1Rectangle.colliderect(carImageShownRectangle12) or playerCarImage1Rectangle.colliderect(carImageShownRectangle13) or playerCarImage1Rectangle.colliderect(carImageShownRectangle14) or playerCarImage1Rectangle.colliderect(carImageShownRectangle15) or playerCarImage1Rectangle.colliderect(carImageShownRectangle16):
            startEndSequence = True #if collided, the end sequence (or explosion) would start
            gameRunning, endMenu = False, True #the actual game would stop running and the end menu would be shown
        window.blit(font.render("Speed: "+str(int((scrollingSpeed-3)*10))+" km/h", False, (255, 255, 255)), (40, 680)) #blits the speed of the player's car onto the screen
        score += 0.1 #score is a derivative of the fps. if the loop runs one time, the score increases by 0.1
        loopCounter += 1 #this loop counter counts the amount of time the loop has run, and is also what the variable "score" derives its value from
        if int((scrollingSpeed-3)*10) > 100 and loopCounter >= 90: #every 2 seconds, or if the loop runs 90 times, and if the speed is above 100 kmh, the score increases by 10
            score += 10 #score increases by 10
            loopCounter = 0 #loop counter resets to 0, and adds 1 every time the loop runs until 90
        if int((scrollingSpeed-3)*10) > 100 and loopCounter <= 45: #every second, if the speed is above 100 kmh, the bonus score is printed
            window.blit(font.render("+10 Points", False, (255, 255, 255)), (620, 20))
            window.blit(font.render("Over 100 km/h", False, (255, 255, 255)), (570, 90))
        window.blit(font.render("Score: "+str(int(score)), False, (255, 255, 255)), (40, 30)) #prints out the score onto the user's screen

        #below are if conditions to determine what key the player pressed 
        if leftKeyPressed:
            if playerCarImage1X == 220: #if the left key is pressed and the player can't go anymore to the left, then the X position doesn't change
                playerCarImage1X -= 0
            else:
                playerCarImage1X -= 10 #if the left key is pressed, move the player's X position 10 to the left
        if rightKeyPressed:
            if playerCarImage1X == 690: #if the right key is pressed and the player can't go anymore to the right, then the X position doesn't change
                playerCarImage1X += 0 
            else:
                playerCarImage1X += 10 #if the right key is pressed, move the player's X position 10 to the right
        if upKeyPressed:
            if scrollingSpeed >= 5 and scrollingSpeed < 15:
                scrollingSpeed += 0.1 #if the up key is pressed and the player's speed is within 5 and 15, speed up the scrollingSpeed of the player's car
        if downKeyPressed:
            if scrollingSpeed > 5 and scrollingSpeed <= 15.1:
                scrollingSpeed -= 0.1 #if the down key is pressed and the player's speed is within 5 and 15, slow down the scrollingSpeed of the player's car
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:          # checks for key press downs       
                if event.key == pygame.K_LEFT:
                    leftKeyPressed = True        
                elif event.key == pygame.K_RIGHT:    
                    rightKeyPressed = True 
                elif event.key == pygame.K_UP:    
                    upKeyPressed = True   
                elif event.key == pygame.K_DOWN:    
                    downKeyPressed = True 
                elif event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    gameRunning, repeatGame = False, False
            elif event.type == pygame.KEYUP:            # check for key releases
                if event.key == pygame.K_LEFT:    
                    leftKeyPressed = False   
                elif event.key == pygame.K_RIGHT:  
                    rightKeyPressed = False  
                elif event.key == pygame.K_UP:        
                    upKeyPressed = False
                elif event.key == pygame.K_DOWN:    
                    downKeyPressed = False 
                elif event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    gameRunning, repeatGame = False, False
        clock.tick(45) #fps

    #when the actual game ends, the values must be initialized again for the next game to start normally
    scrollingSpeed, carScrollingSpeed = 5, 4 #scrolling speed and npc car scrolling speeds must be reset to normal
    leftKeyPressed, rightKeyPressed, upKeyPressed, downKeyPressed = False, False, False, False #the keys that were pressed must not be pressed anymore
    playerCarImage1X = 220 #when the player respawns, their car will spawn on the left lane again

    while endMenu:
        if startEndSequence == True:
            pygame.mixer.Sound.play(explosionFX) #plays the explosion sound fx whe the player crashes
            window.blit(gameOverScreen, (0, 0))
            currentTime = pygame.time.get_ticks()
            startEndSequence = False
            for event in pygame.event.get(): #loops through all pygame events
                keyPressDetection = pygame.key.get_pressed() #function used to detect whether a key was pressed or not
                if event.type == pygame.QUIT or keyPressDetection[pygame.K_ESCAPE]: #if the python window is exited or ESC is pressed, exit the program
                    endMenu, repeatGame = False, False
            pygame.display.flip()
        futureTime = pygame.time.get_ticks()
        if futureTime-currentTime > 3000:
            endMenuFunc("null", score)
            defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16 = movingBackgroundFunc(defaultHighwayBackground1, defaultHighwayBackground1X, defaultHighwayBackground1Y, defaultHighwayBackground2, defaultHighwayBackground2X, defaultHighwayBackground2Y, scrollingSpeed, defaultHighwayBackground1Height, defaultHighwayBackground2Height, randNumber, randNumberForCarPicture, carImageShown, carImage1, carImage2, carImage3, carImage1Y, carScrollingSpeed, carImage1Height, carImage2Height, secondRandNumber, secondrandNumberForCarPicture, thirdRandNumber, thirdrandNumberForCarPicture, fourthRandNumber, fourthrandNumberForCarPicture, carImage2Y, carImage3Y, carImage4Y, carImageShownRectangle1, carImageShownRectangle2, carImageShownRectangle3, carImageShownRectangle4, carImageShownRectangle5, carImageShownRectangle6, carImageShownRectangle7, carImageShownRectangle8, carImageShownRectangle9, carImageShownRectangle10, carImageShownRectangle11, carImageShownRectangle12, carImageShownRectangle13, carImageShownRectangle14, carImageShownRectangle15, carImageShownRectangle16)
            for event in pygame.event.get(): #loops through all pygame events
                keyPressDetection = pygame.key.get_pressed() #function used to detect whether a key was pressed or not
                if event.type == pygame.QUIT or keyPressDetection[pygame.K_ESCAPE]: #if the python window is exited or ESC is pressed, exit the program
                    endMenu, repeatGame = False, False 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if endMenuFunc("playAgainButtonType", score).collidepoint(event.pos):
                        startStartingSequence = True
                        endMenu = False
                        gameRunning = True
                    elif endMenuFunc("creditsButtonType", score).collidepoint(event.pos):
                        endMenu = False
                        creditsMenu = True
                        showCredits("null") #calls the showCredits() menu which shows the credits menu
                        while creditsMenu: #while the credits menu is open, check if the back button is pressed
                            for event in pygame.event.get(): #loops through all pygame events
                                if event.type == pygame.QUIT or keyPressDetection[pygame.K_ESCAPE]: #if the python window is exited or ESC is pressed, exit the program
                                    creditsMenu, endMenu, repeatGame = False, False, False
                                if event.type == pygame.MOUSEBUTTONDOWN: #if the player clicks the mouse left click, check if the mouse click collided with the back button hitbox
                                    if showCredits("backButton").collidepoint(event.pos): #if the mouse click collided with the back button hitbox, hide the credits menu and call the endMenuFunc() function which shows the end menu
                                        creditsMenu = False #hides the credits menu
                                        endMenu = True #shows the end menu again
                                        endMenuFunc("null", score) #calls the endMenuFunc() function which opens the main menu again
                            clock.tick(60) #sets the fps to 60
        clock.tick(60)
    clock.tick(60)
pygame.quit()

