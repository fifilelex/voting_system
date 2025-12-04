from src.io.menu import *
from src.models.candidate import *

def call_submenu_handler(io, election):
    call_submenu()
    match io.getInput():
            case "1": #add candidate
                name = io.getCandidateName_add()
                candid = Candidate(name)
                if election.add_candidate(candid):
                    io.success()
            case "2": #edit candidate
                current_name, new_name = io.getCandidateName_edit()
                if election.edit_candidate(current_name, new_name):
                    io.success()
                else:
                    io.error()
            case "3": #delete candidate
                name = io.getCandidateName_remove()
                if election.delete_candidate(name):
                        io.success()
                else:
                        io.error()
            case "4": #get list of all candidates
                election.getCandidates()
            case "5": #return to main menu
                call_menu_handler(io, election)
            case _:
                io.error()
def call_menu_handler(io, election):
    call_menu()
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