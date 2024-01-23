Problem: Write a program to count the total number of digits in a number using a while loop.
For example, the number is 75869, so the output should be 5.


Solution:
counter = 0
number = 12345

while number != 0:
    number = number // 10
    counter += 1
print("Total digits are: ",counter)
