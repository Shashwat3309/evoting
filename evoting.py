blockchain = []

voters = {"Riya": False, "Simran": False, "Aman": False, "Suraj": False}
candidates = {"Ankur": 0, "Shashwat": 0, "Aman": 0, "Priya": 0}

def cast_vote(voter, candidate):
    if voter not in voters:
        print(f"Error: {voter} is not a registered voter.")
        return

    if voters[voter]:
        print(f"Error: {voter} has already voted.")
        return

    if candidate not in candidates:
        print(f"Error: {candidate} is not a valid candidate.")
        return

    blockchain.append({"voter": voter, "candidate": candidate})
    candidates[candidate] += 1
    voters[voter] = True
    print(f"{voter} successfully voted for {candidate}!")

def display_results():
    print("\nElection Results:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

def view_blockchain():
    print("\nBlockchain Ledger:")
    for block in blockchain:
        print(block)

# Example Usage
if __name__ == "__main__":
    print("Welcome to the E-Voting System!")

    # Cast some votes
    cast_vote("Riya", "Shashwat")
    cast_vote("Simran", "Shashwat")
    cast_vote("Aman", "Shashwat")
    cast_vote("Suraj", "Priya")

    display_results()

    view_blockchain()
