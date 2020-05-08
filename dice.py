def draw_dice(p_dice_number):
	if (p_dice_number == 1):
			print("+-------+")
			print("|       |")
			print("|   O   |")
			print("|       |")
			print("+-------+")
	elif (p_dice_number == 2):
			print("+-------+")
			print("|   O   |")
			print("|       |")
			print("|   O   |")
			print("+-------+")
	if (p_dice_number == 3):
			print("+-------+")
			print("|    O  |")
			print("|   O   |")
			print("|  O    |")
			print("+-------+")
	if (p_dice_number == 4):
			print("+-------+")
			print("| O   O |")
			print("|       |")
			print("| O   O |")
			print("+-------+")
	if (p_dice_number == 5):
			print("+-------+")
			print("| O   O |")
			print("|   O   |")
			print("| O   O |")
			print("+-------+")
	if (p_dice_number == 6):
			print("+-------+")
			print("| O   O |")
			print("| O   O |")
			print("| O   O |")
			print("+-------+")
	return 0


import random

roll_again = "y"
while (roll_again == "y" or roll_again == "Y"):
		dice_number = random.randint(1,6)
		draw_dice(dice_number)
		roll_again = input ("Want to roll the dice again? (y/n)")

