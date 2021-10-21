import logging
import os
import shlex
import shutil
import subprocess

from datetime import datetime

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

def album_download(api=None, album_list=[], exclude_list=[], parent_directory='./'):
    try:
        logging.info('album_list: {}'.format(album_list))
        logging.info('exclude_list: {}'.format(exclude_list))

        for album in album_list:
            if album not in exclude_list:
                album_dir = os.path.join(parent_directory, album)
                album_dir_duplicates = os.path.join(album_dir, 'duplicates')
                album_dir_heic = os.path.join(album_dir, 'heic_photos')
                if not os.path.exists(album_dir):
                    os.makedirs(album_dir_duplicates)
                    os.makedirs(album_dir_heic)

                img_list = []
                img_list_duplicates = []
                img_list_duplicates_extra = []

                photos = api.photos.albums[album]
                logging.info('Starting, total number of object in {}: {}'.format(album, len(photos)))

                for p in photos:
                    try:

                        if (p.filename, p.size) not in img_list:
                            download = p.download()
                            with open('{}/{}'.format(album_dir, p.filename), 'wb') as opened_file:
                                b = opened_file.write(download.raw.read())
                                logging.info('Original (bytes written) {}: {}'.format(p.filename, b))
    
                            if p.filename.lower().endswith('.heic'):
                                heic_name = shlex.quote(os.path.join(album_dir, p.filename))
                                jpg_name = shlex.quote(os.path.join(album_dir, p.filename.lower().replace('.heic', '_from_heic.jpg')))
                                cmd = '/usr/bin/heif-convert {} {}'.format(
                                        heic_name, jpg_name)
                                output = subprocess.run(shlex.split(cmd))
                                logging.info('Created {} from {}: {}'.format(jpg_name, p.filename, output))
    
                                # fix orientation
                                cmd = '/usr/bin/jhead -autorot {}'.format(jpg_name)
                                output = subprocess.run(shlex.split(cmd))
                                logging.info('Autorotated {} to {}: {}'.format(p.filename, jpg_name, output))
    
                                # move to dir, out of the way
                                cmd = '/bin/mv {} {}'.format(heic_name, os.path.join(shlex.quote(album_dir_heic), shlex.quote(p.filename)))
                                output = subprocess.run(shlex.split(cmd))
                                logging.info('Moving {} to heic_photos directory: {}'.format(p.filename, output))
    
                            img_list.append((p.filename, p.size))
    
                        elif (p.filename, p.size) not in img_list_duplicates:
                            download = p.download()
                            with open('{}/{}'.format(album_dir_duplicates, p.filename), 'wb') as opened_file:
                                b = opened_file.write(download.raw.read())
                                logging.info('Duplicate (bytes written) {}: {}'.format(p.filename, b))
    
                            img_list_duplicates.append((p.filename, p.size))
    
                        else:
                           img_list_duplicates_extra.append((p.filename, p.size))

                    except Exception as e:
                        logging.error('Inner error: {} : {} : {}'.format(album_dir, p.filename, e))


                logging.info('Finished, total number of object in {}: {}'.format(album, len(photos)))
                logging.info('Total number of unique object downloaded: {}'.format(len(img_list)))
                logging.info('Total number of duplicate objects downloaded: {}'.format(
                    len(img_list_duplicates)))
                logging.info('Total number of duplicate extra objects, not downloaded: {}'.format(
                    len(img_list_duplicates_extra)))

    except Exception as e:
        logging.error('Outer error: {}'.format(e))

    finally:
        logging.info('Finished downloading')

if __name__ == '__main__':
    logging.info('Starting')

# vim: ai et ts=4 sw=4 sts=4 nu
