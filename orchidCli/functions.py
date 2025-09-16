from roseUtils import common

class fnc_get_orchid_cli_version:
	aliases = ["version", "v"]

	def __init__(self):
		self.version = "Alpha 1"

	def run(self):
		return self.version
	


class fnc_help:
	aliases = ["help", "h"]
	
	def __init__(self):
		self.help = "Unimplemented"

	def run(self):
		return self.help
	

class fnc_exit:
	aliases = ["exit", "quit", "q"]

	def __init__(self):
		rows, columns = common.get_terminal_size()
		common.move(0,rows)
		
		print("Are you sure you want to exit? (y/n): ", end="")

		if input().lower()[0] == "y":
			self.exit = True
		
		else:
			self.exit = False


	def run(self):
		return self.exit