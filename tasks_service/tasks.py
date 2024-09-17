#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tasks.py
@Time    :   2024-08-16 13:50:45
@Author  :   chakcy 
@Email   :   947105045@qq.com
@description   :   tasks
'''

from .ts_item import TSItem


class Tasks():
    TaskClasses = {}

    @classmethod
    def append_Task(cls, tsItme:TSItem):
        cls.TaskClasses[tsItme.TASK_NAME] = tsItme.task_class

    @classmethod
    def run_task(cls, params:dict):
        task_name = params.get('task_name', "")
        id = params.get('id', "")
        args = params.get('args', None)
        TaskClass = cls.TaskClasses.get(task_name, lambda args: {
            "task_name": task_name, 
            "msg": "Task not found",
            "params": params
        }) 
        result = TaskClass({"id":id, "args":args}).result_callback() if args is not None else TaskClass().result_callback()
        return result
    