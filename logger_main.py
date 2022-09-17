import logging

# Прописана конфигурация базовой настройки ведения журнала (Handler и Formatter)
logging.basicConfig(filename='work_logs.log', filemode='a', format='%(name)s %(asctime)s - %(levelname)s:%(message)s',
                    datefmt='%d.%m.%Y %H:%M:%S', encoding='utf-8', level=logging.INFO)

# Прописано имя регистратора
logger = logging.getLogger('PhoneBook')

# Функция логирования с описанием действия (под одно значение)
def unic_function(description, value):
    try:
        if value:
            logger.info(f'{description} - {value}')
    except BaseException as err:
        logger.exception({err})

# Функция логирования добавления контакта
def log_contact_add(name, phone):
    try:
        if name and phone:
            logger.info(f'Успешно добавлен контакт {name} с номером телефона {phone}')
    except BaseException as err:
        logger.exception({err})

# Функция логирования удаления контакта
def log_contact_del(name, phone):
    try:
        if name and phone:
            logger.info(f'Успешно удален контакт {name} с номером телефона {phone}')
    except BaseException as err:
        logger.exception({err})
