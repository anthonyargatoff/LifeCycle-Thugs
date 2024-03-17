class Notification:

    def __init__(self, userId, dbAttributes: str):

        # Define all the variables, then check if they exist
        self.minMagnitude = None
        self.maxMagnitude = None
        self.latitude = None
        self.longitude = None
        self.radius = None
        
        # parse the string with ; as deliminator
        splitString = dbAttributes.split(";")

        for element in splitString:
            #check if magnitude exists, and then assigns it 
            if "magnitude" in element:
                magnitudeSplit = element.split(":")
                magnitudeRange = magnitudeSplit[1].split("-")
                self.minMagnitude, self.maxMagnitude = float(magnitudeRange[0]), float(magnitudeRange[1])

            # check if area exists
            if "area" in element:
                areaSplit = element.split(":")
                location = areaSplit[1].split(",")
                self.latitude, self.longitude, self.radius = float(location[0]), float(location[1]), float(location[2])

    def compareToDatabase(self, magnitude, latitude, longitude, radius) -> bool:
        if (magnitude < self.minMagnitude or magnitude > self.maxMagnitude):
             return False
        else:
            return True