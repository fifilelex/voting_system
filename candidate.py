class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def edit(self, name):
        self.name = name
    def add_vote(self):
        self.votes += 1
    def get_votes(self):
        return self.votes
    def to_dict(self):
        return {"name": self.name, "votes": self.votes}
    def getCandidates(self):
        return self.name
    def __str__(self):
        return f"{self.name} - Votes: {self.votes}" #used to return each candidate name and his result

