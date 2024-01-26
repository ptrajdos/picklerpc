import picklerpc
import numpy as np

# 创建一个RPC客户端
def numpy_create(shape, dtype):
    return np.arange(np.prod(shape), dtype=dtype).reshape(shape)

def hello():
    return "Hello, world!"

def hello2():
    return None

def parse_numpy(array:np.ndarray):
    return array+1

def add(a, b):
    return a+b

server = picklerpc.PickleRPCServer(('0.0.0.0', 20169))
server.register_function(numpy_create)
server.register_function(hello)
server.register_function(hello2)
server.register_function(parse_numpy)
server.register_function(add)
server.serve_forever()
