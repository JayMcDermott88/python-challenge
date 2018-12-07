import csv

# Path to connect data
csvpath = "/Users/jaybaybay/python-challenge/PyBank/budget_data.csv"

totalmonths=0
totalPL=0

# read in CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)



    for row in csvreader:

        #firstrow= next(header)
        #current_row = 
        #previous row = 

# define functions for data
#total months is the numerical counts on months in time period       
        totalmonths = totalmonths+1

# total P/L found as sum of stated Profit/Loss
        totalPL += int(row[1])

    # average change is the rolling average on month over month changes
        averagechange = float(totalmonths/totalPL)

    # greatest increase found as largest one month gain
        greatestincrease = 20

    # greatest decrease found as largest one month loss
        greatestdecrease = 30

print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(totalmonths))
print("Total P/L: " + str(totalPL))   
print("Average Change: " + str(averagechange))
print("Greatest Increase in Profits: " + str(greatestincrease))
print("Greatest Decrease in Profits: " + str(greatestdecrease))

