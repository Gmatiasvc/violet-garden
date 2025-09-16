import os

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def move(x,y):
	print(f"\033[{y};{x}H", end='')

def get_terminal_size():
	rows = os.get_terminal_size().lines
	columns = os.get_terminal_size().columns
	return rows, columns

class style:
	
	red = "\033[31m"
	green = "\033[32m"
	yellow = "\033[33m"
	blue = "\033[34m"
	magenta = "\033[35m"
	cyan = "\033[36m"
	white = "\033[37m"
	reset = "\033[0m"
	bold = "\033[1m"
	underline = "\033[4m"
	italic = "\033[3m"
	blink = "\033[5m"

	def rgb(r,g,b):
		return f"\033[38;2;{r};{g};{b}m"