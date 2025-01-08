from orchidCli import functions
from roseUtils import common

def interface(command: str):
	cmd = command.split(" ")

	if cmd[0] in functions.fnc_help.aliases:
		print(functions.fnc_help().run())

	if cmd[0] in functions.fnc_get_orchid_cli_version.aliases:
		print(functions.fnc_get_orchid_cli_version().run())
	
	if cmd[0] in functions.fnc_exit.aliases:
		if functions.fnc_exit().run():
			exit()
class menu:
	def renderer():
		common.clear()
		rows, columns = function.get_terminal_size()   
		common.move(0,0)

		print(f"DEBUG:\nRows: {rows}\nColumns: {columns}", end="") 

		common.move(0,rows-1)

		print("█"*columns, end="")

		interface(input("\n: "))