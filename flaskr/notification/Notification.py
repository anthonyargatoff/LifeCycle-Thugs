from flaskr.distanceBetweenPoints.distanceBetweenPoints import coordinateCalculator

class Notification:

    def __init__(self, dbAttributes: str):

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

    def isMagnitudeSet(self)->bool:
        return (self.maxMagnitude != None and self.minMagnitude !=None)
    
    def isDistanceSet(self)->bool:
        return (self.latitude != None and self.longitude != None and self.radius != None)
    
    def compareMagnitude(self, magnitude)->bool:
           return (magnitude > self.minMagnitude and magnitude < self.maxMagnitude)

    def compareDistance(self, latitude, longitude)->bool:
        return (coordinateCalculator.getDistanceKilometers(self.latitude, self.longitude, latitude, longitude) <= self.radius)

    def compareNewEvent(self, magnitude, latitude, longitude) -> bool:
        # print ("magnitude set{}\n------\ndistance set {}".format(self.isMagnitudeSet(), self.isDistanceSet()))

        if (self.isMagnitudeSet() and not self.isDistanceSet()):
            if(magnitude):
                return self.compareMagnitude(magnitude)
            else:
                return False
        
        elif (not self.isMagnitudeSet() and self.isDistanceSet()):
            if (latitude and longitude):
                return self.compareDistance(latitude, longitude)
            else:
                return False

        elif (self.isDistanceSet() and self.isDistanceSet()):

            magnitudeBool = False
            distanceBool = False

            if (magnitude):
                magnitudeBool = self.compareMagnitude(magnitude)

            if (latitude and longitude):
                distanceBool = self.compareDistance(latitude, longitude)

            return (magnitudeBool and distanceBool)
        
        else:
            return False

        
        
        
    