#include "matmul.h"

void matmul(const double* A, const double* x, double* y, size_t N, size_t M);

void matmul(const double* A, const double* x, double* y, size_t N, size_t M) {
    // For each row i in [0..N-1]
    for (size_t i = 0; i < N; i++) {
        double sum = 0.0;
        // For each column j in [0..M-1]
        for (size_t j = 0; j < M; j++) {
            // A is in row-major order, so element at row i, column j is A[i*M + j]
            sum += A[i * M + j] * x[j];
        }
        y[i] = sum;
    }
}
