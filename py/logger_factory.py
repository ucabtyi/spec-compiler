import logging
import sys


def get_basic_logger(name):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        stream=sys.stdout)
    return logging.getLogger(name)