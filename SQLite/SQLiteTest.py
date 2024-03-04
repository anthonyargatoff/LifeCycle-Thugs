# Import package
import sqlite3;

# create connection and cursor
con = sqlite3.connect("test.db");
cursor = con.cursor();

#no test for just select, but all tests use select.

# Test that pre-existing table still exists
def TestPersistence(cursor):
    result = cursor.execute("Select * From T1");
    answer = result.fetchall()
    if (answer == [(1, 'first'), (2, 'second')]):
        print('Passed Persistence')
    else: print('Failed Persistence');

# Test that creating tables works
def TestCreate(cursor):
    cursor.execute('Create Table testTable(id Integer)');
    result = cursor.execute("Select name From sqlite_master Where name='testTable'");
    ans = result.fetchone()
    if (ans == ('testTable',)):
        print('Passed Create');
        cursor.execute('Drop Table testTable');
    else: print('Failed Create');

# Test that adding rows works
def TestInsert(cursor):
    cursor.execute("Insert Into T1 values(5,'fifth'),(6,'sixth'),(7,'seventh')");
    result = cursor.execute("Select * From T1 Where id > 3");
    ans = result.fetchall()
    if (ans == [(5, 'fifth'), (6, 'sixth'), (7, 'seventh')]):
        print('Passed Insert');
        cursor.execute("Delete From T1 Where id > 3");
    else: print('Failed Insert');

TestPersistence(cursor);
TestCreate(cursor);
TestInsert(cursor);

con.close();
