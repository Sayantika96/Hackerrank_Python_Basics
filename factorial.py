factorial = 1
user_input = int(input("Enter an integer number : "))

for i in range(1,user_input + 1):
    factorial = factorial * i
print(f"The factorial of {user_input} is: ",factorial)