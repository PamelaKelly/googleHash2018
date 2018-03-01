from hashCode2018.reader import Reader
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
    
    # 
    