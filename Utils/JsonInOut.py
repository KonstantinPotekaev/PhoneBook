import json

dict ={
  "id": "04",
  "name": "sunil",
  "department": "HR"
}

def Export(filename, data):
    with open(filename,"w") as f:
        json.dump(data, f, indent=4)

Export("1.json", dict)