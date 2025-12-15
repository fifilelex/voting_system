from src.services.elections import Election
from tests.test import sample_test_data
def election():
    e = Election("e", 2026)
    sample_test_data(e)
    return e
def test_add_voter():
    e = election()
    name = "Andrew Jones"
    nr = 1
    assert e.isVoter(name, nr) == False, f"Voter {name} with nr {nr} found! Error!"

    assert e.add_voter(name, nr) is True
    assert e.isVoter(name, nr), f"Voter {name} with nr {nr} not found"

    name, nr = "Maciek Orluk", 2
    assert e.add_voter(name, nr) is True
    assert e.isVoter(name, nr), f"Voter {name} with nr {nr} not found"

    name, nr = "Orzeł Ówtąrzszny", 2
    assert e.add_voter(name, nr) is True
    assert e.isVoter(name, nr), f"Voter {name} with nr {nr} not found"
def test_add_n_voters():
    e = election()
    new_voters = [
    ["Anna Kowalska", 1],
    ["Piotr Nowak", 2],
    ["Katarzyna Wiśniewska", 3],
    ["Marcin Wójcik", 4],
    ["Agnieszka Kamińska", 5],
    ["Tomasz Lewandowski", 6],
    ["Magdalena Zielińska", 7],
    ["Paweł Szymański", 8],
    ["Joanna Kaczmarek", 9],
    ["Marek Jabłoński", 10],
    ["Ewa Mazur", 11],
    ["Łukasz Wojciechowski", 12],
    ["Monika Piotrowska", 13],
    ["Krzysztof Grabowski", 14],
    ["Natalia Pawłowska", 15],
    ["Adam Górski", 16],
    ["Barbara Dudek", 17],
    ["Grzegorz Rutkowski", 18],
    ["Sylwia Michalska", 19],
    ["Rafał Nowicki", 20]
]

    for i in range(len(new_voters)):
        name = new_voters[i][0]
        nr = new_voters[i][1]
        e.add_voter(name, nr)
        assert e.isVoter(name, nr), f"Voter {name} with nr {nr} not found"


def test_edit_candidate():
    e = election()

    current_name = "Adrian Zandberg"
    edit_name = "Potężny Duńczyk"
    try:
        e.edit_candidate(current_name, edit_name)
    except StopIteration:
        return f"Candidate {current_name} failed to edit (Candidate not found)."
    assert e.isCandidate(edit_name), f"Candidate {current_name} failed to edit"

    current_name = "Goroncywir21"
    edit_name = "Gżegżółka"
    try:
        e.edit_candidate(current_name, edit_name)
    except StopIteration:
        return f"Candidate {current_name} failed to edit (Candidate not found)."
    assert e.isCandidate(edit_name) == None, f"Candidate {current_name} edited when it was expected to fail."
    current_name = "Jarosław Staszkiewicz"
    edit_name = "Gżegżółką"
    try:
        e.edit_candidate(current_name, edit_name)
    except StopIteration:
        return f"Candidate {current_name} failed to edit (Candidate not found)."
    assert e.isCandidate(edit_name)

