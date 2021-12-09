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

# example: localhost:5000/user/3
@app.get('/artist/<int:id>')
def get_artist_by_id(id):
  # get select and filter with 'id' parameter
  artists = get('SELECT * FROM artists WHERE id = :id', { 'id': id })

  # get() always returns a list, 
  # even if there's only 1 row
  return jsonify(dict(artists[0]))


if __name__ == '__main__':
  app.run(debug=True)