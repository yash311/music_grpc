from concurrent import futures
import time
import math
import logging

import grpc

import song_pb2
import song_pb2_grpc
import song_resources


def get_song(db, songid):
    for request in db:
        if request["id"] == songid:
            return request
    return None

class MySongServicer(song_pb2_grpc.SongServicer):
    # def __init__(self):
    #     self.db = song_resources.read_song_database()

    '''POST Method Implementation'''
    def AddSong(self, request, context):
        title = str(request.title)
        artist = str(request.artist)
        album = str(request.album)
        print("POST request served")

        if title is None:
            print("Title is not provided")
        if artist is None:
            print("Artist is not provided")        
        if album is None:
            print("Album is not provided")
       
        song_resources.add_song_database(title, artist, album)

        print("Data added successfully")
        return song_pb2.SongData(
                id = request.id,
                title = request.title,
                artist = request.artist,
                album = request.album
            )
    
    '''GET Method Implementation'''
    def GetSong(self, request, context):
        db = song_resources.read_song_database()
        request = get_song(db, request.id)
        print("GET request served")
        if request is None:
            return song_pb2.SongData(
                id = -1,
                title = None,
                artist = None,
                album = None
            )
        else:
            return song_pb2.SongData(
                id = request["id"],
                title = request["title"],
                artist = request["artist"],
                album = request["album"]
            )
    
    '''PUT Method Implementation'''
    def UpdateSong(self, request, context):
        res = song_resources.update_song_database(request)
        print("PUT request served")
        if res is 0:
            return song_pb2.SongData(
                id = -1,
                title = "None",
                artist = "None",
                album = "None"
            )
        else:
           return song_pb2.SongData(
                id = request.id,
                title = request.title,
                artist = request.artist,
                album = request.album
            )
    

    '''DELETE Method Implementation'''
    def RemoveSong(self, request, context):
        res = song_resources.delete_song_database(request)
        print("DELETE request served")
        if res == "-1":
            return song_pb2.SongData(
                id = -1,
                title = "Song not found",
                artist = None,
                album = None
            )
        else:
            return song_pb2.SongData(
                id = -1,
                title = "Song deleted successfully",
                artist = None,
                album = None
            )



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    song_pb2_grpc.add_SongServicer_to_server(
        MySongServicer(), server)
    server.add_insecure_port('[::]:9099')
    server.start()
    print("Server started on http://localhost:9099")
    server.wait_for_termination()




if __name__ == '__main__':
    logging.basicConfig()
    serve()
