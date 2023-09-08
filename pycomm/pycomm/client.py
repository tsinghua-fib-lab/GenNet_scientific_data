from __future__ import print_function
import logging
from typing import Dict, List
import time
import grpc
from .protos.wolong.comm.interaction.sim.v1 import (
    dynamic_pb2 as pb_dynamic,
    dynamic_pb2_grpc as grpc_pb_dynamic,
)
from .protos.wolong.comm.interaction.sim.v1 import (
    coverage_pb2 as pb_coverage,
    coverage_pb2_grpc as grpc_pb_coverage,
)
from .protos.wolong.comm.interaction.sim.v1 import (
    energy_pb2 as pb_energy,
    energy_pb2_grpc as grpc_pb_energy,
)
from .protos.wolong.comm.interaction.sim.v1 import (
    sim_service_pb2 as pb_sim,
    sim_service_pb2_grpc as grpc_pb_sim,
)
from .protos.wolong.comm.input.v1 import (
    config_pb2 as pb_config,
    config_pb2_grpc as grpc_pb_config,
)

def _dynamic_optimize_request_packer(
    request_dat: List[Dict], start: int, total: int, interval: int,config:dict
) -> pb_sim.SimRequest:
    dynamic_actions = []
    for request_person in request_dat:
        allocations = []
        for allocation in request_person["base_stations"]:
            allocation_person = pb_dynamic.Allocation(
                base_station_id=allocation[0],
                channel_id=allocation[1],
                power=allocation[2],
            )
            allocations.append(allocation_person)
        action_person = pb_dynamic.DynamicAction(id=request_person["id"], actions=allocations,steps_next = request_person["steps_next"])
        dynamic_actions.append(action_person)
    
    stepinfo = pb_config.ControlStep(start = start, total = total,interval = interval)
    control = pb_sim.Control(step=stepinfo,display_guomao = config['display_micro'],coverage_range = config['coverage_range'],
                             handover_interval = config['handover_interval'],channel_type = config['channel_type'],antenna_type = config['antenna_type'])
    action = pb_sim.Action(dynamics = dynamic_actions)
    # if config['output']:
    #     outputswitch = pb_config.OutputSwitch(person = True,base_station = True,aoi = True,heatmap = True,stats = True)
    #     output = pb_config.Output(switch = outputswitch)
    # else:
    #     outputswitch = pb_config.OutputSwitch(person = False,base_station = False,aoi = False,heatmap = False,stats = False)
    #     output = pb_config.Output(switch = outputswitch)
    
    request = pb_sim.SimRequest(action=action, control=control,job = config['job'],store_keep = config["store_keep"],optimize_type = 1,is_output = config['visualize'])
    return request


def _dynamic_optimize_response_packer(response: pb_sim.SimResponse):
    dynamic_state = []
    dynamic_reward = []
    for person_info in response.persons:
        person_state = {}
        person_state["id"] = person_info.id
        person_state["x"] = person_info.state.xy_position.x
        person_state["y"] = person_info.state.xy_position.y
        person_state["demand"] = person_info.state.demand
        person_state["remain_time"] = person_info.state.remain_time
        person_state["satisfied_flow"] = person_info.state.satisfied_flow
        person_state["demand_next_average"] = person_info.state.next_demand
        dynamic_state.append(person_state)
        person_reward = {}
        person_reward["flow"] = person_info.reward.flow
        person_reward["satisfied_flow"] = person_info.reward.satisfied_flow
        dynamic_reward.append(person_reward)
    visualize = visualize_response_packer(response.output)
    return dynamic_state, dynamic_reward, visualize

