import pygame
import random
import math

'''Game that displays three circles with different colors. Then it 
shows a binary code corresponding to one of the three circles and the user
must guess what the correct color is'''

#Game setup: Initialize pygame and Display
pygame.init()
winDimen = (1200,900)
flags = pygame.RESIZABLE | pygame.SCALED
gameWindow = pygame.display.set_mode(winDimen, flags)

pygame.display.set_caption("What The Bin?")

#Divvy up the screen to fit in the circles nicely
edgePad = winDimen[0]/10
circPad = 5
midRegion = winDimen[0]-2*edgePad
midColumns = midRegion/3

radius = (midColumns-circPad*2)/2
font = pygame.font.Font("assets/Midnew.ttf", 25)

#Main loop. Runs everything
def main():
    #Calls generateCircles
    correctCircle, colorChoice, circlePos, colorList = generateCircles(3)
    binColor = decToBin(colorChoice)
    messageOnScreen(binColor,0.75)
    gameExit = False
    gameOver = False
    choice = False
    while not gameExit:
        while gameOver == True:
            messageOnScreen("Hit C to continue or Q to quit",.90)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameWindow.fill((0,0,0))
                        pygame.display.update()
                        main()
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                        choice = True
            
        #Run through events to check if the user has clicked a color
        while not choice:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if mouseInCircle(correctCircle,circlePos):
                        messageOnScreen("Good Job. You're going places.",.80)
                        choice = True
                        gameOver = True
                    elif mouseInCircle(incorrectCircles(colorList,colorChoice)[0],circlePos):
                        messageOnScreen("Better luck next time",.85)
                        choice = True
                        gameOver = True
                    elif mouseInCircle(incorrectCircles(colorList,colorChoice)[1],circlePos):
                        messageOnScreen("Better luck next time",.85)
                        choice = True
                        gameOver = True
            pygame.display.update()

#Generate the circles with random colors
def generateCircles(circleAmount):
    colorList = []
    circlePos = []
    for x in range(circleAmount):
        randColor = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        # List of lists where each list is a color [[r,g,b]]
        colorList.append(randColor)
        position = (edgePad+midColumns*(x+1)-(radius+circPad),winDimen[0]/4)
        pygame.draw.circle(gameWindow, randColor, position, radius,0)
        circlePos.append(position)
    #Store a random color from the three displayed colors (colorList)
    correctCircle = random.randint(0,2)
    colorChoice = colorList[correctCircle]
    return correctCircle, colorChoice, circlePos, colorList

#Now the hard part, conversion to binary
def decToBin(dec_color):
    binColor = ["{0:08b}".format(x) for x in dec_color]
    binColorStr = " ".join(binColor)
    return binColorStr

#Displays a horizontally centered message(text) on the screen at ycoord
def messageOnScreen(text,ycoord):
    message = font.render(text, True, (255,255,255))
    txtRect = message.get_rect()
    txtRect.center = winDimen[0]/2, winDimen[1]/2
    gameWindow.blit(message, (txtRect[0],winDimen[1]*ycoord))

#Returns True if the mouse is inside of the given circle
def mouseInCircle(circle,circlePos):
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    circX = circlePos[circle][0]
    circY = circlePos[circle][1]
    
    if math.sqrt((x-circX)**2 + (y-circY)**2) < radius:
        return True
    else:
        return False

#Returns a list of the positions of the incorrect circles in list colorList
def incorrectCircles(colorList,colorChoice):
    badCircles = []
    for x in range(len(colorList)):
        if colorList[x] != colorChoice:
            badCircles.append(x)
    return badCircles

main()
