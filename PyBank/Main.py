import os
import csv

csvpath = "/Users/jaybaybay/Downloads/Solved 17/Resources/budget_data.csv"

Total_Months = []
Total = []
Average_Change = []
Greatest_Increase = []
Greatest_Decrease = []

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        jay



