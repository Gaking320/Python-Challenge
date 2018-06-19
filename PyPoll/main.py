#'PyPoll.main
#Objective: Create a python script for analyzing and calculating votes.
#Data:  election_data.csv - columns: 'voter ID', 'County','Candidate'

#Total number of votes cast
#complete list of candidates who received  votes
#Percentage of votes each candidate  received
#Total number of votes each candidate received
#winner of the election based on total votes received

import os
import csv
#path to collect data from the PyPoll folder
election_data.csv = os.path.join("../Users/geoff/Documents/Python-Challenge/PyPoll", election_data.csv)

#Read in csv file
with open('election_data.csv',r) as csvfile:
    cvsreader = csv.reader(csvfile, delimiter=",") #---Split the data on commas as iterator
    cvsreader.next() #---Skip header row
    
    #Total number of votes = Total number of rows in csvfile
    row_count = sum(1 for row in csvreader)

    #Complete list of Candidate names who received votes.
    candidates_list = [row[2] for row in cvsreader]

    #Counter total number of votes per candidate, where k is the candidate key, and v are the votes per candidate
    from collections import Counter
    z = candidates_list
    Counter_list = Counter(z)
    for k, v in Counter_list.items():
        winner = max(Counter_list, key=Counter_list.get) #winner of election based on popular vote
        y = v * 100 / row_count #calculate the percentage of votes each candidate won

        print("Election Results")
        print("------------------------")
        print("Total Votes: " + row_count)
        print("--------------------------")
        print(k ":" + y + "%" + "(" + v +")")
        print("-------------------------")
        print("Winner: " + winner)
        print("----------------------------")
        










    #Define function to get unique values = names
    def unique_list(candidates_list):
        output_list[]
        for word in candidates_list:
            if word not in output_list:
                output_list.append(word)
            print(output_list)
            return output_list
    