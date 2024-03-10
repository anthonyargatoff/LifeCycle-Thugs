
import sqlite3

class DBUser():

    DATABASE = "QuakeBase.db"

    # Create a new tuple in user table with values email, password
    def addUser(email, password):
        try:
            con = sqlite3.connect("QuakeBase.db");
            cursor = con.cursor();
            SQL = 'Insert Into user(email,password) values(\'%s\',\'%s\')'  % (email,password);
            cursor.execute(SQL);
        except:
            print("transaction failed");
    
    # Delete user tuple based on email
    def deleteUser(email):
        try:
            con = sqlite3.connect("QuakeBase.db");
            cursor = con.cursor();
            SQL = 'Delete From user Where email Like \'%s\''  % (email);
            cursor.execute(SQL);
        except:
            print("transaction failed");

    # modify user's email/password based on their userid, which must first be retrieved.
    # if only one field needs modifying, just pass the other as it was retrieved from the database  
    def modifyUser(id, newEmail, newPassword):
        try:
            con = sqlite3.connect("QuakeBase.db");
            cursor = con.cursor();
            SQL = 'Update user Set email = \'%s\', password = \'%s\' Where id = %s '  % (newEmail,newPassword,id);
            cursor.execute(SQL);
        except:
            print("transaction failed");

    # return true if email/password combo is found in DB, else false. Also false on exception, so we can prompt user to try again.
    def validateUser(email,password):
        try:
            con = sqlite3.connect("QuakeBase.db");
            cursor = con.cursor();
            SQL = 'Select email, password From user Where email = \'%s\' and password = \'%s\''  % (email,password);
            result = cursor.execute(SQL);
            list = result.fetchall()
            if (len(list)) != 2: 
                return False;
            if (list[0] == email and list[1] == password):
                return True;
            else: return False;
        except:
            print("transaction failed");
            return False;


class DBEvent():

    def addEvent():
        try: 
            con = sqlite3.connect("QuakeBase.db");
            cursor = con.cursor();
        except:
            print()






