Problem:
Implement a python program using map and lambda to perform element-wise exponentiation on two lists.

Solution:
list_1 = [1,2,3,4]
list_2 = [2,3,4,5]

new_list = list(map(lambda x : x[0]**x[1], zip(list_1,list_2)))

print(f"Exponent of {list_1} and {list_2} is: ",new_list)
