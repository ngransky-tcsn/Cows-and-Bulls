from random import randint

def check(num, guess):
	cows = 0
	bulls = 0
	for i in range(len(num)):
		if guess[i] == number[i]:
			cows += 1
		elif guess[i] in num:
			bulls += 1
	return [cows, bulls]

number = ''
for i in range(4):
	number += str(randint(0, 9))

print(number)

while True:
	guess = input('Give me your best guess: ')
	cowsandbulls = check(number, guess)
	print("Cows: " + str(cowsandbulls[0]))
	print("Bulls: " + str(cowsandbulls[1]))