# Short hand if else notation :


x = int(input("Enter the first number\n"))
y = int(input("Enter the second number\n"))
# if x>y:
#     print("x is greater than y")

if x>y: print("x is greater than y")

# if x>y:
#     print("x is greater than y")
# else:
#     print("Y is greater than x")

print("x is greater than y") if x>y else print("y is greater than x")