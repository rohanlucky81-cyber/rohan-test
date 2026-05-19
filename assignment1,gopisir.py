#1Store vaiables
# name="rohan"
# age="24" 
# city="hyderabad"
# print("NAME:", name)
# print("AGE:", age)
# print("CITY:", city)

#2Create a tuple with 5 fruits and print the third fruit.
# fruits=("banana","apple","watermelon","kiwi","promagranate")
# print(fruits[2])

#3Store marks of 3 subjects in a dictionary and print the marks of "Math"
# marks={"math":99,"physics":98,"chemistry":100}
# print("MATH marks:", marks["math"])

#4Write a program to store 3 integers and print their sum
# gopisir = 100
# jaswanth = 90
# praneeth = 95
# total = ( gopisir + jaswanth + praneeth)
# print("SUM:", total)

#5Create a tuple of 4 colors and print the last color.
# colors=("white","blue","brown","green")
# print(colors[-1])

#6Store employee details (name, ID, department) in a dictionary and print the department.
# employee={"NAME":"rohan","ID":"1234","DEPARTMENT":"TTT"}
# print(employee["DEPARTMENT"])

#7Write a program to store a float, int, and string in variables and print their types
# float_var=14.3
# int_var=10
# string_var="rohanlucky"
# print("FLOAT:", float_var)
# print(type(float_var))
# print("INT:", int_var)
# print(type(int_var))
# print("STRING:", string_var)
# print(type(string_var))

#8################B. Strings (8–14)######################
#Check if "Python" is present in "I am learning Python programming"
# r="iam learning python programming"
# print("python"in r)

#9Print only the first 5 characters of "Hello World"
# s="hello world"
# print(s[:5])

#10Concatenate two strings "Good" and "Morning"
# str1="good"
# str2="morning"
# rohan=str1+str2
# print(rohan)

#11Count how many times "o" appears in "Hello World".
# string="hello world"
# print(string.count("o"))

#12Reverse the string "Python"
# string="python"
# print(string[::-1])
# print(string[::-1])

    #13Check if a string entered by the user starts with "A"
# user="Alphabet"
# if user.startswith("A"):
#         print("diwakarsir")

##14Check if "apple" contains "p".
# string="apple"
# print("p"in string)

#15Take two numbers and print their sum, difference, product, and quotient
# n=10
# m=8
# print("SUM:", n+m)
# print("DIFFERENCE:", n-m)
# print("PRODUCT:", n*m)
# print("QUOTIENT:", n/m)

#16Check if 25 is greater than 20 and less than 30
# if 25>20 and 25<30:
#     print("25 is greater than 20 and less than 30")
#     print("true")

#17Ask the user for two numbers. Print "Both are positive" if both are greater than 0, else "At least one is not positive"
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > 0 and num2 > 0:
#     print("Both are positive")
# else:
#     print("At least one is not positive")

#18 Check if a number is divisible by both 2 and 3
# number = 12
# if number % 2 == 0 and number % 3 == 0:
#     print(f"{number} is divisible by both 2 and 3")
# else:    print(f"{number} is not divisible by both 2 and 3")

#19Check if "a" is in "apple".
# string="apple"
# print("a"in string)

#20Check if a number is between 1 and 100 (inclusive).
# number = 99
# if 1 <= number <= 100:
#     print(f"{number} is between 1 and 100 (inclusive)")
# else:
#     print(f"{number} is not between 1 and 100 (inclusive)")

#21 Compare two strings "cat" and "dog".
# str1="cat"
# str2="dog"
# if str1 == str2:
#     print("The strings are equal.")
# else:    print("The strings are not equal.")

#22Conditional Statements
#Check if a number is positive, negative, or zero.
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")

#23Ask the user to enter their age. If age ≥ 18, print "Eligible to vote", else "Not eligible"
# age=int(input("enter your age:"))
# if age >=18:
#     print("Eligible to vote")
# else:    print("Not eligible")

#24Check if a given number is even or odd.
# num=int(input("enter a number:"))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

#25Input a number and check if it is divisible by 5
# num=int(input("enter a number:"))
# if num % 5 == 0:
#         print("The number is divisible by 5")

#26Ask the user to enter a password. If it matches "admin123", print "Access Granted", else "Access Denied"
# user = input("Enter password:")
# if user == "admin123":
#     print("Access Granted")
# else:    print("Access Denied")

