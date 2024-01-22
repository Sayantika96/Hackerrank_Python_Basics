Problem : Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

user_input = int(input("Enter a valid number: "))
s = 0
for i in range(1, user_input + 1, 1):
    s = s+i
print("Sum is:",s)

