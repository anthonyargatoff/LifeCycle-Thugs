

# Import package
import sqlite3;
import unittest;
import DBManager as DBM;


class test_DBManager(unittest.TestCase):

 #   def setUp(self):
 #       self.con = sqlite3.connect("QuakeBase.db");
 #       self.cursor = self.con.cursor();

    def test_AddUser(self):
        DBM.DBUser.addUser('Sample@test.com','BadPassword');
        
        con = sqlite3.connect("QuakeBase.db");
        cursor = con.cursor();

        result = cursor.execute("Select email, password From user Where email = 'Sample@test.com'");
        self.assertEqual(result.fetchall(), [('Sample@test.com', 'BadPassword')]);
        cursor.execute("Delete From user Where email = 'Sample@test.com'");
        con.close();

    def test_DeleteUser(self):
                
        con = sqlite3.connect("QuakeBase.db");
        cursor = con.cursor();

        cursor.execute("Insert into user(email,password) values('AAAA','BBBB')");
        con.close();

        DBM.DBUser.deleteUser('AAAA');

                
        con = sqlite3.connect("QuakeBase.db");
        cursor = con.cursor();
        result = cursor.execute("Select * From user Where email = 'AAAA'");
        self.assertEqual(result.fetchone(), [()]);
        con.close();

#    def tearDown(self):
 #       self.con.close();

unittest.main();

