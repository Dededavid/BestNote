import spotipy
import spotipy.util as util
from diccionario import friends_dicc
from diccionario import me_dicc
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from diccionario import dicc_nombres 


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

def playlistinfo():
    global sp
    for key,value in friends_dicc.items():
        lista_datos = []
        playlists = sp.user_playlists(value)
        for playl in playlists['items']:
    
            if playl['owner']['display_name'] == key or value:
                #lista_datos.append(playl['owner']['display_name'])
                lista_datos.append(playl['id'])
                #lista_datos.append(playl['uri'])
                #lista_datos.append(playl['images'])
                #lista_datos.append(playl['name'])

        data_dicc[key] = {'id':lista_datos}
    return data_dicc 
        #con el siguiente formato: {nombre : {id : id_playlist}}

    
def playlistId(data_dicc):
    friends_id_playlist = []
    for key , value in data_dicc.items():
        for id_pl in value['id']:
            #dicc_friends[id_pl[0]] = id_pl[1]
            #dicc_friends.update({id_pl[0]:id_pl[1]})
            friends_id_playlist.append((key,id_pl)) #aquí accedemos a la ID de la Plist 

    return friends_id_playlist #aquí está la variable NAME , ID_PLAYLIST

def funcionamigos(useramigo, idplaylistamigo):
        global sp
        playlist_tracks = sp.user_playlist_tracks(useramigo,playlist_id=idplaylistamigo, limit= 1)    
        #print(playlist_tracks['items'][0]["track"]["name"])
        lista = []
        for i in playlist_tracks['items']: 
            #lista.append(i['track']['name'])
            lista.append(i["track"]["id"])
            
            #rutas para encontrar otras features de las canciones
            
            #tracksid = playlist_tracks['items'][0]["track"]["id"]
            #tracksname = playlist_tracks['items'][0]["track"]["name"]
            #tracksartist = playlist_tracks['items'][0]["track"]['album']['artists'][0]['name']
            #identifier = (useramigo, tracksid, tracksartist, tracksname)
            #lista.append(tracksid)
        return lista

def playlistTracks(friends_id_playlist):
    x = [i[0] for i in friends_id_playlist]
    y = [e[1] for e in friends_id_playlist]
    dictio = {}
    for user in range(len(x)-1):
        if x[user] not in dictio:
            dictio[x[user]] = []
        l = funcionamigos(x[user], y[user])
        print(l)
        for songs in l:
            dictio[x[user]].append(songs)
    return dictio

def createMatrix(dictio): 
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
    listener = username
    top_matrix = matrix[listener].sort_values(ascending=False)[1:]
    c_elem = top_matrix.head(1)
    amigo_afin = list(c_elem.index)
    return amigo_afin

def cancionesdelafin(amigo_afin, dictio, listener):
    togetherplaylist = []
    for usuarioelegido in amigo_afin:
        togetherplaylist.append(dictio[usuarioelegido])
    togetherplaylist2 = [num for elem in togetherplaylist for num in elem]
        
    listanovedadesusuario = []
    for elem in togetherplaylist2:
        if elem not in dictio[listener]:
            listanovedadesusuario.append(elem)
    
    #eliminando nulos de la lista
    listanovedadesusuario = [x for x in listanovedadesusuario if x is not None]

    #ordenando por popularidad 
    topReco = listanovedadesusuario[:50]
    plTop = []
    for e in topReco: 
        x = sp.track(e)['popularity']
        plTop.append((e,x))

    plTop = sorted(plTop, key = lambda x: x[1])
    plTop = plTop[:10]

    lst_def = []
    for e in plTop: 
        x = sp.track(e[0])['name']
        lst_def.append(x)
    #return lst_def

    songs_str = ""

    for song in lst_def:
        songs_str += song
        songs_str += "\n"
        
    for key, value in dicc_nombres.items():
        if value == amigo_afin[0]:
            amigo_afin_nombre = key

    texto = "¡Hemos encontrado tu mejor amigo en Spotify!¡Saluda a {} ! Estas son las canciones que te recomendaría: \n {}".format(amigo_afin_nombre, songs_str)

    generated_txt = open('BestNote.txt', 'w+')
    generated_txt.write(texto)
    generated_txt.close()

    return texto
