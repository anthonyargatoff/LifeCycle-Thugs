import unittest
import json
from  EarthquakeApi import EarthquakeApi
import os

class test_Api(unittest.TestCase):

    def setUp(self):
         self.e = EarthquakeApi('https://earthquake.usgs.gov/fdsnws/event/1/')

    def test_getAllJSONData(self):

        self.e.getAllDataJSON("1568-01", "1568-01", "API/testdata")

        with open("API/testdata/getAllDataTest.json", "r") as f1:
            data1 = json.load(f1)
        
        with open("API/testdata/1568_01.json", "r") as f2:
            data2 = json.load(f2)

        self.assertEqual(data1["features"][0]["id"], data2["features"][0]["id"])
        os.remove("API/testdata/1568_01.json")
       

    def test_getParsedDataJSON(self):
        self.e.getParsedDataJSON("1568-01", "1568-01", "API/testdata")

        with open("API/testdata/getParsedDataTest.json", "r") as f:
            data1 = json.load(f)
        with open("API/testdata/getParsedDataTest.json", "r") as f:
            data2 = json.load(f)
        
        self.assertEqual(data1[0]["title"], data2[0]["title"])
        os.remove("API/testdata/earthquakesParsed.json")


    def test_getParsedDataTXT(self):
        self.e.getParsedDataTXT("1568-01", "1568-01", "API/testdata")

        with open("API/testdata/getParsedDataTest.txt") as f:
            data1 = f.read()
        with open("API/testdata/earthquakesParsed.txt") as f:
            data2 = f.read()

        self.assertEqual(data1, data2)
        os.remove("API/testdata/earthquakesParsed.txt")


    def test_getLast24Hours(self):
        self.assertTrue(self.e.getLast24Hours())


unittest.main()