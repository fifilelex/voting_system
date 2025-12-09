from src.io.menu import *
from src.models.candidate import *

def call_submenu_handler(io, election):

    choice = int(io.getInput)
    if choice == 1:
        return election.add_candidate(Candidate(io.getCandidateName_add()))
    elif choice == 2:
        current_name, new_name = io.getCandidateName_edit()
        return election.edit_candidate(current_name, new_name)
    elif choice == 3: #delete candidate
        return election.delete_candidate(io.getCandidateName_remove())
    elif choice ==  4: #get list of all candidates
        election.getCandidates()
        return True
    elif choice == 5: #return to main menu
        return "back"
    else:
        io.error()
def call_menu_handler(io, election):
    match io.getInput():
        case "0": #get list of all candidates
            election.getCandidates()
        case "1": #show menu for candidates management
            call_submenu()
            call_submenu_handler(io, election)
        case "2": #vote for x
            voter_name, candid_name = io.getVotingData()

            if election.vote(voter_name, candid_name):
                io.success()
            else:
                io.error()
        case "3": #get election result
            election.results()
        case "4": #close app
            election.close()
            return False
        case _: #wrong choice
            io.error()
    return True