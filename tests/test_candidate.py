
from src.models.candidate import Candidate
def test_add_vote():
    c = Candidate("Andrzej Duda")
    c.add_vote()
    assert Candidate.get_votes(c) == 1
