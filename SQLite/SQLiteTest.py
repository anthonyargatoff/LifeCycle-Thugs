# Import package
import sqlite3;

# create connection and cursor
con = sqlite3.connect("test.db");
cursor = con.cursor();

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


TestPersistence(cursor);
TestCreate(cursor);
