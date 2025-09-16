
from roseUtils.exceptions import LexerException


symbols = [
	['+'], # addition
	['-'], # substracion
	['*','x'], # multiplication
	['/'], # division
	['0','1','2','3','4','5','6','7','8','9'], # numbers
	['(','[','{'], # aggrupation open
	[')',']','}'] # aggrupation close
]

symbShallow = []
operands = []

for i in symbols:
	for m in i:
		symbShallow.append(m)


for i in symbols[0:4]:
	for m in i:
		operands.append(m)

def checkChars(arr : list) -> list: 
	err = []
	for i in range(len(arr)):
		if arr[i] not in symbShallow:
			err.append(i)
	
	return err

def checkAggrupation(arr: list) -> bool:
	c=0
	for i in range(len(arr)):
		if arr[i] in symbols[5]:
			c+=1
		elif arr[i] in symbols[6]:
			c-=1
	if c != 0:
		return False
	else:
		return True


def lexer(arr: list) -> list:
	
	# vars
	err = checkChars(arr)
	checked = []

	# remove unnecesary chars
	for i in range(len(arr)):
		if i not in err:
			checked.append(arr[i])

	# check parenthesis and others
	if not checkAggrupation(arr):
		raise LexerException("Aggrupation not well defined")


	# tokenizer
	for i in range(len(checked)):
		checked[i]

if __name__ == "__main__":
	pass