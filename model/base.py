#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2024-08-15 12:29:39
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   模型基类
'''

from pydantic import BaseModel
import json
from typing import Dict, Any, Union

class Base(BaseModel):

    @classmethod
    def dict_to_model(cls, data: Union[Dict[str, Any], str]):
        if isinstance(data, str):
            data = {"error": data}
        return cls.model_validate_json(json.dumps(data))
    