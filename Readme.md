### References
* [Description, examples, etc](https://pypi.org/project/pyicloud/)
* [github pyicloud](https://github.com/picklepete/pyicloud)

### Current usage

```
>>> import pyicloud
>>> import album_download_03
>>> api = pyicloud.PyiCloudService('email', 'password', cookie_directory='path to session informaion')

>>> api.requires_2fa
True
>>> 
>>> api.validate_2fa_code('034346')
[21/10/21 10:56:16] Failed to parse response with JSON mimetype
True
>>> api.requires_2fa
False

Note: 2fa is not needed if cookie_directory is still present with session cookies (until they expire)

>>> all_albums = [i for i in api.photos.albums]
>>> album_download_03.album_download(api, album_list=all_albums, exclude_list=['Favorites'], parent_directory=path/to/directory)

Or: 
>>> album_download_03.album_download(api, album_list=['Favorites'], parent_directory='path/to/directory')
Note: path can be absolute or relative. The script will create recursive directories (if perm allow, of course)

```

### System Requirements (Ubuntu)
* [heif-convert](https://stuffjasondoes.com/2019/07/10/batch-convert-heic-to-jpg-in-linux/)
    that is, `sudo apt install libheif-examples`
* [auto rotate](https://www.sentex.ca/~mwandel/jhead/)
    `sudo apt install jhead` and `jhead -autorot IMG_4621.jpg`
