#Shayan Beizaee
# Financial Analysis
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Total number of the months included in the datat set

    totalMonths = 0
    profitloss = []
    months = []
    for row in csvreader:
        totalMonths +=1
        profitloss.append(int(row[1]))
        months.append(row[0])

    change = []
    for i in range(totalMonths - 1):
        change.append(profitloss[i+1] - profitloss[i])
    
    greatincrease = max(change)
    greatdecrease = min(change)

    for i in range(totalMonths - 1):
        if profitloss[i+1] - profitloss[i] == greatincrease:
            monthmax = months[i+1]
        if profitloss[i+1] - profitloss[i] == greatdecrease:
            monthmin = months[i+1]



    


    average = round(sum(change) / len(change), 2)

    


    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${sum(profitloss)}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {monthmax} (${greatincrease})")
    print(f"Greatest Decrease in Profits: {monthmin} (${greatdecrease})")

output_path = os.path.join("..", "PyBank", "PyBank.txt")
with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("--------------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Months: {totalMonths}")
    txtfile.write("\n")
    txtfile.write(f"Total: ${sum(profitloss)}")
    txtfile.write("\n")
    txtfile.write(f"Average Change: ${average}")
    txtfile.write("\n")
    txtfile.write(f"Greatest Increase in Profits: {monthmax} (${greatincrease})")
    txtfile.write("\n")
    txtfile.write(f"Greatest Decrease in Profits: {monthmin} (${greatdecrease})")



