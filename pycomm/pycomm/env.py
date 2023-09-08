import json
import grpc
import time
import logging
from pathlib import Path
from .client import SimClient
from .utils import run, kill
import random
import string

def generate_random_str(randomlength=16):

    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str

class DynamicEnv:
    def __init__(
        self,
        visualize: bool = False, #是否可视化
        visualize_path: str = './', #可视化路径
        channel_type: int = 2, #信道类型
        antenna_type: int = 1, #天线类型
        job: str = 'job0', #任务名
        store_keep: bool = False, #同名job是否继续存储，False为覆盖
        output: bool = False, #是否输出
        display_micro: bool = True, #宏微观区域选择
        coverage_range: int = 1000, #覆盖范围
        handover_interval: int = 1, #切换间隔


    ):
        # 基站信息，id, 位置，功率，频段编号
        self.handle = None
        if job is None:
            job = generate_random_str(7)
        config = {'job':job,'store_keep':store_keep,'channel_type':channel_type,'antenna_type':antenna_type,
                  'display_micro':display_micro,'coverage_range':coverage_range,
                  'handover_interval':handover_interval,'output':output,'visualize':visualize}
        self.config = config
        self.visualize = visualize
        self.visualize_path = visualize_path


        self.optimize_client = SimClient("localhost:51402",optimize_type = 1,
                                         config = self.config)
        self._timestep = 0
    
    def save_visualize(self, visualize,path):
        filename = path +'vis_' +visualize['step'] + '.json'
        with open(filename, 'w') as f:
            json.dump(visualize, f,indent = 0,ensure_ascii=False)

    def step(self, action, start,total,interval):
        self._timestep += 1
        response_coroutine = self.optimize_client.Optimize(action, start,total,interval)
        time.sleep(0.1) # TODO: 上面的请求可能比step慢，导致卡住
        response = response_coroutine
        done = True
        print("step ok")
        if self.visualize:
            self.save_visualize(response[2],self.visualize_path)
        return response, done, {}

    def reset(self):
        if self.handle is not None:
            kill(*self.handle)
            print('kill ok')

class CoverageEnv:
    def __init__(
        self,
        visualize: bool = False, #是否可视化
        visualize_path: str = './', #可视化路径
        channel_type: int = 3, #信道类型
        antenna_type: int = 1, #天线类型
        job: str = 'job0', #任务名
        store_keep: bool = False, #同名job是否继续存储，False为覆盖
        output: bool = False, #是否输出
        display_micro: bool = True, #宏微观区域选择
        coverage_range: int = 1000, #覆盖范围
        handover_interval: int = 1, #切换间隔
        port: int = 51402,

    
):
        # 基站信息，id, 位置，功率，频段编号
        self.handle = None
        if job is None:
            job = generate_random_str(7)
        config = {'job':job,'store_keep':store_keep,'channel_type':channel_type,'antenna_type':antenna_type,
                  'display_micro':display_micro,'coverage_range':coverage_range,
                  'handover_interval':handover_interval,'output':output,'visualize':visualize}
        self.config = config
        self.visualize = visualize
        self.visualize_path = visualize_path

        self.optimize_client = SimClient("localhost:{}".format(port),optimize_type = 2,config=self.config)
        self._timestep = 0
    
    def save_visualize(self, visualize,path):
        filename = path +'vis_' +visualize['step'] + '.json'
        with open(filename, 'w') as f:
            json.dump(visualize, f,indent = 0,ensure_ascii=False)


    def step(self,action,start,total,interval):
        self._timestep += 1
        response_coroutine = self.optimize_client.Optimize(action, start,total,interval)
        # print('print:',response_coroutine)
        time.sleep(0.1) # TODO: 上面的请求可能比step慢，导致卡住
        response = response_coroutine
        done = True
        print("step ok")
        if self.visualize:
            self.save_visualize(response[2],self.visualize_path)

        return response, done, {}
    
    def reset(self):
        if self.handle is not None:
            kill(*self.handle)
            print('kill ok')


class ConserveEnv:
    def __init__(
        self,
        visualize: bool = False, #是否可视化
        channel_type: int = 1, #信道类型
        antenna_type: int = 1, #天线类型
        job: str = 'job0', #任务名
        store_keep: bool = False, #同名job是否继续存储，False为覆盖
        output: bool = False, #是否输出
        display_micro: bool = True, #宏微观区域选择
        coverage_range: int = 1000, #覆盖范围
        handover_interval: int = 1, #切换间隔
        port: int = 51402,
    
):
        # 基站信息，id, 位置，功率，频段编号
        self.handle = None
        if job is None:
            job = generate_random_str(7)
        config = {'job':job,'store_keep':store_keep,'channel_type':channel_type,'antenna_type':antenna_type,
                  'display_micro':display_micro,'coverage_range':coverage_range,
                  'handover_interval':handover_interval,'output':output,'visualize':visualize}
        self.config = config
        self.visualize = visualize
        self.visualize_path = visualize_path


        self.optimize_client = SimClient("localhost:{}".format(port),optimize_type = 3,config=self.config)
        self._timestep = 0

    def save_visualize(self, visualize,path):
        filename = path +'vis_' +visualize['step'] + '.json'
        with open(filename, 'w') as f:
            json.dump(visualize, f,indent = 0,ensure_ascii=False)


    def step(self,action,start,total,interval):
        self._timestep += 1
        response_coroutine = self.optimize_client.Optimize(action, start,total,interval)
        # print('print:',response_coroutine)
        time.sleep(0.1) # TODO: 上面的请求可能比step慢，导致卡住
        response = response_coroutine
        done = True
        print("step ok")
        if self.visualize:
            self.save_visualize(response[2],self.visualize_path)
            
        return response, done, {}
    
    def reset(self):
        if self.handle is not None:
            kill(*self.handle)
            print('kill ok')