def _coverage_optimize_request_packer(
    request_dat: List[Dict], start: int, total: int, interval: int,config:dict
) -> pb_sim.SimRequest:
    coverage_actions = []
    for request_bs in request_dat:
        action = pb_coverage.CoverageAction(
            id=int(request_bs["id"]),
            bs_azi=request_bs["bs_azi"],
            bs_tilt=request_bs["bs_tilt"],
            bw_azi=request_bs["bw_azi"],
            bw_tilt=request_bs["bw_tilt"],
        )
        coverage_actions.append(action)
    stepinfo = pb_config.ControlStep(start = start, total = total,interval = interval)
    control = pb_sim.Control(step=stepinfo,display_guomao = config['display_micro'],coverage_range = config['coverage_range'],
                             handover_interval = config['handover_interval'],channel_type = config['channel_type'],antenna_type = config['antenna_type'])
    action = pb_sim.Action(coverages=coverage_actions)
    # if config['output']:
    #     outputswitch = pb_config.OutputSwitch(person = True,base_station = True,aoi = True,heatmap = True,stats = True)
    #     output = pb_config.Output(switch = outputswitch)
    # else:
    #     outputswitch = pb_config.OutputSwitch(person = False,base_station = False,aoi = False,heatmap = False,stats = False)
    #     output = pb_config.Output(switch = outputswitch)
    request = pb_sim.SimRequest(action=action, control=control,job = config['job'],store_keep = config["store_keep"],optimize_type = 2,is_output = config['visualize'])

    return request

def _coverage_optimize_response_packer(response: pb_sim.SimResponse):
    state = []
    reward = []
    for grid_info in response.grids:
        grid_state = {}
        grid_state["grid_id"] = grid_info.id
        grid_state["signals"] = grid_info.state.signals
        grid_state["user_number"] = grid_info.state.user_number
        grid_state["is_indoor"] = grid_info.state.is_indoor
        state.append(grid_state)
        grid_reward = {}
        grid_reward["grid_id"] = grid_info.id
        grid_reward["coverage"] = grid_info.reward.coverage
        grid_reward["mean_rate"] = grid_info.reward.mean_rate
        reward.append(grid_reward)
    visualize = visualize_response_packer(response.output)
    return state, reward, visualize

def _energy_optimize_request_packer(
    request_dat: List[Dict], start: int, total: int, interval: int,config:dict
) -> pb_sim.SimRequest:  #rl传给模拟器的数据
    traffics = []
    bs_actions = []
    cell_actions = []
    for traffic in request_dat["traffic"]:
        traffics.append(pb_energy.Traffic(user_id = traffic['user_id'], cell_id = traffic['cell_id'], traffic = traffic['traffic']) )
    for bs_action in request_dat["bs_actions"]:
        bs_actions.append(pb_energy.BsAction(bs_id = bs_action[0], bs_control_state = bs_action[1]) )
    for cell_action in request_dat["cell_actions"]:
        cell_actions.append(pb_energy.CellAction(cell_id = cell_action[0], cell_control_state = cell_action[1]) )
    energy_action = pb_energy.ConserveAction(
        cell_actions=cell_actions,
        bs_actions=bs_actions,
        traffic= traffics, 
    )
    # print(energy_action)
        
    stepinfo = pb_config.ControlStep(start = start, total = total,interval = interval)
    control = pb_sim.Control(step=stepinfo,display_guomao = config['display_micro'],coverage_range = config['coverage_range'],
                             handover_interval = config['handover_interval'],channel_type = config['channel_type'],antenna_type = config['antenna_type'])
    action = pb_sim.Action(conservations=energy_action)
    # if config['output']:
    #     outputswitch = pb_config.OutputSwitch(person = True,base_station = True,aoi = True,heatmap = True,stats = True)
    #     output = pb_config.Output(switch = outputswitch)
    # else:
    #     outputswitch = pb_config.OutputSwitch(person = False,base_station = False,aoi = False,heatmap = False,stats = False)
    #     output = pb_config.Output(switch = outputswitch)
    request = pb_sim.SimRequest(action=action, control=control,job = config['job'],store_keep = config["store_keep"],optimize_type = 3,is_output = config['visualize'])
    return request

