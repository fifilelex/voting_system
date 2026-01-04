import json

class JsonData:
    def json_dump_election_data(self, election, cand, voters):
        with open(f"data/{election.name}_candidates.json", 'w', encoding='utf-8') as ca:
            json.dump(cand, ca, indent=4, ensure_ascii=False)
        with open(f"data/{election.name}_voters.json", 'w', encoding='utf-8') as vo:
            json.dump(voters, vo, indent=4, ensure_ascii=False)