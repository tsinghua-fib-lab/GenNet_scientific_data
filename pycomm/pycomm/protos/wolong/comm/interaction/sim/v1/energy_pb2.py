
'Generated protocol buffer code.'
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+wolong/comm/interaction/sim/v1/energy.proto\x12\x1ewolong.comm.interaction.sim.v1"\xe6\x03\n\rConserveState\x12\x0e\n\x06bs_num\x18\x01 \x01(\x05\x12\x11\n\tbbu_power\x18\x02 \x03(\x01\x12\x10\n\x08cell_num\x18\x03 \x01(\x05\x12\x15\n\rcell_capacity\x18\x04 \x03(\x01\x12\x18\n\x10cell_sleep_power\x18\x05 \x03(\x01\x12F\n\x0fcell_power_coef\x18\x06 \x03(\x0b2-.wolong.comm.interaction.sim.v1.CellPowerCoef\x12F\n\x0fbigraph_cell_bs\x18\x07 \x03(\x0b2-.wolong.comm.interaction.sim.v1.BigraphCellBs\x12N\n\x13bigraph_demand_cell\x18\x08 \x03(\x0b21.wolong.comm.interaction.sim.v1.BigraphDemandCell\x126\n\x06demand\x18\t \x03(\x0b2&.wolong.comm.interaction.sim.v1.Demand\x12W\n\x18air_condition_power_coef\x18\n \x03(\x0b25.wolong.comm.interaction.sim.v1.AirConditionPowerCoef")\n\x06Demand\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0e\n\x06demand\x18\x02 \x01(\x01"\xca\x01\n\x0eConserveAction\x12@\n\x0ccell_actions\x18\x01 \x03(\x0b2*.wolong.comm.interaction.sim.v1.CellAction\x12<\n\nbs_actions\x18\x02 \x03(\x0b2(.wolong.comm.interaction.sim.v1.BsAction\x128\n\x07traffic\x18\x03 \x03(\x0b2\'.wolong.comm.interaction.sim.v1.Traffic"k\n\nCellAction\x12\x0f\n\x07cell_id\x18\x01 \x01(\x05\x12L\n\x12cell_control_state\x18\x02 \x01(\x0e20.wolong.comm.interaction.sim.v1.CellControlState"c\n\x08BsAction\x12\r\n\x05bs_id\x18\x01 \x01(\x05\x12H\n\x10bs_control_state\x18\x02 \x01(\x0e2..wolong.comm.interaction.sim.v1.BsControlState">\n\x0eConserveReward\x12\x18\n\x10power_save_ratio\x18\x01 \x01(\x01\x12\x12\n\npower_save\x18\x02 \x01(\x01",\n\rCellPowerCoef\x12\r\n\x05slope\x18\x01 \x01(\x01\x12\x0c\n\x04bias\x18\x02 \x01(\x01"/\n\rBigraphCellBs\x12\x0f\n\x07cell_id\x18\x01 \x01(\x05\x12\r\n\x05bs_id\x18\x02 \x01(\x05"5\n\x11BigraphDemandCell\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07cell_id\x18\x02 \x01(\x05"4\n\x15AirConditionPowerCoef\x12\r\n\x05slope\x18\x01 \x01(\x01\x12\x0c\n\x04bias\x18\x02 \x01(\x01"<\n\x07Traffic\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07cell_id\x18\x02 \x01(\x05\x12\x0f\n\x07traffic\x18\x03 \x01(\x01"\x8c\x01\n\x0cConserveInfo\x12<\n\x05state\x18\x01 \x01(\x0b2-.wolong.comm.interaction.sim.v1.ConserveState\x12>\n\x06reward\x18\x03 \x01(\x0b2..wolong.comm.interaction.sim.v1.ConserveReward*\x8d\x01\n\x10CellControlState\x12"\n\x1eCELL_CONTROL_STATE_UNSPECIFIED\x10\x00\x12\x1b\n\x17CELL_CONTROL_STATE_OPEN\x10\x01\x12\x1c\n\x18CELL_CONTROL_STATE_SLEEP\x10\x02\x12\x1a\n\x16CELL_CONTROL_STATE_OFF\x10\x03*i\n\x0eBsControlState\x12 \n\x1cBS_CONTROL_STATE_UNSPECIFIED\x10\x00\x12\x19\n\x15BS_CONTROL_STATE_OPEN\x10\x01\x12\x1a\n\x16BS_CONTROL_STATE_CLOSE\x10\x02b\x06proto3')
_CELLCONTROLSTATE = DESCRIPTOR.enum_types_by_name['CellControlState']
CellControlState = enum_type_wrapper.EnumTypeWrapper(_CELLCONTROLSTATE)
_BSCONTROLSTATE = DESCRIPTOR.enum_types_by_name['BsControlState']
BsControlState = enum_type_wrapper.EnumTypeWrapper(_BSCONTROLSTATE)
CELL_CONTROL_STATE_UNSPECIFIED = 0
CELL_CONTROL_STATE_OPEN = 1
CELL_CONTROL_STATE_SLEEP = 2
CELL_CONTROL_STATE_OFF = 3
BS_CONTROL_STATE_UNSPECIFIED = 0
BS_CONTROL_STATE_OPEN = 1
BS_CONTROL_STATE_CLOSE = 2
_CONSERVESTATE = DESCRIPTOR.message_types_by_name['ConserveState']
_DEMAND = DESCRIPTOR.message_types_by_name['Demand']
_CONSERVEACTION = DESCRIPTOR.message_types_by_name['ConserveAction']
_CELLACTION = DESCRIPTOR.message_types_by_name['CellAction']
_BSACTION = DESCRIPTOR.message_types_by_name['BsAction']
_CONSERVEREWARD = DESCRIPTOR.message_types_by_name['ConserveReward']
_CELLPOWERCOEF = DESCRIPTOR.message_types_by_name['CellPowerCoef']
_BIGRAPHCELLBS = DESCRIPTOR.message_types_by_name['BigraphCellBs']
_BIGRAPHDEMANDCELL = DESCRIPTOR.message_types_by_name['BigraphDemandCell']
_AIRCONDITIONPOWERCOEF = DESCRIPTOR.message_types_by_name['AirConditionPowerCoef']
_TRAFFIC = DESCRIPTOR.message_types_by_name['Traffic']
_CONSERVEINFO = DESCRIPTOR.message_types_by_name['ConserveInfo']
ConserveState = _reflection.GeneratedProtocolMessageType('ConserveState', (_message.Message,), {'DESCRIPTOR': _CONSERVESTATE, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(ConserveState)
Demand = _reflection.GeneratedProtocolMessageType('Demand', (_message.Message,), {'DESCRIPTOR': _DEMAND, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(Demand)
ConserveAction = _reflection.GeneratedProtocolMessageType('ConserveAction', (_message.Message,), {'DESCRIPTOR': _CONSERVEACTION, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(ConserveAction)
CellAction = _reflection.GeneratedProtocolMessageType('CellAction', (_message.Message,), {'DESCRIPTOR': _CELLACTION, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(CellAction)
BsAction = _reflection.GeneratedProtocolMessageType('BsAction', (_message.Message,), {'DESCRIPTOR': _BSACTION, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(BsAction)
ConserveReward = _reflection.GeneratedProtocolMessageType('ConserveReward', (_message.Message,), {'DESCRIPTOR': _CONSERVEREWARD, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(ConserveReward)
CellPowerCoef = _reflection.GeneratedProtocolMessageType('CellPowerCoef', (_message.Message,), {'DESCRIPTOR': _CELLPOWERCOEF, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(CellPowerCoef)
BigraphCellBs = _reflection.GeneratedProtocolMessageType('BigraphCellBs', (_message.Message,), {'DESCRIPTOR': _BIGRAPHCELLBS, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(BigraphCellBs)
BigraphDemandCell = _reflection.GeneratedProtocolMessageType('BigraphDemandCell', (_message.Message,), {'DESCRIPTOR': _BIGRAPHDEMANDCELL, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(BigraphDemandCell)
AirConditionPowerCoef = _reflection.GeneratedProtocolMessageType('AirConditionPowerCoef', (_message.Message,), {'DESCRIPTOR': _AIRCONDITIONPOWERCOEF, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(AirConditionPowerCoef)
Traffic = _reflection.GeneratedProtocolMessageType('Traffic', (_message.Message,), {'DESCRIPTOR': _TRAFFIC, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(Traffic)
ConserveInfo = _reflection.GeneratedProtocolMessageType('ConserveInfo', (_message.Message,), {'DESCRIPTOR': _CONSERVEINFO, '__module__': 'wolong.comm.interaction.sim.v1.energy_pb2'})
_sym_db.RegisterMessage(ConserveInfo)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _CELLCONTROLSTATE._serialized_start = 1500
    _CELLCONTROLSTATE._serialized_end = 1641
    _BSCONTROLSTATE._serialized_start = 1643
    _BSCONTROLSTATE._serialized_end = 1748
    _CONSERVESTATE._serialized_start = 80
    _CONSERVESTATE._serialized_end = 566
    _DEMAND._serialized_start = 568
    _DEMAND._serialized_end = 609
    _CONSERVEACTION._serialized_start = 612
    _CONSERVEACTION._serialized_end = 814
    _CELLACTION._serialized_start = 816
    _CELLACTION._serialized_end = 923
    _BSACTION._serialized_start = 925
    _BSACTION._serialized_end = 1024
    _CONSERVEREWARD._serialized_start = 1026
    _CONSERVEREWARD._serialized_end = 1088
    _CELLPOWERCOEF._serialized_start = 1090
    _CELLPOWERCOEF._serialized_end = 1134
    _BIGRAPHCELLBS._serialized_start = 1136
    _BIGRAPHCELLBS._serialized_end = 1183
    _BIGRAPHDEMANDCELL._serialized_start = 1185
    _BIGRAPHDEMANDCELL._serialized_end = 1238
    _AIRCONDITIONPOWERCOEF._serialized_start = 1240
    _AIRCONDITIONPOWERCOEF._serialized_end = 1292
    _TRAFFIC._serialized_start = 1294
    _TRAFFIC._serialized_end = 1354
    _CONSERVEINFO._serialized_start = 1357
    _CONSERVEINFO._serialized_end = 1497
