import logging
import os
import sys
from datetime import datetime
from pprint import pprint

if not os.path.exists('logs'):
    os.mkdir('logs')

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s", datefmt="%d/%m/%y %H:%M:%S",
    handlers=[
        logging.FileHandler('logs/download.logs'),
        logging.StreamHandler()
    ]
)

def album_download(api=None, album_list=[], exclude_list=[]):
    try:
        for d in album_list:
            if not os.path.exists(d):
                os.mkdir(d)
        logging.info('album_list: {}'.format(album_list))
    except Exception as e:
        pass
    finally:
        logging.info('Finished downloading')

if __name__ == '__main__':
    logging.info('Starting')

# vim: ai et ts=4 sw=4 sts=4 nu
