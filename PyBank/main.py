#'PyBank.main.PyBank
#Objective: Create a python script for analyzing the financial records of the company
#Data: budget_data.csv - columns: 'date' and 'profit/losses'

#Greatest increase in profits(date and amount over entire period
#Greatest decrease in losses (date and amount) over entire period
#Print output to terminal and export a text file
import os
import csv
# Path to collect data from the PyBank folder
budget_data.csv = os.path.join("../Users/geoff/Documents/Python-Challenge/PyBank", "budget_data.csv")


with open ('budget_data.csv',r) as csvfile: #---Read in csv file
    cvsreader = csv.reader(csvfile, delimiter=",") #---Split the data on commas as iterator
    csvreader.next() #Skip header row
    revenue = []
    date = []
    rev_change = []

    #Total months in dataset = total number of rows in the csvfile, print total
    row_count = sum(1 for row in csvreader)
         
    #Total net amount of profit/losses over period, print  sum total
    total = 0
    for row in csvreader:  
        total += float(row[2])
        
    #Average change in Profit/losses between months over the entire period
    #Difference between all row of column "Revenue" and found total revnue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change) #Max revenue change

        min_rev_change = min(rev_change) #Min revenue change

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])
    
    print("Financial Analysis")
    print("-----------------------------------")
    print( "Total Months: " + row_count)
    print("Total: $"+total)
    print("Avereage Change: $", round(avg_rev_change))
    print("Greatest Increase in profits:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in profits:", min_rev_change_date,"($", min_rev_change,")")
