
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....wolong.config.v1 import config_pb2 as wolong_dot_config_dot_v1_dot_config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!wolong/comm/input/v1/config.proto\x12\x14wolong.comm.input.v1\x1a\x1dwolong/config/v1/config.proto"\x14\n\x03Log\x12\r\n\x05level\x18\x01 \x01(\t"\x99\x02\n\x05Mongo\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12(\n\x03map\x18\x02 \x01(\x0b2\x1b.wolong.config.v1.MongoPath\x123\n\tcomm_topo\x18\x03 \x01(\x0b2\x1b.wolong.config.v1.MongoPathH\x00\x88\x01\x01\x125\n\x0bcomm_demand\x18\x04 \x01(\x0b2\x1b.wolong.config.v1.MongoPathH\x01\x88\x01\x01\x12:\n\x10ray_tracing_loss\x18\x05 \x01(\x0b2\x1b.wolong.config.v1.MongoPathH\x02\x88\x01\x01B\x0c\n\n_comm_topoB\x0e\n\x0c_comm_demandB\x13\n\x11_ray_tracing_loss"=\n\x0bControlStep\x12\r\n\x05start\x18\x01 \x01(\x05\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x10\n\x08interval\x18\x03 \x01(\x01"\x1f\n\rControlThread\x12\x0e\n\x06worker\x18\x01 \x01(\x05"i\n\rControlOutput\x12\x15\n\rmin_longitude\x18\x01 \x01(\x01\x12\x14\n\x0cmin_latitude\x18\x02 \x01(\x01\x12\x15\n\rmax_longitude\x18\x03 \x01(\x01\x12\x14\n\x0cmax_latitude\x18\x04 \x01(\x01"\x96\x04\n\x07Control\x12/\n\x04step\x18\x01 \x01(\x0b2!.wolong.comm.input.v1.ControlStep\x123\n\x06thread\x18\x02 \x01(\x0b2#.wolong.comm.input.v1.ControlThread\x12>\n\x11microscopic_range\x18\x03 \x01(\x0b2#.wolong.comm.input.v1.ControlOutput\x12>\n\x11macroscopic_range\x18\x04 \x01(\x0b2#.wolong.comm.input.v1.ControlOutput\x12\x19\n\x11enable_controlled\x18\n \x01(\x08\x12\x17\n\x0fenable_optimize\x18\x05 \x01(\x08\x12\x1e\n\x11optimize_interval\x18\x06 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\x0edisplay_guomao\x18\x07 \x01(\x08\x12\x16\n\x0ecoverage_range\x18\x08 \x01(\x01\x12\x19\n\x11handover_interval\x18\t \x01(\x05\x127\n\x0cchannel_type\x18\x0b \x01(\x0e2!.wolong.comm.input.v1.ChannelType\x127\n\x0cantenna_type\x18\x0c \x01(\x0e2!.wolong.comm.input.v1.AntennaTypeB\x14\n\x12_optimize_interval"a\n\x0cOutputSwitch\x12\x0e\n\x06person\x18\x01 \x01(\x08\x12\x14\n\x0cbase_station\x18\x02 \x01(\x08\x12\x0b\n\x03aoi\x18\x03 \x01(\x08\x12\x0f\n\x07heatmap\x18\x04 \x01(\x08\x12\r\n\x05stats\x18\x05 \x01(\x08"l\n\x06Output\x12.\n\x06target\x18\x01 \x01(\x0b2\x1e.wolong.config.v1.OutputTarget\x122\n\x06switch\x18\x02 \x01(\x0b2".wolong.comm.input.v1.OutputSwitch"\xba\x01\n\x06Config\x12&\n\x03log\x18\x01 \x01(\x0b2\x19.wolong.comm.input.v1.Log\x12*\n\x05mongo\x18\x02 \x01(\x0b2\x1b.wolong.comm.input.v1.Mongo\x12.\n\x07control\x18\x03 \x01(\x0b2\x1d.wolong.comm.input.v1.Control\x12,\n\x06output\x18\x04 \x01(\x0b2\x1c.wolong.comm.input.v1.Output*\xad\x01\n\x0bChannelType\x12\x1c\n\x18CHANNEL_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15CHANNEL_TYPE_EQUATION\x10\x01\x12\x1c\n\x18CHANNEL_TYPE_RAY_TRACING\x10\x02\x12\x15\n\x11CHANNEL_TYPE_3GPP\x10\x03\x12\x1a\n\x16CHANNEL_TYPE_FREESPACE\x10\x04\x12\x14\n\x10CHANNEL_TYPE_CEM\x10\x05*Y\n\x0bAntennaType\x12\x1c\n\x18ANTENNA_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11ANTENNA_TYPE_SISO\x10\x01\x12\x15\n\x11ANTENNA_TYPE_MIMO\x10\x02b\x06proto3')
_CHANNELTYPE = DESCRIPTOR.enum_types_by_name['ChannelType']
ChannelType = enum_type_wrapper.EnumTypeWrapper(_CHANNELTYPE)
_ANTENNATYPE = DESCRIPTOR.enum_types_by_name['AntennaType']
AntennaType = enum_type_wrapper.EnumTypeWrapper(_ANTENNATYPE)
CHANNEL_TYPE_UNSPECIFIED = 0
CHANNEL_TYPE_EQUATION = 1
CHANNEL_TYPE_RAY_TRACING = 2
CHANNEL_TYPE_3GPP = 3
CHANNEL_TYPE_FREESPACE = 4
CHANNEL_TYPE_CEM = 5
ANTENNA_TYPE_UNSPECIFIED = 0
ANTENNA_TYPE_SISO = 1
ANTENNA_TYPE_MIMO = 2
_LOG = DESCRIPTOR.message_types_by_name['Log']
_MONGO = DESCRIPTOR.message_types_by_name['Mongo']
_CONTROLSTEP = DESCRIPTOR.message_types_by_name['ControlStep']
_CONTROLTHREAD = DESCRIPTOR.message_types_by_name['ControlThread']
_CONTROLOUTPUT = DESCRIPTOR.message_types_by_name['ControlOutput']
_CONTROL = DESCRIPTOR.message_types_by_name['Control']
_OUTPUTSWITCH = DESCRIPTOR.message_types_by_name['OutputSwitch']
_OUTPUT = DESCRIPTOR.message_types_by_name['Output']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), {'DESCRIPTOR': _LOG, '__module__': 'wolong.comm.input.v1.config_pb2'})
_sym_db.RegisterMessage(Log)
Mongo = _reflection.GeneratedProtocolMessageType('Mongo', (_message.Message,), {'DESCRIPTOR': _MONGO, '__module__': 'wolong.comm.input.v1.config_pb2'})
_sym_db.RegisterMessage(Mongo)
ControlStep = _reflection.GeneratedProtocolMessageType('ControlStep', (_message.Message,), {'DESCRIPTOR': _CONTROLSTEP, '__module__': 'wolong.comm.input.v1.config_pb2'})
_sym_db.RegisterMessage(ControlStep)
ControlThread = _reflection.GeneratedProtocolMessageType('ControlThread', (_message.Message,), {'DESCRIPTOR': _CONTROLTHREAD, '__module__': 'wolong.comm.input.v1.config_pb2'})
_sym_db.RegisterMessage(ControlThread)
ControlOutput = _reflection.GeneratedProtocolMessageType('ControlOutput', (_message.Message,), {'DESCRIPTOR': _CONTROLOUTPUT, '__module__': 'wolong.comm.input.v1.config_pb2'})
_sym_db.RegisterMessage(ControlOutput)
Control = _reflection.GeneratedProtocolMessageType('Control', (_message.Message,), {'DESCRIPTOR': _CONTROL, '__module__': 'wolong.comm.input.v1.config_pb2'})
_sym_db.RegisterMessage(Control)
OutputSwitch = _reflection.GeneratedProtocolMessageType('OutputSwitch', (_message.Message,), {'DESCRIPTOR': _OUTPUTSWITCH, '__module__': 'wolong.comm.input.v1.config_pb2'})
_sym_db.RegisterMessage(OutputSwitch)
Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {'DESCRIPTOR': _OUTPUT, '__module__': 'wolong.comm.input.v1.config_pb2'})
_sym_db.RegisterMessage(Output)
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'wolong.comm.input.v1.config_pb2'})
_sym_db.RegisterMessage(Config)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _CHANNELTYPE._serialized_start = 1535
    _CHANNELTYPE._serialized_end = 1708
    _ANTENNATYPE._serialized_start = 1710
    _ANTENNATYPE._serialized_end = 1799
    _LOG._serialized_start = 90
    _LOG._serialized_end = 110
    _MONGO._serialized_start = 113
    _MONGO._serialized_end = 394
    _CONTROLSTEP._serialized_start = 396
    _CONTROLSTEP._serialized_end = 457
    _CONTROLTHREAD._serialized_start = 459
    _CONTROLTHREAD._serialized_end = 490
    _CONTROLOUTPUT._serialized_start = 492
    _CONTROLOUTPUT._serialized_end = 597
    _CONTROL._serialized_start = 600
    _CONTROL._serialized_end = 1134
    _OUTPUTSWITCH._serialized_start = 1136
    _OUTPUTSWITCH._serialized_end = 1233
    _OUTPUT._serialized_start = 1235
    _OUTPUT._serialized_end = 1343
    _CONFIG._serialized_start = 1346
    _CONFIG._serialized_end = 1532
