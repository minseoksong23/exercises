import ctypes
import os
import numpy as np

class MatMul:
    def __init__(self):
        lib_path = os.path.join(os.path.dirname(__file__), "libmatmul.dylib")
        self._lib = ctypes.cdll.LoadLibrary(lib_path)
        self._lib.matmul.argtypes = [
            ctypes.POINTER(ctypes.c_double),
            ctypes.POINTER(ctypes.c_double),
            ctypes.POINTER(ctypes.c_double),
            ctypes.c_size_t,
            ctypes.c_size_t
        ]
        self._lib.matmul.restype = None

    def multiply(self, A, x):
        N, M = A.shape
        y = np.zeros(N, dtype=np.float64)
        self._lib.matmul(
            A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            y.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            N,
            M
        )
        return y
