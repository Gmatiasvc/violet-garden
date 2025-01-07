import os

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def move(x,y):
	print(f"\033[{y};{x}H", end='')