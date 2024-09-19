from pydantic import BaseModel, Field
from ..utils.b64 import base64_encode, base64_decode


class Request(BaseModel):
    task_name: str = Field(title="task_name", 
                           description="需要调用的Task名称")
    id: str = Field(title="id",
                    description="使用uuid4生成的唯一id")
    args: dict = Field(title="args",
                       description="Task任务执行参数")

    def encode(self):
        return base64_encode(self.model_dump_json()).encode()
    