#import billboard

import sqlite3
from sqlite3 import Error

def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    return conn


def closeConnection(_conn, _dbFile):
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)


def dropTable(_conn, tableName):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")
    try:
        cur = _conn.cursor()
        cur.execute("DROP TABLE " + tableName)
        
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def createTableBillboard(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create billboard table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE billboard (\
        b_songkey decimal(2,0) not null, \
        b_artistkey decimal(2,0) not null, \
        b_yearkey decimal(2,0) not null, \
        b_rank decimal(2,0) not null)")

    except Error as e:
        print(e)

def populateBillboard(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
    try:
        cur = _conn.cursor()
        #cur.execute(
        #    "INSERT INTO billboard(b)")
    except Error as e:
        print(e)

def createTableArtist(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create artist table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE artist (\
        a_artistkey decimal(9,0) not null, \
        a_name char(100) not null, \
        a_about char(500) not null)")

    except Error as e:
        print(e)

def populateArtist(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
    try:
        file_path = "DataTotales.txt"
        with open(file_path, "r") as file:
            data = file.readlines()
        cur = _conn.cursor()
        k = 0
        n = "Work in progress"
        for line in data:
            parts = line.strip().split("' by ")
            if len(parts) == 2:
                artist = parts[1].strip()
                cur.execute(
                    "INSERT INTO artist(a_artistkey, a_name, a_about) VALUES (?, ?, ?)", (k, artist, n))
                k = k+1

    except Error as e:
        print(e)


def createTableAlbum(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create album table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE album (\
        al_artistkey decimal(9,0) not null, \
        al_songkey decimal(9,0) not null, \
        al_name char(100) not null)")

    except Error as e:
        print(e)

def createTableSong(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create song table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE song (\
        s_songkey decimal(9,0) not null, \
        s_releaseyearkey decimal(9,0) not null, \
        s_name char(100) not null)")

    except Error as e:
        print(e)

def populateSong(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Song")
    try:
        file_path = "DataTotales.txt"
        with open(file_path, "r") as file:
            data = file.readlines()
        cur = _conn.cursor()
        n = -1
        k = 0
        for line in data:
            parts = line.strip().split("' by ")
            if len(parts) == 2:
                name = parts[0].strip()
                cur.execute(
                    "INSERT INTO song(s_songkey, s_name, s_releaseyearkey) VALUES (?, ?, ?)", (k, name[5:], n))
                k = k+1
        
    except Error as e:
        print(e)

def createTableYear(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create year table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE year (\
        y_yearkey decimal(9,0) not null, \
        y_year decimal(9,0) not null)")

    except Error as e:
        print(e)

def populateYear(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
    try:
        cur = _conn.cursor()
        y = 2000
        k = 0
        for k in range(30):
            cur.execute(
                "INSERT INTO year(y_yearkey, y_year) VALUES (?, ?)", (k, y))
            y = y+1
            k = k+1
    except Error as e:
        print(e)

def createTableGenre(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create genre table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE genre (\
        g_genrekey decimal(9,0), \
        g_name char(100))")

    except Error as e:
        print(e)

def createTableGenrePrSong(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create genreprsong table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE genreprsong (\
        g_genrekey decimal(9,0) not null, \
        g_songkey decimal(9,0) not null)")

    except Error as e:
        print(e)

def main():
#    file_path = 'Data.txt'
#    with open(file_path, 'w') as file:
#        for i in range(2006, 2023):
#            chart = billboard.ChartData('hot-100-songs', year = i)
#            for row in chart:
#                file.write(str(i) + str(row)+'\n')
#sqlite3.connect('DatabaseTotalis.db')

    database = r"DatabaseTotalis.db"
    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn, "song")
        createTableBillboard(conn)
        createTableArtist(conn)
        createTableAlbum(conn)
        createTableSong(conn)
        createTableYear(conn)
        createTableGenre(conn)
        createTableGenrePrSong(conn)

        #populateBillboard
        populateArtist(conn)
        populateYear(conn)
        #populateAlbum
        populateSong(conn)
        
        #populateGenre
        #populateGenrePrSong
        

    closeConnection(conn, database)
if __name__ == '__main__':
    main()
