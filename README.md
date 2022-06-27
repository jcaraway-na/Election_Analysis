# Election Analysis

> The election commission has requested some additional data to complete the audit:
>
> 1. The voter turnout for each county
> 2. The percentage of votes from each county out of the total count
> 3. The county with the highest turnout

The analysis below will provide insight into the following:
- How many votes were cast in this congressional election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county
- Which county had the largest number of votes.
- Provide a breakdown of the number of votes and percentage of the total votes each candidate received.
- Which candidate won the election, what was their vote count, and what was their percentage of the toal votes.

### OBJECTIVE

- DELIVERABLE 1: The election results printed to the command line.
- DELIVERABLE 2: The election results saved to a text file.
- DELIVERABLE 3: A written analysis of the election audit.

---
---
---
## DELIVERABLE 1: Election results printed to terminal

### Election Results Printed to Terminal (command line)

#### Solution 1.0:
![This is an image](https://github.com/jcaraway-na/Election_Analysis/blob/main/resources/election_analysis_terminal.png)

#### Solution Definition 1.0:

> The terminal image above was generated using repetition statements, conditional statements with logical operators, and print statements.

## DELIVERABLE 2: Election results saved to a text file

#### Solution 2.0:
![This is an image](https://github.com/jcaraway-na/Election_Analysis/blob/main/resources/election_analysis_text.png)

#### Solution Definition 2.0:

> The image above is an example of what the election_analysis.txt file looks like.

## DELIVERABLE 3: written analysis of the election audit.

**Congressional Election Total Votes: _369,711_**

#### Voting Analysis Definition

🎉 = Winner

**Voting Breakdown per County**

- [ ]  **Jefferson County**

       - 38,855 votes
       - 10.5% of total votes
- [x]  **Denver County** :tada:
       
       - 306,055 votes
       - 82.8% of total votes
       
- [ ]  **Arapahoe County**
       
       - 24,801 votes
       - 6.7% of total votes

**Voting Breakdown per Candidate**

- [ ]  **Charles Casper Stockham**

       - 85,213 votes
       - 23.0% of total votes
- [x]  **Diana DeGette** :tada:
       
       - 272,892 votes
       - 73.8% of total votes
- [ ]  **Raymon Anthony Doane**
       
       - 11,606 votes
       - 3.1% of total votes

## In Summary:

> The election audit script can quickly run through millions of votes in a very short amount of time. With a total of 163 lines of code, it can be manipulated to        itterate through any CSV files it is given. The CSV must be in the standard voter format before running the code. 
>
> The "file_to_load" location can be easily changed in the code behind the script as shown below. simply copy and paste where your voter data csv file is located and then run the script. 

![This is an image](https://github.com/jcaraway-na/Election_Analysis/blob/main/resources/file_read_from.png)

> Your file output path can also be adjusted as well, just simply follow the same steps as above. navigate to the folder you would like the text file to output to. Then copy and paste the url into the script labeled "file_to_save".

![This is an image](https://github.com/jcaraway-na/Election_Analysis/blob/main/resources/file_write_to.png)
