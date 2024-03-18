# SQLite3

## Setup

### Windows

1. From https://www.sqlite.org/download.html
    -sqlite-dll-win-x86-3450100
    -sqlite-tools-win-x64-3450100

1. Run sqlite3.exe (inside sqlite-tools-win-x64-3450100)
    - open database file with .open FILENAME (.open ../test.db)
    - If a non existent filename is given, it will be created
    - if no name specified creates a temp database that is deleted at the end of the session.

1. Standard SQL syntax. (REQUIRES ; to terminate statement)
    -- currently has
    create table T1(id Integer, name Varchar(50));
    insert into T1 values(1, 'first');
    insert into T1 values(2, 'second');

    For python, use sqlite3 package, https://docs.python.org/3/library/sqlite3.html

### Linux

#### Using Linux Binaries

1. Go to https://www.sqlite.org/download.html
1. Download the linux binaries
1. Add to path, use `sqlite3 test` to create a test database

#### Using package manager

1. Use package manager to download. For debian machines, use `sudo apt install sqlite3`
1. Create a test database with `sqlite3 test`

## Useful commands: 
- .tables (list tables)
- .help (list . commands)
- .changes on|off (toggle whether system outputs numberof rows - changed by a command)
- .quit (exit shell)

## Schema
The schema for the database is the _databaseSchema.sql_ file. It contains a table for earthquakes, users, and notifications.

## Files
- DBManager.py contains database interactivity functionality, such as adding, removing and editing users.
- populateDatabase.py contains class to add data from a txt file to the database
- test.db is a test database, used for unit testing.
