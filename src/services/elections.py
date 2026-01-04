import json
from src.models.candidate import Candidate
from src.models.voter import Voter

class Election:
    def __init__(self, name, year):
        self.name = name
        self.voters = []
        self.candidates = []
        self.year = year

    #EDITING VOTER LIST

    def add_voter(self, name: str, nr: int):
        if self.is_voter(name, nr):
            raise ValueError(f"Voter {name} already exists!")
        self.voters.append(Voter(name, nr))


    def get_voter(self, name: str, nr: int):
        return next((v for v in self.voters if v.name == name), None)


    def is_voter(self, name: str, nr: int):
        return any(v.name == name and v.constituency_nr== nr for v in self.voters)


    # EDITING CANDIDATE LIST

    def add_candidate(self, name: str):
        if self.is_candidate(name):
            raise ValueError(f"Candidate {name} already exists!")
        self.candidates.append(Candidate(name))


    def edit_candidate(self, current_name: str, new_name:str):
        if current_name is None or new_name is None:
            raise ValueError("You need to provide both current name and new name of candidate")
        candidate = self.get_candidate(current_name) #checks whether candidate is in candidate list
        if candidate is None:
            raise ValueError(f"Candidate {current_name} does not exist!")
        candidate.edit(new_name)


    def delete_candidate(self, name: str):
        candidate = self.get_candidate(name)
        if candidate is None:
            raise ValueError(f"Candidate {name} does not exist")
        self.candidates.remove(candidate)


    def is_candidate(self, name: str) -> bool:
        return any(c.name == name for c in self.candidates)


    def get_candidate(self, name: str):
        return next((c for c in self.candidates if c.name == name), None)
    def get_all_candidates(self):
        for c in self.candidates:
            print(Candidate.get_candidates(c))


    def vote(self, voter, candidate):
        if voter is None:
            raise ValueError("Voter not found")
        if candidate is None:
            raise ValueError("Candidate not found")
        if voter.has_voted:
            raise ValueError(f"{voter.name} has already voted")

        candidate.add_vote()
        voter.has_voted = True


    #ELECTION RELATED
    def find_winner(self):
        if not self.candidates:
            raise ValueError("Candidates list is empty!")
        max_votes = max(c.votes for c in self.candidates)
        return [c for c in self.candidates if c.votes == max_votes]


    def results(self): #should be moved to io
        results_data = [c.to_dict() for c in self.candidates] #makes candidates data a dictionary
        winner = self.find_winner()



        return results_data, winner




