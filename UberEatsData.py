import csv
import datetime
import os

# Gets the path of the CSV file realtive to the current directory
csv_path = os.path.join(os.getcwd(), "uber_easts_order.csv")

# Sets up the csv file where all my information is going to be stored
fields = ["Date", "Time", "Miles Driven", "Money Earned"]
with open(csv_path, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    
while True:   
    # Get input from the user for the current order
    today = datetime.datetime.now().strftime("%m/%d/%Y")
    time = input("Enter the time this order was completed (e.g. 3:30 pm): ")
    miles = float(input("Enter the miles driven for this order: "))
    money = float(input("Enter the money earned for this order: "))

    # Write the data to the CSV file
    with open(csv_path, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([today, time, miles, money])

    print("Your order was added to the file")   
    
    # Asks the User if they want to input another order to the CSV file
    answer = input("Do you want to add another order? (y/n): ") 
    if answer.lower() != "y":
        break
    