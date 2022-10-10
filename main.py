import sqlalchemy


db = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# print(engine.get_table_names())
# """What tables are in the database"""

# name and year of release of albums released in 2018
select_1 = connection.execute(
    """SELECT albumname, releasealbumdate FROM album 
    WHERE releasealbumdate BETWEEN '2018-01-01' AND '2018-12-31';"""
)
result_1 = select_1.all()
print(result_1, '\n')

# the name and duration of the longest track
select_2 = connection.execute(
    """SELECT songname, songlength FROM song
    ORDER BY songlength DESC"""
)
result_2 = select_2.all()[0]
print(result_2, '\n')

# The name of songs with a duration if at least 3.5 min
select_3 = connection.execute(
    """SELECT songname FROM song
    WHERE songlength >= '00:03:30'"""
)
result_3 = select_3.all()
print(result_3, '\n')

# Name of collections published in the period from 2018 to 2020 inclusive
select_4 = connection.execute(
    """SELECT collectionname FROM collection
    WHERE releasecollectiondate BETWEEN '2018-01-01' AND '2020-12-31'"""
)
result_4 = select_4.all()
print(result_4, '\n')

# Singres whose Nickname consists of 1 word
select_5 = connection.execute(
    """SELECT nickname FROM singer
    WHERE nickname NOT LIKE '%% %%' AND nickname NOT LIKE '%%.%%'"""
)
result_5 = select_5.all()
print(result_5, '\n')

# The name of the songs that contain the word "my" or "мой"
select_6 = connection.execute(
    """SELECT songname FROM song
    WHERE songname LIKE '%%my%%' OR songname LIKE '%%мой%%'
    OR songname LIKE '%%My%%' OR songname LIKE '%%Мой%%'"""
)
result_6 = select_6.all()
print(result_6, '\n')