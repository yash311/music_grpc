
import json

import song_pb2


def read_song_database():
    feature_list = []
    with open("song_db.json", 'r') as song_db_file:
        for item in json.load(song_db_file)["data"]:
            feature = {
                "id": int(item["id"]),
                "title": str(item["title"]),
                "artist": str(item["artist"]),
                "album": str(item["album"])
            }
            feature_list.append(feature)
    return feature_list


def add_song_database(name, artist, album):
    data = read_song_database()
    new_song = {
        "id": int(len(data)+1),
        "title": str(name),
        "artist": str(artist),
        "album": str(album)
    }

    data = []
    with open("song_db.json", 'r') as song_db_file:
      data = json.load(song_db_file)["data"]
      data.append(new_song)
      song_db_file.close()

    # print("*********************************************")
    # print(data)
    new_data = {}
    new_data["data"] = data
    with open("song_db.json", 'w') as song_db_file:
        json.dump(new_data, song_db_file)


def update_song_database(song):
    data = read_song_database()
    isPresent = False
    # print("data fetched")
    index = 0
    # print("Len: ", len(data))
    for s in data:
        if s["id"] == song.id:
            isPresent = True
            break
        index+=1

    if not isPresent:
        return 0
    else:
        data[index] = {
            "id": data[index]["id"],
            "title": song.title,
            "artist": song.artist,
            "album": song.album
        }

        new_data = {}
        new_data["data"] = data
        with open("song_db.json", 'w') as song_db_file:
            json.dump(new_data, song_db_file)
        return 1


def delete_song_database(song):
    data = read_song_database()
    new_data = []
    isPresent = False
    for request in data:
        if request["id"] is song.id:
            isPresent = True
            continue
        else:
            new_data.append(request)

    if isPresent:
        with open("song_db.json", 'w') as song_db_file:
            json.dump({"data":new_data}, song_db_file)
        return 1
    else:
        return 0
