
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....wolong.sync.v1 import sync_service_pb2 as wolong_dot_sync_dot_v1_dot_sync__service__pb2

class SyncServiceStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Step = channel.unary_unary('/wolong.sync.v1.SyncService/Step', request_serializer=wolong_dot_sync_dot_v1_dot_sync__service__pb2.StepRequest.SerializeToString, response_deserializer=wolong_dot_sync_dot_v1_dot_sync__service__pb2.StepResponse.FromString)

class SyncServiceServicer(object):
    'Missing associated documentation comment in .proto file.'

    def Step(self, request, context):
        '步进\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SyncServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Step': grpc.unary_unary_rpc_method_handler(servicer.Step, request_deserializer=wolong_dot_sync_dot_v1_dot_sync__service__pb2.StepRequest.FromString, response_serializer=wolong_dot_sync_dot_v1_dot_sync__service__pb2.StepResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('wolong.sync.v1.SyncService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class SyncService(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def Step(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wolong.sync.v1.SyncService/Step', wolong_dot_sync_dot_v1_dot_sync__service__pb2.StepRequest.SerializeToString, wolong_dot_sync_dot_v1_dot_sync__service__pb2.StepResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
