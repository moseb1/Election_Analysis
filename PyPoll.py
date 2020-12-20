# Add  dependencies.
import csv
import os
# Assign a variable to load a file from.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to .
file_to_save = os.path.join("analysis", "election_analysis.txt")

#set the counter to accumate the total votes
total_votes = 0

#declare candidate empty string/counta
candidate_options = []
# 1. Open with, with statement

#candates vote count declared
candidate_votes = {}

#Winning candidate and winning tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#with opnen statement
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # print the headers
    headers = next(file_reader)
   
   #print all the rows
    for row in file_reader:
        #add the total value from the loop above 
        total_votes += 1

       #add candate names to row
        candidate_name = row[2]
        #remove candate name doublicates
        if candidate_name not in candidate_options:

       #append to the candidate_option
            candidate_options.append(candidate_name)

            #let's begin to count the cadidates votes
            candidate_votes[candidate_name] = 0

        #Let's track the candidate vote count
        candidate_votes[candidate_name] += 1
    
    #Lets determind the percentage of the candate votes
    #1. iterate thru the candate list
    for candidate_name in candidate_votes:
        
        #the votes tally of the candidates
        votes = candidate_votes[candidate_name]

        #votes received in percentages
        vote_percentage = float(votes) / float(total_votes) * 100
    
    #who won the election?
    #determin if the votes are > the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            #let's reveal the winning candidate's names
            winning_candidate = candidate_name

       #To do: Fianlly, lets reveal the winning candiate, vote count, and percentage to terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print candate votes in percentage
    #print(f"{candidate_name}: receoved {Vote_percentage:.2f}% of the votes.")

    winning_candidate_summary = (
        f"-----------------------------/\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)
    
 # print the total votes
#print(total_votes)

#print (candidate_name)
#print(candidate_options)
#print(candidate_votes)

## Election results
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote