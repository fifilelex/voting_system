from candidate import Candidate
from voter import Voter

def sample_test_data(election): #used as sample data, to make testing faster
    election.add_candidate(Candidate("Grzegorz Braun"))
    election.add_candidate(Candidate("Adrian Zandberg"))
    election.add_candidate(Candidate("Amine Papiński"))
    election.add_candidate(Candidate("Jarosław Staszkiewicz"))
    election.add_voter(Voter("Adenoid Hynkiel", 1))
    election.add_voter(Voter("Tomasz Perła", 2))
    election.add_voter(Voter("Zbigniew Kucharski", 1))
    election.add_voter(Voter("Mikołaj Andrzejuk", 2))