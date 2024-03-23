import sqlite3;
import unittest;
from populateDatabase import populateDb

class test(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("test.db")
        self.cursor = self.con.cursor()

    # Test the populateDatabase.py adding from text file works as expected
    def test_InsertFromTextFile(self):
        self.cursor.execute('CREATE TABLE earthquakesTest (id INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR(50),time BIGINT,magnitude decimal (2, 4),latitude decimal (3, 6),longitude decimal (3, 6), url varchar(200));')
        x = populateDb('test.db', 'API/testdata/multipleLinesTest.txt')
        x.populateAllTxtData("earthquakesTest")
        result = self.cursor.execute("SELECT latitude FROM earthquakesTest WHERE id=4")
        self.assertEqual(result.fetchall(), [(40.059,)])
        self.cursor.execute("DROP TABLE earthquakesTest;")

    def tearDown(self):
        self.con.close()

unittest.main()