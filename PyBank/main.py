import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Variables to hold dates, net total, greatest, smallest, and change variables 
months_years = []
running_total = 0
initial_value = 0
change = 0 
greatest = 0 
smallest = 0
average_change = []

# Read in the CSV file
with open(budget_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header and save it for later (if needed, but it's really not...) 
    header = next(csvreader)

    # Loop through the data by row 
    for row in csvreader:
        
        # Add Profit/Losses of that row to the running total (net total)
        running_total += int(row[1])

        if months_years == [] : # On the first row, we won't have a difference. See if any dates have been placed in the list. 
            initial_value = float(row[1])
        else: 
             # Add Profit/Losses into string that will be averaged later 
            change = float(row[1]) - initial_value 
            average_change.append(change)

            # Check for notable change amount. Assign as applicable 
            if change > greatest: 
                greatest = round(change) # Rounding here did not change the final result
                greatest_date = row[0]
            elif change < smallest: 
                smallest = round(change) # Rounding here did not change the final result
                smallest_date = row[0]

            # Reset initial value to current Profit/Losses and clear out change variable
            initial_value = float(row[1])
            change = 0 

        # Add to our makeshift counter for the months/years 
        if row[0] in months_years: 
            pass 
        else: 
            months_years.append(row[0])

    # Calculate the average change 
    avg = round(sum(average_change)/len(average_change),2)

    # Print summary to terminal
    print(f"""Financial Analysis
    ----------------------------
    Total Months: {len(months_years)}
    Total: ${running_total}
    Average Change: ${avg}
    Greatest Increase in Profits: {greatest_date} (${greatest})
    Greatest Decrease in Profits: {smallest_date} (${smallest})""")

# Print the results to the txt file
analysis = os.path.join('Analysis', 'analysis.txt')
with open(analysis, "w") as output: 
    output.write(f"""Financial Analysis
    ----------------------------
    Total Months: {len(months_years)}
    Total: ${running_total}
    Average Change: ${avg}
    Greatest Increase in Profits: {greatest_date} (${greatest})
    Greatest Decrease in Profits: {smallest_date} (${smallest})""")