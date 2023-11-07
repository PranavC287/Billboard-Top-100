#import billboard

import random
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
    print("Drop table " + tableName)
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
        b_songkey decimal(5,0) not null, \
        b_rank decimal(5,0) not null,\
        b_artistkey decimal(5,0) not null, \
        b_yearkey decimal(5,0) not null)")

    except Error as e:
        print(e)

def populateBillboard(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
    try:
        cur = _conn.cursor()
        for x in range(21):
            for i in range(99):
                s = random.randrange(1000)
                a = random.randrange(1000)
                cur.execute(
                    "INSERT INTO billboard(b_songkey, b_artistkey, b_yearkey, b_rank) VALUES (?, ?, ?, ?)", (s, a, x+3, i+1),)
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
    print("Populate artist table")
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
                    "INSERT OR IGNORE INTO artist(a_artistkey, a_name, a_about) VALUES (?, ?, ?)", (k, artist, n),)
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
        sam = ["Populate", "songkey", "random", "range", "execute"]
        cur = _conn.cursor()
        for i in range(100):
            s = random.randrange(1000)
            a = random.randrange(1000)
            r = random.randrange(5)
            cur.execute(
                "INSERT INTO album(al_songkey, al_artistkey, al_name) VALUES (?, ?, ?)", (s, a, sam[r]),)
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
    print("Populate song table")
    try:
        file_path = "DataTotales.txt"
        with open(file_path, "r") as file:
            data = file.readlines()
        cur = _conn.cursor()
        k = 0
        for line in data:
            a = random.randrange(21)
            parts = line.strip().split("' by ")
            if len(parts) == 2:
                name = parts[0].strip()
                cur.execute(
                    "INSERT OR IGNORE INTO song(s_songkey, s_name, s_releaseyearkey) VALUES (?, ?, ?)", (k, name[5:], a+3),)
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
    print("Populate year table")
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

def populateGenre(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate genre table")
    try:
        file_path = "genre.txt"
        with open(file_path, "r") as file:
            data = file.readlines()
        cur = _conn.cursor()
        k = 0
        for line in data:
            genre = line.strip()
            cur.execute("INSERT INTO genre(g_genrekey, g_name) VALUES (?, ?)", (k, genre),)
            k = k+1

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

def populateGenrePrSong(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate genreprsong table")
    try:
        cur = _conn.cursor()
        for i in range(1000):
            s = random.randrange(1000)
            g = random.randrange(49)
            cur.execute("INSERT INTO genreprsong(g_genrekey, g_songkey) VALUES (?, ?)", (g, s),)

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
        dropTable(conn, "year")
        dropTable(conn, "billboard")
        dropTable(conn, "artist")
        dropTable(conn, "album")
        dropTable(conn, "song")
        dropTable(conn, "genre")
        dropTable(conn, "genreprsong")
        
        
        createTableYear(conn)
        createTableBillboard(conn)
        createTableArtist(conn)
        createTableAlbum(conn)
        createTableSong(conn)
        createTableGenre(conn)
        createTableGenrePrSong(conn)

        populateYear(conn)
        populateBillboard(conn)
        populateArtist(conn)
        populateAlbum(conn)
        populateSong(conn)
        populateGenre(conn)
        populateGenrePrSong(conn)
        

    closeConnection(conn, database)

if __name__ == '__main__':
    main()
