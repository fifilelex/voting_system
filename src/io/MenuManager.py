from src.io.menu import *
from src.models.candidate import *
from src.models.voter import *

def call_submenu_handler(io, election):
    call_submenu()
    match io.getInput():
                case "1":
                    name = io.getCandidateName_add()
                    candid = Candidate(name)
                    election.add_candidate(candid)
                case "2":
                    current_name, new_name = io.getCandidateName_edit()
                    if election.edit_candidate(current_name, new_name):
                        io.success()
                    else:
                        io.error()
                case "3":
                    name = io.getCandidateName_remove()
                    if election.delete_candidate(name):
                        io.success()
                    else:
                        io.error()
                case "4":
                    election.getCandidates()
                case "5":
                    call_menu_handler(io, election)
                case _:
                    io.error()
def call_menu_handler(io, election):
    call_menu()
    match io.getInput():
        case "0":
            election.getCandidates()
        case "1":
            call_submenu()
            call_submenu_handler(io, election)
        case "2":
            voter_name, candid_name = io.getVotingData()

            election.vote(voter_name, candid_name)
        case "3":
            election.results()
        case "4":
            election.close()
            return False
        case _:
            io.error()
    return True