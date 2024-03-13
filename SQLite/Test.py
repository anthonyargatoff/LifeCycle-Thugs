import sqlite3;
import DBManager;

x = DBManager.DBUser('QuakeBase.db');

# test validate
print('Running');
if x.validateUser('aaaa','aaaaa'):
    print('Passed Validate');
else: print('Failed Validate');

# test add
x.addUser('Sample@test.com','BadPassword');
if x.validateUser('Sample@test.com','BadPassword'):
    print('Passed Add');
else: print('Failed Add');

# test Delete
x.deleteUser('Sample@test.com');
if x.validateUser('Sample@test.com','BadPassword'):
    print('Failed Delete');
else: print('Passed Delete');

# test select user id
id = x.selectUserId('aaaa');
if (id[0] == 1):
    print('Passed Id Select');
else: print('Failed Id Select');

# test modify user
x.modifyUser(2,'changed','alsochanged');
if x.validateUser('changed','alsochanged'):
    print('Passed Modify');
else: print('Failed Modify');

x.modifyUser(2,'aaaaa','bbbbbb');



