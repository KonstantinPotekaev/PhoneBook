import json

dict ={
  "id": "04",
  "name": "sunil",
  "department": "HR"
}

def Import(filename):
    data = {}
    with open(filename,"r") as f:
        data = json.load(f)
    return data

def Export(filename, data):
    with open(filename,"r+") as f:
        json.dump(data, f, indent=4)
