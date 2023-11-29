from datetime import datetime, date


def fetch_singers_query(db):
    cursor = db.cursor()
    sql = "SELECT * FROM Singers"
    cursor.execute(sql)
    singers_data = cursor.fetchall()
    singers = []
    for singer in singers_data:
        singers.append(f'{singer[0]} {singer[1]}')
    return singers


def fetch_albums_query(db):
    cursor = db.cursor()
    sql = "SELECT * FROM Albums"
    cursor.execute(sql)
    albums_data = cursor.fetchall()
    albums = []
    for album in albums_data:
        albums.append(f'{album[0]} {album[1]}')
    return albums


def fetch_genres_query(db):
    cursor = db.cursor()
    sql = "SELECT * FROM Genres"
    cursor.execute(sql)
    genres_data = cursor.fetchall()
    genres = []
    for genre in genres_data:
        genres.append(f'{genre[0]} {genre[1]}')
    return genres


def fetch_songs_query(db, using, name):
    cursor = db.cursor()
    if using == 'Song name':
        sql = f"SELECT song_id, song_name FROM Songs WHERE song_name LIKE '%{name.strip()}%'"
    else:
        if using == 'Singer':
            sql = f"""
                SELECT Songs.song_id, Songs.song_name
                FROM Singers 
                INNER JOIN Albums ON Singers.singer_id = Albums.singer_id 
                INNER JOIN Songs ON Albums.album_id = Songs.album_id 
                WHERE Singers.singer_name LIKE '%{name.strip()}%'
            """
        else:
            sql = f"""
                SELECT Songs.song_id, Songs.song_name
                FROM Songs
                INNER JOIN {using+'s'} ON Songs.album_id = {using+'s'}.{using.lower()}_id
                WHERE {using+'s'}.{using.lower()}_name LIKE '%{name.strip()}%'
            """
    cursor.execute(sql)
    songs_data = cursor.fetchall()
    songs = []
    for song in songs_data:
        songs.append(f'{song[0]} {song[1]}')
    return songs


def fetch_song_query(db, song_id):
    cursor = db.cursor()
    sql = f"""
            SELECT 
                Songs.song_name, 
                Songs.song_date, 
                Albums.album_name,
                Singers.singer_name, 
                Genres.genre_name,
                Albums.album_id,
                Genres.genre_id
            FROM Songs
            INNER JOIN Albums ON Songs.album_id = Albums.album_id
            INNER JOIN Singers ON Albums.singer_id = Singers.singer_id
            INNER JOIN Genres ON Songs.genre_id = Genres.genre_id
            WHERE Songs.song_id = {song_id}
        """
    cursor.execute(sql)
    song_data = cursor.fetchall()
    return song_data[0]


def edit_song_query(db, song_id, change: dict):
    cursor = db.cursor()

    sql = "UPDATE songs SET album_id = %s, genre_id = %s WHERE song_id = %s"

    values = (change['album_id'], change['genre_id'], song_id)

    cursor.execute(sql, values)

    db.commit()

    cursor.close()


def delete_song_query(db, song_id):
    cursor = db.cursor()

    sql = "DELETE FROM songs WHERE song_id = %s"

    values = (song_id,)

    cursor.execute(sql, values)

    db.commit()

    cursor.close()


def add_singer_query(db, name, gender):
    cursor = db.cursor()
    singer_data = (name, gender)
    sql = "INSERT INTO Singers (singer_name, gender) VALUES (%s, %s)"
    cursor.execute(sql, singer_data)
    db.commit()


def add_album_query(db, name, singer):
    cursor = db.cursor()
    current_year = datetime.now().year
    singer_data = (name, current_year, singer)
    sql = "INSERT INTO Albums (album_name, album_year, singer_id) VALUES (%s, %s, %s)"
    cursor.execute(sql, singer_data)
    db.commit()


def add_song_query(db, name, album, genre):
    cursor = db.cursor()
    current_date = date.today()
    song_data = (name, current_date, album, genre)
    sql = "INSERT INTO Songs (song_name, song_date, album_id, genre_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, song_data)
    db.commit()
