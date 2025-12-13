from src.models.candidate import Candidate

def call_submenu_handler(io, election):
    try:
        choice = int(io.getInput())
    except ValueError:
        return "Invalid value."
    if choice == 1:
        name = io.getCandidateName_add()
        new_candidate = Candidate(name)
        return election.add_candidate(new_candidate)
    elif choice == 2:
        current_name, new_name = io.getCandidateName_edit()
        return election.edit_candidate(current_name, new_name)
    elif choice == 3: #delete candidate
        deletion_name = io.getCandidateName_remove()
        return election.delete_candidate(deletion_name)
    elif choice ==  4: #get list of all candidates
        election.getCandidates()
        return True
    elif choice == 5: #return to main menu
        return "back"
    else:
        return False
def call_menu_handler(io, election):
        choice = int(io.getInput())
        if choice ==  0: #get list of all candidates
                election.getCandidates()
                return True
        elif choice == 1: #show menu for candidates management
                return "next"
        elif choice == 2: #vote for x
            voter_name, candid_name = io.getVotingData()
            if election.vote(voter_name, candid_name):
                    io.success()
                    return True
            else:
                io.error()
                return False
        elif choice == 3: #get election result
                election.results()
        elif choice == 4: #close app
                election.close()
                return "close"
        else: #wrong choice
            io.error()
            return False