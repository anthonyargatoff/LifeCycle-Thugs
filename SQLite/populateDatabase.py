import sqlite3

class populateDb:
    """
    Populates the database from data file.
    """    
    def __init__(self, dbFileLocation, txtFileLocation):
        """
        Initialize the class.

        Args:
            dbFileLocation (string): File location for the database.
            txtFileLocation (string): File location for the txt file.
        """        
        self.dbFileLocation = dbFileLocation
        self.txtFileLocation = txtFileLocation 

    def populateAllTxtData(self, databaseTableName):     
        con = sqlite3.connect(self.dbFileLocation)
        cursor = con.cursor()

        with open(self.txtFileLocation, 'r') as f:
            lines = f.readlines()

            for line in lines:
                split = line.split(';') # split into array of 6
                title = split[0]
                time = split[1]
                magnitude = split[2]
                latitude = split[3]
                longitude = split[4]
                url = split[5].strip() # remove \n character
                sql = 'INSERT INTO {} (title, time, magnitude, latitude, longitude, url) VALUES(?, ?, ?, ?, ?, ?)'.format(databaseTableName)

                cursor.execute(sql, (title, time, magnitude, latitude, longitude, url))

            con.commit()

            f.close()
