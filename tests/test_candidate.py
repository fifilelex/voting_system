import random
from src.models.candidate import Candidate
def candidate():
    return Candidate("Tytus Ciezki")
def test_add_vote():

    c = candidate()

    for i in range(1, 4):
        c.add_vote()
        assert c.get_votes() == i

    for _ in range(3):
        c.add_vote()

    assert c.get_votes() == 6

    expected_votes = 6
    for i in range(7, 13):
        c.add_vote()
        expected_votes += 1
        assert c.get_votes() == expected_votes

    c.reset_votes()


def test_rand_add_vote():
    random.seed(21)
    c = candidate()
    num = random.randint(2, 400)
    for _ in range(num):
        c.add_vote()
    assert c.get_votes() == num