#27Check if a character entered by the user is a vowel or consonant.
# char=input("Enter a character:")
# if char.lower() in 'aeiou':
#     print("The character is a vowel.")
# else:    print("The character is a consonant.")

#28Check if a given year is a leap year.
# year=int(input("enter a year:"))
# if year % 4 == 0:
#     print("{year} is a leap year")
# else:    print("{year} is not a leap year")

#29Ask the user for marks. Print "Grade A" if marks ≥ 90, "Grade B" if ≥ 75, "Grade C" if ≥ 50, else "Fail"
# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")

#30Check if a number is odd and greater than 50
# num=int(input("enter a number:"))
# if num%2!=0 and num>50:
#     print("The number is odd and greater than 50")
# else:    print("The number is not odd and greater than 50")

####################tuples#################
#31Create a tuple with 6 numbers. Print the largest and smallest number.
# number =(11,25,67,98,65,99)
# print("Largest number:", max(number))
# print("Smallest number:", min(number))

#32Check if 50 exists in (10, 20, 30, 40, 50, 60).
# tuple=(10,20,30,50,60)
# if 50 in tuple:
#     print("50 exists in the tuple.")
# else:    print("50 does not exist in the tuple.")

#33Store 5 colors in a tuple. Ask the user to enter a color name. Check if it exists.
# colors = ("red", "blue", "green", "yellow", "black")

# user_color = input("Enter a color name: ")

# if user_color in colors:
#     print("Color exists")
# else:
#     print("Color not found")

#34 Print the length of a tuple (1, 2, 3, 4, 5).
# tuple=(1,2,3,4,5)
# print(len(tuple))
# print(type(tuple))

#35Create a tuple with 4 strings. Print them one by one using indexing.
# tuple=("python","sql","pyspark","aws")
# print(tuple[0])
# print(tuple[1])
# print(tuple[2])
# print(tuple[3])

######Dictionaries (36–41)
#36Create a dictionary with 3 countries as keys and their capitals as values. Print the capital of "India"
# countries={"india":"new delhi","uk":"london","japan":"tokyo"}
# print(countries["india"])

#37Add a new country-capital pair to an existing dictionary.
# countries["france"] = "paris"
# print(countries)
#38Given a dictionary of student marks, check if "Anita" is present as a key. If yes, print her marks.
# marks = {"Anita": 85, "rohan": 90, "praneeth": 78}
# if "Anita" in marks:
#      print(f"Anita's marks: {marks['Anita']}")

#39Create a dictionary with usernames and passwords. Ask the user to enter a username and password. If both match, print "Login Successful", else "Login Failed"
# users = {
#     "rohan": "1234",
#     "admin": "admin123",
#     "user1": "pass567"
# }
# username = input("Enter username: ")
# password = input("Enter password: ")

# if username in users and users[username] == password:
#     print("Login Successful")
# else:
#     print("Login Failed")

#40Print all keys of a dictionary.
# countries={"india":"new delhi","uk":"london","japan":"tokyo"}
# print(countries.keys())
#41
#Create a dictionary with 3 items and their prices. Ask the user to enter an item name. Print the price if it exists, else "Item not found".
# items = {
#     "Rice": 50,
#     "Milk": 30,
#     "kiwi": 45
# }

# item = input("Enter item name: ")

# if item in items:
#     print(items[item])
# else:
#     print("Item not found")

#42 Create a list of 5 numbers and print the first and last elements.
# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])
# print(numbers[-1])

#43Add a new element to a list.
# numbers = [10, 20, 30, 40, 50]
# numbers.append(60)
# print(numbers)

#44Remove an element from a list.
# numbers = [10, 20, 30, 40, 50]
# numbers.remove(30)
# print(numbers)

#45Create a list of 4 colors and print its length.
# colors = ["red", "blue", "green", "yellow"]
# print(len(colors))

#46Check if "red" exists in a list of colors.
# colors = ["red", "blue", "green", "yellow"]
# if "red" in colors:
#     print("red exists in the list.")
# else:   print("red does not exist in the list.")

#47Print the second to fourth elements of a list.
# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:4])

#48Print the last 3 elements of a list.
# numbers = [10, 20, 30, 40, 50]
# print(numbers[-3:])

#49Store 5 names in a list and print the name at index 2.
# names = ["rohan", "siddiq", "praneeth", "harika", "sunitha"]
# print(names[2])

#50Reverse a list.
# names.reverse()
# print(names)

