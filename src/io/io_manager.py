import json
class IOManager:
    def get_candidate_name_add(self):
        return input('Type name of candidate that you want to add')


    def get_candidate_name_edit(self):
        current_name = input('Type name of candidate that you want to edit')
        new_name = input('Type new name for the candidate')
        return current_name, new_name


    def get_candidate_name_remove(self):
        return input('Type name of candidate that you want to delete')


    def get_voting_data(self):
        voter_name = input("Type your name")
        candid_name = input("Type name of candidate that you want to vote for")
        return voter_name, candid_name


    def get_input(self):
        return input()
    def print_all_candidates(self, candidates):
        for c in candidates:
            print(c)

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


    def save_data(self, election):
        cand = [c.to_dict() for c in election.candidates]
        voters = [v.to_dict() for v in election.voters]
        return cand, voters



    def success(self, msg):
        return print(f"{msg}")


    def error(self, msg):
        return print(msg)
