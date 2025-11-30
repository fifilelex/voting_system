class Voter:
    def __init__(self, name, constituency):
        self.name = name
        self.constituency_nr = constituency
        self.has_voted = False
    def to_dict(self):
        return {
            "name": self.name,
            "constituency number": self.constituency_nr
        }
