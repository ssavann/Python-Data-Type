#About Type Error, Type Checking and Type Conversion


"""
#Type Error

num_char = len(input("What is your name?"))

print("Your name has " + num_char + " characters.")	
#will make Type Error, because we can't concatenate string and integer
"""

'''
#we need to convert the "integer" into a string
num_char = len(input("What is your name?"))

new_num_char = str(num_char)    #will convert an "integer" into a string

print("Your name has " + new_num_char + " characters.")	

'''


a = str(123)
print(type(a))      #will output a "string" class


a = float(123)
print(type(a))      #will output a "float" class

print(70 + float("100.5"))  #will convert "float("100.5")" into a floating number and do the sum


print(str(70) + str(100))   #will equat to: 70100, because it's two strings and not numbers


