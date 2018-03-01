'''
Created on 1 Mar 2018

@author: team binary star
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
        
    def getAvailability(self):
        return self.is_available

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
    
    def getNumberRides(self):
        return self.num_rides

    def getAssignedRides(self):
        return self.assigned_rides

    @staticmethod
    def calculateDistance(start, end):
        distance = abs((start[0]) - (end[0])) + abs((start[1]) - (end[1]))
        return distance

    def findRide(self, availableRides, stepsRemaining):
        best_distance = -1
        for i in range(len(availableRides)-1):
            if availableRides != None:
                distance = Car.calculateDistance(availableRides[i].get_start(), availableRides[i].get_end())
                + Car.calculateDistance(self.current_position, availableRides[i].get_start())
                if distance > best_distance and distance < stepsRemaining and distance < availableRides[i].get_latest():
                    best_index = i
        if best_distance == -1:
            self.current_ride = None
            print("No way Jose!")
            return False
        else:
            self.num_rides += 1
            self.assigned_rides.append(best_index)
            self.current_ride = availableRides[best_index]
            availableRides[best_index] = None
            self.current_dest = self.current_ride.get_start()
    
    #this moves it ONE SPACE horizontally or Vertically.
    #first completes horizontal move and then vertical move.
    def move(self, current_position, current_dest): 
        if self.current_ride != None:
            cur_row = current_position[0]
            cur_col = current_position[1]
            end_row = current_dest[0]
            end_col = current_dest[1]     
            if cur_row - end_row > 0:
                cur_row -= 1
            elif cur_row - end_row < 0:
                cur_row = cur_row + 1
            elif cur_row == end_row:
                if cur_col - end_col > 0:
                    cur_col = cur_col -1
                elif cur_col - end_col < 0:
                    cur_col = cur_col +1
            self.current_position = cur_row, cur_col
    
    def check_idle(self):
        return (self.current_position == self.current_destination) and (self.is_available == True)
    
    def check_final(self):
        return (self.current_position == self.current_dest) and (self.is_available == False)

    def finishRide(self):
        self.is_available = True
        

