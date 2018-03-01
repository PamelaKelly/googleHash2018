class Reader:
    
    @staticmethod
    def read_file(filepath):
        try:
            with open(filepath) as f:
                # get the parameters for the problem from the first line
                problem_data = f.readline().split()
                rides = []
                # individual rides
                for line in f:
                    rides.append(line)
                return problem_data, rides
        except IOError:
            raise
        
    @staticmethod
    def parse_ride(ride_string):
        ride = ride_string.split()
        return [(int(ride[0]), int(ride[1])), (int(ride[2]), int(ride[3])), int(ride[4]), int(ride[5])]