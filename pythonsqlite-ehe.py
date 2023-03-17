import sqlite3

##def readSqliteTable():
##    try:
##        sqliteConnection = sqlite3.connect('activity3.db')
##        cursor = sqliteConnection.cursor()
##        print("Connected to SQLite")
##
##        sqlite_select_query = """SELECT * from tblusers"""
##        cursor.execute(sqlite_select_query)
##        records = cursor.fetchall()
##        print("Total rows are:  ", len(records))
##        print("Printing each row")
##        a=1
##        for row in records:
##            print(a," - ", row[0], " - " , row[1], " - " , row[2] )
####            print("Password: ", row[1])
####            print("Level: ", row[2])
####            print("\n")
##            a=a+1
##        cursor.close()
##
##    except sqlite3.Error as error:
##        print("Failed to read data from sqlite table", error)
##    finally:
##        if sqliteConnection:
##            sqliteConnection.close()
##            print("The SQLite connection is closed")
##
##readSqliteTable()






##try:
##    sqliteConnection = sqlite3.connect('activity3.db')
##    cursor = sqliteConnection.cursor()
##    print("Successfully Connected to SQLite")
##
##    sqlite_insert_query = """INSERT INTO tblusers
##                          (uname, upassword, ulevel) 
##                           VALUES 
##                          ('cailing','faith','admin')"""
##
##    count = cursor.execute(sqlite_insert_query)
##    sqliteConnection.commit()
##    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
##    cursor.close()
##
##except sqlite3.Error as error:
##    print("Failed to insert data into sqlite table", error)
##finally:
##    if sqliteConnection:
##        sqliteConnection.close()
##        print("The SQLite connection is closed")




try:
    sqliteConnection = sqlite3.connect('mylabs.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO tblusers
                          (lname, gender, fling) 
                           VALUES 
                          ('cailing','boy','serious')"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")






##try:
##    sqliteConnection = sqlite3.connect('mylabs.db')
##    sqlite_create_table_query = '''CREATE TABLE tblusers (
##                                lname TEXT PRIMARY KEY,
##                                gender TEXT NOT NULL,
##                                fling TEXT NOT NULL 
##                                );'''
##
##    cursor = sqliteConnection.cursor()
##    print("Successfully Connected to SQLite")
##    cursor.execute(sqlite_create_table_query)
##    sqliteConnection.commit()
##    print("SQLite table created")
##
##    cursor.close()
##
##except sqlite3.Error as error:
##    print("Error while creating a sqlite table", error)
##finally:
##    if sqliteConnection:
##        sqliteConnection.close()
##        print("sqlite connection is closed")

























##import sqlite3
##
##try:
##    sqliteConnection = sqlite3.connect('activity3.db')
##    cursor = sqliteConnection.cursor()
##    print("Database created and Successfully Connected to SQLite")
##
##    sqlite_select_Query = "select sqlite_version();"
##    cursor.execute(sqlite_select_Query)
##    record = cursor.fetchall()
##    print("SQLite Database Version is: ", record)
##    cursor.close()
##
##except sqlite3.Error as error:
##    print("Error while connecting to sqlite", error)
##finally:
##    if sqliteConnection:
##        sqliteConnection.close()
##        print("The SQLite connection is closed")
