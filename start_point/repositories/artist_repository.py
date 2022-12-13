from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING * "
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    value = [id]
    results = run_sql(sql, value)

    if len(results) > 0:
        result = results[0]
        artist = Artist(result["name"], result["id"])
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for result in results:
        artist = Artist(result["name"], result["id"])
        artists.append(artist)
    return artists

def delete_all():
    sql = "DELETE * FROM artist"
    run_sql(sql)
