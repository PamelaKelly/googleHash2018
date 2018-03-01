'''
Created on 1 Mar 2018

@author: katherine
'''

class car(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.is_available = True
        self.current_position = (0,0)
        self.current_dest = None
        self.current_ride = None


    def getAvailablity(self):
        return self.is_available()

    def setAvailability(self, availability):
        self.is_available = availability

    def getCurrentPosition(self):
        return self.current_position

    def setCurrentPosition(self, current_position):
        self.current_position = current_position

    def getCurrentDest(self):
        return self.current_dest

    def setCurrentDest(self, current_dest):
        self.current_dest = current_dest

    def calculateDistance(self, start, end):
        distance = abs((start[0]) - (end[0])) + abs((start[1]) - (end[1]))
        return distance

    def findRide(self, availableRides):
        self.current_ride = availableRides.pop(0)
        self.current_dest = self.current_ride.get_start()
        self.is_available = False

    def finishRide(self):
        self.is_available = True
        self.findRide()

    def move(self):
        pass
