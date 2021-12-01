import os

import sqlalchemy
from databases import Database
from sqlalchemy import Table, Column, Integer, String, ARRAY

DATABASE_URL = os.getenv('DATABASE_URI')

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URL)