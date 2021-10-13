import logging
import os
import sys
from datetime import datetime
from pprint import pprint

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(message)s", datefmt="%d/%m/%y %H:%M:%S"
)

if __name__ == '__main__':
    logging.info('boo')

# vim: ai et ts=4 sw=4 sts=4 nu

