from random import randint

number = ''
for i in range(4):
	number += str(randint(0, 9))

print(number)

while True:
	guess = input('Give me your best guess: ')