import sqlite3
from sqlite3 import Error
k = 3000

def G1(_conn, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("SELECT s_name FROM song")
    try:
        artist = '%'+Aname+'%'
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT a_name AS Artist, s_name AS Song, al_name AS Album FROM album
        INNER JOIN artist ON al_artistkey = a_artistkey
        INNER JOIN song ON al_songkey = s_songkey
        WHERE a_name LIKE '%s'
        OR a_name LIKE '%s'
        OR a_name LIKE '%s' '''% (artist[:len(artist)-1], artist[1:], artist,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)


def Q2(_conn, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Get SongCount from artist")
    try:
        artist = '%'+Aname+'%'
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT '%s' AS Artist, COUNT(*) AS 'Song Count'
        FROM billboard b
        JOIN song s ON b.b_songkey = s.s_songkey
        JOIN artist ON b_artistkey = a_artistkey
        WHERE a_name LIKE '%s'
        OR a_name LIKE '%s'
        OR a_name LIKE '%s'
        ORDER BY b_rank''' % (artist[1:len(artist)-1], artist[:len(artist)-1], artist[1:], artist,))
                        
        data = cur.fetchall()
        for row in data:
            print(row)
            
    except Error as e:
        print(e)

def G3(_conn, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Artist")
    try:
        artist = '%'+Aname+'%'
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT a_name AS Artist, a_about FROM artist
        WHERE a_name LIKE '%s'
        OR a_name LIKE '%s'
        OR a_name LIKE '%s';
        ''' % (artist[:len(artist)-1], artist[1:], artist,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)


def G4(_conn, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT b_rank+1 AS rank, s_name AS Song, a_name AS Artist, y_year AS Year 
        FROM billboard, year, artist, song
        WHERE b_yearkey = y_yearkey
        AND b_artistkey = a_artistkey
        AND b_songkey = s_songkey
        AND y_year = ?;''', (yr,))
        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)


def D5(_conn, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Artist")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        DELETE FROM artist
        WHERE a_name  = '%s'
        ''' % Aname)

        data = cur.fetchall()
        for row in data:
            print(row)
            
    except Error as e:
        print(e)


def G6(_conn, song):
    print("++++++++++++++++++++++++++++++++++")
    print("Get Song")
    try:
        print(song)
        cur = _conn.cursor()
        cur.execute(
        '''SELECT s_name AS Song, y_year AS 'release year' FROM song
        INNER JOIN year ON s_releaseyearkey = y_yearkey
        WHERE s_name = '%s'
        ORDER BY s_name DESC'''% song)

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)                


def Q7(_conn, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT s.s_name 
        FROM song s
        JOIN artist a ON s.s_songkey = a.a_artistkey
        WHERE TRIM(a.a_name) = ?;''', (yr,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)                


def Q8(_conn, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT y_year, COUNT(*) AS SongCount
        FROM year y
        JOIN song s ON y.y_yearkey = s.s_releaseyearkey
        GROUP BY y_year;''', (Aname,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)                               


def Q9(_conn, Aname, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT s_name, b_rank
        FROM song s
        JOIN billboard b ON s.s_songkey = b.b_songkey
        WHERE b_rank BETWEEN 5 AND 10;''', (Aname, yr,))
            
        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)                


def Q10(_conn, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT *
        FROM song
        ORDER BY s_releaseyearkey ASC
        LIMIT 1;''', (yr,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def Q11(_conn, Gname, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT COUNT(*) AS SongCount
        FROM song;''', (Gname, Aname),)

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def Q12(_conn, Bchartdate):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT s_name
        FROM song s
        JOIN billboard b ON s.s_songkey = b.b_songkey
        JOIN year y ON b.b_yearkey = y.y_yearkey
        WHERE y_year = ?;''', (Bchartdate,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def Q13(_conn, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT *
        FROM song
        WHERE s_name LIKE 'Love%';''', ())

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT s_name, b_rank
        FROM billboard b
        JOIN song s ON b.b_songkey = s.s_songkey
        ORDER BY b_rank DESC
        LIMIT 1;''')

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)  


def Q15(_conn, Gname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT al.al_name AS Album, y.y_year AS ReleaseYear
        FROM album al
        JOIN song s ON al.al_songkey = s.s_songkey
        JOIN year y ON s.s_releaseyearkey = y.y_yearkey
        WHERE y.y_year = ?;''', (Gname,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)                  


def Q16(_conn, Sname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT s.s_name AS Song, g.g_name AS Genre
        FROM song s
        JOIN genreprsong gp ON s.s_songkey = gp.g_songkey
        JOIN genre g ON gp.g_genrekey = g.g_genrekey;''', (Sname,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)       


def Q17(_conn, yr, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT g.g_name AS Genre, COUNT(gp.g_songkey) AS SongCount
        FROM genre g
        LEFT JOIN genreprsong gp ON g.g_genrekey = gp.g_genrekey
        GROUP BY g.g_name;''', (yr, Aname,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)             


def I18(_conn, inp, lis):
    print("++++++++++++++++++++++++++++++++++")
    print("INSERT input table artist")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        INSERT INTO artist(a_artistkey, a_name, a_about)
        SELECT a_artistkey+1, '%s', '%s' FROM artist
        ORDER BY a_artistkey DESC
        LIMIT 1''' % (inp, lis))

    except Error as e:
        print(e)          

def D19(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("delete input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT a.a_name AS Artist, al.al_name AS Album
        FROM artist a
        JOIN album al ON a.a_artistkey = al.al_artistkey;''')
        
        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def C20(_conn, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT a.a_name AS Artist, COUNT(b.b_songkey) AS NumOfSongs
        FROM artist a
        JOIN billboard b ON a.a_artistkey = b.b_artistkey
        GROUP BY a.a_name
        ORDER BY NumOfSongs DESC
        LIMIT 3;''', (yr,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          

def main():
    database = r"new.db"
    # create a database connection
    ui = "-1"
    while(ui.upper() != 'Q'):
        conn = sqlite3.connect(database)
        p = ui.split(" ")
        if (p[0].upper() == 'H' or p[0].upper() == 'HELP'):
            print("command 'makea artistname artist_about' inserts artist into artist table with name artistname and artist_about")
            print("command 'geta artistname' returns artist description")
            print("command 'getall artistname' returns artist and song")
            print("command 'gets songname ' returns songs from song table")
            print("command 'getb y' returns billboard from year y")
            print("command 'getb song' returns song from billboard")
            print("command 'songcount artistname' returns amount of songs from artist artistname")
            print("command 'dela artistname' deletes artist artistname")

        with conn:
            if(p[0].upper() == "MAKEA"):
                I18(conn, p[1], " ".join(p[2:]))
            if(p[0].upper() == "GETALL"):
                G1(conn, " ".join(p[1:]))
            if(p[0].upper() == "GETA"):
                G3(conn, " ".join(p[1:]))
            if(p[0].upper() == "GETS"):
                G6(conn, " ".join(p[1:]))
            if(p[0].upper() == "GETB"):
                G4(conn, p[1])
            if(p[0].upper() == "SONGCOUNT"):
                Q2(conn, " ".join(p[1:]))
            if(p[0].upper() == "DELA"):
                D5(conn, " ".join(p[1:]))

        conn.close()
        ui = input("input: ")

if __name__ == '__main__':
    main()
