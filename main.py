from orchidCli import cli
from roseUtils import common
from roseUtils.common import style
from roseUtils.math.calculator import lexer, parser

if __name__ == "_main__":

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

		elif command in ["menu", "m"]:
			while True:
				common.clear()
				cli.render_bg()

		else:
			print(style.red + "Command not found" + style.reset)

if __name__ == "__main__":
	print(parser(lexer("(12+34)*56-78/90")))