#51Replace the second element of a list with "Python".
# names[1] = "Python"
# print(names)

#52Create a list of 5 numbers. Check if a number entered by the user exists in the list.
# numbers = [10, 20, 30, 40, 50]
# user_number = int(input("Enter a number: "))
# if user_number in numbers:
#     print("Number exists in the list.")
# else:
#     print("Number does not exist in the list.")

#53Store 5 subjects in a list. Ask the user to enter a subject name. If it exists, print "Found", else "Not Found".
# subjects = ["Maths", "Science", "English", "Python", "History"]

# name = input("Enter subject: ")

# if name in subjects:
#     print(name, "Found")
# else:
#     print(name, "Not Found")

#54Create a list of marks. If the average is ≥ 50, print "Pass", else "Fail".
# marks = [80, 75, 90, 60, 85]
# average = sum(marks) / len(marks)
# if average >= 50:
#     print("Pass")
# else:    print("Fail")

#55Check if the first and last elements of a list are equal.
# numbers = [10, 20, 30, 40, 10]
# if numbers[0] == numbers[-1]:
#     print("First and last elements are equal.")
# else:
#     print("First and last elements are not equal.")

#56Create a list of strings. Print "Contains Python" if "Python" is in the list.
# strings = ["rohan", "siddiq", "praneeth","jasu"]
# if "Python" in strings:
#     print("Contains Python")
# else:    print("Does not contain Python")

#57Create a list of 5 numbers. Print the largest and smallest numbers
# numbers = [10, 20, 30, 40, 50]
# print("Largest number:", max(numbers))
# print("Smallest number:", min(numbers))

#58Count how many times "apple" appears in a list.
# fruits = ["apple", "banana", "apple", "kiwi", "apple"]
# count = fruits.count("apple")
# print("Number of times 'apple' appears:", count)

#59Store 5 numbers in a list. Print only the even numbers.
# numbers = [10, 15, 20, 25, 30]
# even_numbers = [n for n in numbers if n % 2 == 0]
# print("Even numbers:", even_numbers)

#60Check if a list is empty.
# my_list = []
# if my_list is []:
#     print("List is empty.")
# else:
#     print("List is not empty.")

#61Create a list of 5 numbers. If all numbers are positive, print "All Positive", else "Contains Negative".
# numbers = [10, 20, 30, 40, -1, 50]
# if all(n > 0 for n in numbers):
#     print("All Positive")
# elif any(n < 0 for n in numbers):
#     print("Contains Negative")

#62Store 5 numbers in a tuple. Check if the number 10 is present.
# numbers = (10, 20, 30, 40, 50)
# if 10 in numbers:
#     print("10 is present in the tuple.")
# else:    print("10 is not present in the tuple.")

#63Create a dictionary with student names as keys and marks as values. Check if "Rahul" is in the dictionary.
# students = {"rohan": 85, "siddiq": 90, "praneeth": 78}
# if "Rahul" in students:
#     print("Rahul is in the dictionary.")
# else:
#     print("Rahul is not in the dictionary.")

#64Take a string input and check if it contains the word "Python".
# r_string = input("Enter a string: ")
# if "Python" in r_string:
#     print("The string contains the word 'Python'.")
# else:
#     print("The string does not contain the word 'Python'.")

#65Ask the user for two numbers. Print "Equal" if they are equal, "First is greater" if the first is larger, else "Second is greater".
# a = int(input())
# b = int(input())

# if a > b:
#     print("First is greater")
# elif b > a:
#     print("Second is greater")
# else:
#     print("Equal")

#66Check if a number is divisible by 2 OR 5.
# number = int(input("Enter a number: "))
# if number % 2 == 0 and number % 5 == 0:
#     print(f"{number} is divisible by 2 & 5")
# else:    print(f"{number} is not divisible by 2 or 5")

#67Create a dictionary with 3 employees and their salaries. Print the salary of the employee with the highest pay.
# employees = {"rohan": "500000", "praneeth": "400000", "siddiq": "300000"}
# print(max(employees.values()))

#68Check if a string entered by the user contains both "a" and "b".
# text = input("Enter a string: ")

# if "a" in text and "b" in text:
#     print("Contains both a and b")
# else:
#     print("Does not contain both")

#69Store 5 subjects in a tuple. Ask the user to enter a subject name. If it exists, print "Subject Found", else "Not Found"
# subjects = ("Maths", "Science", "English", "Python", "History")

