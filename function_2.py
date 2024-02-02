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