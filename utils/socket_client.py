#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   socket_client.py
@Time    :   2024-04-28 18:55:40
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   Socket客户端
'''

import socket
import json
from .b64 import base64_encode
from ..config import SocketConfig


host, port = SocketConfig.get_host_port()

def client_send_request(request_data: dict): 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client_socket.connect((host, port))  
    
    # 编码请求数据为json字符串  
    request_data_json = json.dumps(request_data)  
    # print(request_data_json)
    request = base64_encode(request_data_json).encode()
    response = None  
    try:  
        # 发送请求数据给服务器  
        client_socket.sendall(request)  

    except Exception:  
        response = None  
        
    finally:  
        client_socket.close()  
        return response
