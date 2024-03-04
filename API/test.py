import unittest
import json
from  EarthquakeApi import EarthquakeApi

class test_Api(unittest.TestCase):

    testDataFilepath = "testdata"

    def setUp(self):
         self.e = EarthquakeApi('https://earthquake.usgs.gov/fdsnws/event/1/')

    def test_getAllData(self):

        self.e.getAllData("1568-01", "1568-01", "testdata")

        with open("testdata/getAllDataTest.json", "r") as f1:
            data1 = json.load(f1)
        
        with open("testdata/1568_01.json", "r") as f2:
            data2 = json.load(f2)

        self.assertEqual(data1["features"][0]["id"], data2["features"][0]["id"])

    def test_getParsedData(self):
        self.e.getParsedData("1568-01", "1568-01", "testdata")

        with open("testdata/getParsedDataTest.json", "r") as f:
            data1 = json.load(f)
        with open("testdata/getParsedDataTest.json", "r") as f:
            data2 = json.load(f)
        
        self.assertEqual(data1[0]["title"], data2[0]["title"])

    def test_fetLast24Hours(self):
        self.assertTrue(self.e.getLast24Hours())

unittest.main()