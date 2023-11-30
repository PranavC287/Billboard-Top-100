import sqlite3
from sqlite3 import Error

def Q1(_conn, AName):
    print("++++++++++++++++++++++++++++++++++")
    print("SELECT s_name FROM song")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT s_name FROM album, song, artist\
        WHERE al_songkey = s_songkey \
        AND al_artistkey = a_artistkey\
        AND a_name = (?)", (AName,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)


def Q2(_conn, AName):
    print("++++++++++++++++++++++++++++++++++")
    print("Get SongCount from artist")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT COUNT(*) AS SongCount\
        FROM song \
        JOIN ARTIST ON s_songkey = a_artistkey\
        WHERE a_name = (?);", (AName,))
                        
        data = cur.fetchall()
        for row in data:
            print(row)
            
    except Error as e:
        print(e)


def Q3(_conn, byear, syear, Gname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT s_name, b_rank
        FROM song s
        JOIN billboard b ON s.s_songkey = b.b_songkey
        WHERE b.b_yearkey = (SELECT y_yearkey FROM year WHERE y_year = ?)\
        AND s.b_yearkey = (SELECT y_yearkey FROM year WHERE y_year = ?)\
        AND s.s_releaseyearkey = (SELECT g_genrekey FROM genre WHERE g_name = ?)\
        ORDER BY b_rank
        LIMIT 10''', (byear, syear, Gname,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "INSERT INTO song VALUES (101, 11, 'Centuries')")

    except Error as e:
        print(e)


def Q5(_conn, Aname, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''    
        SELECT s_name, b_rank
        FROM song s
        JOIN billboard b ON s.s_songkey = b.b_songkey
        WHERE s.s_songkey = (SELECT a_artistkey FROM artist WHERE a_name = ?)
        AND b.b_yearkey = (SELECT y_yearkey FROM year WHERE y_year = ?)
        AND b_rank <= 10''', (Aname, yr,))

        data = cur.fetchall()
        for row in data:
            print(row)
            
    except Error as e:
        print(e)


def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT a_name, COUNT(s.s_songkey) AS SongCount
        FROM artist a\
        LEFT JOIN song s ON a.a_artistkey = s.s_songkey
        GROUP BY a.a_artistkey
        ORDER BY SongCount DESC
        LIMIT 5''')

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
        '''SELECT g_name, COUNT(*) AS GenreCount
        FROM genre g
        JOIN genreprsong gs ON g.g_genrekey = gs.g_genrekey
        JOIN song s ON gs.g_songkey = s.s_songkey
        WHERE s.s_releaseyearkey = (SELECT y_yearkey FROM year WHERE y_year = ?)
        GROUP BY g.g_genrekey
        ORDER BY GenreCount DESC
        LIMIT 1''', (yr,))

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
        '''SELECT a_name AS Artist, s_name AS Song, y_year AS Year, b_rank
        FROM artist a
        JOIN song s ON a.a_artistkey = s.s_songkey
        JOIN billboard b ON s.s_songkey = b.b_songkey
        JOIN (
        SELECT DISTINCT y_yearkey, MAX(b_rank) AS MaxRank
        FROM billboard
        GROUP BY y_yearkey
        ) MaxRanks ON b.b_yearkey = MaxRanks.y_yearkey AND b_rank = MaxRanks.MaxRank
        JOIN year ON b.b_yearkey = y.y_yearkey
        WHERE a_name = ?''', (Aname,))

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
        JOIN artist a ON b.b_songkey = a.a_artistkey
        WHERE a_name = ? AND b.b_yearkey = (SELECT y_yearkey FROM year WHERE y_year = ?)''', (Aname, yr,))
            
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
        '''
        SELECT a_name, COUNT(*) AS SongCount
        FROM artist a
        JOIN song s ON a.a_artistkey = s.s_songkey
        JOIN billboard b ON s.s_songkey = b.b_songkey
        WHERE b.b_yearkey = (SELECT y_yearkey FROM year WHERE y_year = ?) AND b_rank <= 10
        GROUP BY a.a_artistkey
        ORDER BY SongCount DESC
        LIMIT 1''', (yr,))

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
        '''
        enter query here
        ''', (Gname, Aname),)

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
        '''
        enter query here
        ''', (Bchartdate,))

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
        '''
        enter query here
        ''', (Aname,))

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
        '''
        enter query here
        ''')

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
        '''
        enter query here
        ''', (Gname,))

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
        '''
        enter query here
        ''', (Sname,))

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
        '''
        enter query here
        ''', (yr, Aname,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)             


def Q18(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        enter query here
        ''')
        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          

def Q19(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("delete input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        enter query here
        ''')
        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          


def Q20(_conn, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''
        enter query here
        ''', (yr,))

        data = cur.fetchall()
        for row in data:
            print(row)

    except Error as e:
        print(e)          

def main():
    database = r"new.db"
    # create a database connection
    conn = sqlite3.connect(database)
    with conn:
        Q1(conn, "Beyonce Featuring Slim Thug")
        #Q1(conn, "D4L")
        Q2(conn, "The Black Eyed Peas")

        Q3(conn, 2012, 2012, "Pop")
        #Q4(conn)
        Q5(conn, "Nickelback", 2008)
        Q6(conn)
        Q7(conn, 2017)
        Q8(conn, "Justin Timberlake")
        Q9(conn, "Kelly Clarkson", 2010)
        Q10(conn, 2020)
        
    conn.close()

if __name__ == '__main__':
    main()
