{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMCCfONPL04GiUtteFRWpSd"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "pip install requests"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "GVNk5tBeJhz9",
        "outputId": "7da438a1-584c-407f-c0c8-32c343c9d307"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (2.32.3)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests) (2025.1.31)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "import pandas as pd\n",
        "import os"
      ],
      "metadata": {
        "id": "E63v4H4YQ2AU"
      },
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "with open('KEY.dat','r') as archivo:\n",
        "  api_key =archivo.readline().strip()"
      ],
      "metadata": {
        "id": "xAhCwmJExWor"
      },
      "execution_count": 68,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 66,
      "metadata": {
        "id": "9M3Cex8sJH-J"
      },
      "outputs": [],
      "source": [
        "url = f'https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}&language=es-MX'\n",
        "response = requests.get(url)\n",
        "data = response.json()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Diccionario con los ids y generos de peliculas\n",
        "genres_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=es-MX'\n",
        "genres_response = requests.get(genres_url)\n",
        "genres_data = genres_response.json()\n",
        "print(genres_data)\n",
        "genres_dict = {genre['id']: genre['name'] for genre in genres_data['genres']}\n",
        "\n",
        "\n",
        "movies_list = []\n",
        "# Iterar sobre los resultados y almacenar los datos en la lista\n",
        "for movie in data['results']:\n",
        "        title = movie['title']\n",
        "        release_date = movie['release_date']\n",
        "        vote_average = movie['vote_average']\n",
        "        genre_ids = movie['genre_ids']\n",
        "        generos=  ', '.join([genres_dict.get(genre_id, 'Desconocido') for genre_id in genre_ids])\n",
        "\n",
        "        # Añadir los datos de la película como un diccionario a la lista\n",
        "        movies_list.append({\n",
        "            'Título': title,\n",
        "            'Fecha de estreno': release_date,\n",
        "            'Puntuación promedio': vote_average,\n",
        "            'Genero': generos\n",
        "        })\n",
        "\n",
        "# Crear un DataFrame de pandas con la lista de películas\n",
        "df = pd.DataFrame(movies_list).sort_values(by='Puntuación promedio', ascending=False)"
      ],
      "metadata": {
        "id": "Hr6kmAtqVLwK",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d3b7cdd8-c7fa-4279-8508-ac04c62cdf3d"
      },
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'genres': [{'id': 28, 'name': 'Acción'}, {'id': 12, 'name': 'Aventura'}, {'id': 16, 'name': 'Animación'}, {'id': 35, 'name': 'Comedia'}, {'id': 80, 'name': 'Crimen'}, {'id': 99, 'name': 'Documental'}, {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Familia'}, {'id': 14, 'name': 'Fantasía'}, {'id': 36, 'name': 'Historia'}, {'id': 27, 'name': 'Terror'}, {'id': 10402, 'name': 'Música'}, {'id': 9648, 'name': 'Misterio'}, {'id': 10749, 'name': 'Romance'}, {'id': 878, 'name': 'Ciencia ficción'}, {'id': 10770, 'name': 'Película de TV'}, {'id': 53, 'name': 'Suspense'}, {'id': 10752, 'name': 'Bélica'}, {'id': 37, 'name': 'Western'}]}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 677
        },
        "id": "7zyxwFVTQ_DS",
        "outputId": "06f622c7-9158-4f1e-be13-890c3bf117f8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                              Título Fecha de estreno  Puntuación promedio  \\\n",
              "18                              Flow       2024-08-29                8.300   \n",
              "13                           哪吒之魔童闹海       2025-01-29                7.900   \n",
              "11                    Aún estoy aquí       2024-09-19                7.900   \n",
              "9           Las aventuras de Dog Man       2025-01-24                7.859   \n",
              "0                  El abismo secreto       2025-02-13                7.830   \n",
              "1                Mufasa: El rey león       2024-12-18                7.449   \n",
              "8            Un completo desconocido       2024-12-18                7.300   \n",
              "2                      El brutalista       2024-12-20                7.100   \n",
              "15                      La sustancia       2024-09-07                7.100   \n",
              "5                              Anora       2024-10-14                7.100   \n",
              "10                          Cónclave       2024-10-25                7.094   \n",
              "3                 Compañera perfecta       2025-01-22                7.026   \n",
              "6                             Wicked       2024-11-20                6.900   \n",
              "14  Paddington: Aventura en la selva       2024-11-08                6.859   \n",
              "7                          Nosferatu       2024-12-25                6.700   \n",
              "12           Los chicos de la nickel       2024-12-13                6.407   \n",
              "16                           El mono       2025-02-12                6.300   \n",
              "4    Capitán América: Un nuevo mundo       2025-02-12                6.200   \n",
              "17                         Mickey 17       2025-02-28                6.000   \n",
              "19                Amenaza en el aire       2025-01-22                5.800   \n",
              "\n",
              "                                 Genero  \n",
              "18        Animación, Fantasía, Aventura  \n",
              "13        Animación, Fantasía, Aventura  \n",
              "11                      Drama, Historia  \n",
              "9   Familia, Animación, Comedia, Acción  \n",
              "0    Romance, Ciencia ficción, Suspense  \n",
              "1          Aventura, Familia, Animación  \n",
              "8                         Drama, Música  \n",
              "2                                 Drama  \n",
              "15              Terror, Ciencia ficción  \n",
              "5               Drama, Comedia, Romance  \n",
              "10            Drama, Misterio, Suspense  \n",
              "3             Ciencia ficción, Suspense  \n",
              "6              Drama, Romance, Fantasía  \n",
              "14           Familia, Aventura, Comedia  \n",
              "7                      Fantasía, Terror  \n",
              "12                                Drama  \n",
              "16                      Terror, Comedia  \n",
              "4     Acción, Suspense, Ciencia ficción  \n",
              "17      Ciencia ficción, Comedia, Drama  \n",
              "19             Acción, Suspense, Crimen  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c95365e3-59a7-4ee2-9fff-70ed84e72da7\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Título</th>\n",
              "      <th>Fecha de estreno</th>\n",
              "      <th>Puntuación promedio</th>\n",
              "      <th>Genero</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>Flow</td>\n",
              "      <td>2024-08-29</td>\n",
              "      <td>8.300</td>\n",
              "      <td>Animación, Fantasía, Aventura</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>哪吒之魔童闹海</td>\n",
              "      <td>2025-01-29</td>\n",
              "      <td>7.900</td>\n",
              "      <td>Animación, Fantasía, Aventura</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>Aún estoy aquí</td>\n",
              "      <td>2024-09-19</td>\n",
              "      <td>7.900</td>\n",
              "      <td>Drama, Historia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>Las aventuras de Dog Man</td>\n",
              "      <td>2025-01-24</td>\n",
              "      <td>7.859</td>\n",
              "      <td>Familia, Animación, Comedia, Acción</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>El abismo secreto</td>\n",
              "      <td>2025-02-13</td>\n",
              "      <td>7.830</td>\n",
              "      <td>Romance, Ciencia ficción, Suspense</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Mufasa: El rey león</td>\n",
              "      <td>2024-12-18</td>\n",
              "      <td>7.449</td>\n",
              "      <td>Aventura, Familia, Animación</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>Un completo desconocido</td>\n",
              "      <td>2024-12-18</td>\n",
              "      <td>7.300</td>\n",
              "      <td>Drama, Música</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>El brutalista</td>\n",
              "      <td>2024-12-20</td>\n",
              "      <td>7.100</td>\n",
              "      <td>Drama</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>La sustancia</td>\n",
              "      <td>2024-09-07</td>\n",
              "      <td>7.100</td>\n",
              "      <td>Terror, Ciencia ficción</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Anora</td>\n",
              "      <td>2024-10-14</td>\n",
              "      <td>7.100</td>\n",
              "      <td>Drama, Comedia, Romance</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>Cónclave</td>\n",
              "      <td>2024-10-25</td>\n",
              "      <td>7.094</td>\n",
              "      <td>Drama, Misterio, Suspense</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Compañera perfecta</td>\n",
              "      <td>2025-01-22</td>\n",
              "      <td>7.026</td>\n",
              "      <td>Ciencia ficción, Suspense</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Wicked</td>\n",
              "      <td>2024-11-20</td>\n",
              "      <td>6.900</td>\n",
              "      <td>Drama, Romance, Fantasía</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>Paddington: Aventura en la selva</td>\n",
              "      <td>2024-11-08</td>\n",
              "      <td>6.859</td>\n",
              "      <td>Familia, Aventura, Comedia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>Nosferatu</td>\n",
              "      <td>2024-12-25</td>\n",
              "      <td>6.700</td>\n",
              "      <td>Fantasía, Terror</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>Los chicos de la nickel</td>\n",
              "      <td>2024-12-13</td>\n",
              "      <td>6.407</td>\n",
              "      <td>Drama</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>El mono</td>\n",
              "      <td>2025-02-12</td>\n",
              "      <td>6.300</td>\n",
              "      <td>Terror, Comedia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Capitán América: Un nuevo mundo</td>\n",
              "      <td>2025-02-12</td>\n",
              "      <td>6.200</td>\n",
              "      <td>Acción, Suspense, Ciencia ficción</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>Mickey 17</td>\n",
              "      <td>2025-02-28</td>\n",
              "      <td>6.000</td>\n",
              "      <td>Ciencia ficción, Comedia, Drama</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>Amenaza en el aire</td>\n",
              "      <td>2025-01-22</td>\n",
              "      <td>5.800</td>\n",
              "      <td>Acción, Suspense, Crimen</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c95365e3-59a7-4ee2-9fff-70ed84e72da7')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-c95365e3-59a7-4ee2-9fff-70ed84e72da7 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-c95365e3-59a7-4ee2-9fff-70ed84e72da7');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-56c54ebc-df6e-4978-95b6-876ca7c07755\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-56c54ebc-df6e-4978-95b6-876ca7c07755')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-56c54ebc-df6e-4978-95b6-876ca7c07755 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_6626cafa-c63b-456c-b1df-ab2062ec10ee\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_6626cafa-c63b-456c-b1df-ab2062ec10ee button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 20,\n  \"fields\": [\n    {\n      \"column\": \"T\\u00edtulo\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 20,\n        \"samples\": [\n          \"Flow\",\n          \"Capit\\u00e1n Am\\u00e9rica: Un nuevo mundo\",\n          \"Los chicos de la nickel\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Fecha de estreno\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 17,\n        \"samples\": [\n          \"2024-08-29\",\n          \"2025-01-29\",\n          \"2024-12-18\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Puntuaci\\u00f3n promedio\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.6900135467777732,\n        \"min\": 5.8,\n        \"max\": 8.3,\n        \"num_unique_values\": 17,\n        \"samples\": [\n          8.3,\n          7.9,\n          7.3\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Genero\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 18,\n        \"samples\": [\n          \"Animaci\\u00f3n, Fantas\\u00eda, Aventura\",\n          \"Drama, Historia\",\n          \"Drama, Comedia, Romance\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    }
  ]
}