import random

number = random.randint(1, 100)
guess = 0
count = 0
print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100")
print()
print()


while guess != number:
	guess = input("Enter your guess: ")
	count += 1

	#verifying the guess if it is numeric or not
	try:
		guess = int(guess)
	except:
		print("Invalid input. You should enter a numberic value!")
		continue

	if guess < number:
		print("Too low!")
		print()
	elif guess > number:
		print("Too high!")
		print()
	else:
		print(f"Congratulations! You've guessed the number in {count} attempts!")
