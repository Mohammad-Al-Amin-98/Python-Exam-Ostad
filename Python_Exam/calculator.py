import sys
#simple calculator using python3

#addition function
def add(a, b):
	return a + b

#subtraction function
def subtract(a, b):
	return a - b

#multiplication function
def multiply(a, b):
	return a * b

#division function
def divide(a, b):
	return a / b

#modulo function
def modulus(a, b):
	return a % b

#prompt for user

print("Select operation:")
print()
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print()
choice = int(input("Enter choice(1/2/3/4/5):"))
print()

#invalid choice handling
if choice < 1 or choice > 5:
	while True:
		if choice >= 1 and choice <= 5:
			break
		print("Invalid Choice!")
		choice = int(input("Enter the choice again(1/2/3/4/5):"))
		print()

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

#verifying user given inputs
try:
	num1 = float(num1)
	num2 = float(num2)
except:
	print('Invalid number!')
	sys.exit()
print()

if choice == 1:
	print(f"{num1} + {num2} =", add(num1, num2))
elif choice == 2:
	print(f"{num1} - {num2} =", subtract(num1, num2))
elif choice == 3:
	print(f"{num1} * {num2} =", multiply(num1, num2))
elif choice == 4:
	if num2 == 0:
		print("Division by Zero not possible!")
	else:
		print(f"{num1} / {num2} =", divide(num1, num2))
else:
	print(f"{num1} % {num2} =", modulus(num1, num2))
