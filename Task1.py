#Task 1: Check if a Number is Even or Odd

#num is an variable to store user input
num = int(input("Enter A Number:"))

#if condition is to check whether given number is even or not by performing modulus operator
# if num % 2 == 0 then it prints the even number otherwise it prints else part.
if num%2==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
    
