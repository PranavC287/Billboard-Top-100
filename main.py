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
        file_path = "DataTotales.txt"
        with open(file_path, "r") as file:
            data = file.readlines()
        cur = _conn.cursor()
        cur.execute(
        "CREATE TABLE temp (\
        t_song char(100) not null,\
        t_artist char(100) not null)")
        n = "Work in progress"
        for line in data:
            parts = line.strip().split("' by ")
            if len(parts) == 2:
                song = parts[0].strip()
                artist = parts[1].strip()
                cur.execute(
                    "INSERT OR IGNORE INTO temp(t_song, t_artist) VALUES (?, ?)", (song[5:], artist),)
        cur.execute(
            "INSERT INTO album(al_songkey, al_artistkey, al_name)\
            SELECT s_songkey, a_artistkey FROM temp, artist, song\
            WHERE t_song = s_name \
            AND t_artist = a_name\
            SELECT 'Work in progress'")
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
    print("Populate ong table")
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
                    "INSERT OR IGNORE INTO song(s_songkey, s_name, s_releaseyearkey) VALUES (?, ?, ?)", (k, name[5:], n),)
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


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create genreprsong table")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT a_name FROM artist (\
        WHERE a_name")

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
        #dropTable(conn, "song")
        #dropTable(conn, "artist")
        
        #createTableYear(conn)
        #createTableBillboard(conn)
        #createTableArtist(conn)
        createTableAlbum(conn)
        #createTableSong(conn)
        #createTableGenre(conn)
        #createTableGenrePrSong(conn)

        #populateYear(conn)
        #populateBillboard
        #populateArtist(conn)
        populateAlbum(conn)
        #populateSong(conn)
        #populateGenre
        #populateGenrePrSong

        dropTable(conn, "temp")
        

    closeConnection(conn, database)
if __name__ == '__main__':
    main()
