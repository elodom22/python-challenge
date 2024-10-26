# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources","budget_data.csv")  # Input file path


# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
change_value =0
change = 0
profitlosses=[]
dates=[]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    #Date & Net total
    first_row = next(reader)
    total_months+=1
    total_net+=int(first_row[1])
    change_value = int(first_row[1])

    for row in reader:

        #count the dates
        dates.append(row[0])
   
    #Track the total and net change 
        change= int(row[1])-change_value
        profitlosses.append(change)
        change_value=int(row[1])

    # Track the total
        total_months+= 1

    # Track the net change in profit/losses
        total_net = total_net + int(row[1])
        
    # Calculate the average net change across the months
        avg_change = round(sum(profitlosses)/len(profitlosses),2)
        #print(avg_change)      

        # Calculate the greatest increase in profits (month and amount)
        # Calculate the greatest decrease in losses (month and amount)
        greatest_increase = max(profitlosses)
        increase = profitlosses.index(greatest_increase)
        date_increase = dates[increase]
                #set function to find in list, call function
        greatest_decrease = min(profitlosses)
        decrease = profitlosses.index(greatest_decrease)
        date_decrease = dates[decrease]

# Generate the output summary
        print("Financial Analysis")
        print("--------------------------------")
        print(f"Total Months: {str(total_months)}")
        print(f"Total: ${str((total_net))}")
        print(f"Average Change: ${str((avg_change))}")
        print(f"Greatest Increase in Profits: {date_increase} (${str(greatest_increase)})")
        print(f"Greatest Decrease in Profits: {date_decrease} (${str(greatest_decrease)})")
                     

# Print the output
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Write the results to a text file
txt_file = open(file_to_output, "w")
   
txt_file.write("Financial Analysis\n")
txt_file.write("--------------------------------\n")
txt_file.write(f"Total Months: {total_months}\n")
txt_file.write(f"Total: ${total_net}\n")
txt_file.write(f"Average Change: ${avg_change}\n")
txt_file.write(f"Greatest Increase in Profits: {date_increase} (${str(greatest_increase)})\n")
txt_file.write(f"Greatest Decrease in Profits: {date_decrease} (${str(greatest_decrease)})\n")
txt_file.write("--------------------------------\n")

txt_file.close