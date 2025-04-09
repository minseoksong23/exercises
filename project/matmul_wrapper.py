import ctypes
import os
import numpy as np

class MatMul:
    def __init__(self):
        """
        Load the shared library for matmul.
        We assume that 'libmatmul.so' (Linux/macOS) or 'matmul.dll' (Windows)
        is located in the same directory as this Python file.
        Adjust the path or file name as needed.
        """
        # Detect platform and library filename
        if os.name == "nt":
            lib_filename = "matmul.dll"  # Windows
        elif os.uname().sysname == "Darwin":
            lib_filename = "libmatmul.dylib"  # macOS name can be used
        else:
            lib_filename = "libmatmul.so"  # Linux

        # Build absolute path to the library
        lib_path = os.path.join(os.path.dirname(__file__), lib_filename)

        # Load the library
        self._lib = ctypes.cdll.LoadLibrary(lib_path)

        # Define argument and return types for the function matmul
        self._lib.matmul.argtypes = [
            ctypes.POINTER(ctypes.c_double),  # A
            ctypes.POINTER(ctypes.c_double),  # x
            ctypes.POINTER(ctypes.c_double),  # y
            ctypes.c_size_t,                  # N
            ctypes.c_size_t                   # M
        ]
        self._lib.matmul.restype = None  # matmul returns void

    def multiply(self, A: np.ndarray, x: np.ndarray) -> np.ndarray:
        """
        Multiply the matrix A by the vector x using the loaded C function.

        :param A: 2D numpy array of shape (N, M)
        :param x: 1D numpy array of shape (M,)
        :return: 1D numpy array of shape (N,) containing A*x
        """
        if not isinstance(A, np.ndarray) or not isinstance(x, np.ndarray):
            raise TypeError("A and x must be numpy arrays.")

        # Check shapes
        if A.ndim != 2:
            raise ValueError("A must be a 2D array.")
        if x.ndim != 1:
            raise ValueError("x must be a 1D array.")

        N, M = A.shape
        if x.shape[0] != M:
            raise ValueError("Incompatible dimensions for matrix-vector multiplication.")

        # Prepare output array
        y = np.zeros(N, dtype=np.float64)

        # Convert numpy arrays to ctypes pointers
        A_ptr = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        y_ptr = y.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

        # Call the C function
        self._lib.matmul(A_ptr, x_ptr, y_ptr, N, M)

        return y
