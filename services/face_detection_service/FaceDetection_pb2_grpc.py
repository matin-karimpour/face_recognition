# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import FaceDetection_pb2 as FaceDetection__pb2


class FaceDetectionStub(object):
    """responce server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getStream = channel.unary_unary(
                '/FaceDetection/getStream',
                request_serializer=FaceDetection__pb2.RequestData.SerializeToString,
                response_deserializer=FaceDetection__pb2.ReplyData.FromString,
                )


class FaceDetectionServicer(object):
    """responce server
    """

    def getStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FaceDetectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getStream': grpc.unary_unary_rpc_method_handler(
                    servicer.getStream,
                    request_deserializer=FaceDetection__pb2.RequestData.FromString,
                    response_serializer=FaceDetection__pb2.ReplyData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FaceDetection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FaceDetection(object):
    """responce server
    """

    @staticmethod
    def getStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FaceDetection/getStream',
            FaceDetection__pb2.RequestData.SerializeToString,
            FaceDetection__pb2.ReplyData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)