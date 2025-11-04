#GLOBAL VARIABLES
candidates = ['Zackary Cameron', 'Siobhan Bush', 'Lewis Gardner', 'Michaela Jefferson', 'Camilla Leach',
              'Caitlyn Munoz', 'Vera Li', 'Betty Valdez', 'Clark Mccormick', 'Noel Marshall']
votes = []
voting = False
#CANDIDATE MANAGEMENT
def create_candidate(): #edits in candidate list (only adding yet)
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

def edit_candidate(number): #edit candidate's name
    global candidates
    print(f'CANDIDATE: {candidates[number]}. TYPE EDITED DETAILS: ')
    edited_candidate = input('Type name and surname separated by a space: ')
    candidates[number] = edited_candidate

def create_candidate_id(): #creates ids for every candidate
    global candidates
    candidates_id = []
    for index in (range(len(candidates))):
        candidates_id.append(index)
    return candidates_id

#ELECTION MANAGEMENT
def vote_setup(): #initializes voting list
    global votes
    for i in range(len(candidates)):
        votes.append(0)

def election_initialize(voting):
    r = input('Do you want to start election? ')
    if (r.lower() == 'yes'):
        return True
    elif (r.lower() == 'no'):
        return False
    else:
        print('Provided answer is not a correct answer. Write "yes" or "no" to proceed next time')
        return voting


#VOTING
def vote(number):
    global votes
    votes[number] += 1

#prepare elections
voting = election_initialize(voting)
vote_setup()
while voting: #manage elections
    #split manage and electing:
    #you cant manage during elections (so we avoid things like we have id that does not correspond with any candidate)
    #create exceptions for int inputs
    while True:
        option = int(input('Pick what you want to do: '))
        match option:
            case 0:
                voting = False
                break
            case 1: #view list of candidates
                print(candidates)
            case 2: #add candidate to the list
                create_candidate()
                votes.append(0)
            case 3:
                index = int(input('Type number of the candidate'))
                edit_candidate(index)
            case 4: #vote for someone (no validation yet)

                index = int(input(f'Type number of the candidate'))
                vote(index)
            case 5: #returns election result
                print(votes)