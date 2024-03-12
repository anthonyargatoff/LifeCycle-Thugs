
import sqlite3

class DBUser():

    def __init__(self, dbLocation):
        self.dbLocation = dbLocation;

    # Create a new tuple in user table with values email, password
    def addUser(self, email, password):
        try:
            con = sqlite3.connect(self.dbLocation);
            cursor = con.cursor();
            params = (email, password);
            SQL = "Insert Into user(email,password) values(?,?)";
            cursor.execute(SQL, params);
            con.commit();
            con.close();
        except Exception as e:
            print("transaction failed: ");
            print(e);
    
    # Delete user tuple based on email
    def deleteUser(self, email):
        try:
            con = sqlite3.connect(self.dbLocation);
            cursor = con.cursor();
            params = (email,);
            SQL = 'Delete From user Where email Like ?';
            cursor.execute(SQL,params);
            con.commit();
            con.close();
        except Exception as e:
            print("transaction failed: ");
            print(e);

    # modify user's email/password based on their userid, which must first be retrieved.
    # if only one field needs modifying, just pass the other as it was retrieved from the database  
    def modifyUser(self, id, newEmail, newPassword):
        try:
            con = sqlite3.connect(self.dbLocation);
            cursor = con.cursor();
            params = (newEmail, newPassword, id);
            SQL = 'Update user Set email = ?, password = ? Where userid = ? ';
            cursor.execute(SQL,params);
            con.commit();
            con.close();
        except Exception as e:
            print("transaction failed: ");
            print(e);

    # return true if email/password combo is found in DB, else false. Also false on exception, so we can prompt user to try again.
    def validateUser(self, email,password):
        try:
            con = sqlite3.connect(self.dbLocation);
            cursor = con.cursor();
            params = (email, password);
            SQL = 'Select email, password From user Where email = ? and password = ?';
            result = cursor.execute(SQL, params);
            list = result.fetchall();
            con.close();
            if (len(list)) != 1: 
                return False;
            if (list[0][0] == email and list[0][1] == password):
                return True;
            else: return False;
        except Exception as e:
            print("transaction failed: ");
            print(e);
            return False;

    # Select a users id by email(username). Return False if no user found, else return the id.
    # Not sure if we need this. We could instead usse email as primary key and drop id. 
    # But as long as we have an id we should have a way to access it.
    def selectUserId(self, email):
        try:
            con = sqlite3.connect(self.dbLocation);
            cursor = con.cursor();
            params = (email,);
            SQL = "Select userid From user Where email = ?";
            result = cursor.execute(SQL,params);
            return result.fetchone();
        except Exception as e:
            print("transaction failed: ");
            print(e);
            return False;



