# 1. While loop that multiplies a number by 10 until the product is less than 100
# product = 0
# while product < 100:
#     number = float(input("Enter a number: "))
#     product = number * 10
#     print(f"Product: {product}")

# 2. While loop that adds two numbers and repeats based on user input
# repeat = 'y'
# while (repeat == 'y'):
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     result = num1 + num2
#     print(result)
#     repeat = input("Enter y to add more: ")    

# 3. For loop that displays all odd numbers between 1 and 100

# for i in range (1,100,2):
#     print(i)

# 4. Loop that prompts user to type a word and adds it to text until text length is 10 characters
# text = input("Enter word: ")
# while len(text) < 10:
#     word = input("Type a word: ")
#     text += word
#     print(f"Current text: {text}")
  
# 5. Loop that calculates the total of a specific series of numbers (2, 29, 3, 28, 30, 1, 1, 30, 1, 1, 1...)
# series = [2, 29, 3, 28, 30, 1, 1, 30, 1, 1, 1]
# total = 0
# for number in series:
#     total += number
# print(f"Total: {total}")

# 7. Nested loops that display the first ten values of multiplication tables from 1 to 10

# for i in range(1,11 ):
#     print(sep=" ")
#     for j in range(1,11):
#      print(i, "x",i ,"=",i*j)

# 8. Prompt user to enter a positive nonzero number and validate the input
# number = float(input("Enter a positive nonzero number: "))
# while number <= 0:
#     print("Invalid input. Please enter a positive nonzero number.")
#     number = float(input("Enter a positive nonzero number: "))
# print(f"You entered: {number}")

# 9. Prompt user to enter a number in the range of 1 through 100 and validate the input
number = int(input("Enter a number between 1 and 100: "))
while number < 1 or number > 100:
    print("Invalid input. Please enter a number between 1 and 100.")
    number = int(input("Enter a number between 1 and 100: "))
print(f"You entered: {number}")

