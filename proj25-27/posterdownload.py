import requests
import json
import os
import time
import threading
movie_name = raw_input("Enter a movie name: ")

start_time = time.time()
r = requests.get(r'https://www.omdbapi.com/?s='+ movie_name +'&apikey=b4e17ea0')

if not os.path.exists(movie_name):
    os.mkdir(movie_name)

def download(movie):
    print movie['Title']
    poster_url = movie['Poster']
    if not poster_url == 'N/A':
        poster = requests.get(poster_url)
        file_name = movie_name + "/" + movie['imdbID'] + '.jpg'
        if poster.ok:
            with open(file_name, 'wb') as fh:
                fh.write(poster.content)


if r.ok:
    data = json.loads(r.text)
    for movie in data['Search']:
        t1 = threading.Thread(target=download, args = [movie])
        t1.start()
        #t1.join()

end_time = time.time()
print "Took: ", end_time - start_time