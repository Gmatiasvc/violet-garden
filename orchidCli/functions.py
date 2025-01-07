
class fnc_get_orchid_cli_version:
	def __init__(self):
		self.version = "0.1"

	def run(self):
		return self.version
	


class fnc_help:
	aliases = ["help", "h"]
	
	def __init__(self):
		self.help = "Unimplemented"

	def run(self):
		return self.help