from roseUtils.exceptions import LexerException


symbols = [
    ["+"],  # 0 addition
    ["-"],  # 1 substracion
    ["*", "x"],  # 2 multiplication
    ["/"],  # 3 division
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],  # 4 numbers
    ["(", "[", "{"],  # 5 aggrupation open
    [")", "]", "}"],  # 6 aggrupation close
]

symbShallow = []
operands = []

for i in symbols:
    for m in i:
        symbShallow.append(m)


for i in symbols[0:4]:
    for m in i:
        operands.append(m)


def checkChars(arr: list) -> list:
    err = []
    for i in range(len(arr)):
        if arr[i] not in symbShallow:
            err.append(i)

    return err


def checkAggrupation(arr: list) -> bool:
    c = 0
    for i in range(len(arr)):
        if arr[i] in symbols[5]:
            c += 1
        elif arr[i] in symbols[6]:
            c -= 1
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

    return checked


def parser(arr: list) -> list:
    parsed = []
    num = 0
    isNumActive = False
    for i in arr:
        if i not in symbols[4] and isNumActive:
            parsed.append(num)
            parsed.append(i)
            num = 0
            isNumActive = False

        elif i in symbols[4] and not isNumActive:
            num = i
            isNumActive = True

        elif i in symbols[4] and isNumActive:
            i = float(i)
            num = (float(num) * 10) + i
            
        else:
            parsed.append(i)
    if isNumActive:
        parsed.append(num)
    return parsed

def evaluator(arr:list)-> float:
    pass

if __name__ == "__main__":
    pass
