import json
import sys

def json_export(d):
	with open("data.json", "w") as write_file:
		json.dump(d, write_file)