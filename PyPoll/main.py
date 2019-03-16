#Election Results

import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    voterID = []
    county = []
    candidate = []

    khan = 0
    correy = 0
    li = 0
    tooley = 0

    for row in csvreader:
        voterID.append(row[0])
        if row[1] not in county:
            county.append(row[1])
        if row[2] not in candidate:
            candidate.append(row[2])
        if row[2] == "Khan":
            khan += 1
        if row[2] == "Correy":
            correy += 1
        if row[2] == "Li":
            li += 1
        if row[2] == "O'Tooley":
            tooley += 1

    TotalVote = len(voterID)

        
    votedict = {candidate[0]: [round(((khan/TotalVote)*100), 3), khan],
                candidate[1]: [round(((correy/TotalVote)*100), 3), correy],
                candidate[2]: [round(((li/TotalVote)*100), 3), li],
                candidate[3]: [round(((tooley/TotalVote)*100), 3), tooley]}

    listofvote = [khan, correy, li, tooley]
    maxvote = max(listofvote)
    
    if votedict["Khan"][1] == maxvote:
        winner = "Khan"
    if votedict["Correy"][1] == maxvote:
        winner = "Correy"
    if votedict["Li"][1] == maxvote:
        winner = "Li"
    if votedict["O'Tooley"][1] == maxvote:
        winner = "O'Tooley"

    
    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {TotalVote}")
    print("-----------------------")
    print(f"Khan: {votedict['Khan'][0]}% ({khan})")
    print(f"Correy: {votedict['Correy'][0]}% ({correy})")
    print(f"Li: {votedict['Li'][0]}% ({li})")
    print(f"O'Tooley: {round(((tooley/TotalVote)*100), 3)}% ({tooley})")
    print("-----------------------")
    print(f"Winner: {winner}")
    print("-----------------------")

output_path = os.path.join("PyPoll.txt")
with open(output_path, 'w') as txtfile:

    txtfile.write("Election Results")
    txtfile.write("\n")
    txtfile.write("-----------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {TotalVote}")
    txtfile.write("\n")
    txtfile.write("-----------------------")
    txtfile.write("\n")
    txtfile.write(f"Khan: {votedict['Khan'][0]}% ({khan})")
    txtfile.write("\n")
    txtfile.write(f"Correy: {votedict['Correy'][0]}% ({correy})")
    txtfile.write("\n")
    txtfile.write(f"Li: {votedict['Li'][0]}% ({li})")
    txtfile.write("\n")
    txtfile.write(f"O'Tooley: {round(((tooley/TotalVote)*100), 3)}% ({tooley})")
    txtfile.write("\n")
    txtfile.write("-----------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("\n")
    txtfile.write("-----------------------")






