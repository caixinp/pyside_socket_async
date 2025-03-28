#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2024-08-15 12:32:30
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   PySide6异步Socket通信
'''

import logging

import colorlog

from . import cache
from . import utils
from . import constants
from .socket_thread import create_socket_server_thread

from .tasks_service import TS # noqa: F401
import uuid # noqa: F401
import requests # noqa: F401


# 创建日志
logger = colorlog.getLogger()
logger.setLevel(logging.DEBUG)
ch = colorlog.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s %(levelname)s \n%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
ch.setFormatter(formatter)
logger.addHandler(ch)

__all__ = ['cache', 'utils', 'create_socket_server_thread', "constants"]
