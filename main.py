import os

#Module for reading the PyBank CSV file
import csv

pybank = os.path.join ("..","Resources","election_data.csv")
print(pybank)

with open(pybank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


print("Election Results")
print("-------------------------------")
print("Total Votes:",)
print("-------------------------------")
print("Khan:")
print("Correy:")
print("Li:")
print("O'Tooley:")
print("-------------------------------")
print("Winner:")
print("-------------------------------")
