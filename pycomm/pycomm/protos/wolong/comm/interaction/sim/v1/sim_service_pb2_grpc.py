
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ......wolong.comm.interaction.sim.v1 import sim_service_pb2 as wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2

class SimServiceStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Sim = channel.unary_unary('/wolong.comm.interaction.sim.v1.SimService/Sim', request_serializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.SimRequest.SerializeToString, response_deserializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.SimResponse.FromString)
        self.StartSim = channel.unary_unary('/wolong.comm.interaction.sim.v1.SimService/StartSim', request_serializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.StartSimRequest.SerializeToString, response_deserializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.StartSimResponse.FromString)
        self.GetJobStatus = channel.unary_unary('/wolong.comm.interaction.sim.v1.SimService/GetJobStatus', request_serializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.GetJobStatusRequest.SerializeToString, response_deserializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.GetJobStatusResponse.FromString)

class SimServiceServicer(object):
    'Missing associated documentation comment in .proto file.'

    def Sim(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartSim(self, request, context):
        '仅激活计算，不接收Response（用于前端）\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJobStatus(self, request, context):
        '用于前端，查询某个Job当前模拟进度（仅追踪通过StartSim异步启动的Job）\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SimServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Sim': grpc.unary_unary_rpc_method_handler(servicer.Sim, request_deserializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.SimRequest.FromString, response_serializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.SimResponse.SerializeToString), 'StartSim': grpc.unary_unary_rpc_method_handler(servicer.StartSim, request_deserializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.StartSimRequest.FromString, response_serializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.StartSimResponse.SerializeToString), 'GetJobStatus': grpc.unary_unary_rpc_method_handler(servicer.GetJobStatus, request_deserializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.GetJobStatusRequest.FromString, response_serializer=wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.GetJobStatusResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('wolong.comm.interaction.sim.v1.SimService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class SimService(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def Sim(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wolong.comm.interaction.sim.v1.SimService/Sim', wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.SimRequest.SerializeToString, wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.SimResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartSim(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wolong.comm.interaction.sim.v1.SimService/StartSim', wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.StartSimRequest.SerializeToString, wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.StartSimResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJobStatus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wolong.comm.interaction.sim.v1.SimService/GetJobStatus', wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.GetJobStatusRequest.SerializeToString, wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_sim__service__pb2.GetJobStatusResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
