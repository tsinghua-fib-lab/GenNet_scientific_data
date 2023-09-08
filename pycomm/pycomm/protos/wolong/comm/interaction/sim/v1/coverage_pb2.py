
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-wolong/comm/interaction/sim/v1/coverage.proto\x12\x1ewolong.comm.interaction.sim.v1"^\n\x0eCoverageAction\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06bs_azi\x18\x02 \x01(\x01\x12\x0f\n\x07bs_tilt\x18\x03 \x01(\x01\x12\x0e\n\x06bw_azi\x18\x04 \x01(\x01\x12\x0f\n\x07bw_tilt\x18\x05 \x01(\x01"5\n\x0eCoverageReward\x12\x10\n\x08coverage\x18\x01 \x01(\x08\x12\x11\n\tmean_rate\x18\x02 \x01(\x01"B\n\x07BsState\x12\x0f\n\x07signals\x18\x01 \x03(\x01\x12\x13\n\x0buser_number\x18\x02 \x01(\x05\x12\x11\n\tis_indoor\x18\x03 \x01(\x08"\x8e\x01\n\x08GridInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x126\n\x05state\x18\x02 \x01(\x0b2\'.wolong.comm.interaction.sim.v1.BsState\x12>\n\x06reward\x18\x03 \x01(\x0b2..wolong.comm.interaction.sim.v1.CoverageRewardb\x06proto3')
_COVERAGEACTION = DESCRIPTOR.message_types_by_name['CoverageAction']
_COVERAGEREWARD = DESCRIPTOR.message_types_by_name['CoverageReward']
_BSSTATE = DESCRIPTOR.message_types_by_name['BsState']
_GRIDINFO = DESCRIPTOR.message_types_by_name['GridInfo']
CoverageAction = _reflection.GeneratedProtocolMessageType('CoverageAction', (_message.Message,), {'DESCRIPTOR': _COVERAGEACTION, '__module__': 'wolong.comm.interaction.sim.v1.coverage_pb2'})
_sym_db.RegisterMessage(CoverageAction)
CoverageReward = _reflection.GeneratedProtocolMessageType('CoverageReward', (_message.Message,), {'DESCRIPTOR': _COVERAGEREWARD, '__module__': 'wolong.comm.interaction.sim.v1.coverage_pb2'})
_sym_db.RegisterMessage(CoverageReward)
BsState = _reflection.GeneratedProtocolMessageType('BsState', (_message.Message,), {'DESCRIPTOR': _BSSTATE, '__module__': 'wolong.comm.interaction.sim.v1.coverage_pb2'})
_sym_db.RegisterMessage(BsState)
GridInfo = _reflection.GeneratedProtocolMessageType('GridInfo', (_message.Message,), {'DESCRIPTOR': _GRIDINFO, '__module__': 'wolong.comm.interaction.sim.v1.coverage_pb2'})
_sym_db.RegisterMessage(GridInfo)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _COVERAGEACTION._serialized_start = 81
    _COVERAGEACTION._serialized_end = 175
    _COVERAGEREWARD._serialized_start = 177
    _COVERAGEREWARD._serialized_end = 230
    _BSSTATE._serialized_start = 232
    _BSSTATE._serialized_end = 298
    _GRIDINFO._serialized_start = 301
    _GRIDINFO._serialized_end = 443