# sub = input("Enter subject: ")

# if sub in subjects:
#     print("Subject Found")
# else:
#     print("Not Found")
#70Check if a number entered by the user is both even and between 10 and 50.
# num = int(input("Enter a number: "))

# if num % 2 == 0 and num >= 10 and num <= 50:
#     print("Yes")
# else:
#     print("No")

#71Convert a string to uppercase.
# text = input("Enter a string: ")

# print(text.upper())

#72Convert a string to lowercase
# text = input("Enter a string: ")
# print(text.lower())


#73Replace one word in a string with another.

# text = "I like python"
# new_text = text.replace("python","java")

# print(new_text)

#74Remove extra spaces from a string
# text = "   Hello World!   "
# new_text = text.strip()
# print(new_text)

#75Split a string into a list of words.
# text = input("Enter words: ")

# words = list(text.split())

# print(words)

#76Join a list of words into a single string.
# words = ["Hello", "World", "Python"]
# text = " ".join(words)
# print(text)


#77Count how many times a letter appears in a string
# text = input("Enter a string: ")
# letter = input("Enter a letter: ")

# print(text.count(letter))

#78Find the position of a character in a string.
# text = input("Enter a string: ")
# char = input("Enter a character: ")
# position = text.find(char)
# if position != -1:
#     print(f"Position of '{char}': {position}")
# else:
#     print(f"'{char}' not found in the string.")

#79Check if a string contains only letters and numbers.
# text = input("Enter a string: ")

# if text.isalnum():
#     print("Yes")
# else:
#     print("No")

#80Check if a string contains only digits
# text = input("Enter a string: ")

# if text.isdigit():
#     print("Yes")
# else:
#     print("No")

#81Add an element to the end of a list.
# num=[1,2,3,4,5]
# num.append(6)
# print(num)

#82Add multiple elements to a list at once.
# num=[1,2,3,4,5]
# num.extend([6,7,8])
# print(num)

#83Insert an element at a specific position in a list.
# num=[1,2,3,4,5]
# num.insert(2,10)
# print(num)

#84Remove a specific element from a list.
# num=[1,2,3,4,5]
# num.remove(3)
# print(num)

#85Remove the last element from a list.
# num=[1,2,3,4,5]
# num.pop()
# print(num)

#86Arrange the elements of a list in ascending order.
# num=[5,2,9,1,3]
# num.sort()
# print(num)
#87Reverse the order of elements in a list.
# num=[1,2,3,4,5]
# num.reverse()
# print(num)

#88Find the position of an element in a list.
# num=[10,20,30,40,50]
# print(num.index(30))

#89Count how many times a number appears in a list.
# num=[1,2,3,2,4,5,2]
# print(num.count(2))

#90Remove all elements from a list.
# num=[1,2,3,4,5]
# num.clear()
# print(num)

#91 Print all keys of a dictionary
# countries={"india":"new delhi","uk":"london","japan":"tokyo"}
# print(countries.keys())

#92Print all values of a dictionary.
# countries={"india":"new delhi","uk":"london","japan":"tokyo"}
# print(countries.values())

#93Print all key-value pairs of a dictionary.
# countries={"india":"new delhi","uk":"london","japan":"tokyo"}
# print(countries.items())

#94Access the value of a key safely.
# student = {"name": "Ravi", "age": 20}

# print(student.get("name"))

 #95Add a new key-value pair to a dictionary.
# student = {"name": "Ravi", "age": 20}
# student["grade"] = "A"
# print(student)

#96Remove a specific key from a dictionary.
# student = {"name": "Ravi", "age": 20, "grade": "A"}
# del student["age"]
# print(student)

#97Remove the last inserted item from a dictionary.
# student = {"name": "Ravi", "age": 20, "grade": "A"}
# student.popitem()
# print(student)

#98Check if a key exists in a dictionary.
# student = {"name": "Ravi", "age": 20, "grade": "A"}
# if "name" in student:
#     print("Key exists in the dictionary.")
# else:
#     print("Key does not exist in the dictionary.")

#99Create a dictionary with given keys and the same default value.
# keys = ["name", "age", "grade"]
# default_value = "unknown"
# student = dict.fromkeys(keys, default_value)
# print(student)

#100Make a copy of a dictionary.
# student = {"name": "Ravi", "age": 20, "grade": "A"}
# student_copy = student.copy()
# print(student_copy)