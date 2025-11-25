# GLOBAL VARIABLES
#candidates = ['Zackary Cameron', 'Siobhan Bush', 'Lewis Gardner', 'Michaela Jefferson', 'Camilla Leach',
#              'Caitlyn Munoz', 'Vera Li', 'Betty Valdez', 'Clark Mccormick', 'Noel Marshall']
#voting_mode = ''

#CLASSES
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
    def __str__(self):
        return f"{self.name} - Votes: {self.votes}" #used to return each candidate name and his result


class Voter:
    def __init__(self, name, constituency):
        self.name = name
        self.constituency_nr = constituency
        self.has_voted = False
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
#MENU
election = Election()
while True:
    choice = input("""
--------------------------
---------ELECTION---------

Pick what you want to do:
0. Show candidate list
1. Manage candidates list
2. Vote
3. Check results

--------------------------
--------------------------
""")
    match choice:
        case "0":
            election.results()
        case "1":
            sub_choice = input("""
--------------------------
---------ELECTION---------

Pick what you want to do:
1. Add candidate
2. Edit candidate
3. Delete candidate
4. Show candidate list
5. Back to main menu

--------------------------
--------------------------
            """)
            if sub_choice == "1":
                candid_name = input('Type name of candidate that you want to add')
                candid = Candidate(candid_name)
                election.add_candidate(candid)
                print(f"Candidate {candid_name} added successfully.")
            elif sub_choice == "2":
                current_name = input('Type name of candidate that you want to edit')
                new_name = input('Type new name for the candidate')
                if election.edit_candidate(current_name, new_name):
                    print(f"Candidate {current_name} edited to {new_name}.")
                else:
                    print(f"Candidate {current_name} not found.")
            elif sub_choice == "3":
                candid_name = input('Type name of candidate that you want to delete')
                if election.delete_candidate(candid_name):
                    print(f"Candidate {candid_name} deleted successfully.")
                else:
                    print(f"Error while trying to delete candidate {candid_name}")
            elif sub_choice == "4":
                election.results()
            elif sub_choice == "5":
                break
            else:
                print("Wrong choice!")
        case "2":
            voter_name = input("Type your name")
            candid_name = input("Type name of candidate that you want to vote for")
            election.vote(voter_name, candid_name)
        case "3":
            election.results()
