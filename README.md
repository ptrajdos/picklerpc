# Pickle RPC in Python


![Python versions](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
[![PyPI version](https://img.shields.io/pypi/v/picklerpc.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/picklerpc/)
[![PyPI downloads](https://img.shields.io/pypi/dm/picklerpc.svg)](https://pypistats.org/packages/picklerpc)
![Code size](https://shields.io/github/languages/code-size/chenxinfeng4/picklerpc
)
![Last Commit](https://shields.io/github/last-commit/chenxinfeng4/picklerpc)

Very simple RPCs built with sockets & pickle in python. Support numpy as input and output arguments.

## Install
```bash
pip install picklerpc
```

## Example
Server
```python
import picklerpc
import numpy as np

# function
def func_numpy(data:np.ndarray) -> np.ndarray:
    return data + np.random.random(size=data.shape)

def func_str(name: None) -> str:
    return "Hello, %s" % name

def func_none() -> None:
    return None

def func_number(a, b):
    return a+b

class HelloRPC(object):
    def func_obj(self, name) -> str:
        return "Hello, %s" % name

# register
server = picklerpc.PickleRPCServer(('localhost', 9102))
server.register_function(func_numpy)
server.register_function(func_str)
server.register_function(func_none)
server.register_function(func_number)
server.register_function(lambda x,y: x-y, 'func_lambda')
server.register_instance(HelloRPC())  #from instance
server.serve_forever()
```

Client
```python
import picklerpc
import numpy as np

client = picklerpc.PickleRPCClient(('localhost', 9102))

print(client.func_numpy(np.arange(10), dtype=np.float32))
print(client.func_str('Pickle RPC'))
print(client.func_none())
print(client.func_number(np.range(10), 3))
print(client.func_lambda(np.range(10), 3))
print(client.func_obj('Pickle RPC'))
```

## Speed faster

The picklerpc is most **10x faster** than `zerorpc` and `xmlrpc`.

|                    | zerorpc | xmlrpc  | picklerpc (mine)    |
| ------------------ | ------- | ------- | ------------------- |
| Protocal           | tcp     | http    | tcp                 |
| Data Stream        | -       | xml     | pickle              |
| Multiple Client    | Yes     | Yes     | Yes                 |
| Data Types         | Natives | Natives | Natives + **Numpy** |
| Speed (local loop) | 683 µs  | 462 µs  | 59 µs               |
| Speed (remote)     | 2.76 ms | 4.64 ms | 0.54 ms             |





## Reference

> Thanks https://github.com/TarasZhere/RPC