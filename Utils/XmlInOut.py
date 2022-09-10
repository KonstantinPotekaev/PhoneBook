import dicttoxml
from xml.dom.minidom import parseString


data = {'name1': '111',
        'name2': '222',
        'name3': '333',
        'name4': '444',
        'name5': '555'}

def Out(filename, data):
    raw_data = dicttoxml.dicttoxml(data, attr_type = False)
    str_data = parseString(raw_data)
    with open(filename, "w") as f:
        f.write(str_data.toprettyxml())


Out('1.xml', data)
