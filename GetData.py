import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

#with open('KEY.dat','r') as archivo:
#  api_key =archivo.readline().strip()

url = f'https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}&language=es-MX'
response = requests.get(url)
data = response.json()

#Diccionario con los ids y generos de peliculas
genres_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=es-MX'
genres_response = requests.get(genres_url)
genres_data = genres_response.json()
print(genres_data)
genres_dict = {genre['id']: genre['name'] for genre in genres_data['genres']}


movies_list = []
# Iterar sobre los resultados y almacenar los datos en la lista
for movie in data['results']:
        title = movie['title']
        release_date = movie['release_date']
        vote_average = movie['vote_average']
        genre_ids = movie['genre_ids']
        generos=  ', '.join([genres_dict.get(genre_id, 'Desconocido') for genre_id in genre_ids])

        # Añadir los datos de la película como un diccionario a la lista
        movies_list.append({
            'Título': title,
            'Fecha de estreno': release_date,
            'Puntuación promedio': vote_average,
            'Genero': generos
        })

# Crear un DataFrame de pandas con la lista de películas
df = pd.DataFrame(movies_list).sort_values(by='Puntuación promedio', ascending=False)
df
