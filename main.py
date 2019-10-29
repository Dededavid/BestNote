# -*- coding: utf-8 -*-
import sys
import spotipy
import spotipy.util as util
import os
from dotenv import load_dotenv
from diccionario import me_dicc
import funciones as func
import pandas as pd

#cargando contraseñas de la API
load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")


#scope = 'playlist-read-private'
scope = 'playlist-modify-public'

#elegimos nuestro usuario
token, username = func.initSP (client_id,client_secret,redirect_uri)

#importando [nombre : user] de amigos
from diccionario import dicc
friends_dicc = dicc

#creando un diccionario con los datos de cada uno de los users
data_dicc = {}
if token:
    func.funcion1()
    
        

#consiguiendo las canciones de las playlists:
    canciones_playlist = func.funcion2()


else:
    print("Can't get token for ", username)

#obteniendo ID de cada cancion de cada playlist
func.funcion3(canciones_playlist)

#creando el dataframe
import pandas as pd
func.function4

#creando un algoritmo de recomendacion:
from scipy.spatial.distance import pdist, squareform
func.algoritmorecomendacion

#extrayendo el amigo más afin:
func.amigoafin

#creo un set de canciones del amigo más afín, evitando poner dos canciones repetidas en listas diferentes
func.set_canciones