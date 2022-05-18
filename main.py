# Nicholas Eguizabal
# A GUI for the Deck of Worlds Cards

from tkinter import Tk, Frame, Canvas, BOTH, Button, Label, CENTER
from deck import Deck
from math import ceil

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Deck of Worlds')
        self.master.geometry('1000x1000')

        self.deck = Deck()
        self.inPlay = {}
        self.cardNumber = 0

        self.makeFrame()
        self.makeCanvas()
        self.createButtons()

        master.bind('<Escape>', self.quit)
        self.canvas.bind('<Button-1>', self.getIt)
        master.bind('<B1-Motion>', self.moveIt)
        master.bind('<Motion>', self.updateLabels)

    def makeFrame(self):
        self.menuContainer = Frame(self.master)
        self.menuContainer.grid(row = 0, column = 0, sticky = 'NESW')

        self.canvasContainer = Frame(self.master)
        self.canvasContainer.grid(row = 0, column = 1, sticky = 'NESW')

        self.master.grid_rowconfigure(0, weight = 1)
        self.master.grid_columnconfigure(1, weight = 1)

        self.menuContainer.grid_columnconfigure((0, 1, 2), weight = 1)

        self.xLabel = Label(self.menuContainer, text = 0)
        self.xLabel.grid(row = 6, column = 0)

        self.yLabel = Label(self.menuContainer, text = 0)
        self.yLabel.grid(row = 6, column = 1)

    def makeCanvas(self):
        self.canvas = Canvas(self.canvasContainer, background = '#e3d8a1', width = 500, height = 500)
        self.canvas.pack(fill = BOTH, expand = True)

    def createButtons(self):
        self.liftButton = Button(self.menuContainer, text = 'Raise Card', command = self.raiseCard)
        self.liftButton.grid(row = 0, column = 0, sticky = 'NESW')

        self.lowerButton = Button(self.menuContainer, text = 'Lower Card', command = self.lowerCard)
        self.lowerButton.grid(row = 0, column = 1, sticky = 'NESW')

        self.regionButton = Button(self.menuContainer, text = 'Region', command = self.createRegion)
        self.regionButton.grid(row = 2, column = 0, sticky = 'NESW')

        self.landmarkButton = Button(self.menuContainer, text = 'Landmark', command = self.createLandmark)
        self.landmarkButton.grid(row = 2, column = 1, sticky = 'NESW')

        self.namesakeButton = Button(self.menuContainer, text = 'Namesake', command = self.createNamesake)
        self.namesakeButton.grid(row = 2, column = 2, sticky = 'NESW')

        self.originButton = Button(self.menuContainer, text = 'Origin', command = self.createOrigin)
        self.originButton.grid(row = 3, column = 0, sticky = 'NESW')

        self.attributeButton = Button(self.menuContainer, text = 'Attribute', command = self.createAttribute)
        self.attributeButton.grid(row = 3, column = 1, sticky = 'NESW')

        self.adventButton = Button(self.menuContainer, text = 'Advent', command = self.createAdvent)
        self.adventButton.grid(row = 3, column = 2, sticky = 'NESW')

        self.rotateButton = Button(self.menuContainer, text = 'Rotate', command = self.rotateCard)
        self.rotateButton.grid(row = 0, column = 2, sticky = 'NESW')

        self.deleteButton = Button(self.menuContainer, text = 'Delete', command = self.deleteCard)
        self.deleteButton.grid(row =1, column = 1, sticky = 'NESW')

    def raiseCard(self):
        if self.selectedCard:
            self.canvas.tag_raise(self.canvas.gettags(self.selectedCard)[0])

    def lowerCard(self):
        if self.selectedCard:
            self.canvas.tag_lower(self.canvas.gettags(self.selectedCard)[0])

    def deleteCard(self):
        if self.selectedCard:
            self.canvas.delete(self.canvas.gettags(self.selectedCard)[0])

    def shiftText(self, objId, objInd, x, y, anglePlz):
        self.canvas.coords(self.inPlay[objId][objInd], x, y)
        self.canvas.itemconfig(self.inPlay[objId][objInd], angle = anglePlz)

    def shiftTwoText(self, objId, objInd1, objInd2, lists, elem1, elem2):
        self.shiftText(objId, objInd1, lists[elem1][0], lists[elem1][1], lists[elem1][2])
        self.shiftText(objId, objInd2, lists[elem2][0], lists[elem2][1], lists[elem2][2])

    def shiftFourText(self, objId, objInd1, objInd2, objInd3, objInd4, lists, elem1, elem2, elem3, elem4):
        self.shiftText(objId, objInd1, lists[elem1][0], lists[elem1][1], lists[elem1][2])
        self.shiftText(objId, objInd2, lists[elem2][0], lists[elem2][1], lists[elem2][2])
        self.shiftText(objId, objInd3, lists[elem3][0], lists[elem3][1], lists[elem3][2])
        self.shiftText(objId, objInd4, lists[elem4][0], lists[elem4][1], lists[elem4][2])

    def rotateCard(self):
        if self.selectedCard:
            # Grabs the number at the end of the rectangle's tag
            if len(self.canvas.gettags(self.selectedCard)[0]) < 6:
                objId = int(self.canvas.gettags(self.selectedCard)[0][4])
            else:
                size = len(self.canvas.gettags(self.selectedCard)[0])
                objId = int(self.canvas.gettags(self.selectedCard)[0][4:size])
            # Grabs the first coordinate of the rectangle
            test = self.canvas.coords(self.inPlay[objId][0])
            # These are all the different positions and angles relative to the rectangle
            locations = [[test[0] + 100, test[1] + 20, 180],
                         [test[0] + 180, test[1] + 100, 90],
                         [test[0] + 100, test[1] + 180, 0],
                         [test[0] + 20, test[1] + 100, 270]]
            locationsAdvent = [[test[0] + 100, test[1] + 40, 180],
                               [test[0] + 160, test[1] + 100, 90],
                               [test[0] + 100, test[1] + 160, 0],
                               [test[0] + 40, test[1] + 100, 270]]
            # Grabs the first coordinate of the first text object
            text = self.canvas.coords(self.inPlay[objId][1])
            if (text[0] == locations[0][0] and text[1] == locations[0][1]) or (text[0] == locationsAdvent[0][0] and text[1] == locationsAdvent[0][1]):
                if self.inPlay[objId][3] == 'landmark':
                    self.shiftTwoText(objId, 1, 2, locations, 1, 3)
                elif self.inPlay[objId][3] == 'advent':
                    self.shiftTwoText(objId, 1, 2, locationsAdvent, 1, 3)
                elif len(self.inPlay[objId]) > 4:
                    self.shiftFourText(objId, 1, 2, 3, 4, locations, 1, 2, 3, 0)
            elif (text[0] == locations[1][0] and text[1] == locations[1][1]) or (text[0] == locationsAdvent[1][0] and text[1] == locationsAdvent[1][1]):
                if self.inPlay[objId][3] == 'landmark':
                    self.shiftTwoText(objId, 1, 2, locations, 2, 0)
                elif self.inPlay[objId][3] == 'advent':
                    print('Made it!')
                    self.shiftTwoText(objId, 1, 2, locationsAdvent, 2, 0)
                elif len(self.inPlay[objId]) > 4:
                    self.shiftFourText(objId, 1, 2, 3, 4, locations, 2, 3, 0, 1)
            elif (text[0] == locations[2][0] and text[1] == locations[2][1]) or (text[0] == locationsAdvent[2][0] and text[1] == locationsAdvent[2][1]):
                if self.inPlay[objId][3] == 'landmark':
                    self.shiftTwoText(objId, 1, 2, locations, 3, 1)
                elif self.inPlay[objId][3] == 'advent':
                    self.shiftTwoText(objId, 1, 2, locationsAdvent, 3, 1)
                elif len(self.inPlay[objId]) > 4:
                    self.shiftFourText(objId, 1, 2, 3, 4, locations, 3, 0, 1, 2)
            elif (text[0] == locations[3][0] and text[1] == locations[3][1]) or (text[0] == locationsAdvent[3][0] and text[1] == locationsAdvent[3][1]):
                if self.inPlay[objId][3] == 'landmark':
                    self.shiftTwoText(objId, 1, 2, locations, 0, 2)
                elif self.inPlay[objId][3] == 'advent':
                    self.shiftTwoText(objId, 1, 2, locationsAdvent, 0, 2)
                elif len(self.inPlay[objId]) > 4:
                    self.shiftFourText(objId, 1, 2, 3, 4, locations, 0, 1, 2, 3)

    def createRegion(self):
        # Create a Rectangle on a specific location
        # Create Text on top of the rectangle relative to a certain part of the rectangle
        # Give them identical tags for a future move action to work with all at once
        tagN = 'Card%s' % self.cardNumber
        self.inPlay[self.cardNumber] = [self.canvas.create_rectangle(0, 0, 200, 200, fill = 'green', tag = ('Card%s' % self.cardNumber)),
                                        self.canvas.create_text(100, 100, text = self.deck.pullRegion(), fill = 'black', tag = tagN, justify = CENTER, width = 120)]
        self.cardNumber += 1

    def createLandmark(self):
        landmarks = self.deck.pullLandmark()
        tagN = 'Card%s' % self.cardNumber
        self.inPlay[self.cardNumber] = [self.canvas.create_rectangle(0, 0, 200, 200, fill = 'brown', tag = tagN),
                                        self.canvas.create_text(100, 20, text = landmarks[0], fill = 'white', tag = tagN, justify = CENTER, width = 120, angle = 180),
                                        self.canvas.create_text(100, 180, text = landmarks[1], fill = 'white', tag = tagN, justify = CENTER, width = 120), 'landmark']
        self.cardNumber += 1

    def createNamesake(self):
        nameSake = self.deck.pullNamesake()
        tagN = 'Card%s' % self.cardNumber
        self.inPlay[self.cardNumber] = [self.canvas.create_rectangle(0, 0, 200, 200, fill = 'orange', tag = tagN),
                                        self.canvas.create_text(100, 20, text = nameSake[0], fill = 'white', tag = tagN, justify = CENTER, width = 120, angle = 180),
                                        self.canvas.create_text(180, 100, text = nameSake[1], fill = 'white', tag = tagN, justify = CENTER, width = 120, angle = 90),
                                        self.canvas.create_text(100, 180, text = nameSake[2], fill = 'white', tag = tagN, justify = CENTER, width = 120),
                                        self.canvas.create_text(20, 100, text = nameSake[3], fill = 'white', tag = tagN, justify = CENTER, width = 120, angle = 270)]
        self.cardNumber += 1

    def createOrigin(self):
        origin = self.deck.pullOrigin()
        tagN = 'Card%s' % self.cardNumber
        self.inPlay[self.cardNumber] = [self.canvas.create_rectangle(0, 0, 200, 200, fill = 'blue', tag = tagN),
                                        self.canvas.create_text(100, 20, text = origin[0], fill = 'white', tag = tagN, justify = CENTER, width = 120, angle = 180),
                                        self.canvas.create_text(180, 100, text = origin[1], fill = 'white', tag = tagN, justify = CENTER, width = 120, angle = 90),
                                        self.canvas.create_text(100, 180, text = origin[2], fill = 'white', tag = tagN, justify = CENTER, width = 120),
                                        self.canvas.create_text(20, 100, text = origin[3], fill = 'white', tag = tagN, justify = CENTER, width = 120, angle = 270)]
        self.cardNumber += 1

    def createAttribute(self):
        attribute = self.deck.pullAttribute()
        print(attribute)
        tagN = 'Card%s' % self.cardNumber
        self.inPlay[self.cardNumber] = [self.canvas.create_rectangle(0, 0, 200, 200, fill = 'cyan', tag = tagN),
                                        self.canvas.create_text(100, 20, text = attribute[0], fill = 'black', tag = tagN, justify = CENTER, width = 120, angle = 180),
                                        self.canvas.create_text(180, 100, text = attribute[1], fill = 'black', tag = tagN, justify = CENTER, width = 120, angle = 90),
                                        self.canvas.create_text(100, 180, text = attribute[2], fill = 'black', tag = tagN, justify = CENTER, width = 120),
                                        self.canvas.create_text(20, 100, text = attribute[3], fill = 'black', tag = tagN, justify = CENTER, width = 120, angle = 270)]
        self.cardNumber += 1

    def createAdvent(self):
        advent = self.deck.pullAdvent()
        tagN = 'Card%s' % self.cardNumber
        self.inPlay[self.cardNumber] = [self.canvas.create_rectangle(0, 0, 200, 200, fill = 'magenta', tag = tagN),
                                        self.canvas.create_text(100, 40, text = advent[0], fill = 'white', tag = tagN, justify = CENTER, width = 180, angle = 180),
                                        self.canvas.create_text(100, 160, text = advent[1], fill = 'white', tag = tagN, justify = CENTER, width = 180), 'advent']
        self.cardNumber += 1

    def inCard(self, event, item):
        # bBox is a method to call on a canvas with a canvas object ID
        # bBox returns the different coordinates of the canvas object called as a tuple
        bBox = self.canvas.bbox(item)
        # Compares the Coordinates of the click to the canvas object coordinates
        # To make sure that the click is within the object
        return bBox[0] < event.x < bBox[2] and bBox[1] < event.y < bBox[3]

    def getIt(self, event):
        delta = 5
        self.selectedCard = self.canvas.find_closest(event.x, event.y)
        print('get', self.canvas.gettags(self.selectedCard))
        try:
            if not self.inCard(event, self.selectedCard):
                self.selectedCard = None
        except (NameError, TypeError):
            print('No card selected')

    def moveIt(self, event):
        if self.selectedCard:
            (xPos, yPos) = (event.x, event.y)
            (xObject, yObject) = (self.canvas.coords(self.selectedCard)[0], self.canvas.coords(self.selectedCard)[1])

            self.canvas.move(self.canvas.gettags(self.selectedCard)[0], xPos-xObject, yPos-yObject)

    def updateLabels(self, event):
        self.xLabel.config(text = event.x)
        self.yLabel.config(text = event.y)

    def quit(self, event):
        self.master.destroy()


root = Tk()
gui = GUI(root)
root.mainloop()
