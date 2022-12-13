# Use this file to test your repository functions 
import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


artist_1 = Artist('linkin park')
artist_2 = Artist("blink 182")
artist_3 = Artist("david guetta")
artist_4 = Artist("david guetta")
artist_5 = Artist("alan walker")
artist_repository.save(artist_1)
artist_repository.save(artist_2)
artist_repository.save(artist_3)
artist_repository.save(artist_4)
artist_repository.save(artist_5)

album_1 = Album('hybrid theory', 'rock', artist_1)
album_2 = Album('enemy of the stat', 'rock', artist_2)
album_3 = Album('nothing but the beat', 'dance', artist_3)
album_4 = Album('one love', 'dance', artist_4)
album_5 = Album('faded', 'dance', artist_5)
album_repository.save(album_1)
album_repository.save(album_2)
album_repository.save(album_3)
album_repository.save(album_4)
album_repository.save(album_5)

print(artist_repository.select(1).__dict__)
print(artist_repository.select(2).__dict__)
print(artist_repository.select(3).__dict__)
print(artist_repository.select(4).__dict__)
print(artist_repository.select(5).__dict__)

print(album_repository.list_albums_by_artist("david guetta"))

artist_repository.select_all()