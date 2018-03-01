'''
Created on 1 Mar 2018

@author: katherine
'''

class Car(object):
    '''
    classdocs
    '''

    def __init__(self, id):
        '''
        Constructor
        '''
        self.is_available = True # don't need? 
        self.current_position = (0,0)
        self.current_dest = None
        self.id = id
        self.num_rides = 0
        self.assigned_rides = []
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

    @staticmethod
    def calculateDistance(start, end):
        distance = abs((start[0]) - (end[0])) + abs((start[1]) - (end[1]))
        return distance

    def findRide(self, availableRides, stepsRemaining):
        best = availableRides[0]
        best_index = 0
        best_distance = Car.calculateDistance(best.get_start(), best.get_end()) 
        + Car.calculateDistance(self.current_position, best.get_start())
        for i in range(len(availableRides)-1):
            distance = Car.calculateDistance(availableRides[i].get_start, availableRides[i].get_end)
            + Car.calculateDistance(self.current_position, availableRides[i].get_start())
            if distance > best_distance and distance < stepsRemaining:
                best = availableRides[i]
                best_index = i
        self.current_ride = availableRides.pop(best_index)
        self.current_dest = self.current_ride.get_start()
    
    #this moves it ONE SPACE horizontally AND Vertically.
    #should only move one at a time
    def move(self, current_position, current_dest): 
        cur_row = current_position[0]
        cur_col = current_position[1]
        end_row = current_dest[0]
        end_col = current_dest[1]
        if current_position == current_dest:
            self.finishRide()
        else:
            if cur_row - end_row > 0:
                cur_row -= 1
            else:
                cur_row = cur_row + 1
            if cur_col - end_col > 0:
                cur_col = cur_col -1
            else:
                cur_col = cur_col +1
        
        return (cur_row, cur_col)
            

    def finishRide(self):
        self.is_available = True

