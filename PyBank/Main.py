import csv

# Path to connect data
csvpath = "/Users/jaybaybay/python-challenge/budget_data.csv"

# define functions for data
def getnumbers(budget_data):

    # total months is the numerical counts on months in time period
    totalmonths = len(budget_data[0])
    
    # total P/L found as sum of stated Profit/Loss
    totalPL = sum(budget_data[1])

    # average change is the rolling average on month over month changes
    averagechange = ((startingvalue-endingvalue)/totalmonths)

    # greatest increase found as largest one month gain
    greatestincrease = 

    # greatest decrease found as largest one month loss
    greatestdecrease = 

    Print("Financial Analysis")
    Print("----------------------------------")
    print(f"Total Months: {str(totalmonths)}")
    print(f"Total Profit/Loss: {str(totalPL)}")
    print(f"Average Change: {str(averagechange)}")
    print(f"Greatest Increase in Profits: {str(greatestincrease)}")
    print(f"Greatest Decrease in Profits: {str(greatestdecrease)}")


# read in CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader
        print(getnumbers)

