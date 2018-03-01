from hashCode2018.reader import Reader
from hashCode2018.car import Car
from hashCode2018.ride import Ride
def main():
    """ Top level function to run the program. """

    #STEP 1: READ THE FILE
    data = Reader.read_file("#")
    program_details = data[0]
    rides = data[1]
    # details
    rows = program_details[0]
    columns = program_details[1]
    fleet_num = program_details[2]
    rides_num = program_details[3]
    bonus = program_details[4]
    steps = program_details[5]
    cars = []

    # STEP 2: CREATE CARS
    for i in range(1, fleet_num + 1):
        car = Car(i)
        cars.append(car)

    # STEP 3: CREATE RIDES & AVAILABLE RIDES
    for i in range(rides_num - 1):
        ride_details = Reader.parse_ride(rides[i])
        rides[i] = Ride(ride_details)

    #Car.set_available_rides(len(rides))

    # STEP 3: MAIN FUNCTIONALITY
    for i in range(steps):
        for car in cars:
            if car.is_available:
                car.findRide(rides)
            car.move()
