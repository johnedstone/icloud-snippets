img_list = []
pa = 'All Photos'

if not os.path.exists(pa):
    os.mkdir(pa)

photos = api.photos.albums[pa]
total = photos.__len__()

print('length of photo album({}): {}'.format(pa, total))

if total:
    for i,photo in enumerate(photos):
        if (photo.filename, photo.size) in img_list:
            pass
        else:
            download = photo.download()
            with open('{}/{}'.format(pa, photo.filename), 'wb') as opened_file:
                opened_file.write(download.raw.read())
            img_list.append((photo.filename, photo.size))

print('Files downloaded: {}'.format(len(img_list)))
