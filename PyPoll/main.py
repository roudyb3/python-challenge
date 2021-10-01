#module for creating file paths across operating systems
import os

#Module for reading the PyPoll CSV file
import csv
pypoll_csv = os.path.join('Resources','election_data.csv')
#print(pypoll_csv)

#create a list to hold the variables
votes = []
candidates = []
candidates_unique = []
candidate_vote = []

#initialize the vote counts before appending data
total_count = 0

#create a function to add the data from the column to the list
def pypoll(columns):
    
    voter_id = (columns[0])
    votes.append(voter_id)

    county = (columns[1])
    
    candidate = (columns[2])
    candidates.append(candidate)

#read the csv file
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    #write a for loop to go through the file 
    for row in csvreader:
        total_count += 1
        pypoll(row)        

for candidate in candidates:
    if candidate not in candidates_unique:
        candidates_unique.append(candidate)
   
for candidate in candidates_unique:
    candidates_count = candidates.count(candidate)
    candidate_vote.append(candidates_count)

#assign each candidate the proper vote total
khan_votes = candidate_vote[0]
correy_votes = candidate_vote[1]
li_votes = candidate_vote[2]
otooley_votes = candidate_vote[3]

#find the percentage of the vote each canddidate received
khan_pct = (khan_votes/total_count)*100
correy_pct = (correy_votes/total_count)*100
li_pct = (li_votes/total_count)*100
otooley_pct = (otooley_votes/total_count)*100

#find the winner
winning_candidate = max(candidate_vote)
winner = candidates_unique[candidate_vote.index(winning_candidate)]


#print the output
print("Election Results")
print("-------------------------------")
print("Total Votes:",(total_count))
print("-------------------------------")
print("Khan: ", (khan_pct), "% ", (khan_votes))
print("Correy: ", (correy_pct), "% ", (correy_votes))
print("Li: ", (li_pct), "% ", (li_votes))
print("O'Tooley: ", (otooley_pct), "% ", (otooley_votes))
print("-------------------------------")
print("Winner: ", (winner))
print("-------------------------------")

#write in the results to a textfile
output_file = os.path.join('Analysis', 'output.txt')
with open (output_file, 'w') as text_file:
    text_file.write("Election Results")
    text_file.write(" ")
    text_file.write("-------------------------------")
    text_file.write(" ")
    text_file.write(f"Total Votes:{total_count}")
    text_file.write(" ")
    text_file.write("-------------------------------")
    text_file.write(" ")
    text_file.write(f"Khan: {khan_pct:.3f}% ({khan_votes})")
    text_file.write(" ")
    text_file.write(f"Correy: {correy_pct:.3f}%  ({correy_votes})")
    text_file.write(" ")
    text_file.write(f"Li:  {li_pct:.3f}%  {li_votes}")
    text_file.write(" ")
    text_file.write(f"O'Tooley: {otooley_pct:.3f}% ({otooley_votes})")
    text_file.write(" ")
    text_file.write("-------------------------------")
    text_file.write(" ")
    text_file.write(f"Winner: {winner}")