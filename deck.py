# Nicholas Eguizabal
# Program to randomly pull cards from the Deck of Worlds

# Creates a dictionary that holds every card
# Each card needs a unique name
# Each card needs to take a specific number of inputs based on the card type
# Make a dictionary for each type

from random import randint, choice

class Deck():
    def __init__(self):
        self.regions = []
        self.landmarks = {}
        self.namesakes = {}
        self.origins = {}
        self.attributes = {}
        self.advents = {}

        self.populateRegions()
        self.populateLandmarks()
        self.populateNamesake()
        self.populateOrigin()
        self.populateAttributes()
        self.populateAdvents()

        #self.pullRegion()
        #self.pullLandmark()
        #self.pullNamesake()
        #self.pullOrigin()
        #self.pullAttribute()
        #self.pullAdvent()

    def populateRegions(self):
        file_name = 'regions.txt'
        try:
            with open(file_name) as f_obj:
                regionsList = f_obj.readlines()
        except FileNotFoundError:
            print("That file doesn't exist!")

        for region in regionsList:
            # Grabs the length of the string and subtracts 1
            # Doesn't subtract 2 because the index starts at 0
            size = len(region) - 1
            self.regions.append(region[0:size])

    def pullRegion(self):
        return choice(self.regions)

    def populateLandmarks(self):
        temp = []
        file_name = 'landmarks.txt'
        try:
            with open(file_name) as f_obj:
                landmarksList = f_obj.readlines()
        except FileNotFoundError:
            print("That file doesn't exist!")

        dictIndex = 0
        for landmarks in landmarksList:
            size = len(landmarks) - 1
            temp.append(landmarks[0:size])
            if len(temp) == 2:
                self.landmarks[dictIndex] = temp
                temp = []
                dictIndex += 1

    def pullLandmark(self):
        return choice(self.landmarks)

    def populateNamesake(self):
        file_name = 'namesake.txt'
        temp = []
        try:
            with open(file_name) as f_obj:
                namesakeList = f_obj.readlines()
        except FileNotFoundError:
            print("That file doesn't exist")

        dictIndex = 0
        for namesakes in namesakeList:
            size = len(namesakes) - 1
            temp.append(namesakes[0:size])
            if len(temp) == 4:
                self.namesakes[dictIndex] = temp
                temp = []
                dictIndex += 1

    def pullNamesake(self):
        return choice(self.namesakes)

    def populateOrigin(self):
        file_name = 'origins.txt'
        temp = []
        try:
            with open(file_name) as f_obj:
                originList = f_obj.readlines()
        except FileNotFoundError:
            print("That file doesn't exist")

        dictIndex = 0
        for origins in originList:
            size = len(origins) - 1
            temp.append(origins[0:size])
            if len(temp) == 4:
                self.origins[dictIndex] = temp
                temp = []
                dictIndex += 1

    def pullOrigin(self):
        return choice(self.origins)

    def populateAttributes(self):
        file_name = 'attribute.txt'
        temp = []
        try:
            with open(file_name) as f_obj:
                attributeList = f_obj.readlines()
        except FileNotFoundError:
            print("That file doesn't exist")

        dictIndex = 0
        for attribute in attributeList:
            size = len(attribute) - 1
            temp.append(attribute[0:size])
            if len(temp) == 4:
                self.attributes[dictIndex] = temp
                temp = []
                dictIndex += 1

    def pullAttribute(self):
        return choice(self.attributes)

    def populateAdvents(self):
        file_name = 'advent.txt'
        temp = []
        try:
            with open(file_name) as f_obj:
                adventList = f_obj.readlines()
        except FileNotFoundError:
            print("That file doesn't exist")

        dictIndex = 0
        for advent in adventList:
            size = len(advent) - 1
            temp.append(advent[0:size])
            if len(temp) == 2:
                self.advents[dictIndex] = temp
                temp = []
                dictIndex += 1

    def pullAdvent(self):
        return choice(self.advents)

#deck = Deck()
