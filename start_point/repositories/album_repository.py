from db.run_sql import run_sql


from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository.select(result['user_id'])
        album = Album(result['description'], artist, result['duration'], result['completed'], result['id'])
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    result = run_sql(sql)

    for results in result:
        artist = artist_repository.select(results["id"])
        album = Album(results["title"], results["genre"], artist)
        albums.append(album)
    return albums

def delete_all():
    sql = "DELETE * FROM album"
    run_sql(sql)





