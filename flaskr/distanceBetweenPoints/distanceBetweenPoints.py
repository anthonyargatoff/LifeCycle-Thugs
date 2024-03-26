import math

class coordinateCalculator:

    """
    Use class to calculate coordinate distances.

    Can return a metric (kilometer) or imperial (miles) value
    """    
    
    @staticmethod
    def getDistanceKilometers(latitude1:float, longitude1:float, latitude2:float, longitude2:float):
        """
        This method returns the distance between two coordinates in kilometers

        Args:
            latitude1 (float): First latitude coordinate
            longitude1 (float): First longitude coordinate
            latitude2 (float): Second latitude coordinate
            longitude2 (float): Second longitude coordinate

        Returns:
            Float: Returns distance in kilometers as a float
        """        
        return coordinateCalculator.__getDistance(latitude1, longitude1, latitude2, longitude2)

    @staticmethod
    def getDistanceMiles(latitude1:float, longitude1:float, latitude2:float, longitude2:float):
        """
        This method returns the distance between two coordinates in miles

        Args:
            latitude1 (float): First latitude coordinate
            longitude1 (float): First longitude coordinate
            latitude2 (float): Second latitude coordinate
            longitude2 (float): Second longitude coordinate

        Returns:
            Float: Returns distance in miles as a float
        """        
        return coordinateCalculator.__getDistance(latitude1, longitude1, latitude2, longitude2) / 1.60934

    def __getDistance(latitude1:float, longitude1:float, latitude2:float, longitude2:float):

        """
        Gets the distance. Use of a private method so that we can return both kilometers and miles, if wanted. 

        Raises:
            ValueError: If coordinates are invalid (latitude: -90 - 90, longitude: -180 - 180) will raise ValueError exception.

        Returns:
            Float: Returns distance in kilometers.
        """    
        # Error handling if input is bad
        if not (-90 <= latitude1 <= 90) or not (-90 <= latitude2 <= 90) or not (-180 <= longitude1 <= 180) or not (-180 <= longitude2 <= 180):
            raise ValueError("Latitude and longitude must be within valid range (-90 to 90 for latitude, -180 to 180 for longitude)")
        
        earthRadius = 6371 # kilometers
        # Convert degrees to radians.
        latitude1 = math.radians(latitude1)
        longitude1 = math.radians(longitude1)
        latitude2 = math.radians(latitude2)
        longitude2 = math.radians(longitude2)

        # Haversine formula
        latitudeDifference = latitude2 - latitude1
        longitudeDifference = longitude2 - longitude1
        a = math.sin(latitudeDifference / 2) ** 2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(longitudeDifference / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        distance = earthRadius * c

        return distance