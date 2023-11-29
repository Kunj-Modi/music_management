from datetime import datetime, date


def fetch_singers(db):
    cursor = db.cursor()
    sql = "SELECT * FROM Singers"
    cursor.execute(sql)
    singers_data = cursor.fetchall()
    singers = []
    for singer in singers_data:
        singers.append(f'{singer[0]} {singer[1]}')
    return singers


def fetch_albums(db):
    cursor = db.cursor()
    sql = "SELECT * FROM Albums"
    cursor.execute(sql)
    albums_data = cursor.fetchall()
    albums = []
    for album in albums_data:
        albums.append(f'{album[0]} {album[1]}')
    return albums


def fetch_genres(db):
    cursor = db.cursor()
    sql = "SELECT * FROM Genres"
    cursor.execute(sql)
    genres_data = cursor.fetchall()
    genres = []
    for genre in genres_data:
        genres.append(f'{genre[0]} {genre[1]}')
    return genres_data


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
