import spotipy
import spotipy.util as util
from diccionario import dicc
from diccionario import me_dicc
import pandas as pd
from scipy.spatial.distance import pdist, squareform


data_dicc = {}
sp = None

def initSP(client_id, client_secret, redirect_uri):
    global sp
    main_user = input('Introduce tu username:\n')
    username = str(main_user)
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri)

    sp = spotipy.Spotify(auth=token)
    return token,username

def funcion1():
    global sp
    for key,value in dicc.items():
        lista_datos = []
        playlists = sp.user_playlists(key)
        for playl in playlists['items']:
    
            if playl['owner']['display_name'] == key or value:
                #lista_datos.append(playl['owner']['display_name'])
                lista_datos.append(playl['id'])
                #lista_datos.append(playl['uri'])
                #lista_datos.append(playl['images'])
                #lista_datos.append(playl['name'])

        data_dicc[key] = {'id':lista_datos}
        #con el siguiente formato: {nombre : {id : id_playlist}}
        return data_dicc       
    
    return sp
    
def funcion2():
    friends_id_playlist = []
    for key , value in data_dicc.items():
        for id_pl in value['id']:
            friends_id_playlist.append((key,id_pl)) 
            #aquí accedemos a la ID de la playlist 

    return friends_id_playlist 
    #aquí está la variable NAME , ID_PLAYLIST

def funcion3(friends_id_playlist):
    x = [e[0] for e in friends_id_playlist]
    y = [e[1] for e in friends_id_playlist]
    dictio = {}

    def funcionamigos(useramigo, idplaylistamigo):
        global sp
        playlist_tracks = sp.user_playlist_tracks(useramigo,playlist_id=idplaylistamigo, limit= 10)    
        #print(playlist_tracks['items'][0]["track"]["name"])
        lista = []
        for i in playlist_tracks['items']: 
            #lista.append(i['track']['name'])
            lista.append(i["track"]["id"])
            
            #las siguientes variables son útiles para mejorar los resultados en caso de ser necesario
            
            #tracksid = playlist_tracks['items'][0]["track"]["id"]
            #tracksname = playlist_tracks['items'][0]["track"]["name"]
            #tracksartist = playlist_tracks['items'][0]["track"]['album']['artists'][0]['name']
            #identifier = (useramigo, tracksid, tracksartist, tracksname)
            #lista.append(tracksid)
        return lista
    
    for user in range(len(x)-1):
        if x[user] not in dictio:
            dictio[x[user]] = []
        l = funcionamigos(x[user], y[user])
        for songs in l:
            dictio[x[user]].append(songs)
    return dictio

def function4(dictio): 
    df = pd.DataFrame(list(dictio.items()))
    df.columns = ['users','canciones']
    songs = [song for row in df["canciones"] for song in row]
    
    for song in songs:
        df[song] = 0
    
    for song in songs:
        canciones_count = []
        for _, row in df.iterrows():
            canciones_count.append(row["canciones"].count(song))
        df[song] = canciones_count
    
    df = df.drop(columns=['canciones'])
    df = df.set_index('users')
    
    return df

def algoritmorecomendacion(df):
    matrix1 = pdist(df, 'euclidean')
    m_matrix = squareform(matrix1)

    matrix = pd.DataFrame(1/(1+m_matrix),index=df.index, columns=df.index)
    matrix.sort_values('users', ascending=True)
    return matrix

def amigoafin(username,matrix):
    listener = username #aquí deberíamos pasarle el [0] del diccionario de usuarios
    top_matrix = matrix[listener].sort_values(ascending=False)[1:]
    c_elem = top_matrix.head(1)
    amigo_afin = list(c_elem.index)
    return amigo_afin

def set_canciones(amigo_afin, dictio,listener):
    #esta primera parte se queda creada por si quisiéramos devolver una playlist basada en más de un amigo afín
    togetherplaylist = []
    for usuarioelegido in amigo_afin:
        togetherplaylist.append(dictio[usuarioelegido])
    togetherplaylist2 = [num for elem in togetherplaylist for num in elem]
    #en esta segunda parte creamos la playlist de canciones únicas si solo queremos la del más afín
    listanovedadesusuario = []
    for elem in togetherplaylist2:
        if elem not in dictio[listener]:
            listanovedadesusuario.append(elem)
    return listanovedadesusuario
