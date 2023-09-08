
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!wolong/sync/v1/sync_service.proto\x12\x0ewolong.sync.v1")\n\x0bStepRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04step\x18\x02 \x01(\x05"\x1d\n\x0cStepResponse\x12\r\n\x05close\x18\x01 \x01(\x082P\n\x0bSyncService\x12A\n\x04Step\x12\x1b.wolong.sync.v1.StepRequest\x1a\x1c.wolong.sync.v1.StepResponseb\x06proto3')
_STEPREQUEST = DESCRIPTOR.message_types_by_name['StepRequest']
_STEPRESPONSE = DESCRIPTOR.message_types_by_name['StepResponse']
StepRequest = _reflection.GeneratedProtocolMessageType('StepRequest', (_message.Message,), {'DESCRIPTOR': _STEPREQUEST, '__module__': 'wolong.sync.v1.sync_service_pb2'})
_sym_db.RegisterMessage(StepRequest)
StepResponse = _reflection.GeneratedProtocolMessageType('StepResponse', (_message.Message,), {'DESCRIPTOR': _STEPRESPONSE, '__module__': 'wolong.sync.v1.sync_service_pb2'})
_sym_db.RegisterMessage(StepResponse)
_SYNCSERVICE = DESCRIPTOR.services_by_name['SyncService']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _STEPREQUEST._serialized_start = 53
    _STEPREQUEST._serialized_end = 94
    _STEPRESPONSE._serialized_start = 96
    _STEPRESPONSE._serialized_end = 125
    _SYNCSERVICE._serialized_start = 127
    _SYNCSERVICE._serialized_end = 207
