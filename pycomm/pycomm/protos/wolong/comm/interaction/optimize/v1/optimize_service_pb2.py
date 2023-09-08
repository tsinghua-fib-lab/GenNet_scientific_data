
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......wolong.geo.v2 import geo_pb2 as wolong_dot_geo_dot_v2_dot_geo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:wolong/comm/interaction/optimize/v1/optimize_service.proto\x12#wolong.comm.interaction.optimize.v1\x1a\x17wolong/geo/v2/geo.proto"Z\n\x0cPersonDemand\x12\n\n\x02id\x18\x01 \x01(\x05\x12.\n\x0bxy_position\x18\x02 \x01(\x0b2\x19.wolong.geo.v2.XYPosition\x12\x0e\n\x06demand\x18\x03 \x01(\x01"e\n\x18OptimizeParameterRequest\x12I\n\x0eperson_demands\x18\x01 \x03(\x0b21.wolong.comm.interaction.optimize.v1.PersonDemand"Q\n\x13AllocateBaseStation\x12\x17\n\x0fbase_station_id\x18\x01 \x01(\x05\x12\x12\n\nchannel_id\x18\x02 \x01(\x05\x12\r\n\x05power\x18\x03 \x01(\x01"\x82\x01\n\x1aPersonAllocateBaseStations\x12\n\n\x02id\x18\x01 \x01(\x05\x12X\n\x16allocate_base_stations\x18\x02 \x03(\x0b28.wolong.comm.interaction.optimize.v1.AllocateBaseStation"\x84\x01\n\x19OptimizeParameterResponse\x12g\n\x1epersons_allocate_base_stations\x18\x01 \x03(\x0b2?.wolong.comm.interaction.optimize.v1.PersonAllocateBaseStations"\'\n\x15OptimizeStatusRequest\x12\x0e\n\x06status\x18\x01 \x01(\x08"\x18\n\x16OptimizeStatusResponse2\xb2\x02\n\x0fOptimizeService\x12\x89\x01\n\x0eOptimizeStatus\x12:.wolong.comm.interaction.optimize.v1.OptimizeStatusRequest\x1a;.wolong.comm.interaction.optimize.v1.OptimizeStatusResponse\x12\x92\x01\n\x11OptimizeParameter\x12=.wolong.comm.interaction.optimize.v1.OptimizeParameterRequest\x1a>.wolong.comm.interaction.optimize.v1.OptimizeParameterResponseb\x06proto3')
_PERSONDEMAND = DESCRIPTOR.message_types_by_name['PersonDemand']
_OPTIMIZEPARAMETERREQUEST = DESCRIPTOR.message_types_by_name['OptimizeParameterRequest']
_ALLOCATEBASESTATION = DESCRIPTOR.message_types_by_name['AllocateBaseStation']
_PERSONALLOCATEBASESTATIONS = DESCRIPTOR.message_types_by_name['PersonAllocateBaseStations']
_OPTIMIZEPARAMETERRESPONSE = DESCRIPTOR.message_types_by_name['OptimizeParameterResponse']
_OPTIMIZESTATUSREQUEST = DESCRIPTOR.message_types_by_name['OptimizeStatusRequest']
_OPTIMIZESTATUSRESPONSE = DESCRIPTOR.message_types_by_name['OptimizeStatusResponse']
PersonDemand = _reflection.GeneratedProtocolMessageType('PersonDemand', (_message.Message,), {'DESCRIPTOR': _PERSONDEMAND, '__module__': 'wolong.comm.interaction.optimize.v1.optimize_service_pb2'})
_sym_db.RegisterMessage(PersonDemand)
OptimizeParameterRequest = _reflection.GeneratedProtocolMessageType('OptimizeParameterRequest', (_message.Message,), {'DESCRIPTOR': _OPTIMIZEPARAMETERREQUEST, '__module__': 'wolong.comm.interaction.optimize.v1.optimize_service_pb2'})
_sym_db.RegisterMessage(OptimizeParameterRequest)
AllocateBaseStation = _reflection.GeneratedProtocolMessageType('AllocateBaseStation', (_message.Message,), {'DESCRIPTOR': _ALLOCATEBASESTATION, '__module__': 'wolong.comm.interaction.optimize.v1.optimize_service_pb2'})
_sym_db.RegisterMessage(AllocateBaseStation)
PersonAllocateBaseStations = _reflection.GeneratedProtocolMessageType('PersonAllocateBaseStations', (_message.Message,), {'DESCRIPTOR': _PERSONALLOCATEBASESTATIONS, '__module__': 'wolong.comm.interaction.optimize.v1.optimize_service_pb2'})
_sym_db.RegisterMessage(PersonAllocateBaseStations)
OptimizeParameterResponse = _reflection.GeneratedProtocolMessageType('OptimizeParameterResponse', (_message.Message,), {'DESCRIPTOR': _OPTIMIZEPARAMETERRESPONSE, '__module__': 'wolong.comm.interaction.optimize.v1.optimize_service_pb2'})
_sym_db.RegisterMessage(OptimizeParameterResponse)
OptimizeStatusRequest = _reflection.GeneratedProtocolMessageType('OptimizeStatusRequest', (_message.Message,), {'DESCRIPTOR': _OPTIMIZESTATUSREQUEST, '__module__': 'wolong.comm.interaction.optimize.v1.optimize_service_pb2'})
_sym_db.RegisterMessage(OptimizeStatusRequest)
OptimizeStatusResponse = _reflection.GeneratedProtocolMessageType('OptimizeStatusResponse', (_message.Message,), {'DESCRIPTOR': _OPTIMIZESTATUSRESPONSE, '__module__': 'wolong.comm.interaction.optimize.v1.optimize_service_pb2'})
_sym_db.RegisterMessage(OptimizeStatusResponse)
_OPTIMIZESERVICE = DESCRIPTOR.services_by_name['OptimizeService']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _PERSONDEMAND._serialized_start = 124
    _PERSONDEMAND._serialized_end = 214
    _OPTIMIZEPARAMETERREQUEST._serialized_start = 216
    _OPTIMIZEPARAMETERREQUEST._serialized_end = 317
    _ALLOCATEBASESTATION._serialized_start = 319
    _ALLOCATEBASESTATION._serialized_end = 400
    _PERSONALLOCATEBASESTATIONS._serialized_start = 403
    _PERSONALLOCATEBASESTATIONS._serialized_end = 533
    _OPTIMIZEPARAMETERRESPONSE._serialized_start = 536
    _OPTIMIZEPARAMETERRESPONSE._serialized_end = 668
    _OPTIMIZESTATUSREQUEST._serialized_start = 670
    _OPTIMIZESTATUSREQUEST._serialized_end = 709
    _OPTIMIZESTATUSRESPONSE._serialized_start = 711
    _OPTIMIZESTATUSRESPONSE._serialized_end = 735
    _OPTIMIZESERVICE._serialized_start = 738
    _OPTIMIZESERVICE._serialized_end = 1044
