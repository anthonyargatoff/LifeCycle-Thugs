import requests
import json
import calendar
import os
from datetime import date
from datetime import timedelta
import time

class EarthquakeApi:
    """
    A class for manipulating data results from specified API (https://earthquake.usgs.gov/fdsnws/event/1/)
    """    
    def __init__(self, url):
        """
        Set url

        Args:
            url (string): URL of API.
        """        
        self.url = url

    def getAllDataJSON(self, startDate, endDate, fileLocation):
        """
        Gets API data in a .json file format up to the specified time in a specific file location.

        Args:
            startDate (string): Enter the start-date in yyyy-mm format
            endDate (string): Enter end-date in yyyy-mm format
            fileLocation (string): Specify file location
        """
        # Parse the end-month and end-year.
        endYear, endMonth = endDate.split("-")
        endYear = int(endYear)
        endMonth = int(endMonth)
        startYear, startMonth = startDate.split("-")
        startYear = int(startYear)
        startMonth = int(startMonth)

        for year in range(startYear, endYear + 1):
            for month in range(1, 13):
                if year == endYear and month > endMonth: # If the date is larger than the requested date, program stops
                    break
                if year == startYear and month < startMonth:
                    continue
                numberOfDays = calendar.monthrange(year, month)[1] # Return the number of days in the current month
                startDate = "{}-{:02d}-01".format(year, month)
                endDate = "{}-{:02d}-{}".format(year, month, numberOfDays)


                # Get requests for API
                response = requests.get("{}query?format=geojson&starttime={}&endtime={}".format(self.url, startDate, endDate)).json()

                # Create files with correct dates
                with open("{}/{}_{:02d}.json".format(fileLocation, year, month), "w") as outfile:
                    json.dump(response, outfile, indent=4)
        
    def getParsedDataJSON(self, startDate, endDate, fileLocation):
        """
        This method returns a condensed version of the API data, keeping most important data (time, location, strength, and a URL if more info is needed). If ran multiple times, it will replace the old json file with a newer version.

        Args:
            startDate (string): Enter the start-date in a yyyy-mm format
            endDate (string): Enter the end-date in a yyyy-mm format
            fileLocation (location): Specify location to save the json data.
        """        
        endYear, endMonth = endDate.split("-")
        endYear = int(endYear)
        endMonth = int(endMonth)
        startYear, startMonth = startDate.split("-")
        startYear = int(startYear)
        startMonth = int(startMonth)

        if os.path.exists("earthquakeJsonData/earthquakesParsed.json"):
            os.remove("earthquakeJsonData/earthquakesParsed.json")

        # Opens the json file for writing
        with open("{}/earthquakesParsed.json".format(fileLocation), "a") as outfile:

            first_object_written = False # Keeps track of where to put the json syntax characters
            for year in range(startYear, endYear + 1):
                for month in range(1, 13):
                    if year == endYear and month > endMonth: # If the date is larger than the requested date, program stops
                        break
                    numberOfDays = calendar.monthrange(year, month)[1] # gets the number of days in the current month
                    startDate = "{}-{:02d}-01".format(year, month)
                    endDate = "{}-{:02d}-{}".format(year, month, numberOfDays)
                    
                    try:
                        # Get requests for API
                        response = requests.get("{}query?format=geojson&starttime={}&endtime={}".format(self.url, startDate, endDate)).json()

                        # Parses the data we require
                        for feature in response["features"]:
                            properties = feature["properties"]
                            time = properties["time"] # in milliseconds
                            mag = properties["mag"]
                            title = properties["title"]
                            url = properties["detail"]
                            geometry = feature["geometry"]
                            longitude = geometry["coordinates"][0]
                            latitude = geometry["coordinates"][1]

                            jsonExport = {"title":title, "mag":mag, "time":time, "lat":latitude, "lon":longitude, "url":url}
                            
                            if not first_object_written:
                                outfile.write("[\n")
                                first_object_written = True
                            else:
                                outfile.write(",\n")

                            json.dump(jsonExport, outfile, indent=4)

                    except:
                        print("Error: cannot make get request")
                            
            # Close the file
            outfile.write("\n]")
            outfile.close()

    def getParsedDataTXT (self, startDate, endDate, fileLocation):
        """
        Get data from the api from a start date to end date and outputs as a txt file. 

        Args:
            startDate (string): Date in format yyyy-mm
            endDate (string): Date in format yyyy-mm
            fileLocation (string): Specify relative file location (ex: API/earthquakeData)
        """             
        endYear, endMonth = endDate.split("-")
        endYear = int(endYear)
        endMonth = int(endMonth)
        startYear, startMonth = startDate.split("-")
        startYear = int(startYear)
        startMonth = int(startMonth)

        if os.path.exists("earthquakeJsonData/earthquakesParsed.txt"):
            os.remove("earthquakeJsonData/earthquakesParsed.txt")

        # Opens the json file for writing
        with open("{}/earthquakesParsed.txt".format(fileLocation), "w") as outfile:

            for year in range(startYear, endYear + 1):
                for month in range(1, 13):
                    if year == endYear and month > endMonth: # If the date is larger than the requested date, program stops
                        break
                    numberOfDays = calendar.monthrange(year, month)[1] # gets the number of days in the current month
                    startDate = "{}-{:02d}-01".format(year, month)
                    endDate = "{}-{:02d}-{}".format(year, month, numberOfDays)

                    while 1: # Will keep trying to get data even if the ip is temporarily banned from making requests.
                        try:
                            # Get requests for API
                            response = requests.get("{}query?format=geojson&starttime={}&endtime={}".format(self.url, startDate, endDate)).json()
                            print("{}query?format=geojson&starttime={}&endtime={}".format(self.url, startDate, endDate))
                            
                            # Parses the data we require
                            for feature in response["features"]:
                                properties = feature["properties"]
                                event_time = properties["time"] # in milliseconds
                                mag = properties["mag"]
                                title = properties["title"]
                                url = properties["detail"]
                                geometry = feature["geometry"]
                                longitude = geometry["coordinates"][0]
                                latitude = geometry["coordinates"][1]
                                
                                outfile.write("{};{};{};{};{};{}\n".format(title, event_time, mag, latitude, longitude, url)) # Using ";" as the deliminator

                            break

                        except Exception as e:
                            print("Max query limit reached. Error: {}\nRetrying in 1 minute\n".format(e))
                            time.sleep(60)
                            
            # Close the file
            outfile.close()

    def getLast24Hours(self):
        """
        Get the API results for the last 2 days

        Returns:
            List: Returns a list of objects containing the earthquake data.
        """        
        
        data = [] # list to store the objects
        response = requests.get("{}query?format=geojson&starttime={}&endtime={}".format(self.url, (date.today() - timedelta(days = 1)), date.today())).json()

        for feature in response["features"]:
            properties = feature["properties"]
            time = properties["time"] # in milliseconds
            mag = properties["mag"]
            title = properties["title"]
            url = properties["detail"]
            geometry = feature["geometry"]
            longitude = geometry["coordinates"][0]
            latitude = geometry["coordinates"][1]

            jsonExport = {"title":title, "mag":mag, "time":time, "lat":latitude, "lon":longitude, "url":url}
            data.append(jsonExport)

        return data

x = EarthquakeApi("https://earthquake.usgs.gov/fdsnws/event/1/")
x.getParsedDataTXT("1920-01", "1920-01", "API/earthquakeData")