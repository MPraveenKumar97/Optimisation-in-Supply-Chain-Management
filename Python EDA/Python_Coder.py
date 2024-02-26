# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:56:14 2024

@author: prave
"""

exp1 = eval(input())
print(exp1)
# Here are the two main ways you can convert data types in Python:

# 1. Automatic Casting (Python's helping hand):
# Imagine someone in the toolbox workshop saying, "Hey, you need a nail, not a screw. Here you go!"
# Python automatically changes between types when needed, like turning a number into a string when you print it. 
# and if you do 5 + 5.15 it gives 10.15 coverts the result into float

# 2. Manual Casting (telling Python what to do):
# This is like grabbing a tool yourself and putting it in a different compartment.
# You use built-in functions like int(), float(), and str() to tell Python what type you want something to be.
# For example, int("5") takes the string "5" and turns it into the number 5.


#Swapping
#method 1

x = 12
y = 14

temp = x
print(temp)
x = y
print(x)
y = temp
print(y)

print("The value of x is: ", x)
print("The value of y is: ", y)

#method 2 
a = 20
b = 30
a,b = b,a
print(a,b)

a = int(input("enter a number: "))
print(type(a))
a = float(a)
print("after coversion:",a," is", type(a))

marks = 99

if (marks>=95):
    print("Topper")


if (marks>100):
    print('Excellent')
else:
    print("That's outstanding")
    
if (marks>95):
    print("O")
elif (marks>90):
    print("A+")
else:
    print("A")
    
# Nested if example

# Taking user input for age
age = int(input("Enter your age: "))

# Checking age conditions
if age >= 18:
    print("You are eligible to vote.")
    
    # Checking additional condition for eligibility to run for office
    if age >= 25:
        print("You are also eligible to run for public office.")
    else:
        print("You cannot run for public office yet.")
else:
    print("You are not eligible to vote.")

#short hand if statement
if (marks >= 90): print("you will get a new phone")

#short hand if else statement

lottery = 999

print("You can go to a trip") if lottery == 999 else print("you cannot go to the trip")

#checking if a number is postive or negative

num = int(input("enter a number: "))

if (num>0):
    print("it is positive")
else:
    print("it is negative")
    
 #checking if a number is even or odd

num = int(input("enter a number: "))

if (num%2)==0:
    print("it is even")
else:
    print("it is odd")

#write a program to create a area calculator

print ("*****AREA CALCULATOR*****")
print ("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle""")

choice = int(input('enter a number between 1-4: '))

if choice == 1:
    side = float(input("enter the length of one side: "))
    area = side**2
    print("the area of square is ", area)

elif choice == 2:
    length = float(input("enter the length of the rectangle: "))
    width = float(input("enter the width of the rectangle: "))
    area = length * width
    print("the area of rectangle is ", area)

elif choice == 3:
    radius = float(input("enter the radius of the circle: "))
    area = ((22/7)*(radius**2))
    print ("the area of the circle is", area)

elif choice == 4:
    base = float(input("enter the base of the triangle: "))
    height = float(input("enter the height of the triangle: "))
    area = 0.5*base*height
    print ("the area of the triangle is", area)
    
else:
    print("invalid input")
    
#write a program to chexk the letter is vowel or not

letter = input("enter a letter: ")

if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is a vowel")
else:
    print("it is not a vowel")
    
# Write a program to check if a number is a single digit number, double digit, triple or so on upto 5

num = int(input("enter a num upto 5 digits: "))

if (num>=0) and (num<=9):
    print("It is a single digit number")
    
elif (num>=10) and (num<=99):
    print("It is a double digit number")
    
elif (num>=100) and (num<=999):
    print("It is a triple digit number")
    
elif (num>=1000) and (num<=9999):
    print("It is a four digit number")
    
elif (num>=10000) and (num<=99999):
    print("It is a five digit number")
    
else:
    print("invalid entry, please try again")
    
for i in range(1,6,2):
    print("hello")
    
n = 7

for i in range(1,11):
    print(n,"*",i,"=",n*i)
    
n = 0

while n<=5:
    print(n)
    n += 1
    
n = 1
m = 7
while n<=10:
    print(m,"x",n,"=",n*m)
    n += 1
    
for i in range(1,4):
    for j in range(1,11):
        print(j, end = "")
    print()
    
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end =' ')
    print()

#Write a program to check if a number is divisible by 8 and 12,upto 100
    
for i in range(1,101):
    if (i%8 == 0) and (i%12 == 0):
        print(i)
        
n = 1

while n<=11:
    if n==3:
        print("Add this to favs")
    else:
        print(n)
    n+=1
    
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i)

for i in range(1,11):
    if i==7:
        break
    else:
        print(i)
        
#Write a program to find the sum of all even numbers upto 50

x=0
for i in range(0,51):
    if (i%2==0):
        x+=i
print(x)

sum = 0

for i in range(0,51,2):
    sum +=i

print(sum)

#Write a program to write first 20 numbers and their squared numbers

for i in range(1,21):
    print(i,i**2)
    
#Write a program to find the sum of first 10 odd numbers using while loop

sum = 0
n = 0

while n <= 20:
    if (n%2!=0):
        sum += n
    n += 1
print(sum)

#write a program to create a billing system at supermarket

while True:
    name = input("Enter customer's name: ")
    total = 0
    
    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter amount: "))
        quantity = float(input("Enter quantity: "))
        total += amount * quantity
        
        repeat = input("do you want to add more items? [yes/no]: ")
        
        if repeat == "no" or repeat == "No":
            break
    
    print('-'*40)
    print("Name: ", name)
    print("Amount to be paid: ", total)
    print('-'*40)
    
    repeat = input("do you want to go to next customer? [yes/no]: ")
    if repeat == "no" or repeat == "No":
        break
        




