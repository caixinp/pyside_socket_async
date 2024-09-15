# PySide6 Socket 异步框架

作者：chakcy

简介：利用 socket、threding 和 Qt 插槽实现的异步通信框架。

## 目录

[TOC]

## 1. 介绍

本框架旨在将运行时间较长的方法在一个线程中执行，最后通过插槽将结果返回给界面，其中涉及 socket 的通信，Qt多线程，Qt插槽，以及任务注册的概念。

## 2. 主要实现思路

在开启 pyside 应用的同时启动另一个线程，该线程启动一个socket 服务，用于与界面进行交互。

在开启 socket 服务线程前，动态的检测某路径下的模块，将带有 @task_function 装饰器的方法动态的生成 TSItem类，并将它们添加到 TS 类的 services 和 tasks 中，tasks 会被初始化到 socket 线程中作为待调用的方法，而 services 则是主线程发送调用方法的指令，即但主线程调用 services 中的某个方法后，会向 socket 服务发送一个请求，该请求无需等待结果，socket 服务会开启一个线程调用对应的 task 方法，执行完成后，将结果通过插槽返回给主线程，TS 会通过某种机制将结果返回给对应 service 的回调函数。

## 3. 使用案例

目录结构

```
demo
├── app
│   ├── engine
│   │   ├── __init__.py
│   │   └── test.py
│   ├── views
│   │   ├── __init__.py
│   │   └── window.py
│   └── __init__.py
└── main.py
```

`main.py`

```python
import sys
from app import app, window_view

if __name__ == "__main__":
    window_view.show()
    sys.exit(app.exec())
```

`app/__init__.py`

```python
import sys
from .views import MainWindow

from PySide6 import QtWidgets

from pyside_socket_async.socket import create_socket_server_thread
from .engine import task_service


app = QtWidgets.QApplication(sys.argv)
window_view = MainWindow()

create_socket_server_thread(task_service, app)

```

`app/engine/__init__.py`

```python
from pyside_socket_async.tasks_service import discover_and_mount_ts_item

task_service, send_data = discover_and_mount_ts_item('app.engine')
print(task_service.get_all_task_names())
```

`app/engine/test.py`

```python
import time
from pyside_socket_async.tasks_service import task_function


@task_function
def test(args):
    time.sleep(5)
    return "test"
```

`app/view/__init__.py`

```python
from .window import MainWindow


__all__ = ["MainWindow"]
```

`app/view/window.py`

```python
from PySide6.QtWidgets import QPushButton, QMainWindow, QWidget, QVBoxLayout

from ..engine import send_data
from pyside_socket_async.model import Result
from pyside_socket_async.utils import TaskStatus


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.centralwidget = QWidget(self)
        self.init_ui()
        self.bind()

    def init_ui(self):
        self.pushButtion = QPushButton(self.centralwidget)
        self.pushButtion.setText("点击我")

    def bind(self):
        self.pushButtion.clicked.connect(self.test)
    
    def test(self):
        def callback(result):
            
            res = Result.dict_to_model(result)
            if res.status == TaskStatus.SUCCEEDED:
                print(f"返回结果为：{res.result}")
            else: 
                print(res)
        
        send_data('test', {}, callback)
```