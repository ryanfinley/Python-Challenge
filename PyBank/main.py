import os
import csv



#specify the file to read to
csvpath = os.path.join('GitHub Repositories/Python-Challenge/Python-Challenge/Resources/budget_data.csv')

outputFile = os.path.join("GitHub Repositories/Python-Challenge/Python-Challenge/Analysis/PyBankAnalysis.txt")

# set variable for total months
totalMonths = 0
# set variable for total Profits
totalProfits = 0
#initialize the list of monthly changes
monthlyChanges = []
#initialize the list of months
months = []

with open(csvpath, newline = "") as budgetData:

# CSV reader specifies delimiter and variable that holds contents
#create csv reader object
    csvreader = csv.reader(budgetData, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    header = next(csvreader)

    #move to the first row
    firstRow = next(csvreader)

    

    # increment the count of the total months
    totalMonths += 1

    # add on to the total amount of Profits
        #profits is in index 1
    totalProfits += float(firstRow[1])

    #establish the previous profit
        #previous profit is in index 1
    previousProfits = float(firstRow[1])

    # Read each row of data after the header
    for row in csvreader:
        # increment the count of the total months
        totalMonths += 1

        # add on to the total amount of Profits]
            #profits is in index 1
        totalProfits += float(row[1])

        # calculate the net change in profits
        netChange = float(row[1]) - previousProfits

        # add on to the list of monthy changes
        monthlyChanges.append(netChange)

        # add the first month that a change occurred
            #month is in index 0
        months.append(row[0])

        # update the previous profit
        previousProfits = float(row[1])

# calculate the average net change per month
averageNetChange = sum(monthlyChanges) / len(monthlyChanges)

# set variable for greatest increase
greatestIncrease = [months[0], monthlyChanges[0]]
# set variable for the greates decrease
greatestDecrease = [months[0], monthlyChanges[0]]

# use loop to calculte the index of the greatest and least monthly change

for m in range(len(monthlyChanges)):
    #calculate the greatest increase and decrease
    if monthlyChanges[m] > greatestIncrease[1]:
        # if the value is greater than the greatest increase, that value become the new greatst increase
        greatestIncrease[1] = monthlyChanges[m]
        #update the month
        greatestIncrease[0] = months[m]

    if monthlyChanges[m] < greatestDecrease[1]:
        # if the value is less than the greatest increase, that value become the new greatst decrease
        greatestDecrease[1] = monthlyChanges[m]
        #update the month
        greatestDecrease[0] = months[m]

# start generating the output
# Title the output file
output = (
    f"Financial Analysis \n"
    f"------------------------- \n"
    f"Total Months: {totalMonths} \n"
    f"Total Profits/Losses: ${totalProfits:,.2f} \n"
    f"Average Change: ${averageNetChange:,.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f} \n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f} \n"
    )

#print the output to the terminal
print(output)

# export the output variable to the output text file
with open(outputFile, "w") as textFile:
    textFile.write(output)
