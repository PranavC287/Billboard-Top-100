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
        SELECT b_rank AS rank, s_name AS Song, a_name AS Artist, y_year AS Year 
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


def A7(_conn, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Average rank of songs by a specific artist")
    try:
        artist = '%'+Aname+'%'
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT AVG(b_rank) AS 'Average Rank'
        FROM artist, billboard, song
        WHERE a_artistkey = b_artistkey
        AND b_songkey = s_songkey
        AND (a_name LIKE '%s'
        OR a_name LIKE '%s'
        OR a_name LIKE '%s');
    ''' %  (artist[:len(artist)-1], artist[1:], artist,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)                

 
def P8(_conn, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Popular Genre By Given Year")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT g_name, COUNT(*) AS GenreCount FROM genre, genreprsong, song, billboard
        WHERE g_genrekey = gs_genrekey
        AND gs_songkey = s_songkey
        AND s_songkey = b_songkey
        AND b_yearkey = (SELECT y_yearkey FROM year WHERE y_year = ?)
        GROUP BY g_name
        ORDER BY GenreCount DESC
        ''', (yr,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)                               


def B9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("return top 10 billboards")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT b_rank AS Rank, s_name AS Song, a_name AS Artist, y_year AS Year 
        FROM billboard, artist, song, year
        WHERE b_artistkey = a_artistkey
        AND b_songkey = s_songkey
        AND b_yearkey = y_yearkey
        AND b_rank <11
        ORDER BY y_year
        ''')
            
        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)                


def G10(_conn, genre):
    print("++++++++++++++++++++++++++++++++++")
    print("Songs from Particular Genre")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
            SELECT s_name
            FROM song, genreprsong, genre
            WHERE s_songkey = gs_songkey
            AND gs_genrekey = g_genrekey
            AND g_name = '%s'
            ''' % genre)

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def L11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Availabe Genres")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT g_name AS Genres FROM genre''')

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def L12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Availabe Years")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT y_year AS 'Availabe Years' FROM year''')

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def P13(_conn, limit):
    print("++++++++++++++++++++++++++++++++++")
    print("Most Popular Songs of all time")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT s_name AS Songs, COUNT(*) AS Appearance
        FROM billboard, artist, song, year
        WHERE b_artistkey = a_artistkey
        AND b_songkey = s_songkey
        AND b_yearkey = y_yearkey
        GROUP BY s_name
        ORDER BY Appearance DESC
        LIMIT ?
        ''', (limit,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def D14(_conn, Sname):
    print("++++++++++++++++++++++++++++++++++")
    print("Deletes song")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        DELETE FROM song
        WHERE s_name  = '%s'
        ''' % Sname)

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)  


def I15(_conn, genre):
    print("++++++++++++++++++++++++++++++++++")
    print("Add new genre to table")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        INSERT INTO genre(g_genrekey, g_name)
        SELECT  g_genrekey+1, '%s' FROM genre
        ORDER BY g_genrekey DESC LIMIT 1
        ''' % genre )

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)                  


def D16(_conn, Sname):
    print("++++++++++++++++++++++++++++++++++")
    print("Delete Genre from table")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        DELETE FROM genre
        WHERE g_name  = '%s'
        ''' % Sname)

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)       


