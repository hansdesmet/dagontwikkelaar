from repository import cat_voted, dog_voted, read_votes, engine

def reset_votes():
    with engine.begin() as connection:
        connection.execute("update votes set cat=0, dog=0")

def test_read_votes():
    reset_votes()
    votes = read_votes()
    assert votes.cat == 0
    assert votes.dog == 0

def test_cat_voted():
    reset_votes()
    cat_voted()
    votes = read_votes()
    assert votes.cat == 1
    assert votes.dog == 0

def test_dog_voted():
    reset_votes()
    dog_voted()
    votes = read_votes()
    assert votes.cat==0
    assert votes.dog==1