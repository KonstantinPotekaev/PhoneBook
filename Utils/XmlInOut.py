
import dicttoxml
import xmltodict

data = {'name1': '111',
        'name2': '222',
        'name3': '333',
        'name4': '444',
        'name5': '555'}

def Out(filename, data):
    raw_data = dicttoxml.dicttoxml(data, attr_type = False, custom_root='phone_book')
    str_data = raw_data.decode()
    with open(filename, "w") as f:
        f.write(str_data)


Out('1.xml', data)
