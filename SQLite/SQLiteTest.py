# Import package
import sqlite3;
import unittest;
from populateDatabase import populateDb

class test_SQLite(unittest.TestCase):

    # create connection and cursor
    def setUp(self):
        self.con = sqlite3.connect("test.db");
        self.cursor = self.con.cursor();


    #no test for just select, but all tests use select.

    # Test that pre-existing table still exists
    def test_Persistence(self):
        result = self.cursor.execute("Select * From T1");
        self.assertEqual(result.fetchall(),[(1, 'first'), (2, 'second')]);

    # Test that creating tables works
    def test_Create(self):
        self.cursor.execute('Create Table testTable(id Integer)');
        result = self.cursor.execute("Select name From sqlite_master Where name='testTable'");
        self.assertEqual(result.fetchone(), ('testTable',));
        self.cursor.execute('Drop Table testTable');

    # Test that adding rows works
    def test_Insert(self):
        self.cursor.execute("Insert Into T1 values(5,'fifth'),(6,'sixth'),(7,'seventh')");
        result = self.cursor.execute("Select * From T1 Where id > 3");
        self.assertEqual(result.fetchall(), [(5, 'fifth'), (6, 'sixth'), (7, 'seventh')]);
        self.cursor.execute("Delete From T1 Where id > 3");
    
    # Test the populateDatabase.py adding from text file works as expected
    def test_InsertFromTextFile(self):
        self.cursor.execute('CREATE TABLE earthquakesTest (id INTEGER PRIMARY KEY AUTOINCREMENT,title VARCHAR(50),time BIGINT,magnitude decimal (2, 4),latitude decimal (3, 6),longitude decimal (3, 6), url varchar(200));')
        x = populateDb('test.db', '../API/testdata/multipleLinesTest.txt')
        x.populateAllTxtData("earthquakesTest")
        result = self.cursor.execute("SELECT latitude FROM earthquakesTest WHERE id=4")
        self.assertEqual(result.fetchall(), [(40.059,)])
        self.cursor.execute("DROP TABLE earthquakesTest;")
    
    def tearDown(self):
        self.con.close();

unittest.main();
