
# n = 10
# num1 = 0
# num2 = 1
# next_number = num2 
# count = 1

# while count <= n:
# 	print(next_number, end=" ")
# 	count += 1
# 	num1, num2 = num2, next_number
# 	next_number = num1 + num2
# print()


print("Enter your age")
age = int(input())
if age<18:
    print("You cannot drive")
elif age==18:
    print("We will think about you")
else:
    print("You can drive")
    