from voter import Voter
from candidate import Candidate
from elections import Election
from test import sample_test_data


#MENU
election = Election()
sample_test_data(election)
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