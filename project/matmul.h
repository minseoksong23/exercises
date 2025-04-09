#ifndef MATMUL_H
#define MATMUL_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * Multiplies an N x M matrix A by an M x 1 vector x, producing an N x 1 vector y.
 *
 * @param A  Pointer to the first element of the matrix A (row-major order).
 * @param x  Pointer to the first element of the vector x.
 * @param y  Pointer to the first element of the output vector y.
 * @param N  Number of rows in A.
 * @param M  Number of columns in A (and length of vector x).
 */
void matmul(const double* A, const double* x, double* y, size_t N, size_t M);

#ifdef __cplusplus
}
#endif

#endif // MATMUL_H
