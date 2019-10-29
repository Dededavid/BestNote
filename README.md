# **BestNote**

Este proyecto se basa en la simbiosis de dos conceptos: la capacidad de un algoritmo para encontrar personas afines a ti si le muestras los datos idóneos y la autoridad de un buen amigo para recomendarte canciones. Con esta idea nace BestNote, un programa creado para encontrar a tu amigo de Spotify con quien más música compartes y que sea él quien te enseñe canciones que desconocías.

![logo_BestNote](https://github.com/Dededavid/Friendlify/blob/master/code/logo_BestNote.png)


## **¿Cómo lo hace?**
BestNote utiliza el 'user' introducido de un usuario de Spotify como centro de la comparativa. Añadiendo el 'user' de tus amigos el programa recorre cada una de las playlist con 'owned' asociado al usuario en cuestión y extrae las canciones -todas aquellas playlist cuyo usuario y creador de la misma es idéntico-. En una matriz de relación (recommended system) relaciona las canciones guardadas y los usuarios añadidos y nos devuelve la afinidad existente entre ellos para crear una lista de títulos únicos. 

## **Paso a paso:**
Introducción usuario principal > añadir 'user ID' de los usuarios entre los que queremos encontrar al más afín > selección de playlist cuyo 'owner' y 'user' es el mismo > comparativa (mayor afinidad cuantas más canciones en común) > extracción de amigo afín > creación lista de canciones únicas que el usuario principal no tiene guardadas. 


## **Próximas implementaciones**
Trabajando sobre la incorporación de las siguientes características: 
- Una base de datos: que evitará tiempos largos de espera y la gestión mediante API de las playlist/canciones de cada usuario
- Implementación de funcionalidades: creación de playlists en la propia cuenta del usuario o filtro de creación de playlist basadas en la afinidad pero también añadiendo el componente del género musical.
- Creación de una interfaz: mayor accesibilidad. Facilita la introducción en el sistema de amigos.

-----------------------------------------------------------------------------------------------------------------------------

# **BestNote [English]**

This project is based on the symbiosis of two concepts: the ability of an algorithm to find people related to you if you show the right data and the authority of a good friend to recommend songs. BestNote was born with this idea: a program created to find your Spotify friend with whom you share the most music and let him teach you songs that you didn't know.


## **How it does?**
BestNote uses the 'user' introduced by a Spotify user as the center of the comparison. Adding the 'user' of your friends, the program runs through each of the playlists with 'owned' associated with the user in question and extracts the songs - all those playlists whose user and creator of the same is identical. In a relationship matrix (recommended system), it lists the saved songs and the added users and returns the affinity between them to create a list of unique titles.

## **Step by Step:**
Main user introduction> add 'user ID' of the users among whom we want to find the most similar> playlist selection whose 'owner' and 'user' is the same> comparative (greater affinity the more songs in common)> friend extraction related> creation list of unique songs that the main user does not have saved.


## ** Upcoming implementations**
Working on the incorporation of the following characteristics:
- A database: which will avoid long waiting times and management by API of the playlist / songs of each user
- Implementation of functionalities: creation of playlists in the user's own account or filter of creation of playlist based on affinity but also adding the component of the musical genre.
- Creation of an interface: greater accessibility. It facilitates the introduction into the friends system.
