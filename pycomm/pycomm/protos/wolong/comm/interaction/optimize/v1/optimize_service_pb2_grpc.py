
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ......wolong.comm.interaction.optimize.v1 import optimize_service_pb2 as wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2

class OptimizeServiceStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.OptimizeStatus = channel.unary_unary('/wolong.comm.interaction.optimize.v1.OptimizeService/OptimizeStatus', request_serializer=wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeStatusRequest.SerializeToString, response_deserializer=wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeStatusResponse.FromString)
        self.OptimizeParameter = channel.unary_unary('/wolong.comm.interaction.optimize.v1.OptimizeService/OptimizeParameter', request_serializer=wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeParameterRequest.SerializeToString, response_deserializer=wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeParameterResponse.FromString)

class OptimizeServiceServicer(object):
    'Missing associated documentation comment in .proto file.'

    def OptimizeStatus(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OptimizeParameter(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_OptimizeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'OptimizeStatus': grpc.unary_unary_rpc_method_handler(servicer.OptimizeStatus, request_deserializer=wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeStatusRequest.FromString, response_serializer=wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeStatusResponse.SerializeToString), 'OptimizeParameter': grpc.unary_unary_rpc_method_handler(servicer.OptimizeParameter, request_deserializer=wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeParameterRequest.FromString, response_serializer=wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeParameterResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('wolong.comm.interaction.optimize.v1.OptimizeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class OptimizeService(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def OptimizeStatus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wolong.comm.interaction.optimize.v1.OptimizeService/OptimizeStatus', wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeStatusRequest.SerializeToString, wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeStatusResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OptimizeParameter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wolong.comm.interaction.optimize.v1.OptimizeService/OptimizeParameter', wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeParameterRequest.SerializeToString, wolong_dot_comm_dot_interaction_dot_optimize_dot_v1_dot_optimize__service__pb2.OptimizeParameterResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
