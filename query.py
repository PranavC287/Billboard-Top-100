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


def Q3(_conn, yr, year, Gname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT S.Name, B.Rank\
        FROM SONGS S\
        JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key\
        WHERE B.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?)\
        AND S.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?)\
        AND S.G_Key = (SELECT G_Key FROM GENRE WHERE Name = ?)\
        ORDER BY B.Rank\
        LIMIT 10;", (yr, year, Gname))

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
        "SELECT S.Name, B.Rank\
        FROM SONGS S\
        JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key\
        WHERE S.N_Key = (SELECT N_Key FROM ARTIST WHERE Name = ?)\
        AND B.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?)\
        AND B.Rank <= 10;", (Aname, yr))

    except Error as e:
        print(e)


def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT A.Name, COUNT(S.N_Key) AS SongCount\
        FROM ARTIST A\
        LEFT JOIN SONGS S ON A.N_Key = S.N_Key\
        GROUP BY A.N_Key\
        ORDER BY SongCount DESC\
        LIMIT 5;")

    except Error as e:
        print(e)                


def Q7(_conn, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT G.Name, COUNT(*) AS GenreCount\
        FROM GENRE G\
        JOIN GENRE_PER_SONG GS ON G.G_Key = GS.G_Key\
        JOIN SONGS S ON GS.S_Key = S.S_Key\
        WHERE S.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?)\
        GROUP BY G.G_Key\
        ORDER BY GenreCount DESC\
        LIMIT 1;", (yr),)

    except Error as e:
        print(e)                


def Q8(_conn, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT A.Name AS Artist, S.Name AS Song, YEAR.Year AS Year, B.Rank\
        FROM ARTIST A\
        JOIN SONGS S ON A.N_Key = S.N_Key\
        JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key\
        JOIN (\
            SELECT DISTINCT Y_Key, MAX(Rank) AS MaxRank\
            FROM BILLBOARD_TOP_100\
            GROUP BY Y_Key\
        ) MaxRanks ON B.Y_Key = MaxRanks.Y_Key AND B.Rank = MaxRanks.MaxRank\
        JOIN YEAR ON B.Y_Key = YEAR.Y_Key\
        WHERE A.Name = ?;", (Aname))

    except Error as e:
        print(e)                               


def Q9(_conn, Aname, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT S.Name, B.Rank\
        FROM SONGS S\
        JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key\
        JOIN ARTIST A ON B.N_Key = A.N_Key\
        WHERE A.Name = ? AND B.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?);", (Aname, yr),)

    except Error as e:
        print(e)                


def Q10(_conn, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT A.Name, COUNT(*) AS SongCount\
        FROM ARTIST A\
        JOIN SONGS S ON A.N_Key = S.N_Key\
        JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key\
        WHERE B.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?) AND B.Rank <= 10\
        GROUP BY A.N_Key\
        ORDER BY SongCount DESC\
        LIMIT 1;", (yr),)

    except Error as e:
        print(e)          


def Q11(_conn, Gname, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT S.Name\
        FROM SONGS S\
        JOIN GENRE_PER_SONG GS ON S.S_Key = GS.S_Key\
        JOIN GENRE G ON GS.G_Key = G.G_Key\
        JOIN ARTIST A ON S.N_Key = A.N_Key\
        WHERE G.Name = ? AND A.Name = ?;", (Gname, Aname),)

    except Error as e:
        print(e)          


def Q12(_conn, Bchartdate):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT S.Name\
        FROM SONGS S\
        JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key\
        WHERE B.ChartDate = ?;", (Bchartdate),)

    except Error as e:
        print(e)          


def Q13(_conn, Aname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT AVG(B.Rank) AS AverageRank\
        FROM ARTIST A\
        JOIN SONGS S ON A.N_Key = S.N_Key\
        JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key\
        WHERE A.Name = ?;", (Aname),)

    except Error as e:
        print(e)          


def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT Y.Year, COUNT(S.S_Key) AS SongCount\
        FROM YEAR Y\
        LEFT JOIN SONGS S ON Y.Y_Key = S.Y_Key\
        GROUP BY Y.Year;")

    except Error as e:
        print(e)  


def Q15(_conn, Gname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT S.Name, B.Rank\
        FROM SONGS S\
        JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key\
        LEFT JOIN GENRE_PER_SONG GS ON S.S_Key = GS.S_Key\
        LEFT JOIN GENRE G ON GS.G_Key = G.G_Key\
        WHERE G.Name <> ?\
        ORDER BY B.Rank\
        LIMIT 10;", (Gname),)

    except Error as e:
        print(e)                  


def Q16(_conn, Sname):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT s_name \
        FROM song\
        WHERE s_name = ?;", (Sname,))

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
        "SELECT S.Name\
        FROM SONGS S\
        JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key\
        JOIN YEAR Y ON B.Y_Key = Y.Y_Key\
        JOIN ARTIST A ON S.N_Key = A.N_Key\
        WHERE Y.Year = ? AND A.Name = ?\
        ORDER BY B", (yr, Aname),)

    except Error as e:
        print(e)             


def Q18(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "UPDATE song SET s_songkey = (SELECT y_yearkey FROM year\
        WHERE y_year = 2006)")
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
        "DELETE FROM song\
        WHERE s_songkey = 0")
        _conn.commit()
    except Error as e:
        print(e)          


def Q20(_conn, yr):
    print("++++++++++++++++++++++++++++++++++")
    print("Create input table name")
    try:
        cur = _conn.cursor()
        cur.execute(
        "SELECT Name\
        FROM SONGS\
        WHERE Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = (?))\
        ORDER BY S_Key\
        LIMIT 1;", (yr,))

    except Error as e:
        print(e)          

def main():
    database = r"new.db"
    # create a database connection
    conn = sqlite3.connect(database)
    with conn:
        Q1(conn, "Beyonce Featuring Slim Thug")
        Q1(conn, "D4L")
        
        Q2(conn, "Justin Timberlake")
        Q4(conn)
        Q16(conn, "Bad Day")
        #Q18(conn)
        Q19(conn)
    conn.close()

if __name__ == '__main__':
    main()
