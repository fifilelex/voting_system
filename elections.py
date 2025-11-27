import json

class Election:
    def __init__(self, name, year):
        self.name = name
        self.voters = []
        self.candidates = []
        self.year = year
    def add_voter(self, voter):
        self.voters.append(voter)
    def add_candidate(self, candidate):
        self.candidates.append(candidate)
    def edit_candidate(self, current_name, new_name):
        candidate = self.get_candid_name(current_name)
        if candidate:
            candidate.edit(new_name)
            return True
        return False

    def delete_candidate(self, name):
        candidate = self.get_candid_name(name)
        if candidate:
            self.candidates.remove(candidate)
            return True
        else:
            return False
    def get_candid_name(self, name):
        return next((c for c in self.candidates if c.name == name), None)
    def vote(self, voter_name, candidate_name):
        voter = next((v for v in self.voters if v.name == voter_name), None)
        candidate = next((c for c in self.candidates if c.name == candidate_name), None)
        if voter and candidate and not voter.has_voted:
            candidate.add_vote()
            voter.has_voted = True
        else:
            print('Error or voter already voted')
    def findWinner(self):
        if not self.candidates:
            return []
        max_votes = max(c.votes for c in self.candidates)
        return [c for c in self.candidates if c.votes == max_votes]
    def results(self):
        results_data = [c.to_dict() for c in self.candidates] #makes candidates data a dictionary

        with open(f"{self.name}_results.json", 'w', encoding='utf-8' ) as f:
            json.dump({
                "Election": self.name,
                "Candidates": results_data
            }, f, indent=4, ensure_ascii=False)

        for c in self.candidates:
            print(c)

        winner = self.findWinner()
        if winner:
            print("\nElection winner(s):")
            for w in winner:
                print(f"{w.name} with {w.votes} votes")
        data_winner = {
            "Election": self.name,
            "Winners": [c.to_dict() for c in winner]
        }
        with open(f"{self.name}_results.json", 'w', encoding='utf-8') as f:
            json.dump(data_winner, f, indent=4, ensure_ascii=False)
        return winner

