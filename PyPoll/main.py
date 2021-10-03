"""
ou will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


The total number of votes cast


A complete list of candidates who received votes


The percentage of votes each candidate won


The total number of votes each candidate won


The winner of the election based on popular vote.

"""

# import modules
import os
import csv
# load the file to read election data
inputFile = os.path.join("GitHub Repositories/python-challenge/Resources/election_data.csv")

# output file location for PyPoll analysis
outputFile = os.path.join("GitHub Repositories/python-challenge/Analysis/PyPollAnalysis.txt")

#variables
#variable that holds the total number of votes
totalVotes = 0
# list that holds the Candidates in the Election
candidates =[]
# dictionary that will hold the votes each candidate received
candidateVotes = {}

#VARIABLE TO HOLD WINNING COUNT
winningCount = 0

winningCandidate = ""


# read the csv file
with open(inputFile) as electionData:
    # create the csv reader
    csvreader = csv.reader(electionData)

    # read the header
    header = next(csvreader)

    #move to the first row
    firstRow = next(csvreader)

    #increment the count of the total votes
    totalVotes += 1

    #row will be lists
        # index 0 is the Voter ID
        # index 2 is the Candidate

    #REad each row of data after the header
    for row in csvreader:
        #increment the count of the total votes
        totalVotes += 1

        #check to see if the candidate is in the list of candidates
        if row[2] not in candidates:
            # aif candidate is not in the list, add candidate to the list of candidates
            candidates.append(row[2])

            # add the values to the dictionary as well
            #start the count at one for the votes
            candidateVotes[row[2]] = 1

        else:
            # the candidate is in the list of candidates
            # add a vote to the vote count
            candidateVotes[row[2]] += 1
voteOutput = ""

# print candidate votes
for candidates in candidateVotes:
    # get the vote count and the percentage of the votes
    votes = candidateVotes.get(candidates)
    votePct = float(votes) / float(totalVotes) * 100.00

    voteOutput += f"{candidates}: {votePct:.2f}% ({votes:,})\n"
    
    #compare the votes to the winning count
    if votes > winningCount:
        # update the votes to be the new
        winningCount = votes
        #update the winning candidate
        winningCandidate = candidates

winningCandidateOutput = f"Winner: {winningCandidate}\n"

#start generating the output
#Title the outputfile
output = (
    f"Election Results \n"
    f"------------------------- \n"
    f"Total Votes: {totalVotes:,} \n"
    f"------------------------- \n"
    f"{voteOutput}"
    f"------------------------- \n"
    f"{winningCandidateOutput}"
)


#print the output to the terminal
print(output)

#export the output variable to the output text file
with open(outputFile, "w") as textFile:
    textFile.write(output)



