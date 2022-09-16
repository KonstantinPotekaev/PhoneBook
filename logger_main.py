import logging

logging.basicConfig(filename='work_logs.log', filemode='a', format='%(asctime)s -- %(levelname)s:%(message)s',
                    datefmt='%d.%m.%Y %I:%M:%S %p', encoding='utf-8', level='DEBUG')
logger = logging.getLogger(__name__)