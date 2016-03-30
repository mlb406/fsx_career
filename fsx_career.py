# fsx_career.py

import json

def open_file(filename):
	f = open(filename, "r");
	return f



def main():
	airports = json.load(open_file("data/airports.json").read())
	


if __name__ == '__main__':
	main()