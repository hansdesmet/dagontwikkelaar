from sqlalchemy import create_engine
from os import environ

if 'DATABASE_URL' in environ:
    # web applicatie run op heroku:
    database_URL = environ['DATABASE_URL']
    database_URL = database_URL.replace("postgres://", "postgresql://")
    engine = create_engine(database_URL)
else:
    # web applicatie op mijn eigen computer:
    engine = create_engine("postgresql://petlover:petlover@localhost/catdog")

def cat_voted():
    with engine.begin() as connection:
        connection.execute("update votes set cat=cat+1")

def dog_voted():
    with engine.begin() as connection:
        connection.execute("update votes set dog=dog+1")

def read_votes():
    with engine.begin() as connection:
        return connection.execute("select cat, dog from votes").first()        