#Calculate how many weeks left if you can reach to 90 years old

age = input("What is your current age? ")

nbOfYearsRemaining = 90 - int(age)
nbOfDays = nbOfYearsRemaining * 365
nbOfWeeks = nbOfYearsRemaining * 52
nbOfMonths = nbOfYearsRemaining * 12


#F-string function
message = (f"You have {nbOfDays} days, {nbOfWeeks} weeks, and {nbOfMonths} months left until 90")
print(message)