def Q17(_conn, Limit):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT a_name, s_name, g_name FROM artist, album, song, genreprsong, genre
            WHERE a_artistkey = al_artistkey
            AND al_songkey = s_songkey
            AND s_songkey = gs_songkey
            AND gs_genrekey = g_genrekey
            LIMIT ?
        ''', (Limit,))

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

def I19(_conn, inp, release):
    print("++++++++++++++++++++++++++++++++++")
    print("Create song")
    try:
        print(inp)
        print(release)
        cur = _conn.cursor()
        cur.execute(
        '''
        INSERT INTO song(s_songkey, s_name, s_releaseyearkey)
        SELECT s_songkey+1, '%s', %s-2006 FROM song
        ORDER BY s_songkey DESC
        LIMIT 1
        ''' % (inp, int(release)))
        
        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def P20(_conn, limit):
    print("++++++++++++++++++++++++++++++++++")
    print("Artist with the most songs in the billboards")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        SELECT a_name AS Artists, COUNT(*) AS Songs
        FROM billboard, artist, song, year
        WHERE b_artistkey = a_artistkey
        AND b_songkey = s_songkey
        AND b_yearkey = y_yearkey
        GROUP BY a_name
        ORDER BY Songs DESC
        LIMIT ?
        ''', (limit,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          

def main():
    database = r"DatabaseTotalis.db"
    # create a database connection
    ui = "-1"
    print("WARNING: used '%/s' %/ song instead of '?', (song,) for some queries, might cause issues with old version of python")
            
    while(ui.upper() != 'Q'):
        conn = sqlite3.connect(database)
        p = ui.split(" ")
        if (p[0].upper() == 'H' or p[0].upper() == 'HELP'):
            print("command 'getall artistname' returns artist and song")
            print("command 'songcount artistname' returns amount of songs from artist artistname")
            print("command 'geta artistname' returns artist description")
            print("command 'getby year' returns billboard from year y")
            print("command 'dela artistname' deletes artist artistname")
            print("command 'gets songname' returns songs from song table")
            print("command 'avrank artistname' returns average song rank from artist artistname")
            print("command 'popgy year' returns the most popular genres from the given year (Descending)")
            print("command 'gettopb' returns billboards from all years in the top 10") 
            print("command 'spg genrename' returns songs in genre genrename")
            print("command 'listg' returns all genres")
            print("command 'listy' returns all available years")
            print("command 'pops x' returns top x number of most popular songs of all time from the billboard (Descending)")
            print("command 'dels songname' returns songs from song table")
            print("command 'makeg genrename' inserts into genre table newgenre")
            print("command 'delg genrename' deletes genre newgenre")
            print("command 'asg x' Shows  Artist, Song, Genre in limit x")
            print("command 'makea artistname artist_about' inserts into artist table artistname and artist_about (LIMITED TO SINGLE ARTIST NAME)")
            print("command 'makes songname releasedate' inserts into song table songname and song release date")
            print("command 'popa x' returns top x number of most popular artist of all time from the billboard (Descending)")

            
        with conn:
            if(p[0].upper() == "GETALL"):
                G1(conn, " ".join(p[1:]))
            if(p[0].upper() == "SONGCOUNT"):
                Q2(conn, " ".join(p[1:]))
            if(p[0].upper() == "GETA"):
                G3(conn, " ".join(p[1:]))
            if(p[0].upper() == "GETBY"):
                G4(conn, p[1])
            if(p[0].upper() == "DELA"):
                D5(conn, " ".join(p[1:]))  
            if(p[0].upper() == "GETS"):
                G6(conn, " ".join(p[1:]))          
            if(p[0].upper() == "AVRANK"):
                A7(conn, " ".join(p[1:]))
            if(p[0].upper() == "POPGY"):
                P8(conn, " ".join(p[1:]))
            if(p[0].upper() == "GETTOPB"):
                B9(conn)
            if(p[0].upper() == "SPG"):
                G10(conn, " ".join(p[1:]))  
            if(p[0].upper() == "LISTG"):
                L11(conn)
            if(p[0].upper() == "LISTY"):
                L12(conn)           
            if(p[0].upper() == "POPS"):
                P13(conn, p[1])
            if(p[0].upper() == "DELS"):
                D14(conn, " ".join(p[1:]))     
            if(p[0].upper() == "MAKEG"):
                I15(conn, " ".join(p[1:])) 
            if(p[0].upper() == "DELG"):
                D16(conn, " ".join(p[1:]))  
            if(p[0].upper() == "ASG"):
                Q17(conn, p[1])                    
            if(p[0].upper() == "MAKEA"):
                I18(conn, p[1], " ".join(p[2:]))
            if(p[0].upper() == "MAKES"):
                I19(conn, " ".join(p[1:len(p)-1]), p[len(p)-1])
            if(p[0].upper() == "POPA"):
                P20(conn, p[1])
        conn.close()
        ui = input("input: ")

if __name__ == '__main__':
    main()
