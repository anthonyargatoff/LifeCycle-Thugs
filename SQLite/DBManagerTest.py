

# Import package
import sqlite3;
import unittest;
import DBManager as DBM;


class test_DBManager(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("QuakeBase.db");
        self.cursor = self.con.cursor();
        self.cursor.execute("Insert into user(email,password) values('AAAA','BBBB')");
        self.cursor.execute("Insert into user(email,password) values('CCCC','DDDD')");

    def test_AddUser(self):
        DBM.DBUser.addUser('Sample@test.com','BadPassword');
        self.assertTrue(DBM.DBUser.validateUser('Sample@test.com','BadPassword'));
   #     result = self.cursor.execute("Select email, password From user Where email = 'Sample@test.com'");
    #    self.assertEqual(result.fetchall(), [('Sample@test.com', 'BadPassword')]);

    def test_ValidateUser(self):
        self.assertTrue(DBM.DBUser.validateUser('CCCC','DDDD'));

    def test_DeleteUser(self):
        DBM.DBUser.deleteUser('AAAA');
        result = self.cursor.execute("Select * From user Where email = 'AAAA'");
        self.assertEqual(result.fetchone(), [()]);

    def tearDown(self):
        self.cursor.execute("Delete From user Where email = 'Sample@test.com'");

        self.con.close();



unittest.main();

