import requests
import json
import sqlite3

key = '66ed6267'
movie = input('შეიყვანეთ ფილმი: ')

url = f'http://www.omdbapi.com/?t={movie}&apikey={key}'
resp = requests.get(url)
print(resp.headers)
print(resp.status_code)
content = resp.json()
print(json.dumps(content, indent=4))


print(f"Title: {content['Title']}")
print(f"Director: {content['Director']}")
print(f"Year: {content['Year']}")
print(f"Genre: {content['Genre']}")
print(f"Runtime: {content['Runtime']}")
print(f"Rating: {content['imdbRating']}")

conn = sqlite3.connect('movies.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title,
        year,
        genre,
        runtime,
        director,
        rating)
''')
c.execute('INSERT INTO movies (title, year, genre, runtime, director, rating) VALUES (?,?,?,?,?,?)', (content['Title'], content['Year'], content['Genre'], content['Runtime'], content['Director'], content['imdbRating']))
conn.commit()
conn.close()