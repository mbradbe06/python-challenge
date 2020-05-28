import os
import csv

election_csv = os.path.join("..","Resources","election_data.csv")

#variables and lists to track to accomplish HW obj
Total_Votes = 0
Candidates = []
Khan_Votes = 0
Correy_Votes = 0
Li_Votes = 0
OTooley_Votes = 0

#open and read file row by row
with open (election_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip header
    next(csvreader)

    for row in csvreader:
        #Count total votes
        Total_Votes += 1
        #format Candidates list with unique candidate names
        if row[2] not in Candidates:
            Candidates.append(row[2])
        #Candidates print as ['Khan', 'Correy', 'Li', "O'Tooley"]
        
        #Tally their individual vote counts
        if row[2] == Candidates[0]:
            Khan_Votes += 1
        elif row[2] == Candidates[1]:
            Correy_Votes += 1
        elif row[2] == Candidates[2]:
            Li_Votes += 1
        elif row[2] == Candidates[3]:
            OTooley_Votes += 1

#function to figure out percentage of votes for each candidate
def percentage(votes):
    percentage = round(((votes/Total_Votes)*100),2)
    return(percentage)

Khan_Percentage = percentage(Khan_Votes)
Correy_Percentage = percentage(Correy_Votes)
Li_Percentage = percentage(Li_Votes)
OTooley_Percentage = percentage(OTooley_Votes)

Khan=(Candidates[0],Khan_Percentage,Khan_Votes)
Correy=(Candidates[1],Correy_Percentage,Correy_Votes)
Li=(Candidates[2],Li_Percentage,Li_Votes)
OTooley=(Candidates[3],OTooley_Percentage,OTooley_Votes)

#determine winner from above tuples placed together
Candidate_Summary = (Khan,Li,Correy,OTooley)
Winner = max(Candidate_Summary, key = lambda i : i[1])

print('Election Results')
print('------------------------')
print(f'Total Votes: {Total_Votes}')
print('------------------------')
print(f'{Candidates[0]}: {Khan_Percentage}% ({Khan_Votes})')
print(f'{Candidates[1]}: {Correy_Percentage}% ({Correy_Votes})')
print(f'{Candidates[2]}: {Li_Percentage}% ({Li_Votes})')
print(f'{Candidates[3]}: {OTooley_Percentage}% ({OTooley_Votes})')
print("------------------------")
print(f'Winner: {Winner[0]}')
print('------------------------')

output_path = os.path.join('..',"Analysis","PyPoll.txt")

with open(output_path, 'a') as txtfile:

    print('Election Results', file=txtfile)
    print('------------------------', file=txtfile)
    print(f'Total Votes: {Total_Votes}', file=txtfile)
    print('------------------------', file=txtfile)
    print(f'{Candidates[0]}: {Khan_Percentage}% ({Khan_Votes})', file=txtfile)
    print(f'{Candidates[1]}: {Correy_Percentage}% ({Correy_Votes})', file=txtfile)
    print(f'{Candidates[2]}: {Li_Percentage}% ({Li_Votes})', file=txtfile)
    print(f'{Candidates[3]}: {OTooley_Percentage}% ({OTooley_Votes})', file=txtfile)
    print("------------------------", file=txtfile)
    print(f'Winner: {Winner[0]}', file=txtfile)
    print('------------------------', file=txtfile)