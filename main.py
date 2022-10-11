import sqlalchemy


db = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# print(engine.get_table_names())
# """What tables are in the database"""

# # Number of singers in each style
# select_1 = connection.execute(
#     """;"""
# )
# result_1 = select_1.all()
# print(result_1, '\n')

# Number of songs included in albums 2019-2020
select_2 = connection.execute(
    """SELECT album_name, release_album_date, num_of_songs 
    FROM album AS a
    LEFT JOIN song AS s ON s.album_id = id_album 
    WHERE (release_album_date>='2019-01-01') AND (release_album_date<='2020-12-31')
    GROUP BY (album_name, release_album_date, num_of_songs);"""
)
result_2 = select_2.all()[0][2]
print(result_2, '\n')

# # Number of singers in each style
# select_1 = connection.execute(
#     """;"""
# )
# result_1 = select_1.all()
# print(result_1, '\n')

# # Number of singers in each style
# select_1 = connection.execute(
#     """;"""
# )
# result_1 = select_1.all()
# print(result_1, '\n')

# # Number of singers in each style
# select_1 = connection.execute(
#     """;"""
# )
# result_1 = select_1.all()
# print(result_1, '\n')

# # Number of singers in each style
# select_1 = connection.execute(
#     """;"""
# )
# result_1 = select_1.all()
# print(result_1, '\n')