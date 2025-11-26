class Election:
    def __init__(self):
        self.voters = []
        self.candidates = []
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
    def results(self):
        for c in self.candidates:
            print(c)