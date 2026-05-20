#1Write a loop that prints only the even numbers from a list.
# numbers=[1,2,3,4,5,6,7,8,10,12]
# for i in numbers:
#     if i%2==0:
#         print(i)
#2Given a list of integers, use a loop and conditionals to separate positive and negative numbers into two new lists.

# numbers=[1,-1,2,-2,3,-3,4,-4,5,-5]
# positive_numbers=[]
# negative_numbers=[]
# for num in numbers:
#     if num>0:
#         positive_numbers.append(num)
#     elif num<0:
#         negative_numbers.append(num)
# print("Positive numbers:", positive_numbers)
# print("Negative numbers:", negative_numbers)

#3Write a loop that prints "Big" if a list element is greater than 50, otherwise print "Small".
# num=[51,55,57,59,989]
# for n in num:
#  if n>50:
#         print("Big")
#  else:        print("Small")

#4Use a loop to count how many elements in a list are divisible by 3.
# numbers=[1,2,3,4,5,6,7,8,9,10,12,15,18]
# count=0
# for num in numbers:
#     if num%3==0:
#         count+=1
# print("Count of numbers divisible by 3:", count)

#5Write a loop that replaces all negative numbers in a list with 0.
# num=[-1,-2,-3,-4,-5,-6,7,8,9,1,2,3,]
# for i in range(len(num)):
#     if num[i]<0:
#         num[i]=0
# print(num)

#6Write a loop that prints elements of a tuple only if they are greater than 10
# numbers=(11,12,14,18,16,9,5,6,7,)
# for num in numbers:
#     if num>10:
#         print(num)

#7Given a tuple of numbers, use a loop to print "Odd" or "Even" for each element
# numbers=(1,2,3,4,5,6,7,8,9,10)
# for num in numbers:
#     if num%2==0:
#         print("Even")
#     else:       print("Odd")




#8Write a loop that finds the largest odd number in a tuple.
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# largest = 0

# for num in numbers:
#     if num % 2 != 0 and num > largest:
#         largest = num

# print(largest)

#9Use a loop to count how many elements in a tuple are prime numbers.
# numbers = (2, 3, 4, 5, 6)

# count = 0

# for num in numbers:
#     if num == 2 or num == 3 or num == 5:
#         count += 1

# print(count)

#10Write a loop that prints "High" if a tuple element is above 100, otherwise "Low".
# numbers = (50, 150, 200, 75, 25)
# for num in numbers:
#     if num > 100:
#         print("High")
#     else:        print("Low")


#11 Write a loop that prints only odd numbers from a set.
# numbers={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# for num in numbers:
#     if num % 2 != 0:
#         print(num)

#12Given a set of integers, use a loop to remove all numbers less than 5.
numbers = {1, 3, 5, 7, 2, 9, 4}

for num in list(numbers):
    if num < 5:
        numbers.remove(num)

print(numbers)