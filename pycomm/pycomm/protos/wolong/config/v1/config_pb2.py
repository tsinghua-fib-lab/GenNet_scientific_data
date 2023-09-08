
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dwolong/config/v1/config.proto\x12\x10wolong.config.v1"$\n\tMongoPath\x12\n\n\x02db\x18\x01 \x01(\t\x12\x0b\n\x03col\x18\x02 \x01(\t"\x1b\n\x0cOutputTarget\x12\x0b\n\x03sql\x18\x01 \x01(\tb\x06proto3')
_MONGOPATH = DESCRIPTOR.message_types_by_name['MongoPath']
_OUTPUTTARGET = DESCRIPTOR.message_types_by_name['OutputTarget']
MongoPath = _reflection.GeneratedProtocolMessageType('MongoPath', (_message.Message,), {'DESCRIPTOR': _MONGOPATH, '__module__': 'wolong.config.v1.config_pb2'})
_sym_db.RegisterMessage(MongoPath)
OutputTarget = _reflection.GeneratedProtocolMessageType('OutputTarget', (_message.Message,), {'DESCRIPTOR': _OUTPUTTARGET, '__module__': 'wolong.config.v1.config_pb2'})
_sym_db.RegisterMessage(OutputTarget)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _MONGOPATH._serialized_start = 51
    _MONGOPATH._serialized_end = 87
    _OUTPUTTARGET._serialized_start = 89
    _OUTPUTTARGET._serialized_end = 116
