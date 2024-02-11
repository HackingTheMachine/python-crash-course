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

make_album("Guns n Roses", "Use Your Illusion I")
make_album("Linkin Park", "Meteora", 13)
