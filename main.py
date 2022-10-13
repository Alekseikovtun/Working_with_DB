import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

db = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = sq.create_engine(db)
Session = sessionmaker(bind=engine)
connection = engine.connect()


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
    is_deleted = sq.Column(sq.Boolean)

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


# create row

# new_song1 = Song(id_song=21, song_name='aaa', song_length='00:03:00', is_deleted=True)
# new_song2 = Song(id_song=22, song_name='bbb', song_length='00:03:30', is_deleted=True)
# session.add_all([new_song1, new_song2])
# session.commit()

#update row

# update_song = session.query(Song).filter(Song.id_song == 21)
# record = update_song.one()
# record.is_deleted = False
# session.commit()
# or I could use: record = update(Song).where(Song.id_song == 21).values(is_deleted=False)

# delete row

# deleting_song = session.query(Song).filter(Song.id_song == 22).delete()
# session.commit()