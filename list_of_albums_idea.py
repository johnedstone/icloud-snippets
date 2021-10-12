>>> photo_albums_list = [i for i in iter(api.photos.albums.keys())]
>>> photo_albums_list
['All Photos', 'Time-lapse', 'Videos', 'Slo-mo', 'Bursts', 'Favorites', 'Panoramas', 'Screenshots', 'Live', 'Recently Deleted', 'Hidden', 'My movies', 'Third Fourth']
>> for i in photo_albums_list:
...     print(i, ": ", len(api.photos.albums[i]))
... 
All Photos :  326
Time-lapse :  0
Videos :  1
Slo-mo :  0
Bursts :  0
Favorites :  0
Panoramas :  0
Screenshots :  0
Live :  19
Recently Deleted :  27
Hidden :  0
My movies :  2
Third Fourth :  324

>>> album_exclude = ['Time-lapse', 'Favorites']
>>> for i in photo_albums_list:
...     if i not in album_exclude:
...         print("{}: {}".format(i, len(api.photos.albums[i])))
...
All Photos: 326
Videos: 1
Slo-mo: 0
Bursts: 0
Panoramas: 0
Screenshots: 0
Live: 19
Recently Deleted: 27
Hidden: 0
My movies: 2
Third Fourth: 324

