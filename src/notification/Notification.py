class Notification:
    """
    Gets custom user notification attributes from the database and compares them to newly acquired data from the API.
    """    

    def __init__(self, userId, dbAttributes: str):
        """
        Initializes the object and parses the string.

        Args:
            userId (int): Stores the user id so that a notification may be sent to them
            dbAttributes (str): Attribute string from database in format "magnitude:4.56-7.56;area:24.54,46.34,50;". The magnitude attribute will accept a float to a float of magnitude rating a user is interested in. The area is latitude, longitude, and radius.
        """    
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

    def compareToDatabase(self, magnitude: float, latitude: float, longitude: float) -> bool:
        """
        Will get the new results from the database and make a comparison to determine if a notification is to be sent.


        Args:
            magnitude (float): The magnitude of the event
            latitude (float): Latitude of the event
            longitude (float): Longitude of the event

        Returns:
            bool: Returns true if the new data matches the users notification, else will return false.
        """            
        if (magnitude < self.minMagnitude or magnitude > self.maxMagnitude):
             return False
        # elif distance calculation will go here
        else:
            return True