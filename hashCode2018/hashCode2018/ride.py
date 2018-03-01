class Ride():
    __start
    __end
    __earliest
    __latest

    def __init__(self, in_start, in_end, in_earliest, in_latest):
        __start = in_start
        __end = in_end
        __earliest = in_earliest
        __latest = in_latest

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_earliest(self):
        return self.__earliest

    def get_latest(self):
        return self.__latest
