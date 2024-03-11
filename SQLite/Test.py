import sqlite3;
import DBManager as DBM;


# test validate
print('Running');
if DBM.DBUser.validateUser('aaaa','aaaaa'):
    print('Passed Validate');
else: print('Failed Validate');

# test add
DBM.DBUser.addUser('Sample@test.com','BadPassword');
if DBM.DBUser.validateUser('Sample@test.com','BadPassword'):
    print('Passed Add');
else: print('Failed Add');

# test Delete
DBM.DBUser.deleteUser('Sample@test.com');
if DBM.DBUser.validateUser('Sample@test.com','BadPassword'):
    print('Failed Delete');
else: print('Passed Delete');

# test select user id
id = DBM.DBUser.selectUserId('aaaa');
if (id[0] == 1):
    print('Passed Id Select');
else: print('Failed Id Select');

# test modify user
DBM.DBUser.modifyUser(2,'changed','alsochanged');
if DBM.DBUser.validateUser('changed','alsochanged'):
    print('Passed Modify');
else: print('Failed Modify');

DBM.DBUser.modifyUser(2,'aaaaa','bbbbbb');



