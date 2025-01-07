import os

def get_terminal_size():
    rows = os.get_terminal_size().lines
    columns = os.get_terminal_size().columns
    return rows, columns

if __name__ == '__main__':
	print("Terminal size: \n from get_terminal_size():")
	rows, columns = get_terminal_size()
	print(f"rows: {rows}, columns: {columns}")