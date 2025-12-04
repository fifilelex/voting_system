from src.io.io_manager import IOManager
from src.io.menu import *
from src.models.candidate import Candidate
from src.services.elections import Election
from tests.test import sample_test_data


#MENU
election = Election("wybory prezydenckie", 2045)
io = IOManager()
sample_test_data(election)

while True:
    call_menu()
    choice = input()
    match choice:
        case "0":
            election.getCandidates()
        case "1":
            call_submenu()
            sub_choice = input()
            if sub_choice == "1":
                name = io.getCandidateName_add()
                candid = Candidate(name)
                election.add_candidate(candid)
                print(f"Candidate {name} added successfully.")
            elif sub_choice == "2":
                current_name, new_name = io.getCandidateName_edit()
                if election.edit_candidate(current_name, new_name):
                    print(f"Candidate {current_name} edited to {new_name}.")
                else:
                    print(f"Candidate {current_name} not found.")
            elif sub_choice == "3":
                name = io.getCandidateName_remove()
                if election.delete_candidate(name):
                    print(f"Candidate {name} deleted successfully.")
                else:
                    print(f"Error while trying to delete candidate {name}")
            elif sub_choice == "4":
                election.getCandidates()
            elif sub_choice == "5":
                break
            else:
                print("Wrong choice!")
        case "2":
            voter_name, candid_name = io.getVotingData()

            election.vote(voter_name, candid_name)
        case "3":
            election.results()
        case "4":
            election.close()
            break
