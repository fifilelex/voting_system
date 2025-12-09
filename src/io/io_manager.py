class IOManager:
    def getCandidateName_add(self):
        return input('Type name of candidate that you want to add')

    def getCandidateName_edit(self):
        current_name = input('Type name of candidate that you want to edit')
        new_name = input('Type new name for the candidate')
        return current_name, new_name
    def getCandidateName_remove(self):
        return input('Type name of candidate that you want to delete')

    def getVotingData(self):
        voter_name = input("Type your name")
        candid_name = input("Type name of candidate that you want to vote for")
        return voter_name, candid_name
    def getInput(self):
        return input()
    def success(self):
        return print("Success!")
    def error(self):
        return print("Error!")
