import csv

csvpath = "/Users/jaybaybay/Downloads/Solved 17/Resources/budget_data.csv"

def getnumbers(records)

totalmonths = len(int(row[0]))
totalPL = sum(int(row[1]))
averagechange = 
greatestincrease = 
greatestdecrease = 

Print("Financial Analysis")
Print("----------------------------------")
print(f"Total Months: {str(totalmonths)}")
print(f"Total: {str(totalPL)}")
print(f"Average Change: {str(averagechange)}")
print(f"Greatest Increase in Profits: {str(greatestincrease)}")
print(f"Greatest Decrease in Profits: {str(greatestdecrease)}")

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
