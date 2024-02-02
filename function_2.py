Problem: Implement a simple loan eligibility function that takes three parameters - age, income, and credit_score. If the applicant's age is greater than or equal to 19 years, their annual income is more than $100,00, and their credit_score is greater than or equal to 650, then they are eligible for the loan otherwise not. 
Apply this function to a dictionary having keys 'age', 'income', and 'credit_score'.

Solution:
def check_loan_eligible(age, income, credit_score):
    if age >= 19 and income >= 10000 and credit_score >= 650:
        return True
    else:
        return False
age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))
credit_score = int(input("Enter your credit score: "))
eligible = check_loan_eligible(age, income, credit_score)

if eligible:
    print("You're eligible for loan!!!")
else:
    print("Sorry!! Next time...")
