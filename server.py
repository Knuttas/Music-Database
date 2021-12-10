from flask import Flask, jsonify, render_template, redirect, request
from flask.wrappers import Request
from database import run, get

app = Flask(__name__)

@app.get('/')
def index():
  return render_template('index.html')


@app.get('/artists')
def get_artists():
  artists = get('SELECT name FROM artists')
  artists = [dict(artist) for artist in artists]
  return jsonify(artists)

@app.get('/oldest-album')
def get_oldest_album():
  oldest = get('SELECT title, MIN(year_released) FROM albums')
  oldest = [dict(oldest) for oldest in oldest]
  return jsonify(oldest)

@app.get('/longest-playtime')
def get_longest_playtime():
  longest = get('SELECT albums.title, SUM(songs.duration) FROM songs JOIN albums on songs.album_id = albums.id JOIN artists ON albums.artist_id = artists.id GROUP BY songs.album_id ORDER BY sum(songs.duration) DESC limit 1')
  longest = [dict(longest) for longest in longest]
  return jsonify(longest)

@app.get('/update-year')
def update_year():
  return render_template('update-year.html')

@app.post('/select-year')
def select_year():
  year = dict(request.form)
  year = year['year']
  run('UPDATE albums SET year_released = ' + year + ' WHERE title = "Blood Mountain"')
  return redirect('/')

@app.get('/add-artist')
def add_artist():
  return render_template('add-artist.html')

@app.post('/submit-artist')
def submit_artist():
  artist = dict(request.form)
  artist_name = artist['name']
  artist_description = artist['description']
  run(f'INSERT INTO artists VALUES (NULL, "{artist_name}", "{artist_description}")')
  return redirect('/')

@app.get('/remove-artist')
def remove_artist():
  return render_template('remove-artist.html')

@app.post('/submit-artist-remove')
def submit_artist_remove():
  remove = dict(request.form)
  remove = remove['name']
  run(f'DELETE FROM artists WHERE artists.name = "{remove}"')
  return redirect('/')

@app.get('/add-album')
def add_album():
  return render_template('add-album.html')

@app.post('/submit-album')
def submit_album():
  album = dict(request.form)
  album_artist = album['artist']
  album_title = album['title']
  album_description = album['description']
  album_release = album['release']
  existing_artists = get(f'SELECT name, id FROM artists WHERE artists.name = "{album_artist}"')
  if (existing_artists):
    existing_artists = [dict(existing_artists) for existing_artists in existing_artists]
    jsonify(existing_artists)
    existing_artists_id = existing_artists[0]['id']
    run(f'INSERT INTO albums VALUES (NULL, "{album_title}", "{album_description}", {album_release}, {existing_artists_id})')
    return redirect('/')
  else:
    return render_template('/error-artist.html')

@app.get('/remove-album')
def remove_album():
  return render_template('remove-album.html')

@app.post('/submit-album-remove')
def submit_album_remove():
  remove = dict(request.form)
  remove = remove['name']
  run(f'DELETE FROM albums WHERE albums.title = "{remove}"')
  return redirect('/')

@app.get('/add-song')
def add_song():
  return render_template('add-song.html')

@app.post('/submit-song')
def submit_song():
  song = dict(request.form)
  song_album = song['album']
  song_title = song['title']
  song_duration = song['duration']
  existing_album = get(f'SELECT title, id FROM albums WHERE albums.title = "{song_album}"')
  if (existing_album):
    existing_album = [dict(existing_album) for existing_album in existing_album]
    jsonify(existing_album)
    existing_album_id = existing_album[0]['id']
    run(f'INSERT INTO songs VALUES (NULL, "{song_title}", {song_duration}, {existing_album_id})')
    return redirect('/')
  else:
    return render_template('/error-album.html')

@app.get('/remove-song')
def remove_song():
  return render_template('remove-song.html')

@app.post('/submit-song-remove')
def submit_song_remove():
  remove = dict(request.form)
  remove = remove['name']
  run(f'DELETE FROM songs WHERE songs.name = "{remove}"')
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)