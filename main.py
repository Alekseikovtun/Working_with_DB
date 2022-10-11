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