import csv
import os

file_to_load = "budget_data.csv"
file_to_output = "financial_analysis.txt"

months = 0
amount = 0
previous = 0
month_change = []
profit_change_list = []
max_increase = 0 
max_decrease = 0

with open(file_to_load) as profit_data:
    reader = csv.DictReader(profit_data)

    for row in reader:

        months = months + 1 
        amount = amount + int(row["Profit/Losses"])


        if months > 1:
            change = int(row["Profit/Losses"])-previous
            month_change.append(change)

            if change > max_increase:
                max_increase = change
                max_increase_month = row["Date"]

            if change < max_decrease:
                max_decrease = change
                max_decrease_month = row["Date"]

        previous = int(row["Profit/Losses"])

average = round(sum(month_change)/(len(month_change)+ 0.0),2)

output = ('Financial Analysis'+ '\n'+
          '.........................'+ '\n'  +
          'Total Months: ' + str(months) + '\n' +
          'Total: ' + ' $'+ str(amount) + '\n' +
          'Average Change:' + ' $' + str(average) + '\n' +
          'The Greatest Increase in Profits: ' + max_increase_month + ' $' + str(max_increase) + '\n' +
          'The Greatest Decrease in Profits: ' + max_decrease_month + ' $' + str(max_decrease) + '\n')

      

print(output)

with open(file_to_output, 'w') as outputfile:
    outputfile.write(output)