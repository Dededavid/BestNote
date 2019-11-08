# -*- coding: utf-8 -*-
import sys
import spotipy
import spotipy.util as util
import os
from dotenv import load_dotenv
from diccionario import me_dicc
import funciones as func
from diccionario import friends_dicc
import pandas as pd
from scipy.spatial.distance import pdist, squareform

#cargando contraseñas de la API
load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")

#scope = 'playlist-read-private'
scope = 'playlist-modify-public'

#elegimos nuestro usuario
token, username = func.initSP (client_id,client_secret,redirect_uri)


#creando un diccionario con los datos de cada uno de los users
data_dicc = {}
if token:
    data_dicc = func.playlistinfo()
   
        
#extrayendo ID de las playlists:
    canciones_playlist = func.playlistId(data_dicc)

#extraemos las tracks de playlist
    dictio = func.playlistTracks(canciones_playlist)

#creando el dataframe
    df = func.createMatrix(dictio)

#aplicando el algoritmo de recomendación:
    matrix = func.algoritmorecomendacion(df)

#extrayendo el amigo más afin a User:
    amigoafin = func.amigoafin(username, matrix)

#devuelvo una lista de canciones recomendadas del amigo afin ordenadas por popularidad
    listafinal = func.cancionesdelafin(amigoafin, dictio, username)
    print(listafinal)
else:
    print("Can't get token for ", username)


