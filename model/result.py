#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   result.py
@Time    :   2024-08-15 12:30:13
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   任务结果模型
'''

from .base import Base
from typing import Union

class Result(Base):
    id: str
    result: Union[dict, str]
    status: str
    task_name: str
    created_at: float
    updated_at: float
    