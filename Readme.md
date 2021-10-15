### References
* [Description, examples, etc](https://pypi.org/project/pyicloud/)
* [github pyicloud](https://github.com/picklepete/pyicloud)

### Current usage

```
>>> import pyicloud
>>> import album_download_03
>>> api = pyicloud.PyiCloudService('email', 'password', cookie_directory='path to session informaion')
>>> api.requires_2fa
False
>>> all_albums = [i for i in api.photos.albums]
>>> album_download_03.album_download(api, album_list=all_albums, exclude_list=['Favorites'])