def _energy_optimize_response_packer(response: pb_sim.SimResponse):   #模拟器传过来的数据
    state = {}
    reward = {}
    cell_power_coefs = []
    for cell_power_coef in response.conserve.state.cell_power_coef:
        cell_power_coefs.append([cell_power_coef.slope, cell_power_coef.bias])
    bigraph_cell_bss = []
    for bigraph_cell_bs in response.conserve.state.bigraph_cell_bs:
        bigraph_cell_bss.append([bigraph_cell_bs.cell_id, bigraph_cell_bs.bs_id])
    bigraph_demand_cells = []
    for bigraph_demand_cell in response.conserve.state.bigraph_demand_cell:
        bigraph_demand_cells.append([bigraph_demand_cell.user_id, bigraph_demand_cell.cell_id])
    air_condition_power_coefs = []
    for air_condition_power_coef in response.conserve.state.air_condition_power_coef:
        air_condition_power_coefs.append([air_condition_power_coef.slope, air_condition_power_coef.bias])
    demands = []
    for demand in response.conserve.state.demand:
        demands.append({"user_id": demand.user_id, "demand": demand.demand})
    # TODO:是否映射cell/user/bs从0开始
    state["bs_num"] = response.conserve.state.bs_num
    state["bbu_power"] = response.conserve.state.bbu_power
    state["cell_num"] = response.conserve.state.cell_num
    state["cell_sleep_power"] = response.conserve.state.cell_sleep_power 
    state['cell_capacity'] = response.conserve.state.cell_capacity
    state["cell_power_coef"] = cell_power_coefs
    state["bigraph_cell_bs"] = bigraph_cell_bss
    state["bigraph_demand_cell"] = bigraph_demand_cells
    state["demand"] = demands
    state["air_condition_power_coef"] = air_condition_power_coefs

    reward["power_save_ratio"] = response.conserve.reward.power_save_ratio
    reward["power_save"] = response.conserve.reward.power_save
    visualize = visualize_response_packer(response.output)

    return state, reward, visualize

