import sqlite3;
import unittest;
#from populateDatabase import populateDb
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from flaskr import populateDatabase


class test(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("test.db")
        self.cursor = self.con.cursor()
        self.cursor.execute('CREATE TABLE earthquakesTest (id INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR(50),time BIGINT,magnitude decimal (2, 4),latitude decimal (3, 6),longitude decimal (3, 6), url varchar(200));')

    # Test the populateDatabase.py adding from text file works as expected
    def test_InsertFromTextFile(self):
        x = populateDatabase.populateDb('test.db', '../API/testdata/multipleLinesTest.txt')
        x.populateAllTxtData("earthquakesTest")
        result = self.cursor.execute("SELECT latitude FROM earthquakesTest WHERE id=4")
        self.assertEqual(result.fetchall(), [(40.059,)])


    def tearDown(self):
        self.cursor.execute("DROP TABLE earthquakesTest;")
        self.con.close()

unittest.main()