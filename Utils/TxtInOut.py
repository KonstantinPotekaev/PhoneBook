
def Import(filename):
        data = {}
        with open(filename) as f:
            lines = f.read().splitlines() # исключаем пустые строки
            for line in lines:
                key, value = line.split(': ')
                data.update({key: value})
        return data

# def Export(filename, data):
    #     with open(filename) as f:
    #
    #         for key, value in data.items:
    #             f.write(f'{key}: {value}')
