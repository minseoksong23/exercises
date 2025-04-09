import numpy as np
from matmul_wrapper import MatMul

def test_small():
    A = np.array([[1, 2],
                  [3, 4]], dtype=np.float64)
    x = np.array([5, 6], dtype=np.float64)
    y = MatMul().multiply(A, x)
    assert np.allclose(y, [17, 39])
    print("Test passed! A*x =", y)

if __name__ == "__main__":
    test_small()
