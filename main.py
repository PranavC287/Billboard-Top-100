#import billboard

import sqlite3
from sqlite3 import Error
import random

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
    print("Drop table " + tableName)
    try:
        cur = _conn.cursor()
        cur.execute("DROP TABLE " + tableName)
        
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def createEverything(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create billboard table")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''CREATE TABLE everything (
        song char(100) not null,
        artist char(100) not null,
        year decimal(2,0) not null)''')

    except Error as e:
        print(e)

def populateEverything(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
    try:
        file_path = "DataTotales.txt"
        #file_path = "tester.txt"

        with open(file_path, "r") as file:
            data = file.readlines()
        cur = _conn.cursor()
        k = 0
        n = "Work in progress"
        for line in data:
            parts = line.strip().split("' by ")
            if len(parts) == 2:
                name = parts[0].strip()
                artist = parts[1].strip()
                cur.execute(
                    "INSERT INTO everything(song, artist, year) values(?, ?, ?)", (name[5:], artist, name[0:4],))
                k = k+1

    except Error as e:
        print(e)

def createTableBillboard(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create billboard table")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''CREATE TABLE billboard (
        b_rank decimal(2,0) not null,
        b_songkey decimal(2,0) not null,
        b_artistkey decimal(2,0) not null, 
        b_yearkey decimal(2,0) not null)''')

    except Error as e:
        print(e)

def populateBillboard(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
    try:
        cur = _conn.cursor()
        cur.execute(
            '''
            INSERT INTO billboard(b_rank, b_songkey, b_artistkey, b_yearkey)
            SELECT row_number() over (PARTITION BY year)-1 AS Rank, row_number() over () -1 AS s_key,
            (
            SELECT COUNT(*)
            FROM everything e2
            WHERE e2.artist <= e1.artist
            AND e2.artist <> e1.artist
            ) AS a_key,
            (
            SELECT COUNT(*)
            FROM everything e2
            WHERE e2.year <= e1.year
            AND e2.year <> e1.year
            )/100 AS y_key
            FROM everything e1
            ''')
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
        a_name char(100) not null UNIQUE, \
        a_about char(500) not null)")

    except Error as e:
        print(e)

def populateArtist(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate artist table")
    try:
        cur = _conn.cursor()
        cur.execute(
            '''
            INSERT OR IGNORE INTO artist(a_artistkey, a_name, a_about)
            SELECT
            (
            SELECT COUNT(*)
            FROM everything e2
            WHERE e2.artist <= e1.artist
            AND e2.artist <> e1.artist
            ) AS a_key, artist, 'Work in progress' 
            FROM everything e1
            ''')

    except Error as e:
        print(e)


def createTableAlbum(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create album table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE album (\
        al_songkey decimal(9,0) not null,\
        al_artistkey decimal(9,0) not null,\
        al_name char(100) not null,\
        FOREIGN KEY (al_artistkey) REFERENCES artist (a_artistkey),\
        FOREIGN KEY (al_songkey) REFERENCES song (s_songkey))")

    except Error as e:
        print(e)

def populateAlbum(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate album table")
    try:
        cur = _conn.cursor()
        cur.execute(
            '''
            INSERT INTO album(al_songkey, al_artistkey, al_name)
            SELECT row_number() over () AS s_key, 
            (
            SELECT COUNT(*)
            FROM everything e2
            WHERE e2.artist <= e1.artist
            AND e2.artist <> e1.artist
            ) AS a_key, 'WiP' 
            FROM everything e1
            ''')
    except Error as e:
        print(e)

def createTableSong(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create song table")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        CREATE TABLE song (
        s_songkey decimal(9,0) not null,
        s_name char(100) not null,
        s_releaseyearkey decimal(9,0) not null)''')

    except Error as e:
        print(e)

def populateSong(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate song table")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        INSERT INTO song(s_songkey, s_name, s_releaseyearkey)
        SELECT row_number() over ()-1 AS s_key, 
        song,
        (
        SELECT COUNT(*)
        FROM everything e2
        WHERE e2.year <= e1.year
        AND e2.year <> e1.year
        )/100 AS y_key
        FROM everything e1
        ''')
        
    except Error as e:
        print(e)

def createTableYear(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create year table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE year (\
        y_yearkey decimal(9,0) not null PRIMARY KEY, \
        y_year decimal(9,0) not null)")

    except Error as e:
        print(e)

def populateYear(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate year table")
    try:
        cur = _conn.cursor()
        y = 2006
        k = 0
        for k in range(20):
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

def populateGenre(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate genre table")
    try:
        file_path = "genre.txt"

        with open(file_path, "r") as file:
            data = file.readlines()
        cur = _conn.cursor()
        i = 0
        for k in data:
            cur.execute(
                "INSERT INTO genre(g_genrekey, g_name) VALUES (?, ?)", (i, k))
            i=i+1
    except Error as e:
        print(e)

def createTableGenrePrSong(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create genreprsong table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE genreprsong (\
        gs_genrekey decimal(9,0) not null, \
        gs_songkey decimal(9,0) not null)")

    except Error as e:
        print(e)

def populateGenrePrSong(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate genreprsong table")
    try:
        cur = _conn.cursor()
        i = random.randint(0, 48)
        for k in range(0, 1697):
            cur.execute(
                "INSERT INTO genreprsong(gs_genrekey, gs_songkey) VALUES (?, ?)", (i, k))
            i = random.randint(0, 48)

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
        dropTable(conn, "album")
        dropTable(conn, "song")
        dropTable(conn, "artist")
        dropTable(conn, "everything")
        dropTable(conn, "year")
        dropTable(conn, "billboard")
        dropTable(conn, "genreprsong")
        dropTable(conn, "genre")


        createEverything(conn)
        createTableYear(conn)
        createTableBillboard(conn)
        createTableArtist(conn)
        createTableSong(conn)
        createTableAlbum(conn)
        createTableGenre(conn)
        createTableGenrePrSong(conn)

        populateEverything(conn)
        populateYear(conn)
        populateBillboard(conn)
        populateArtist(conn)
        populateSong(conn)
        populateAlbum(conn)
        populateGenre(conn)
        populateGenrePrSong(conn)
        

    closeConnection(conn, database)
if __name__ == '__main__':
    main()
