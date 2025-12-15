import json
from src.models.candidate import Candidate
from src.models.voter import Voter

class Election:
    def __init__(self, name, year):
        self.name = name
        self.voters = []
        self.candidates = []
        self.year = year
    def add_voter(self, name, nr):
        voter = Voter(name, nr)
        self.voters.append(voter)
        return True
    def isVoter(self, name, nr):
        return any (v.name == name and v.constituency_nr== nr for v in self.voters)
    def add_candidate(self, name):
        new_candidate = Candidate(name)
        self.candidates.append(new_candidate)
        return True
    def edit_candidate(self, current_name, new_name):
        candidate = self.get_candidate(current_name) #checks whether candidate is in candidate list
        if candidate:
            candidate.edit(new_name)
            return True
        return False

    def delete_candidate(self, name):
        candidate = self.get_candidate(name)
        if candidate:
            self.candidates.remove(candidate)
            return True
        else:
            return False
    def isCandidate(self, name):
        for c in self.candidates:
            if name == c.name:
                return True
        else:
            return False
    def get_candidate(self, name):
        return next((c for c in self.candidates if c.name == name), None)
    def get_all_candidates(self):
        for c in self.candidates:
            print(Candidate.getCandidates(c))

    def vote(self, voter_name, candidate_name):
        voter = next((v for v in self.voters if v.name == voter_name), None)
        candidate = next((c for c in self.candidates if c.name == candidate_name), None)
        if voter and candidate and not voter.has_voted:
            candidate.add_vote()
            voter.has_voted = True
            return True
        else:
            return False

    def findWinner(self):
        if not self.candidates:
            return []
        max_votes = max(c.votes for c in self.candidates)
        return [c for c in self.candidates if c.votes == max_votes]
    def results(self):
        results_data = [c.to_dict() for c in self.candidates] #makes candidates data a dictionary
        winner = self.findWinner()

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

