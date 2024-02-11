def make_album(artist_name,album_name, songs_number = None):
    album_data = {"Artist" : artist_name,
                  "Album" : album_name,
                 }
    if songs_number != None:
        album_data["Songs number"] = songs_number 
        for key,value  in album_data.items():
            print(f"{key}: {value}")
    else:
         for key,value  in album_data.items():
            print(f"{key}: {value}")

flag = True

while flag:
    print("Enter the artist, the album name and, not mandatory, the number of songs in the album (or type 'quit' to exit)")
    #Input and exit logic
    artist = input("Artist's name: ")
    if artist.lower() == "quit":
        break
    else:
        pass
    album = input("Album name : ")
    if album.lower() == "quit":
        break
    else:
        pass
    songs = input("Song's number: ")
    if songs.lower() == "quit":
        break
    else:
        pass

    make_album(artist,album,songs)
