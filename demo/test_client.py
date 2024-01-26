import picklerpc
import numpy as np

client = picklerpc.PickleRPCClient(('10.50.60.6', 20169))
client = PickleRPCClient(('10.50.60.6', 20169))
client.hello()
client.numpy_create((3,4), dtype=np.float32)

%timeit client.numpy_create((3,4), dtype=np.float32)
%timeit client.hello()