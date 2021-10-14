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
        logging.info('album_list: {}'.format(album_list))
        logging.info('exclude_list: {}'.format(exclude_list))

        for album in album_list:
            if album not in exclude_list:
                if not os.path.exists(album):
                    os.mkdir(album)
                if not os.path.exists('{}/duplicates'.format(album)):
                    os.mkdir('{}/duplicates'.format(album))

                img_list = []
                img_list_duplicates = []
                img_list_duplicates_extra = []

                photos = api.photos.albums[album]
                logging.info('Starting, total number of object in {}: {}'.format(album, len(photos)))

                for p in photos:
                    if (p.filename, p.size) not in img_list:
                        download = p.download()
                        with open('{}/{}'.format(album, p.filename), 'wb') as opened_file:
                            opened_file.write(download.raw.read())

                        img_list.append((p.filename, p.size))

                    elif (p.filename, p.size) not in img_list_duplicates:
                        download = p.download()
                        with open('{}/duplicates/{}'.format(album, p.filename), 'wb') as opened_file:
                            b = opened_file.write(download.raw.read())
                            logging.info('{}: {}'.format(p.filename, b))

                        img_list_duplicates.append((p.filename, p.size))

                    else:
                       img_list_duplicates_extra.append((p.filename, p.size))

                logging.info('Finished, total number of object in {}: {}'.format(album, len(photos)))
                logging.info('Total number of unique object in album: {}'.format(len(img_list)))
                logging.info('Total number of duplicates object in album: {}'.format(
                    len(img_list_duplicates)))
                logging.info('Total number of duplicate extras object in album: {}'.format(
                    len(img_list_duplicates_extra)))

    except Exception as e:
        logging.error('Error: {}'.format(e))

    finally:
        logging.info('Finished downloading')

if __name__ == '__main__':
    logging.info('Starting')

# vim: ai et ts=4 sw=4 sts=4 nu
