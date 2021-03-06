# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import song_pb2 as song__pb2


class SongStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddSong = channel.unary_unary(
                '/musicGrpc.Song/AddSong',
                request_serializer=song__pb2.SongData.SerializeToString,
                response_deserializer=song__pb2.SongData.FromString,
                )
        self.UpdateSong = channel.unary_unary(
                '/musicGrpc.Song/UpdateSong',
                request_serializer=song__pb2.SongData.SerializeToString,
                response_deserializer=song__pb2.SongData.FromString,
                )
        self.GetSong = channel.unary_unary(
                '/musicGrpc.Song/GetSong',
                request_serializer=song__pb2.SongID.SerializeToString,
                response_deserializer=song__pb2.SongData.FromString,
                )
        self.RemoveSong = channel.unary_unary(
                '/musicGrpc.Song/RemoveSong',
                request_serializer=song__pb2.SongID.SerializeToString,
                response_deserializer=song__pb2.SongData.FromString,
                )


class SongServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddSong(self, request, context):
        """POST
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSong(self, request, context):
        """PUT
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSong(self, request, context):
        """GET
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveSong(self, request, context):
        """DELETE
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SongServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddSong': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSong,
                    request_deserializer=song__pb2.SongData.FromString,
                    response_serializer=song__pb2.SongData.SerializeToString,
            ),
            'UpdateSong': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSong,
                    request_deserializer=song__pb2.SongData.FromString,
                    response_serializer=song__pb2.SongData.SerializeToString,
            ),
            'GetSong': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSong,
                    request_deserializer=song__pb2.SongID.FromString,
                    response_serializer=song__pb2.SongData.SerializeToString,
            ),
            'RemoveSong': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveSong,
                    request_deserializer=song__pb2.SongID.FromString,
                    response_serializer=song__pb2.SongData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'musicGrpc.Song', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Song(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddSong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/musicGrpc.Song/AddSong',
            song__pb2.SongData.SerializeToString,
            song__pb2.SongData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/musicGrpc.Song/UpdateSong',
            song__pb2.SongData.SerializeToString,
            song__pb2.SongData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/musicGrpc.Song/GetSong',
            song__pb2.SongID.SerializeToString,
            song__pb2.SongData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveSong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/musicGrpc.Song/RemoveSong',
            song__pb2.SongID.SerializeToString,
            song__pb2.SongData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
