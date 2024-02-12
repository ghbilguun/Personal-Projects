from graphics2 import *
import random
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DEFAULT_FISH_NUM = 10
DEFAULT_BUBBLE_NUM = 25


#This fish class creates a fish and has a move function that moves the fish inside the window

class Fish:
    def __init__(self, x, y, color, speed, count):
        self.fishSpeed = speed
        self.movement = 1
        self.count = count
        
        self.bodyPoint1 = Point(x - 30, y - 20)
        self.bodyPoint2 = Point(x + 30, y + 20)
        self.fishBody = Oval(self.bodyPoint1, self.bodyPoint2)
        self.fishBody.setFill(color)
        
        self.tailPoint1 = Point(x - 20, y - 30)
        self.tailPoint2 = Point(x + 0, y + 30)
        self.fishTail = Oval(self.tailPoint1, self.tailPoint2)
        self.fishTail.setFill(color)
        
        self.eye = Circle(Point(x + 15, y - 5), 3)
        self.eye.setFill('white')
        
    def drawFish(self, win):
        self.fishTail.draw(win)
        self.fishBody.draw(win)
        self.eye.draw(win)
        
    def moveFish(self):
        if self.fishBody.getCenter().getX() > WINDOW_WIDTH + 10:
            self.fishBody.move(-WINDOW_WIDTH - 10, 0)
        
        if self.fishTail.getCenter().getX() > WINDOW_WIDTH + 10:
            self.fishTail.move(-WINDOW_WIDTH - 10, 0)
            
        if self.eye.getCenter().getX() > WINDOW_WIDTH + 10:
            self.eye.move(-WINDOW_WIDTH - 10, 0)
            
        if self.count == 20:
            self.movement = 0
            self.count = 0   
        
        elif self.count < 10:
            self.movement = 1
            self.count = self.count + 1
        
        elif self.count < 20:
            self.movement = - 1
            self.count = self.count + 1
        
        self.fishBody.move(self.fishSpeed, self.movement)
        self.fishTail.move(self.fishSpeed, self.movement)
        self.eye.move(self.fishSpeed, self.movement)
        

#Almost very similar to the fish class but the movement instead is going up


class Bubble:
    
    def __init__(self, x, y, speed, count):
        self.bubble = Circle(Point(x, y), 5)
        self.speed = speed
        self.bubble.setFill('white')
        self.count = count
        self.movement = 1
        
    def drawBubble(self, win):
        self.bubble.draw(win)
        
    def move(self):
        if self.bubble.getCenter().getY() < 0:
            self.bubble.move(0, WINDOW_HEIGHT + 10)
           
        if self.count == 20:
            self.movement = 0
            self.count = 0
            self.bubble.move(self.movement, self.speed)   
        
        elif self.count < 10:
            self.movement = 1
            self.count = self.count + 1
            self.bubble.move(self.movement, self.speed)
        
        elif self.count < 20:
            self.movement = - 1
            self.count = self.count + 1
            self.bubble.move(self.movement, self.speed)

            
#------------------
# HELPER FUNCTIONS
#------------------

def setupInput(win, point, text):
    '''
    creates an Entry box with a label
    
    Params:
    win (GraphWin): the window the Entry box and label with be drawn in.
    point (Point): the location od the center of the text label
    text (str): the words that will be used to label the Entry box
    
    Returns:
    the Entry object created
    '''
    winText = Text(point, text)
    winText.setSize(18)
    winText.draw(win)
    winBox = Entry(Point(point.getX() + 225, point.getY()), 5)
    winBox.setSize(18)
    winBox.draw(win)
    return winBox

def getInput(win):
    '''
    Allows the user to enter the number of fish and bubbles for the aquarium.
    If a value is not entered or an invalid value (like a letter) is entered,
    the default number is used for that value.
    
    Params:
    win (GraphWin): the window the Entry box is in
    
    Returns:
    the number of fish and number of bubbles that will be drawn in the aquarium
    as a tuple
    '''
    directions = Text(Point(WINDOW_WIDTH/2 , 400), 'Enter the number of fish and bubbles, then click in the window.')
    directions.draw(win)
    fishEntry = setupInput(win, Point(300, 200), "Enter number of fish:")
    bubbleEntry = setupInput(win, Point(300, 300), "Enter number of bubbles:")
    win.getMouse()
    if fishEntry.getText().isdigit() and int(fishEntry.getText()) >= 0:
        numFish = int(fishEntry.getText())
    else:
        numFish = DEFAULT_FISH_NUM
    if bubbleEntry.getText().isdigit() and int(bubbleEntry.getText()) >= 0:
        numBubbles = int(bubbleEntry.getText())
    else:
        numBubbles = DEFAULT_BUBBLE_NUM
    fishEntry.undraw()
    bubbleEntry.undraw()
    directions.undraw()
    cover = Rectangle(Point(0, 0), Point(WINDOW_WIDTH, WINDOW_HEIGHT))
    cover.setFill("cyan")
    cover.draw(win)
    return numFish, numBubbles

def randColor():
    '''
    Returns a random color created from randomly generated red, green, and blue values
    '''
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return color_rgb(red, green, blue)


def setupFish(numFish):
    '''
    Creates the list of fish with random position, color and speed
    
    Params:
    numFish (int): the number of fish to be added to the list
    
    Returns:
    the list of fish
    '''
    fishList = []
    
    COUNT = random.randrange(0, 20)
    
    for num in range(numFish):
        x = random.randrange(WINDOW_WIDTH)
        y = random.randrange(WINDOW_HEIGHT)
        fishSpeed = random.randrange(2, 6)
        color = randColor()
        fish = Fish(x, y, color, fishSpeed, COUNT)
        fishList.append(fish)
        
    return fishList


def setupBubbles(numBubbles):
    '''
    Creates the list of bubbles with random position and speed
    
    Params:
    numBubbles (int): the number of bubbles to be added to the list
    
    Returns:
    the list of bubbles
    '''
    bubbleList = []
    
    COUNT = random.randrange(0, 20)
    
    for num in range(numBubbles):
        x = random.randrange(WINDOW_WIDTH)
        y = random.randrange(WINDOW_HEIGHT)
        bubbleSpeed = random.randrange(-5, 0)
        bubble = Bubble(x, y, bubbleSpeed, COUNT)
        bubbleList.append(bubble)
    
    return bubbleList
        

def main():

    # make the graphics window (use autoflush=False to update more frequently)
    # makes the animation move more smoothly
    win = GraphWin("Swimming Fish", WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=False)
    win.setBackground("cyan2")
    
    numFish, numBubbles = getInput(win)
                      
    # call helper functions to setup the fish and bubble lists
    bubbleList = setupBubbles(numBubbles)
    fishList = setupFish(numFish)
    # draw the fish and bubbles in their initial locations
    for bubble in bubbleList:
        bubble.drawBubble(win)
    for fish in fishList:
        fish.drawFish(win)
        
    # continue swimming until the user clicks
    keepSwimming = True
    
    while keepSwimming:
        # loop through all the fish calling move method on each fish
        for fish in fishList:
            fish.moveFish()

        # loop through all the bubbles calling move method on each bubble
        # The bubble are after the fish so that the bubbles are drawn in front of the fish
        for bubble in bubbleList:
            bubble.move()
        
        update(50) # call update to flush the window
        # if user clicks: stop swimming
        if win.checkMouse() != None:
            keepSwimming = False

    win.close()

if __name__ == '__main__':
    main()
