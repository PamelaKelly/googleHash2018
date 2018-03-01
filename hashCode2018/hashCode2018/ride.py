class Ride():

    def __init__(self, in_start, in_end, in_earliest, in_latest):
        self.start = in_start
        self.end = in_end
        self.earliest = in_earliest
        self.latest = in_latest

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_earliest(self):
        return self.__earliest

    def get_latest(self):
        return self.__latest
    
    def ready(self, currentStep):
        return self.earliest <= currentStep
    
    
