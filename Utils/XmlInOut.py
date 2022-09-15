import dicttoxml
import xmltodict


def Import(filename):
    xml_data = open(filename).read()
    data = xmltodict.parse(xml_data)
    return data

def Export(filename, data):
    raw_data = dicttoxml.dicttoxml(data, attr_type=False, custom_root='phone_book')
    str_data = raw_data.decode()
    with open(filename, "w") as f:
        f.write(str_data)



