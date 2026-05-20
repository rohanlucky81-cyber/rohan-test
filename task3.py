#1Write a loop that prints numbers from 1 to 10, but stops completely when the number is 6.
# for i in range(1,11):
#     if i==6:
#         break
#     print(i)

#2Write a loop that prints numbers from 1 to 10, but skips printing the number 5.
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

#3Write a loop that prints only odd numbers between 1 and 10 using continue.
# for i in range(1,11):
#    if i%2==0:
#     continue
#    print(i)
#4Write a loop that prints numbers from 1 to 20, but breaks when the number is divisible by 7.
# for i in range(1,21):
#     if i%7==0:
#         break
#     print(i)

#5Write a loop that prints numbers from 1 to 10, but skips all even numbers
# for i in range(1,11):
#     if i%2==0:
#         continue
#     print(i)

#6Write a loop that prints numbers from 1 to 10, but stops when the number is greater than 8.
# for i in range(1,11):
#     if i>8:
#         break
#     print(i)

#7Write a loop that prints numbers from 1 to 15, but skips numbers divisible by 3.
# for i in range(1,16):
#     if i %3==0:
#         continue
#     print(i)

#8Write a loop that prints numbers from 1 to 10, but breaks when the number is equal to 4.
# for i in range(1,11):
#     if i ==4:
#         break
#     print(i)

#9Write a loop that prints numbers from 1 to 10, but skips printing 2 and 7.
# for i in range(1,11):
#     if i ==2 or i==7:
#         continue
#     print(i)

#10Write a loop that prints numbers from 1 to 10, but breaks when the number is 9.
# for i in range(1,11):
#     if i==9:
#         break
#     print(i)

#11 Ternary Operator Practice
#11Write a program that checks if a number is even or odd using a ternary operator.
# num=9
# result="even" if num%2==0 else"odd"
# print(result)

#12Write a program that prints "Positive" if a number is greater than 0, otherwise "Negative or Zero".
# num=-5
# result="positive" if num>0 else"negative"or"zero"
# print(result)

#13Write a program that prints "Adult" if age ≥ 18, otherwise "Minor"
# age=17
# result="Adult" if age>=18 else"Minor"
# print(result)

#14Write a program that prints "Pass" if marks ≥ 40, otherwise "Fail".
# marks=50
# result="pass" if marks>=40 else"fail"
# print(result)

#15Write a program that prints "Big" if a number > 100, otherwise "Small".
# num=150
# result="big" if num>100 else"small"
# print(result)

#16Write a program that prints "Equal" if two numbers are the same, otherwise "Not Equal".
# num1=5
# num2=111
# result="equal" if num1==num2 else"not equal"
# print(result)

#17Write a program that prints "Divisible by 5" if a number is divisible by 5, otherwise "Not Divisible".
# number=100
# result="Divisible by 5" if number%5==0 else"Not Divisible"
# print(result)


#18Write a program that prints "Leap Year" if a year is divisible by 4, otherwise "Not Leap Year".
# year=202000
# result="leap year" if year%4==0 else "not leap year"
# print(result)

#19Write a program that prints "Yes" if a number is positive, otherwise "No"
# num=10
# result="positive" if num>0 else"negative"
# print(result)

#20Write a program that prints "First" if a > b, otherwise "Second"
# a=5
# b=111
# result="first" if a>b else"second"
# print(result)

#21 write 
for num in range(1,28):
    if num%2!=0:
     continue
    print(num)