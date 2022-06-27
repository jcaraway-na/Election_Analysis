from ast import operator
import csv
import imp
from optparse import Values
import os

file_to_load = os.path.join("C:/Users/Jennings/Desktop/Analysis Projects/Election_Analysis/Python_Challenge/resources/election_results.csv")
print(file_to_load)
file_to_save = os.path.join("C:/Users/Jennings/Desktop/Analysis Projects/Election_Analysis/Python_Challenge/resources/election_analysis.text")

county_options = []
county_votes = {}

largest_county = ""
county_voter_turnout = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        county_name = row[1]

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

print(county_options)
print(county_votes)
print(">.....................................")


with open(file_to_save,"w") as txt_file:

    
    winning_county_votes = 0
    winning_county = max(county_votes,key=county_votes.get)

    print(county_votes[winning_county])

    print(">.....................................")

    total_county_votes = sum(county_votes.values())
    print(total_county_votes)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:
        # 6b: Retrieve the county vote count. 
        votes = county_votes.get(county)
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = (float(votes)/float(total_county_votes))*100
        # 6d: Print the county results to the terminal.
        county_results =(
        f"-------------------------\n"
        f"Winner: {county}\n"
        f"Winning Vote Count: {votes:,}\n"
        f"Winning Percentage: {vote_percentage:.1f}%\n"
        f"-------------------------\n")
        # Save the winning candidate's name to the text file
        print(county_results,end="")
        txt_file.write(county_results)

    print(">.....................................")


