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


    def print_results(self, election, results_data, winner):
        if winner:
            print("\nElection winner(s):")
            for w in winner:
                print(f"{w.name} with {w.votes} votes")
        with open(f"data/{election.name}_results.json", 'w', encoding='utf-8' ) as f:
            json.dump({
                "Election": election.name,
                "Candidates": results_data,
                "Winners": [c.to_dict() for c in winner]
            }, f, indent=4, ensure_ascii=False)

        for c in election.candidates:
            print(c)


    def close(self, election): #should be moved to io
        with open(f"data/{election.name}_candidates.json", 'w', encoding='utf-8') as ca:
            cand = [c.to_dict() for c in election.candidates]
            json.dump(cand, ca, indent=4, ensure_ascii=False)
        with open(f"data/{election.name}_voters.json", 'w', encoding='utf-8') as vo:
            voters = [v.to_dict() for v in election.voters]
            json.dump(voters, vo, indent=4, ensure_ascii=False)


    def success(self, msg):
        return print(f"{msg}")
    def error(self, msg):
        return print(msg)
