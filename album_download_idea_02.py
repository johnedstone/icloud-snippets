>> import pyicloud
>>> dir(api)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'api' is not defined
>>> dir(pyicloud)
['PyiCloudService', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'base', 'exceptions', 'logging', 'services', 'utils']
>>> api = pyicloud.PyiCloudService('email', 'password', cookie_directory='path to session cookies')
>>> api.requires_2fa
False
>>> api.photos.albums
{'All Photos': <PhotoAlbum: 'All Photos'>, 'Time-lapse': <PhotoAlbum: 'Time-lapse'>, 'Videos': <PhotoAlbum: 'Videos'>, 'Slo-mo': <PhotoAlbum: 'Slo-mo'>, 'Bursts': <PhotoAlbum: 'Bursts'>, 'Favorites': <PhotoAlbum: 'Favorites'>, 'Panoramas': <PhotoAlbum: 'Panoramas'>, 'Screenshots': <PhotoAlbum: 'Screenshots'>, 'Live': <PhotoAlbum: 'Live'>, 'Recently Deleted': <PhotoAlbum: 'Recently Deleted'>, 'Hidden': <PhotoAlbum: 'Hidden'>, 'My movies': <PhotoAlbum: 'My movies'>, 'Third Fourth': <PhotoAlbum: 'Third Fourth'>}
>>> img_list = []
>>> img_list_duplicates = []
>>> img_list_duplicates_extra = []
>>> api.photos.albums
{'All Photos': <PhotoAlbum: 'All Photos'>, 'Time-lapse': <PhotoAlbum: 'Time-lapse'>, 'Videos': <PhotoAlbum: 'Videos'>, 'Slo-mo': <PhotoAlbum: 'Slo-mo'>, 'Bursts': <PhotoAlbum: 'Bursts'>, 'Favorites': <PhotoAlbum: 'Favorites'>, 'Panoramas': <PhotoAlbum: 'Panoramas'>, 'Screenshots': <PhotoAlbum: 'Screenshots'>, 'Live': <PhotoAlbum: 'Live'>, 'Recently Deleted': <PhotoAlbum: 'Recently Deleted'>, 'Hidden': <PhotoAlbum: 'Hidden'>, 'My movies': <PhotoAlbum: 'My movies'>, 'Third Fourth': <PhotoAlbum: 'Third Fourth'>}
>>> pa = 'Third Fourth'
>>> dir_list = [pa, pa + '/duplicates']
>>> import os
>>> for d in dir_list:
...     if not os.path.exists(d):
...         os.mkdir(d)
... 
>>> photos = api.photos.albums['Third Fourth']
>>> len(photos)
324
>>> for p in photos:
...     if (p.filename, p.size) not in img_list:
...         download = p.download()
...         with open('{}/{}'.format(pa, p.filename), 'wb') as opened_file:
...             opened_file.write(download.raw.read())
...         img_list.append((p.filename, p.size))
...     elif (p.filename, p.size) not in img_list_duplicates:
...         download = p.download()
...         with open('{}/duplicates/{}'.format(pa, p.filename), 'wb') as opened_file:
...             opened_file.write(download.raw.read())
...         img_list_duplicates.append((p.filename, p.size))
...     else:
...         img_list_duplicates_extra.append((p.filename, p.size))

>>> len(img_list)
69
>>> len(img_list_duplicates)
68
>>> len(img_list_duplicates_extra)
187
>>> 68 + 69 +187
324

# vim: ai et ts=4 sts=4 sw=4 nu
