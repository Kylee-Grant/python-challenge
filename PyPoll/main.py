import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# Variables to hold candidate names, votes, and total votes 
vote_ticker = 0
candidates_dict = {} # Where we will store names and votes; candidate names are keys 

# Read in the CSV file
with open(election_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header and save it for later (if needed, but it's really not...) 
    header = next(csvreader)

    # Loop through the data by row 
    for row in csvreader:
        
        # Total number of votes cast goes up each iteration. 
        vote_ticker += 1 

        # If the name is in the dict, add to the candidate's vote total. 
        if row[2] in candidates_dict:
            candidates_dict[row[2]] += 1
        # If the name is not in dict, add them as a new key. 
        else: 
            candidates_dict.update({row[2]: 1}) # Vote starts at 1 due to triggering event

    # Return the key with the max value, referenced: http://bit.ly/2LdcvcP
    winner = max(candidates_dict, key=candidates_dict.get)

# Print the results to the terminal 
print(f"""Election Results
-------------------------
Total Votes: {vote_ticker}
-------------------------""")
# Enter a for loop to iterate through all the candidates in the dict
for names in candidates_dict: 
    percent = "{:.3%}".format(candidates_dict[names]/vote_ticker) # Calculate and format: http://bit.ly/38avLkq
    print(f"{names}: {percent}% ({candidates_dict[names]})")
print(f"""-------------------------
Winner: {winner}
-------------------------""")

# Print the results to the txt file. \r to left-align. Indentation issue. 
analysis = os.path.join('Analysis', 'analysis.txt')
with open(analysis, "w") as output: 
    output.write(f"""Election Results
    \r-------------------------
    \rTotal Votes: {vote_ticker}
    \r-------------------------\n""")
    # Enter a for loop to iterate through all the candidates in the dict
    for names in candidates_dict: 
        percent = "{:.3%}".format(candidates_dict[names]/vote_ticker) # Calculate and format: http://bit.ly/38avLkq
        output.write(f"\n{names}: {percent}% ({candidates_dict[names]})")
    output.write(f"""\n\r-------------------------
    \rWinner: {winner}
    \r-------------------------""")