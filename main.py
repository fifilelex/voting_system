from src.io.io_manager import *
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

    match io.getInput():
        case "0":
            election.getCandidates()
        case "1":
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
                    break
                case _:
                    io.error()
        case "2":
            voter_name, candid_name = io.getVotingData()

            election.vote(voter_name, candid_name)
        case "3":
            election.results()
        case "4":
            election.close()
            break
        case _:
            io.error()
