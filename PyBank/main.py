import os
import csv

budget_csv = os.path.join("..","Resources","budget_data.csv")

#variables/lists to collect data we need to find to meet HW objectives
Total_Months = 0
Total = 0
Month_change = []
Profit_Loss = []
PL_change = []

#tally total months of info and sum all P/L #'s - collect Months and PL #'s into list to manipulate find change data
with open(budget_csv) as bank_data:
    reader = csv.reader(bank_data)
    
    #skip header
    next(reader)
    #first line of data
    first_line = next(reader)
    #tally first month and sum first row of PL data
    Total_Months += 1
    Total += int(first_line[1])
    #add PL data to new list to be used to find change data between months
    Profit_Loss += [first_line[1]]

    for row in reader:
        #tally the rest of the months
        Total_Months += 1
        #sum remaining rows of PL data
        Total += int(row[1])
        #add Month elements into new list sans the first month as we need to format a new series containing Months and PL delta - doesn't include first month, starts on second month Feb '10
        Month_change += [row[0]]
        #continue adding PL data to new list for finding change data
        Profit_Loss += [row[1]]

#for loop to calculate the difference between months PL - added to new list 'PL_change'
for i in range(1, len(Profit_Loss)):
    PL_change += [(int(Profit_Loss[i]) - int(Profit_Loss[i-1]))]

#function for finding the Avg Change
def Change_Avg(PL_change):
    return round(sum(PL_change) / len(PL_change),2)

Average_Change = Change_Avg(PL_change)

#reference PL_change to find Greatest Increase/Decrease - reference second list element using lambda and max/min functions
Combined_Months_Change = zip(Month_change,PL_change)
Greatest_Increase = max(Combined_Months_Change, key = lambda i : i[1])

Combined_Months_Change = zip(Month_change,PL_change)
Greatest_Decrease = min(Combined_Months_Change, key = lambda i : i[1])

print("Financial Analysis")
print("-------------------------")
print("Total Months:" + str(Total_Months))
print("Total: $"+ str(Total))
print("Average Change: $"+str(Average_Change))
print("Greatest Increase in Profits: " + Greatest_Increase[0] + " ($"+str(Greatest_Increase[1])+")")
print("Greatest Decrease in Profits: " + Greatest_Decrease[0] + " ($"+str(Greatest_Decrease[1])+")")

output_path = os.path.join('..',"Analysis","PyBank.txt")

with open(output_path, 'a') as txtfile:

    print("Financial Analysis", file=txtfile) 
    print("-------------------------", file=txtfile)
    print("Total Months:" + str(Total_Months), file=txtfile)
    print("Total: $"+ str(Total), file=txtfile)
    print("Average Change: $"+str(Average_Change), file=txtfile)
    print("Greatest Increase in Profits: " + Greatest_Increase[0] + " ($"+str(Greatest_Increase[1])+")", file=txtfile)
    print("Greatest Decrease in Profits: " + Greatest_Decrease[0] + " ($"+str(Greatest_Decrease[1])+")", file=txtfile)

