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
>>> album_download_03.album_download(api, album_list=['All Photos', 'Third Fourth', 'Favorites'], exclude_list=['Favorites'])