def visualize_response_packer(response: pb_sim.SimResponse.output):
    visualize = {}
    visualize['step'] = response.step

    base_stations = []
    for base_station in response.base_stations:
        base_stations.append({"id": base_station.id, "demand_flow": base_station.demand_flow, "actual_flow": base_station.actual_flow,
                              "num_agents": base_station.num_agents, "unsatisfied_num": base_station.unsatisfied_num, "satisfied_num": base_station.satisfied_num,
                              "outage_num": base_station.outage_num, "transmit_power": base_station.transmit_power, "resource_block_ratio": base_station.resource_block_ratio,
                              "energy_efficiency": base_station.energy_efficiency, "load_status": base_station.load_status, "rate_com": base_station.rate_com,
                              "freq_range_id": base_station.freq_range_id,"power_consumption": base_station.power_consumption,"base_station_type": base_station.base_station_type,
                              "max_power": base_station.max_power,"bs_azi": base_station.bs_azi,"bs_tilt": base_station.bs_tilt})
    visualize['base_stations'] = base_stations

    aois = []
    for aoi in response.aois:
        aois.append({"id": aoi.id, "demand_flow": aoi.demand_flow, "actual_flow": aoi.actual_flow,
                     "num_agents": aoi.num_agents, "unsatisfied_num": aoi.unsatisfied_num, "satisfied_num": aoi.satisfied_num,
                     "active_user_num": aoi.active_user_num, "outage_num": aoi.outage_num, })
    visualize['aois'] = aois

    strengths = []
    for strength in response.heatmap.strength:
        strengths.append(strength)
    base_station_ids = []
    for base_station_id in response.heatmap.base_station_id:
        base_station_ids.append(base_station_id)
    freq_range_ids = []
    for freq_range_id in response.heatmap.freq_range_id:
        freq_range_ids.append(freq_range_id)
    rates = []
    for rate in response.heatmap.rate:
        rates.append(rate)
    unsatisfied_ratios = []
    for unsatisfied_ratio in response.heatmap.unsatisfied_ratio:
        unsatisfied_ratios.append(unsatisfied_ratio)
    visualize['heatmap'] = {'num_rows': response.heatmap.num_rows, 'num_columns': response.heatmap.num_columns,'strength': strengths,
                                  'base_station_id': base_station_ids,'freq_range_id': freq_range_ids,'rate': rates,'unsatisfied_ratio': unsatisfied_ratios}
    
    strengths = []
    for strength in response.small_heatmap.strength:
        strengths.append(strength)
    base_station_ids = []
    for base_station_id in response.small_heatmap.base_station_id:
        base_station_ids.append(base_station_id)
    freq_range_ids = []
    for freq_range_id in response.small_heatmap.freq_range_id:
        freq_range_ids.append(freq_range_id)
    rates = []
    for rate in response.small_heatmap.rate:
        rates.append(rate)
    unsatisfied_ratios = []
    for unsatisfied_ratio in response.small_heatmap.unsatisfied_ratio:
        unsatisfied_ratios.append(unsatisfied_ratio)
    visualize['small_heatmap'] = {'num_rows': response.small_heatmap.num_rows, 'num_columns': response.small_heatmap.num_columns,'strength': strengths,
                                  'base_station_id': base_station_ids,'freq_range_id': freq_range_ids,'rate': rates,'unsatisfied_ratio': unsatisfied_ratios}
    persons = []
    for person in response.persons:
        freq_range_ids = []
        for freq_range_id in person.freq_range_ids:
            freq_range_ids.append(freq_range_id)
        persons.append({"id": person.id, 'demand_rate':person.demand_rate,'actual_rate':person.actual_rate,
                        'connect_status':person.connect_status,'demand_status':person.demand_status,
                        'strength':person.strength,'base_station_id':person.base_station_id,'freq_range_ids':freq_range_ids,
                        'received_power':person.received_power,'num_channels':person.num_channels,'demand_flow':person.demand_flow,
                        'actual_flow':person.actual_flow,'person_type':person.person_type,'lng':person.lng,'lat':person.lat})
        
    visualize['persons'] = persons
    
    visualize['statistics'] = {'num_agent':response.statistics.num_agent,'num_satisfied_agent':response.statistics.num_satisfied_agent,
                               'num_unsatisfied_agent':response.statistics.num_unsatisfied_agent,'num_outage_agent':response.statistics.num_outage_agent,
                               'num_outage_agent':response.statistics.num_outage_agent,'num_active_agent':response.statistics.num_active_agent,
                               'num_connect_agent':response.statistics.num_connect_agent,'demand_flow':response.statistics.demand_flow,
                               'actual_flow':response.statistics.actual_flow,'num_base_station':response.statistics.num_base_station,
                               'num_high_load_base_station':response.statistics.num_high_load_base_station,'num_low_load_base_station':response.statistics.num_low_load_base_station,
                               'num_ok_load_base_station':response.statistics.num_ok_load_base_station,'power_consumption':response.statistics.power_consumption}
    return visualize







class SimClient(object):
    def __init__(self, listen_address,optimize_type,config):
        optimize_channel = grpc.insecure_channel(
            listen_address,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )
        self.config = config
        self.optimize_type = optimize_type
        self._optimize_stub = grpc_pb_sim.SimServiceStub(optimize_channel)

    def Optimize(self, request_data: List[Dict], start: int, total: int, interval: int,):
        if self.optimize_type == 2:

            def _async_parser(response):
                return _coverage_optimize_response_packer(response)

            req = _coverage_optimize_request_packer(request_data, start, total, interval,self.config)
            res = self._optimize_stub.Sim(req)
            return _async_parser(res)
        
        elif self.optimize_type == 1:
            
            def _async_parser(response):
                return _dynamic_optimize_response_packer(response)

            req = _dynamic_optimize_request_packer(request_data, start, total, interval,self.config)
            res = self._optimize_stub.Sim(req)
            return _async_parser(res)
        
                
        elif self.optimize_type == 3:
            
            def _async_parser(response):
                return _energy_optimize_response_packer(response)

            req = _energy_optimize_request_packer(request_data, start, total, interval,self.config)
            res = self._optimize_stub.Sim(req)
            return _async_parser(res)
        
