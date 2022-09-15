import json
import sys

def json_import():
	with open('data.json', 'r', encoding='utf-8') as fh: 
		d = json.load(fh)
	return d

def json_export(d):
	with open("data.json", "w") as write_file:
		json.dump(d, write_file)