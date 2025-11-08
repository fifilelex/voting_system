# GLOBAL VARIABLES
candidates = ['Zackary Cameron', 'Siobhan Bush', 'Lewis Gardner', 'Michaela Jefferson', 'Camilla Leach',
              'Caitlyn Munoz', 'Vera Li', 'Betty Valdez', 'Clark Mccormick', 'Noel Marshall']
votes = []
voting_mode = ''


# CANDIDATE MANAGEMENT
def create_candidate():  # edits in candidate list (only adding yet)
    global candidates

    should_exit = False
    print(f'If you want to close and save changes, write "close"')
    while not should_exit:
        c = input(f"Write down candidate's name and surname. ")
        if c.lower() == 'close':
            should_exit = True
            break
        if c not in candidates:
            candidates.append(c)
            print(f'Candidate {c} added successfully. ')


def edit_candidate(number):  # edit candidate's name
    global candidates

    print(f'CANDIDATE: {candidates[number]}. TYPE EDITED DETAILS: ')
    try:
        edited_candidate = input('Type name and surname separated by a space: ')
        candidates[number] = edited_candidate
    except ValueError:
        print('You have to type a name and surname!')


def delete_candidate():
    global candidates
    try:
        index = int(input(f"Type candidate's number: "))
        try:
            candidates.remove(candidates[index])
        except IndexError:
            print('Selected candidate is not in list')

    except ValueError:
        print("You have to type candidate's number! ")


def create_candidate_id():  # creates ids for every candidate
    global candidates
    candidates_id = []
    for index in (range(len(candidates))):
        candidates_id.append(index)
    return candidates_id


# ELECTION MANAGEMENT
def vote_setup():  # initializes voting list
    global votes
    for i in range(len(candidates)):
        votes.append(0)


def election_initialize():
    try:
        work_mode = input("""
    ----------ELECTION_APP----------
    Select mode:
    MANAGE - manager mode
    USER - used to vote
    -------------------------------- """)
    except ValueError:
        print('You have to type a number!')
    if work_mode.upper() == 'MANAGE':
        return work_mode
    elif work_mode.upper() == 'USER':
        return work_mode

    if work_mode.upper() in ['MANAGE', 'USER']:
        return work_mode
    else:
        print('It is not a valid work mode.')
        return election_initialize()


# VOTING
def vote(number):
    global votes
    votes[number] += 1


# prepare elections
voting_mode = election_initialize().upper()
vote_setup()
print(voting_mode)
while voting_mode in ['MANAGE', 'USER']:  # manage elections

    # create exceptions for int inputs
    while voting_mode == 'MANAGE':
        try:
            option = int(input('Pick what you want to do: '))
        except ValueError:
            print('You have to type a number!')
        match option:
            case 0:
                voting_mode = 'exit'
                break
            case 1:  # view list of candidates
                print(candidates)
            case 2:  # add candidate to the list
                create_candidate()
                votes.append(0)
            case 3:
                try:
                    index = int(input('Type number of the candidate'))
                except ValueError:
                    print('You have to type a number!')
                edit_candidate(index)
            case 4:
                delete_candidate()
            case 5:  # vote for someone (no validation yet)

                try:
                    index = int(input('Type number of the candidate'))
                except ValueError:
                    print('You have to type a number!')
                vote(index)
            case 6:  # returns election result
                print(votes)
            case _:
                print('Invalid value.')
    while voting_mode == 'USER':
        try:
            option = int(input('Pick what you want to do: '))
        except ValueError:
            print('You have to type a number!')
        match option:
            case 0:
                voting_mode = 'exit'
                break
            case 1:
                print(candidates)
            case 2:  # vote for someone (no validation yet)
                try:
                    index = int(input(f'Type number of the candidate'))
                except ValueError:
                    print('You have to type a number!')
                vote(index)
            case _:
                print('Invalid value.')
