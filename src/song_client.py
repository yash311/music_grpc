from __future__ import print_function

import random
import logging

import grpc
import song_pb2_grpc
import song_pb2
import song_resources




def getSongUtils(stub, songid):
    song = stub.GetSong(songid)
    
    if song.id == -1:
        print("Song Not found for the given ID\n")
    else:
        print("______Song Found______")
        print("Song ID: ", song.id)
        print("Song Name: ", song.title)
        print("Song Artist: ", song.artist)
        print("Song Album: ", song.album)
        print("_____________________________________")


def handleGet(stub):
    sid = int(input("Enter Song ID to get the song: "))
    getSongUtils(stub, song_pb2.SongID(id=sid))

def handlePost(stub):
    print("________ Enter song details to be added _________")
    sname = str(input("Song name: "))
    sartist = str(input("Song Artist: "))
    salbum = str(input("Song Album: "))
    
    song = stub.AddSong(song_pb2.SongData(id=1, title=sname, artist=sartist, album=salbum))

    if song:
        print("Song Added Succesfully")
    



def handlePut(stub):
    print("________ Enter song details to be updated _________")
    sid = int(input("Sonng ID: "))
    sname = str(input("Song name: "))
    sartist = str(input("Song Artist: "))
    salbum = str(input("Song Album: "))
    
    updatedSong = stub.UpdateSong(song_pb2.SongData(id=sid, title=sname, artist=sartist, album=salbum))

    print(updatedSong)


def handleDelete(stub):
    print("________ Enter song details to be deleted _________")
    sid = int(input("Sonng ID: "))

    deletedSong = stub.RemoveSong(song_pb2.SongID(id = sid))

    print(deletedSong)
    

def run():
    with grpc.insecure_channel('localhost:9099') as channel:
        stub = song_pb2_grpc.SongStub(channel)

        while True:
            in1 = str(input("********** 1:GET, 2:POST, 3:PUT, 4:DELETE, 5:EXIT **********\n"))

            if in1=="1":
                handleGet(stub)
            elif in1=="2":
                handlePost(stub)
            elif in1=="3":
                handlePut(stub)
            elif in1=="4":
                handleDelete(stub)
            elif in1=="5":
                break
            else:
                print("Invalid input")



        # print("-------------- GetFeature --------------")
        # guide_get_feature(stub)
        # print("-------------- ListFeatures --------------")
        # guide_list_features(stub)
        # print("-------------- RecordRoute --------------")
        # guide_record_route(stub)
        # print("-------------- RouteChat --------------")
        # guide_route_chat(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()