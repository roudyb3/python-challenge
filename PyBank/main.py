#module for creating file paths across operating systems
import os

#module for reading CSV files
import csv
pybank_csv = os.path.join ("Resources","budget_data.csv")
print(pybank_csv)

# create a list to add the data in from the csv file 
total_months = []
months = []
monthly_change = []
total_profit = []


#initialize month and profit at 0 before appending data
total_months = 0


#create a function to append column data to the list
def pybank(columns):
    date = str(columns[0])
    months.append(date) 
    
    profit_loss = int(columns[1])
    total_profit.append(profit_loss)

#read the csv file
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print (csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #use a for loop functions to loop through the file and extract data
    for row in csvreader:
        #print(row)
        #calculate the total number of months
        total_months += 1
        pybank(row)

#determine number of rows in the profit_loss list to find the monthly_change
row_numbers = len(total_profit)

#figure out the difference in pl for the months using a for loop
for i in range(1, row_numbers):
    monthly_change.append(total_profit[i]-total_profit[i-1])

#calculate everything
total = sum(total_profit)
average_change = sum(monthly_change)/len(monthly_change)
greatest_increase_pl = max(monthly_change)
greatest_decrease_pl = min(monthly_change)
greatest_increase_date = months[monthly_change.index(greatest_increase_pl)+1]
greatest_decrease_date = months[monthly_change.index(greatest_decrease_pl)+1]

#print statements
print("Financial Analysis")
print("-------------------------------")
print("Total Months: ",(total_months))
print("Total: $",(total))
print("Average Change: $",(average_change))
print("Greatest Increase in Profits:",(greatest_increase_date), ('$'),(greatest_increase_pl))
print("Greatest Decrease in Profits:",(greatest_decrease_date), ('$'),(greatest_decrease_pl))

#write in the results to a text file
output_file = os.path.join('Analysis','output.txt')
with open (output_file, 'w') as text_file:
    text_file.write("Financial Analysis")
    text_file.write(" ")
    text_file.write("-------------------------------")
    text_file.write(" ")
    text_file.write(f'Total Months: {total_months}')
    text_file.write(" ")
    text_file.write(f'Total: ${total}')
    text_file.write(" ")
    text_file.write(f'Average Change: ${average_change}')
    text_file.write(" ")
    text_file.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_pl})')
    text_file.write(" ")
    text_file.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_pl})')