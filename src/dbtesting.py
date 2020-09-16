import json


def write():
    data = read()
    new_song = {
      "id": 1,
      "title": "str(name)",
      "artist": "str(artist)",
      "album": "str(album)"
      }
    
    data.append(new_song)
    with open("song_db.json", 'w') as song_db_file:
        json.dump(data, song_db_file)
        song_db_file.close()
    print("Added")


def read():

    feature_list = []
    with open("song_db.json", 'r') as song_db_file:
        for item in json.load(song_db_file):
            feature_list.append(item)
        print(feature_list)
        song_db_file.close()
    return feature_list



write()
write()
write()
read()
write()
read()