from src.models.candidate import Candidate
from src.models.voter import Voter

def sample_test_data(election): #used as sample data, to make testing faster
    election.add_candidate(Candidate("Grzegorz Braun"))
    election.add_candidate(Candidate("Adrian Zandberg"))
    election.add_candidate(Candidate("Amine Papiński"))
    election.add_candidate(Candidate("Jarosław Staszkiewicz"))
    election.add_voter("Adenoid Hynkiel", 1)
    election.add_voter("Tomasz Perła", 2)
    election.add_voter("Zbigniew Kucharski", 1)
    election.add_voter("Mikołaj Andrzejuk", 2)