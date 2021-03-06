from car import Car
class Ride():

    def __init__(self, in_start, in_end, in_earliest, in_latest):
        self.start = in_start
        self.end = in_end
        self.earliest = in_earliest
        self.latest = in_latest
        self.ride_length = Car.calculateDistance(self.start, self.end)

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_earliest(self):
        return self.earliest

    def get_latest(self):
        return self.latest
    
    def ready(self, currentStep):
        return self.earliest <= currentStep
    
    
