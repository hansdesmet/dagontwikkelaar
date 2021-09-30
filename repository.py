from sqlalchemy import create_engine

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