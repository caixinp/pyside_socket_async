#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   result.py
@Time    :   2024-08-15 12:30:13
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   任务结果模型
'''

from pydantic import BaseModel, model_validator, Field
from typing import Union
from ..constants import TaskStatus

class Result(BaseModel):
    id: str = Field(title="id",
                    description="执行结束返回的 Task id 用于在 TS 类中找出对应的回调函数")
    result: Union[dict, str] = Field(title="result",
                                     description="执行结果")
    status: str = Field(title="status",
                        description="Task的执行状态，包括 PENDING、RUNNING、SUCCEEDED、FAILED 四种")
    task_name: str = Field(title="task_name", 
                           default="Task 任务名称")
    created_at: float = Field(title="created_at",
                              description="任务开始的时间辍")
    updated_at: float = Field(title="updated_at",
                              default="任务状态更新的时间一般为任务结束时间")

    @model_validator(mode="after")
    def check_result(self):
        if self.status != TaskStatus.SUCCEEDED:
            raise ValueError(self)
        return self
