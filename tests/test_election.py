import pytest

from src.services.elections import Election
from tests.test import sample_test_data

@pytest.fixture
def election_with_data():
    e = Election("e", 2026)
    sample_test_data(e)
    return e


def test_add_voter(election_with_data):
    e = election_with_data
    name = 'Adrian Zandberg'
    nr = 2
    e.add_voter(name, nr)
    assert e.isVoter(name, nr)

    assert e.add_voter(input_x, input_y) == expected

def test_add_candidate_duplicate(election_with_data):
    e = election_with_data
    e.add_candidate("Maciek Orluk")
    with pytest.raises(ValueError, match="already exists"):
        e.add_candidate("Maciek Orluk")

    for i in range(len(new_voters)):
        name = new_voters[i][0]
        nr = new_voters[i][1]
        assert e.add_voter(name, nr)
        assert e.isVoter(name, nr), f"Voter {name} with nr {nr} not found"

def test_is_voter(election_with_data):
    e = election_with_data
    assert e.isVoter("Maciej Orluk", 1) is False
    assert e.isVoter("Adenoid Hynkiel", 1) is True

#TEST EDITING CANDIDATE'S LIST
def test_add_single_candidate(election_with_data):
    e = election_with_data

    new_name = "Ola Owca"
    assert e.add_candidate(new_name) is True
    assert e.isCandidate(new_name) is True, f"Candidate {new_name} is not on the list."
def test_add_multiple_candidates(election_with_data):
    e = election_with_data

    new_candidates = [
        ["Anna Kowalska"],
        ["Piotr Nowak"]]
    for i in range(len(new_candidates)):
        assert e.add_candidate(new_candidates[i]) is True
        assert e.isCandidate(new_candidates[i]) is True, f"Candidate {new_candidates[i]} is not on the list."


def test_edit_candidate(election_with_data):
    e = election_with_data

    current_name = "Adrian Zandberg"
    edit_name = "Potężny Duńczyk"
    assert e.edit_candidate(current_name, edit_name), f"Candidate {current_name} failed to edit (Candidate not found)."
    assert e.isCandidate(edit_name), f"Candidate {current_name} failed to edit"

    current_name = "Goroncywir21"
    edit_name = "Gżegżółka"
    assert e.edit_candidate(current_name, edit_name) is False
    assert e.isCandidate(edit_name) is False, f"Candidate {current_name} edited when it was expected to fail."

def test_delete_existing_candidate(election_with_data):
    e = election_with_data

    assert e.isCandidate("Grzegorz Braun")
    e.delete_candidate(name="Grzegorz Braun")
    assert e.isCandidate("Grzegorz Braun") is False
def test_delete_nonexisting_candidate(election_with_data):
    e = election_with_data

    assert e.delete_candidate("Nieistniejący") is False
def test_delete_just_added_candidate(election_with_data):
    e = election_with_data

    e.add_candidate("Maciej Orluk")
    e.delete_candidate("Maciej Orluk")
    assert e.isCandidate("Maciej Orluk") is False

def test_get_existing_candidate(election_with_data):
    e = election_with_data

    assert e.get_candidate("Grzegorz Braun") is not None

def test_get_nonexisting_candidate(election_with_data):
    e = election_with_data

    assert e.get_candidate("Maciek Maciek Maciek") is None

def test_get_blank_candidate(election_with_data):
    e = election_with_data

    assert e.get_candidate("") is None

def test_vote(election_with_data):
    e = election_with_data
    c = e.get_candidate(name = "Amine Papiński")
    v = e.get_voter(name = "Adenoid Hynkiel", nr=1)
    assert e.vote(v, c) is True

def test_vote_nonexistent_candid(election_with_data):
    e = election_with_data
    c = e.get_candidate(name = "w")
    v = e.get_voter(name = "Adenoid Hynkiel", nr=1)
    assert e.vote(v, c) is False

