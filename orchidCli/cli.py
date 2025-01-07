from orchidCli import functions
from roseUtils import common
from leafyFetcher import envProperties

def interface(command: str):
	cmd = command.split(" ")

	if cmd[0] in functions.fnc_help.aliases:
		print(functions.fnc_help().run())

def menu_renderer():
    common.clear()
    rows, columns = envProperties.get_terminal_size()   
    common.move(0,0)
    
    print(f"DEBUG:\nRows: {rows}\nColumns: {columns}", end="") 
    
    common.move(0,rows-1)
    
    print("█"*columns, end="")
    
    interface(input("\n: "))