--Find the top 1 song in a specific year.

SELECT Name
FROM SONGS
WHERE Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = (?))
ORDER BY S_Key
LIMIT 1;

--Find the artist's name for the song with the title "?".

SELECT A.Name
FROM ARTIST A
JOIN SONGS S ON A.N_Key = S.N_Key
WHERE S.Name = ?;

--List all songs by the artist "?"

SELECT S.Name
FROM SONGS S
JOIN ARTIST A ON S.N_Key = A.N_Key
WHERE A.Name = ?;

--Get the number of songs by the artist "?".

SELECT COUNT(*) AS SongCount
FROM SONGS S
JOIN ARTIST A ON S.N_Key = A.N_Key
WHERE A.Name = ?;

--List the top-ranked songs in the year "?" for a specific genre.

SELECT S.Name, B.Rank
FROM SONGS S
JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key
WHERE B.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?)
AND S.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?)
AND S.G_Key = (SELECT G_Key FROM GENRE WHERE Name = ?)
ORDER BY B.Rank
LIMIT 10;




--Find the artist who released the song "?" in the year "?".

SELECT A.Name
FROM ARTIST A
JOIN SONGS S ON A.N_Key = S.N_Key
WHERE S.Name = ? AND S.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?);

--List the songs by a specific artist that charted in the top 10 in the year "?".

SELECT S.Name, B.Rank
FROM SONGS S
JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key
WHERE S.N_Key = (SELECT N_Key FROM ARTIST WHERE Name = ?)
AND B.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?)
AND B.Rank <= 10;

--Retrieve the names of the top 5 artists with the most songs in the database.

SELECT A.Name, COUNT(S.N_Key) AS SongCount
FROM ARTIST A
LEFT JOIN SONGS S ON A.N_Key = S.N_Key
GROUP BY A.N_Key
ORDER BY SongCount DESC
LIMIT 5;

--Find the most common genre for songs released in the year "?".

SELECT G.Name, COUNT(*) AS GenreCount
FROM GENRE G
JOIN GENRE_PER_SONG GS ON G.G_Key = GS.G_Key
JOIN SONGS S ON GS.S_Key = S.S_Key
WHERE S.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?)
GROUP BY G.G_Key
ORDER BY GenreCount DESC
LIMIT 1;

--Get the top-ranked song for each year from a specific artist "?".

SELECT A.Name AS Artist, S.Name AS Song, YEAR.Year AS Year, B.Rank
FROM ARTIST A
JOIN SONGS S ON A.N_Key = S.N_Key
JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key
JOIN (
    SELECT DISTINCT Y_Key, MAX(Rank) AS MaxRank
    FROM BILLBOARD_TOP_100
    GROUP BY Y_Key
) MaxRanks ON B.Y_Key = MaxRanks.Y_Key AND B.Rank = MaxRanks.MaxRank
JOIN YEAR ON B.Y_Key = YEAR.Y_Key
WHERE A.Name = ?;

--List the songs that charted for an artist in a specific year "?".

SELECT S.Name, B.Rank
FROM SONGS S
JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key
JOIN ARTIST A ON B.N_Key = A.N_Key
WHERE A.Name = ? AND B.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?);

--Find the artist with the most songs that charted in the top 10 in a specific year "?".

SELECT A.Name, COUNT(*) AS SongCount
FROM ARTIST A
JOIN SONGS S ON A.N_Key = S.N_Key
JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key
WHERE B.Y_Key = (SELECT Y_Key FROM YEAR WHERE Year = ?) AND B.Rank <= 10
GROUP BY A.N_Key
ORDER BY SongCount DESC
LIMIT 1;

--List all songs in a specific genre "?" by a particular artist "?".

SELECT S.Name
FROM SONGS S
JOIN GENRE_PER_SONG GS ON S.S_Key = GS.S_Key
JOIN GENRE G ON GS.G_Key = G.G_Key
JOIN ARTIST A ON S.N_Key = A.N_Key
WHERE G.Name = ? AND A.Name = ?;

--Retrieve the songs that have charted on a specific date "?".

SELECT S.Name
FROM SONGS S
JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key
WHERE B.ChartDate = ?;

--Calculate the average rank of songs by a specific artist "?".



SELECT AVG(B.Rank) AS AverageRank
FROM ARTIST A
JOIN SONGS S ON A.N_Key = S.N_Key
JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key
WHERE A.Name = ?;

--Find the number of songs released in each year in the database.

SELECT Y.Year, COUNT(S.S_Key) AS SongCount
FROM YEAR Y
LEFT JOIN SONGS S ON Y.Y_Key = S.Y_Key
GROUP BY Y.Year;

--List the top-ranked songs that are not in a specific genre "?".

SELECT S.Name, B.Rank
FROM SONGS S
JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key
LEFT JOIN GENRE_PER_SONG GS ON S.S_Key = GS.S_Key
LEFT JOIN GENRE G ON GS.G_Key = G.G_Key
WHERE G.Name <> ?
ORDER BY B.Rank
LIMIT 10;

--Calculate the total number of songs in the database by a specific artist "?".

SELECT COUNT(*) AS SongCount
FROM SONGS S
JOIN ARTIST A ON S.N_Key = A.N_Key
WHERE A.Name = ?;

--Find the top-ranked song from the year "?" by a specific artist "?".

SELECT S.Name
FROM SONGS S
JOIN BILLBOARD_TOP_100 B ON S.N_Key = B.N_Key
JOIN YEAR Y ON B.Y_Key = Y.Y_Key
JOIN ARTIST A ON S.N_Key = A.N_Key
WHERE Y.Year = ? AND A.Name = ?
ORDER BY B

--Find the artist with the most songs in the "SONGS" table.


