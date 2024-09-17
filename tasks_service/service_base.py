#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   service_item.py
@Time    :   2024-04-28 18:55:18
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   Service 父类
'''

from ..utils import client_send_request  
from ..model import Result


class ServiceBase:

    def __init__(self, task_name):
        self.task_name = task_name

    def request(self, send_data_dict):
        client_send_request(send_data_dict)

    def callback(self, result: Result):
        try:
            print(f"{self.task_name} callback result: {result}")
            self.callback_func(result)
            
        except Exception as e:
            # print(f"{self.task_name} callback error: {e}")
            Exception(f"{self.task_name} callback error: {e}")
        
        # finally:
            # print(f"{self.task_name} callback result: {result}")

    def callback_func(self, data):
        pass
    