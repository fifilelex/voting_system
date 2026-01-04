from src.models.candidate import Candidate
from enum import Enum

class MENURESULTS(Enum):
    CONTINUE = 1
    BACK = 2
    NEXT = 3
    EXIT = 4


def call_submenu_handler(io, election):
    try:
        choice = int(io.get_input())
    except ValueError:
        return "Invalid value."
    if choice == 1:
        name = io.get_candidate_name_add()
        election.add_candidate(name)
        return MENURESULTS.CONTINUE
    elif choice == 2:
        current_name, new_name = io.get_candidate_name_edit()
        election.edit_candidate(current_name, new_name)
        return MENURESULTS.CONTINUE
    elif choice == 3: #delete candidate
        deletion_name = io.get_candidate_name_remove()
        election.delete_candidate(deletion_name)
        return MENURESULTS.CONTINUE
    elif choice ==  4: #get list of all candidates
        election.get_all_candidates()
        return MENURESULTS.CONTINUE
    elif choice == 5: #return to main menu
        return MENURESULTS.BACK
    else:
        io.error()
        return MENURESULTS.BACK
def call_menu_handler(io, election, data):
        try:
            choice = int(io.get_input())
        except ValueError:
            return "Invalid value."
        if choice ==  0: #get list of all candidates
                candids = election.get_all_candidates()
                io.print_all_candidates(candids)
                return MENURESULTS.CONTINUE
        elif choice == 1: #show menu for candidates management
                return MENURESULTS.NEXT
        elif choice == 2: #vote for x
            voter_name, candid_name = io.get_voting_data()
            c = election.get_candidate(candid_name)
            v = election.get_voter(voter_name)
            try:
                election.vote(v, c)
            except ValueError as e:
                io.error(str(e))
            else:
                io.success("Vote casted successfully!")
            return MENURESULTS.CONTINUE
        elif choice == 3: #get election result
                election.results()
                return MENURESULTS.CONTINUE
        elif choice == 4: #close app
                cand, voters = io.save_data(election)
                data.json_dump_election_data(election, cand, voters)
                return MENURESULTS.EXIT
        else: #wrong choice
            io.error()
            return MENURESULTS.BACK