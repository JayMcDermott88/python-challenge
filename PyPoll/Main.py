import csv

# Path to connect data
csvpath = "/Users/jaybaybay/python-challenge/PyPoll/election_data.csv"

# read in CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader
        print(row)
