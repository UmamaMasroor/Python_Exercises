# Example code..................
# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ]
# if ( a in list ):
#  print ("Line 1 - a is available in the given list")
# else:
#  print ("Line 1 - a is not available in the given list")
# if ( b not in list ):
#  print ("Line 2 - b is not available in the given list")
# else:
#  print ("Line 2 - b is available in the given list")
# c = b/a
# if ( c in list ):
#  print ("Line 3 - a is available in the given list")
# else:
#  print ("Line 3 - a is not available in the given list")


# Question 1......................
# month_number = int(input("Enter month in number: "))
# if 1 <= month_number <= 12:
#     if month_number in [1,3,5,7,8,10,12]:
#         print("Month", month_number ," has 31 days"  )

#     elif month_number in [4,6,9,11]:
#         print ("Month", month_number ," has 30 days"  )
#     else:
#         print("Feburary has 29 days")
# else:
#     print("Ivalid syntax! Please enter correct number (1 to 12) ")       

# Question 2...................... 
# number = int(input("Enter a number: "))
# if (number % 2==0 ):
#     print("You write even number")
# else:
#     print("You write odd number") 

#  Question 4......................     
# fruit = "apple"
# for fruit in ["I like to eat an a day"]:
#     print("Yes it is")

#  Question 5......................  
# user_input = input("Enter a character: ")
# if len(user_input)==1:
#     data = user_input
#     if data.isalpha():
#         print("ALPHABET")
#     elif data.isdigit():
#         print("NUMBER")
#     else:
#         print("Special Character")   
# else:
#     print("Invalid data!")   

#  Question 6......................     
# • If the temperature is below 0, then print the message “It is snowing outside”
# • If the temperature is between 0 and 10, then print the message “It is cold today”
# • If the temperature is between 11 and 20, then print the message “It is pleasant today”
# • If the temperature is between 21 and 35, then print the message “It is hot today”
# • If the temperature is above 35, then print the message “It is difficult to survive the heat
# today”      

# temperature = int(input("Enter temperature in centigrade: "))
# if temperature < 0 :
#     print("It is snowing outside")
# elif temperature <= 10 :
#      print("It is cold today")
# elif temperature <= 20 :
#      print("It is pleasant today")  
# elif temperature <= 35 :
#      print("It is hot today")
# else :
#      print("It is difficult to survive the heat today")             

#  Question 7...................... 
# number1 = float(input("Enter number of your own choice: "))    
# number2 = float(input("Enter number of your own choice: "))
# number3 = float(input("Enter number of your own choice: "))  
# maximum = max(number1,number2,number3)
# print("The maximum number is : ", maximum)

# 2ND METHOD...........
# value = number1

# # Compare the second number with the current maximum value
# if number2 > value:
#     value = number2

# # Compare the third number with the current maximum value
# if number3 > value:
#     value = number3

# # Print the maximum number
# if value == number1:
#     print("Maximum is", number1)
# elif value == number2:
#     print("Maximum is", number2)
# elif value == number3:
#     print("Maximum is", number3)
# else:
#     print("Invalid")
    

#  Question 8 ...................... 
# a = float(input("Enter number of your own choice: "))    
# b = float(input("Enter number of your own choice: "))
# c = float(input("Enter number of your own choice: "))  
# minimum = min(a,b,c)
# print("The minimum number is : ", minimum)


#Question 9..............

# maths = float(input("Enter marks of Maths: "))
# physics = float(input("Enter marks of Physics: "))
# chemistry = float(input("Enter marks of Chemistry: "))

# total = maths + physics + chemistry

# if maths >= 65:
#     if physics >= 55:
#         if chemistry >= 50:
#             if total >= 180:
#                 print("Congrats! You are eligible for the admission")
#             elif maths + max(physics, chemistry) >= 140:
#                 print("Congrats! You are eligible for the admission")
#             else:
#                 print("You are not eligible")
#         else:
#             print("Not eligible! Your marks in chemistry do not satisfy the requirement")
#     else:
#         print("Not eligible! Your marks in Physics do not satisfy the requirement")
# else:
#     print("Not eligible! Your marks in Maths do not satisfy the requirement")
  

# Question 10
user_id= input("Enter you id here: ")
user_name= input("Enter you name: ")
unit_consumed = int(input("Enter units consumed"))

if unit_consumed < 5:
    print("Enter valid input")
else:
    if unit_consumed <= 199:
        charge_per_unit = 10.20    
    elif unit_consumed < 400:
        charge_per_unit = 15.50  
    elif unit_consumed < 600:
        charge_per_unit = 18.80
    else : 
        charge_per_unit = 20.00           

total_amount = unit_consumed * charge_per_unit
if total_amount > 800:
    surcharge = total_amount * 0.15
    total_amount += surcharge
total_amount= max(total_amount, 80)

print ("Customer ID : ", user_id)
print ("Customer name : ", user_name)
print("Unit Consumed : ", unit_consumed)
print ("Total Amount to pay Rs: ", total_amount)
