class Writer:
    #output = number of rides assigned, ride numbers
    @staticmethod
    def write_file(outputfile, carsList):
        try:
            f = open(outputfile, 'w')
            #number of car objects in list
            for car in carsList:
                #collating string of num rides + list of rides
                output = car.getNumberRides()
                for carRide in car.getAssignedRides():
                    output += carRide
                print >> f, output
        except IOError:
            raise