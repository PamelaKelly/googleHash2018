from hashCode2018.reader import Reader
from hashCode2018.car import Car
from hashCode2018.ride import Ride
from hashCode2018.writer import Writer

def main():
    """ Top level function to run the program. """

    #STEP 1: READ THE FILE
    data = Reader.read_file("inputs/c_no_hurry.in")
    program_details = data[0]
    rides = data[1]
    for i in range(len(rides)):
        ride = rides[i]
        rides[i] = Reader.parse_ride(ride)
    # details
    rows = int(program_details[0])
    columns = int(program_details[1])
    fleet_num = int(program_details[2])
    rides_num = int(program_details[3])
    bonus = int(program_details[4])
    steps = int(program_details[5])
    cars = []

    # STEP 2: CREATE CARS
    for i in range(1, fleet_num + 1):
        car = Car(i)
        cars.append(car)

    # STEP 3: CREATE RIDES & AVAILABLE RIDES
    for i in range(rides_num - 1):
        ride_details = rides[i]
        rides[i] = Ride(ride_details[0], ride_details[1], ride_details[2], ride_details[3])

    #Car.set_available_rides(len(rides))

    #  if no cars available? 

    # STEP 3: MAIN FUNCTIONALITY
    for i in range(1, steps + 1):
        for car in cars:
            if car.getAvailability():
                car.findRide(rides, i, steps)
            car.move(car.getCurrentPosition(), car.getCurrentDest())     
    # STEP 4: WRITE TO FILE
    Writer.write_file("outputs/c.out", cars)
    
main()
    
    
