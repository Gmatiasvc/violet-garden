
from orchidCli import cli
from roseUtils import common
from roseUtils.common import style

if __name__ == "__main__":
	cursor = style.yellow + " $ " + style.reset
	command = ""
	print("Blooming Boxes Utilities [Alpha 1]")
	while True:
		print(cursor, end="")
		command = str(input())

		if command in ["exit", "quit", "q"]:
			break

		elif command in ["clear", "cls"]:
			common.clear()

		elif command == "menu":
			cli.menu.renderer()

		else:
			print(style.red + "Command not found" + style.reset)