>>> photo_albums_list = [i for i in iter(api.photos.albums.keys())]
>>> photo_albums_list
['All Photos', 'Time-lapse', 'Videos', 'Slo-mo', 'Bursts', 'Favorites', 'Panoramas', 'Screenshots', 'Live', 'Recently Deleted', 'Hidden', 'My movies', 'Third Fourth']
>>> for i in photo_albums_list:
...     len(api.photos.albums[i])
... 
326
0
1
0
0
0
0
0
19
27
0
2
324

