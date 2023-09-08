from __future__ import print_function
from typing import Dict, List
from multiprocessing import Pool
import grpc
import time
from .protos.wolong.sync.v1 import (
    sync_service_pb2 as pb,
    sync_service_pb2_grpc as grpc_pb,
)


class SyncClient(object):
    def __init__(self, listen_address):
        optimize_channel = grpc.aio.insecure_channel(listen_address)
        self._optimize_stub = grpc_pb.SyncServiceStub(optimize_channel)

    def Step(self, step):
        async def _async_parser(response):
            return await response

        req = pb.StepRequest(step=step)
        res = self._optimize_stub.Step(req)
        return _async_parser(res)





