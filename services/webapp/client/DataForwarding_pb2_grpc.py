# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import DataForwarding_pb2 as DataForwarding__pb2


class DataForwardingStub(object):
    """responce server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getStream = channel.unary_unary(
                '/DataForwarding/getStream',
                request_serializer=DataForwarding__pb2.RequestForward.SerializeToString,
                response_deserializer=DataForwarding__pb2.ReplyForward.FromString,
                )


class DataForwardingServicer(object):
    """responce server
    """

    def getStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataForwardingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getStream': grpc.unary_unary_rpc_method_handler(
                    servicer.getStream,
                    request_deserializer=DataForwarding__pb2.RequestForward.FromString,
                    response_serializer=DataForwarding__pb2.ReplyForward.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataForwarding', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataForwarding(object):
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
        return grpc.experimental.unary_unary(request, target, '/DataForwarding/getStream',
            DataForwarding__pb2.RequestForward.SerializeToString,
            DataForwarding__pb2.ReplyForward.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)