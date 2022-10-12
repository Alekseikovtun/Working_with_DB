import sqlalchemy


db = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# print(engine.get_table_names())
# """What tables are in the database"""

# Number of singers in each style
select_1 = connection.execute(
    """SELECT singer_id, COUNT(style_name) FROM singersong
    LEFT JOIN stylesong ON singersong.song_id = stylesong.song_id
    LEFT JOIN style ON stylesong.style_id = style.id_style
    GROUP BY singer_id;"""
)
result_1 = select_1.all()
print(result_1, '\n')

# Number of songs included in albums 2019-2020
select_2 = connection.execute(
    """SELECT album_name, release_album_date, num_of_songs
    FROM album AS a
    LEFT JOIN song AS s ON s.album_id = id_album
    WHERE (release_album_date>='2019-01-01') AND
    (release_album_date<='2020-12-31')
    GROUP BY (album_name, release_album_date, num_of_songs);"""
)
result_2 = select_2.all()[0][2]
print(result_2, '\n')

# Average duration of songs for each album
select_3 = connection.execute(
    """SELECT album_name, AVG(song_length) FROM album
    LEFT JOIN song ON song.album_id = album.id_album
    GROUP BY album_name
    ORDER BY AVG(song_length);;"""
)
result_3 = select_3.all()
print(result_3, '\n')

# All singers who have not released albums in 2020
select_4 = connection.execute(
    """SELECT DISTINCT singer_id FROM singersong
    WHERE singer_id NOT IN (
        SELECT DISTINCT singer_id
        FROM singersong
        LEFT JOIN song ON song.id_song  = singersong.song_id
        LEFT JOIN album ON album.id_album = song.album_id
        WHERE album.release_album_date > '2020-01-01' AND
        album.release_album_date <= '2020-12-31'
    )
    order by singer_id;"""
)
result_4 = select_4.all()
print(result_4, '\n')

# # The names of collections in which a specific singer (Tim Erna) is present
# select_5 = connection.execute(
#     """select distinct collection_name from collection
#     left join collectionsong on collection.id_collection = collectionsong.collection_id
#     left join song on song.id_song = collectionsong.song_id
#     left join singersong on singersong.song_id = song.id_song
#     left join singer on singer.nickname = singersong.singer_id
#     where singer.nickname like '%Tim Erna%'
#     order by collection_name;"""
# )
# result_5 = select_5.all()
# print(result_5, '\n')

# The name of albums featuring singers of more than 1 style
select_6 = connection.execute(
    """select album_name from album
    left join song on album.id_album = song.album_id
    left join stylesong on stylesong.song_id = song.id_song
    left join style on style.id_style = stylesong.style_id
    left join singersong on singersong.song_id = song.id_song
    left join singer on singer.nickname = singersong.singer_id
    group by album_name
    having count(distinct style.style_name) > 1
    order by album_name;"""
)
result_6 = select_6.all()
print(result_6, '\n')

# The name of songs that are not included in the collections
select_7 = connection.execute(
    """select song_name from song
    left join collectionsong on song.id_song = collectionsong.song_id
    where collectionsong.song_id is NULL"""
)
result_7 = select_7.all()
print(result_7, '\n')

# The singer(s) who wrote the shortest song in duration
select_8 = connection.execute(
    """select singer.nickname, song_length from song
    left join album on album.id_album = song.id_song 
    left join singersong on singersong.song_id = song.id_song 
    left join singer on singer.nickname = singersong.singer_id
    group by singer.nickname, song_length
    having song_length = (select min(song_length) from song)
    order by singer.nickname"""
)
result_8 = select_8.all()
print(result_8, '\n')

# The name of albums containing the least number of songs
select_9 = connection.execute(
    """select album_name from album
    where num_of_songs = (select min(num_of_songs) from album);"""
)
result_9 = select_9.all()
print(result_9, '\n')
