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
        if self.isVoter(name, nr):
            raise ValueError(f"Voter {name} already exists!")
        self.voters.append(Voter(name, nr))


    def get_voter(self, name: str, nr: int):
        return next((v for v in self.voters if v.name == name), False)
    def isVoter(self, name: str, nr: int):
        return any (v.name == name and v.constituency_nr== nr for v in self.voters)

    # EDITING CANDIDATE LIST

    def add_candidate(self, name: str):
        if self.isCandidate(name):
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
            print(Candidate.getCandidates(c))


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
        if self.candidates is None:
            raise ValueError("Candidates list is empty!")
        max_votes = max(c.votes for c in self.candidates)
        return [c for c in self.candidates if c.votes == max_votes]
    def results(self):
        results_data = [c.to_dict() for c in self.candidates] #makes candidates data a dictionary
        winner = self.find_winner()

        if winner:
            print("\nElection winner(s):")
            for w in winner:
                print(f"{w.name} with {w.votes} votes")
        with open(f"data/{self.name}_results.json", 'w', encoding='utf-8' ) as f:
            json.dump({
                "Election": self.name,
                "Candidates": results_data,
                "Winners": [c.to_dict() for c in winner]
            }, f, indent=4, ensure_ascii=False)

        for c in self.candidates:
            print(c)

        return winner
    def close(self):
        with open(f"data/{self.name}_candidates.json", 'w', encoding='utf-8') as ca:
            cand = [c.to_dict() for c in self.candidates]
            json.dump(cand, ca, indent=4, ensure_ascii=False)
        with open(f"data/{self.name}_voters.json", 'w', encoding='utf-8') as vo:
            voters = [v.to_dict() for v in self.voters]
            json.dump(voters, vo, indent=4, ensure_ascii=False)

