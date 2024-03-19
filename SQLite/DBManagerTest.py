
# Import package
import sqlite3;
import unittest;
import DBManager as DBM;

class test_DBManager(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("TestUser.db");
        self.cursor = self.con.cursor();
        self.cursor.execute("Insert into user(email,password) values('AAAA','BBBB')");
        self.cursor.execute("Insert into user(email,password) values('CCCC','DDDD')");
        self.con.commit();
        self.User = DBM.DBUser("TestUser.db");
    
    def test_a_ValidateUser(self):
        self.assertTrue(self.User.validateUser('CCCC','DDDD'));

    def test_b_AddUser(self):
        self.User.addUser('Sample@test.com','BadPassword');
        self.assertTrue(self.User.validateUser('Sample@test.com','BadPassword'));
    
    def test_c_DeleteUser(self):
        self.User.deleteUser('AAAA');
        result = self.cursor.execute("Select * From user Where email = 'AAAA'");
        self.assertEqual(result.fetchone(), None);
    
    def test_d_ModifyUser(self):
        self.User.modifyUser(2,'changed','alsochanged');
        self.assertTrue(self.User.validateUser('changed','alsochanged'));
        self.User.modifyUser(2,'aaaaa','bbbbbb');
    
    def test_e_SelectUserId(self):
        id = self.User.selectUserId('CCCC');
        self.assertEqual(id[0],4)

    def tearDown(self):
        self.cursor.execute("Delete From user Where email = 'Sample@test.com'");
        self.cursor.execute("Delete From user Where email = 'CCCC'");
        self.cursor.execute("Delete From user Where email = 'AAAA'");
        self.con.commit();
        self.con.close();



unittest.main();

