from src.services.elections import Election
def election():
    return Election("e", 2026)
def test_add_voter():
    e = election()
    name = "Andrew Jones"
    nr = 1
    e.add_voter(name, nr)
    assert e.isVoter(name, nr) == True
    name, nr = "Maciek Orluk", 2
    e.add_voter(name, nr)
    assert e.isVoter(name, nr) == True
    name, nr = "Orzeł Ówtąrzszny", 2
    e.add_voter(name, nr)
    assert e.isVoter(name, nr) == True


