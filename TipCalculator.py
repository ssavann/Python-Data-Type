#Tip Calculator
print("Welcome to the Tip Calculator")

theBill = float(input("What was the total bill? "))

theTip = int(input("What % tip would you like to give? 10, 12, 15 or 20? "))

splitPeople = int(input("How many people to split the bill? "))

tipConvertion = (theTip / 100) + 1

#will calculate the "bill" * "tip" and divide by the number of people 
billToSplit = (theBill * tipConvertion) / (splitPeople) 

roundBill = round(billToSplit, 2)          #to get only two decimals and to round it
roundBill = "{:.2f}".format(roundBill)     #to get 2 digits after coma $33.60 instead of $33.6

print(f"Each person should pay: ${roundBill}")

