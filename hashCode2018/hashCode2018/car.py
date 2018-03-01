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
        pass
    
    #this moves it ONE SPACE horizontally AND Vertically.
    #should only move one at a time
    def move(self, current_position, current_dest):
        cur_row = current_position[0]
        cur_col = current_position[1]
        end_row = current_dest[0]
        end_col = current_dest[1]
        if cur_row - end_row > 0:
            cur_row = cur_row - 1
        else:
            cur_row = cur_row + 1
        if cur_col - end_col > 0:
            cur_col = cur_col -1
        else:
            cur_col = cur_col +1
        
        return (cur_row, cur_col)
            
            
            
        
        pass
    
    