class Writer:
    #output = number of rides assigned, ride numbers
    @staticmethod
    def write_file(outputfile, carsList):
        try:
            f = open(outputfile, 'w')
            #number of car objects in list
            for car in range(0, len(carsList)):
                #collating string of num rides + list of rides
                output = str(car.getNumberRides()) + " " + str(car.getAssignedRides())
                print >> f, output
        except IOError:
            raise