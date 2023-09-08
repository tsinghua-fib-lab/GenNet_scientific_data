
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17wolong/geo/v2/geo.proto\x12\rwolong.geo.v2"6\n\x0fLongLatPosition\x12\x11\n\tlongitude\x18\x01 \x01(\x01\x12\x10\n\x08latitude\x18\x02 \x01(\x01""\n\nXYPosition\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01"*\n\x0cLanePosition\x12\x0f\n\x07lane_id\x18\x01 \x01(\x05\x12\t\n\x01s\x18\x02 \x01(\x01"\x1d\n\x0bAoiPosition\x12\x0e\n\x06aoi_id\x18\x01 \x01(\x05"\xb6\x02\n\x08Position\x127\n\rlane_position\x18\x01 \x01(\x0b2\x1b.wolong.geo.v2.LanePositionH\x00\x88\x01\x01\x125\n\x0caoi_position\x18\x02 \x01(\x0b2\x1a.wolong.geo.v2.AoiPositionH\x01\x88\x01\x01\x12=\n\x10longlat_position\x18\x03 \x01(\x0b2\x1e.wolong.geo.v2.LongLatPositionH\x02\x88\x01\x01\x123\n\x0bxy_position\x18\x04 \x01(\x0b2\x19.wolong.geo.v2.XYPositionH\x03\x88\x01\x01B\x10\n\x0e_lane_positionB\x0f\n\r_aoi_positionB\x13\n\x11_longlat_positionB\x0e\n\x0c_xy_position"i\n\x0fLongLatRectArea\x12*\n\x02ne\x18\x01 \x01(\x0b2\x1e.wolong.geo.v2.LongLatPosition\x12*\n\x02sw\x18\x02 \x01(\x0b2\x1e.wolong.geo.v2.LongLatPositionb\x06proto3')
_LONGLATPOSITION = DESCRIPTOR.message_types_by_name['LongLatPosition']
_XYPOSITION = DESCRIPTOR.message_types_by_name['XYPosition']
_LANEPOSITION = DESCRIPTOR.message_types_by_name['LanePosition']
_AOIPOSITION = DESCRIPTOR.message_types_by_name['AoiPosition']
_POSITION = DESCRIPTOR.message_types_by_name['Position']
_LONGLATRECTAREA = DESCRIPTOR.message_types_by_name['LongLatRectArea']
LongLatPosition = _reflection.GeneratedProtocolMessageType('LongLatPosition', (_message.Message,), {'DESCRIPTOR': _LONGLATPOSITION, '__module__': 'wolong.geo.v2.geo_pb2'})
_sym_db.RegisterMessage(LongLatPosition)
XYPosition = _reflection.GeneratedProtocolMessageType('XYPosition', (_message.Message,), {'DESCRIPTOR': _XYPOSITION, '__module__': 'wolong.geo.v2.geo_pb2'})
_sym_db.RegisterMessage(XYPosition)
LanePosition = _reflection.GeneratedProtocolMessageType('LanePosition', (_message.Message,), {'DESCRIPTOR': _LANEPOSITION, '__module__': 'wolong.geo.v2.geo_pb2'})
_sym_db.RegisterMessage(LanePosition)
AoiPosition = _reflection.GeneratedProtocolMessageType('AoiPosition', (_message.Message,), {'DESCRIPTOR': _AOIPOSITION, '__module__': 'wolong.geo.v2.geo_pb2'})
_sym_db.RegisterMessage(AoiPosition)
Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {'DESCRIPTOR': _POSITION, '__module__': 'wolong.geo.v2.geo_pb2'})
_sym_db.RegisterMessage(Position)
LongLatRectArea = _reflection.GeneratedProtocolMessageType('LongLatRectArea', (_message.Message,), {'DESCRIPTOR': _LONGLATRECTAREA, '__module__': 'wolong.geo.v2.geo_pb2'})
_sym_db.RegisterMessage(LongLatRectArea)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _LONGLATPOSITION._serialized_start = 42
    _LONGLATPOSITION._serialized_end = 96
    _XYPOSITION._serialized_start = 98
    _XYPOSITION._serialized_end = 132
    _LANEPOSITION._serialized_start = 134
    _LANEPOSITION._serialized_end = 176
    _AOIPOSITION._serialized_start = 178
    _AOIPOSITION._serialized_end = 207
    _POSITION._serialized_start = 210
    _POSITION._serialized_end = 520
    _LONGLATRECTAREA._serialized_start = 522
    _LONGLATRECTAREA._serialized_end = 627
