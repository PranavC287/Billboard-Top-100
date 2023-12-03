import sqlite3
from sqlite3 import Error

def Q1(_conn, AName):
    print("++++++++++++++++++++++++++++++++++")
    print("SELECT s_name FROM song")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT a.a_name AS Artist, s.s_name AS Song, al.al_name AS Album
        FROM artist a
        JOIN album al ON a.a_artistkey = al.al_artistkey
        JOIN song s ON al.al_songkey = s.s_songkey
        WHERE a.a_name = (?);''', (AName,))

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
        '''SELECT s_name, b_rank
        FROM billboard b
        JOIN song s ON b.b_songkey = s.s_songkey
        ORDER BY b_rank
        LIMIT 10;''', (AName,))
                        
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
        '''SELECT y_year, COUNT(*) AS SongCount\
        FROM year y\
        JOIN billboard b ON y.y_yearkey = b.b_yearkey\
        GROUP BY y_year;''', (byear, syear, Gname,))

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
        '''SELECT s_name
        FROM song s
        JOIN billboard b ON s.s_songkey = b.b_songkey
        JOIN year y ON b.b_yearkey = y.y_yearkey
        WHERE b_rank = 1 AND y_year = ?;''', (Aname,))

    except Error as e:
        print(e)


def Q5(_conn, Aname, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT AVG(b_rank) AS AverageRank
        FROM billboard;''', (Aname, yr,))

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
        '''SELECT * FROM song
        ORDER BY s_songkey DESC
        LIMIT 1;''')

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
        WHERE s_name LIKE 'Love%';''', (Aname,))

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


def Q18(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        '''SELECT al.al_name AS Album, COUNT(al.al_songkey) AS SongCount
        FROM album al
        GROUP BY al.al_name
        HAVING COUNT(al.al_songkey) > 12;''')
        
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
        '''SELECT a.a_name AS Artist, al.al_name AS Album
        FROM artist a
        JOIN album al ON a.a_artistkey = al.al_artistkey;''')
        
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
