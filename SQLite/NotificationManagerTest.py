
# Import packages
import sqlite3;
import unittest;
import NotificationManager as NM;


class test_DBManager(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("TestNotify.db");
        self.con.execute("PRAGMA foreign_keys = 1");
        self.cursor = self.con.cursor();
        self.cursor.execute("Insert into notification(userid,attributes) values(2,'TestGet')");
        self.cursor.execute("Insert into notification(userid,attributes) values(2,'TestGet2')");
        self.cursor.execute("Insert into notification(userid,attributes) values(1,'TestDelete')");
        self.notify = NM.DBNotification("TestNotify.db");
        self.con.commit();

    def test_a_AddNotify(self):
        self.notify.addNotify('1', 'TestAdd');
        result = self.con.execute("Select attributes From notification where attributes = 'TestAdd'");
        self.assertEqual(result.fetchall(),[('TestAdd',)]);

    def test_b_GetUsersNotifications(self):
        result = self.notify.getUsersNotifications('2');
        self.assertEqual(result,[(1,'TestGet'),(2,'TestGet2')]);
    
    def test_c_DeleteNotify(self):
        self.notify.deleteNotify('3');
        result = self.con.execute('Select attributes From notification where notifyid = 3');
        self.assertEqual(result.fetchall(),[]);
    
    

    def tearDown(self):
        self.cursor.execute("Delete From notification Where attributes = 'TestAdd'");
        self.cursor.execute("Delete From notification Where attributes = 'TestDelete'");
        self.cursor.execute("Delete From notification Where userid = 2");
        self.con.commit()
        self.con.close();

unittest.main();