DELETE FROM song
WHERE s_songkey = 0

UPDATE song SET s_songkey = (SELECT y_yearkey FROM year
WHERE y_year = 2006)

INSERT INTO song VALUES (101, 11, "Centuries")

SELECT row_number() over () AS s_key, song, 
(
SELECT COUNT(*)
FROM everything e2
WHERE e2.artist <= e1.artist
AND e2.artist <> e1.artist
) AS a_key, artist, year 
FROM everything e1
ORDER BY artist

SELECT row_number() over (PARTITION BY year)-1 AS Rank, row_number() over () -1 AS s_key, song, artist, 
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

SELECT * FROM artist
ORDER BY a_artistkey DESC 

SELECT a_name AS Artist, a_about FROM artist
WHERE a_name LIKE 'chuck%'
OR a_name LIKE '%chuck'
OR a_name LIKE '%chuck%';

INSERT INTO artist(a_artistkey, a_name, a_about)
SELECT a_artistkey+1, 'john', 'he is a man who likes hats' FROM artist
ORDER BY a_artistkey DESC
LIMIT 1

DELETE FROM artist
WHERE a_about LIKE 'in%'

SELECT *
FROM billboard b
JOIN song s ON b.b_songkey = s.s_songkey
JOIN artist ON b_artistkey = a_artistkey
WHERE a_name LIKE '%DJ Khaled'
OR a_name LIKE 'DJ Khaled%'
OR a_name LIKE '%DJ Khaled%'
ORDER BY b_rank

        SELECT b_rank+1 AS rank, s_name AS Song, a_name AS Artist, y_year AS Year 
        FROM billboard, year, artist, song
        WHERE b_yearkey = y_yearkey
        AND b_artistkey = a_artistkey
        AND b_songkey = s_songkey
        AND y_year = 2011;

        SELECT AVG(b_rank) AS 'Average Rank'
        FROM artist, billboard, song
        WHERE a_artistkey = b_artistkey
        AND b_songkey = s_songkey
        AND (a_name LIKE '%Kanye West%'
        OR a_name LIKE '%Kanye West'
        OR a_name LIKE 'Kanye West%')

        SELECT g_name, COUNT(*) AS GenreCount FROM genre, genreprsong, song, billboard
        WHERE g_genrekey = gs_genrekey
        AND gs_songkey = s_songkey
        AND s_songkey = b_songkey
        AND b_yearkey = (SELECT y_yearkey FROM year WHERE y_year = 2011)
        GROUP BY g_name
        ORDER BY GenreCount DESC
        LIMIT 1


        SELECT b_rank AS Rank, s_name AS Song, a_name AS Artist, y_year AS Year 
        FROM billboard, artist, song, year
        WHERE b_artistkey = a_artistkey
        AND b_songkey = s_songkey
        AND b_yearkey = y_yearkey
        AND b_rank <11
        ORDER BY y_year

        SELECT s_name
        FROM song, genreprsong, genre
        WHERE s_songkey = gs_songkey
        AND gs_genrekey = g_genrekey
        AND g_name = 'Pop'

        DROP TRIGGER mkyr;
        CREATE TRIGGER mkyr
        AFTER INSERT ON song
        WHEN (NEW.s_releaseyearkey> 19 OR NEW.s_releaseyearkey < 0) 
        BEGIN
            DELETE FROM song
            WHERE s_releaseyearkey = NEW.s_releaseyearkey;
        END;

        INSERT INTO song(s_songkey, s_name, s_releaseyearkey)
        SELECT s_songkey+1, 'Fetty Wap', 2033-2006 FROM song
        ORDER BY s_songkey DESC
        LIMIT 1

        SELECT * FROM song
        WHERE s_name = 'Fetty Wap'

        DELETE FROM song
        WHERE s_name = 'Fetty Wap'

        SELECT a_name AS Artists, COUNT(*) AS Songs
        FROM billboard, artist, song, year
        WHERE b_artistkey = a_artistkey
        AND b_songkey = s_songkey
        AND b_yearkey = y_yearkey
        GROUP BY a_name
        ORDER BY Songs DESC
        LIMIT 10

        SELECT s_name AS Songs, COUNT(*) AS Appearance
        FROM billboard, artist, song, year
        WHERE b_artistkey = a_artistkey
        AND b_songkey = s_songkey
        AND b_yearkey = y_yearkey
        GROUP BY s_name
        ORDER BY Appearance DESC
        LIMIT 20


        DROP TRIGGER mkart;
        CREATE TRIGGER mkart
        AFTER INSERT ON song
        WHEN (NEW.s_releaseyearkey> 19 OR NEW.s_releaseyearkey < 0) 
        BEGIN
            DELETE FROM song
            WHERE s_releaseyearkey = NEW.s_releaseyearkey;
        END;

        INSERT INTO album(al_songkey, al_artistkey, al_name)
        SELECT s_songkey+1,
            CASE
                WHEN NOT 'Fetty Wap' = (SELECT a_name FROM artist WHERE a_name = 'Fetty Wap' LIMIT 1) 
                    THEN (SELECT a_artistkey+1 FROM artist
                        ORDER BY s_songkey DESC LIMIT 1)
                ELSE (SELECT a_artistkey FROM artist
                        WHERE a_name = 'Fetty Wap' LIMIT 1)
            END,
            'Yesterday' FROM song
            ORDER BY s_songkey DESC LIMIT 1

SELECT a_name, s_name, g_name FROM artist, album, song, genreprsong, genre
    WHERE a_artistkey = al_artistkey
    AND al_songkey = s_songkey
    AND s_songkey = gs_songkey
    AND gs_genrekey = g_genrekey

        SELECT * FROM song 
        ORDER BY s_songkey DESC