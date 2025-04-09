import numpy as np
from matmul_wrapper import MatMul

def test_small():
    # Example matrix A (2x2)
    A = np.array([[1, 2],
                  [3, 4]], dtype=np.float64)
    # Example vector x (2x1)
    x = np.array([5, 6], dtype=np.float64)

    # Create an instance of our MatMul wrapper
    matmul_instance = MatMul()

    # Perform the multiplication
    y = matmul_instance.multiply(A, x)

    # Print the result and verify
    print("Matrix A:")
    print(A)
    print("Vector x:")
    print(x)
    print("Result of A*x = y:")
    print(y)  # Should be [17, 39] for [ [1,2],[3,4] ] x [5,6]

    # Simple check
    assert np.allclose(y, [17, 39]), "MatMul result does not match expected value."
    print("Test passed!")

if __name__ == "__main__":
    test_small()
