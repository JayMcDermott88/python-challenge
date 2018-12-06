import csv

# Path to connect data
csvpath = "/Users/jaybaybay/python-challenge/PyPoll/election_data.csv"

totalvotes=0

# read in CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    candidates = ["Khan",  
                "Correy", 
                "Li", 
                "O'Tooley"]

    for row in csvreader:

        #The total number of votes cast
        totalvotes = totalvotes+1

        #A complete list of candidates who received votes
        

        #The percentage of votes each candidate won
        if row[2] == "Khan" 
            totalkhan = totalkhan+1
            totalkhan_percent = (totalkhan/totalvotes) * 100

        if row[2} == "Correy"
            totalcorrey = totalcorrey+1
            totalcorrey_percent = (totalcorrey/totalvotes) * 100

        if  row[2} == "Li"
            totalli = totalli+1
            totalli_percent = (totalli/totalvotes) * 100
        #The total number of votes each candidate won
         if row[2} == "O'Tooley"
            totalotooley = totalotooley+1
            totalotooley_percent = (totalcorrey/totalvotes) * 100

        #The winner of the election based on popular vote.
        winner = 

print("Election Results")
print("----------------------------------")
print("Total Votes: " (str(totalvotes)
print("----------------------------------")
print(f"Khan: " (str(totalkhan) , str(totalkhan_percent))
print(f"Correy: " (str(totalcorrey , str(totalcorrey_percent))
print(f"Li: " (str(totalli) , str(totalli_percent))
print(f"(O'Tooley: " (str(totalotooley) , str(totalotooley_percent))
print("----------------------------------"
print("Winner: " winner)
