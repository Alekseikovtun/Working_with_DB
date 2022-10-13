import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

db = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = sq.create_engine(db)
Session = sessionmaker(bind=engine)


class Album(Base):
    __tablename__ = 'album'
    id_album = sq.Column(sq.Integer, primary_key=True)
    album_name = sq.Column(sq.String(50))
    release_album_date = sq.Column(sq.Date)
    num_of_songs = sq.Column(sq.Integer)

    songs = relationship('Song', backref='album')


class Collection(Base):
    __tablename__ = 'collection'
    id_collection = sq.Column(sq.Integer, primary_key=True)
    collection_name = sq.Column(sq.String(50))
    release_collection_date = sq.Column(sq.Date)

    songs = relationship('Song_Collection')


class Singer(Base):
    __tablename__ = 'singer'
    nickname = sq.Column(sq.String, primary_key=True)
    fsc = sq.Column(sq.String(50))
    sin_age = sq.Column(sq.Integer)

    songs = relationship('Song_Singer')


class Style(Base):
    __tablename__ = 'style'
    id_style = sq.Column(sq.Integer, primary_key=True)
    style_name = sq.Column(sq.String(40))

    songs = relationship('Song_Style')


class Song(Base):
    __tablename__ = 'song'
    id_song = sq.Column(sq.Integer, primary_key=True)
    song_name = sq.Column(sq.String(50))
    song_length = sq.Column(sq.Time)

    album_id = sq.Column(sq.Integer, sq.ForeignKey('album.id_album'))
    collection = relationship('Song_Collection')
    singer = relationship('Song_Singer')
    styles = relationship('Song_Style')


class Song_Style(Base):
    __tablename__ = 'song_style'
    id = sq.Column(sq.Integer, primary_key=True)
    id_song = sq.Column(sq.Integer, sq.ForeignKey('song.id_song'))
    id_style = sq.Column(sq.Integer, sq.ForeignKey('style.id_style'))


class Song_Singer(Base):
    __tablename__ = 'song_singer'
    id = sq.Column(sq.Integer, primary_key=True)
    id_song = sq.Column(sq.Integer, sq.ForeignKey('song.id_song'))
    id_singer = sq.Column(sq.String, sq.ForeignKey('singer.nickname'))


class Song_Collection(Base):
    __tablename__ = 'song_collection'
    id = sq.Column(sq.Integer, primary_key=True)
    id_song = sq.Column(sq.Integer, sq.ForeignKey('song.id_song'))
    id_collection = sq.Column(sq.Integer, sq.ForeignKey('collection.id_collection'))


session = Session()

# query = session.query(Album)
a = session.query(Album).filter(Album.release_album_date > '2020-01-01')
res = a.all()[0]
print()
print(res.songs)
print()
b = res.songs
for item in b:
    print(item.song_name)
