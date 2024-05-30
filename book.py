#  # Create a variable to control the loop.
# keep_going = 'y'

#  # Calculate a series of commissions.
# while keep_going == 'y':
#  # Get a salesperson's sales and commission rate.
#  sales = float(input('Enter the amount of sales: '))
#  comm_rate = float(input('Enter the commission rate: '))

#  # Calculate the commission.
#  commission = sales * comm_rate

#  # Display the commission.
#  print(f'The commission is ${commission:,.2f}.')

#  # See if the user wants to do another one.
#  keep_going = input('Do you want to calculate another ' +
#  'commission (Enter y for yes): ')


# A project currently underway at Chemical Labs, Inc. requires that a substance be continually heated in a vat. A technician must check the substance’s temperature every 15 minutes.
# If the substance’s temperature does not exceed 102.5 degrees Celsius, then the technician
# does nothing. However, if the temperature is greater than 102.5 degrees Celsius, the technician must turn down the vat’s thermostat, wait 5 minutes, and check the temperature again.
# The technician repeats these steps until the temperature does not exceed 102.5 degrees
# Celsius. The director of engineering has asked you to write a program that guides the technician through this process.
# MAX_TEMP = 102.5
# temperature = float(input("Enter the substance's Celsius temperature: "))
# while temperature > MAX_TEMP:
#   print('The temperature is too high.')
#   print('Turn the thermostat down and wait')
#   print('5 minutes. Then take the temperature')
#   print('again and enter it.')
#   temperature = float(input('Enter the new Celsius temperature: '))
# # Remind the user to check the temperature again
# # in 15 minutes.
# print('The temperature is acceptable.')
# print('Check it again in 15 minutes.')


# Print the table headings.
# print('Number\tSquare')
# print('--------------')

# for number in range(1, 11):
#  square = number**2
# #  print(f'{number}\t{square}')
#  print(number , '\t', square)

# print("KPH \t MPH")
# print("----------------")
# for i in range(60,131,10):
#  MPH = i * 0.6214
#  print(i , "\t", MPH)


# Get the starting value.
# print('This program displays a list of numbers')
# print('and their squares.')
# start = int(input('Enter the starting number: '))

# # Get the ending limit.
# end = int(input('How high should I go? '))

# # Print the table headings.
# print()
# print('Number\tSquare')
# print('--------------')

# # Print the numbers and their squares.
# for number in range(start, end + 1):
#  square = number**2
#  print(f'{number}\t{square}')


# # This program calculates the sum of a series
# # of numbers entered by the user.
# MAX = 5 # The maximum number
# # Initialize an accumulator variable.
# total = 0.0
# # Explain what we are doing.
# print('This program calculates the sum of ', end='')
# print(f'{MAX} numbers you will enter.')
# # Get the numbers and accumulate them.
# for counter in range(MAX):
#  number = int(input('Enter a number: '))
#  total = total + number
# # Display the total of the numbers.
# print(f'The total is {total}.')


# The county tax office calculates the annual taxes on property using the following formula:
# property tax 5 property value 3 0.0065
# Every day, a clerk in the tax office gets a list of properties and has to calculate the tax for
# each property on the list. You have been asked to design a program that the clerk can use to
# perform these calculations.
# In your interview with the tax clerk, you learn that each property is assigned a lot number,
# and all lot numbers are 1 or greater. You decide to write a loop that uses the number 0 as
# a sentinel value. During each loop iteration, the program will ask the clerk to enter either
# a property’s lot number, or 0 to end
# TAX_FACTOR = 0.0065 # Represents the tax factor.

# # Get the first lot number.
# print('Enter the property lot number or enter 0 to end.')
# lot = int(input('Lot number: '))
# # Continue processing as long as the user
# # does not enter lot number 0.
# while lot != 0:
# # Get the property value.
#  value = float(input('Enter the property value: '))
# # Calculate the property's tax.
#  tax = value * TAX_FACTOR

# # Display the tax.
#  print(f'Property tax: ${tax:,.2f}')
# # Get the next lot number.
#  print('Enter the next lot number or enter 0 to end.')
#  lot = int(input('Lot number: '))


# # This program calculates retail prices.
# MARK_UP = 2.5  # The markup percentage
# another = 'y'  # Variable to control the loop.

# # Process one or more items.
# while another.lower() == 'y':
#     # Get the item's wholesale cost.
#     wholesale = float(input("Enter the item's wholesale cost: "))
    
#     # Validate the wholesale cost.
#     while wholesale < 0:
#         print('ERROR: the cost cannot be negative.')
#         wholesale = float(input('Enter the correct wholesale cost: '))
    
#     # Calculate the retail price.
#     retail = wholesale * MARK_UP
    
#     # Display the retail price.
#     print(f'Retail price: ${retail:,.2f}')
    
#     # Do this again?
#     another = input('Do you have another item? (Enter y for yes): ')

 
# This program averages test scores. It asks the user for the
# number of students and the number of test scores per student.

# students = int(input("Enter number of students : "))
# tests = int(input("Enter number of each student test(s): "))

# for student in range (students):
#     total = 0.0
#     print(f'Student number {student + 1}')
#     print('-----------------')
#     for test in range(tests):
#         print(f' test {test + 1}')
#         score = float(input('Score : '))
#         total += score
#     average = total / tests
#     print(f'The average for student number {student + 1} is: {average:.1f}')
    # print()

