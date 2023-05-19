import numpy as np
from numpy.typing import NDArray


def lu(A: NDArray, permute: bool) -> tuple[NDArray, NDArray, NDArray]:
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()
    P = np.eye(n)

    for k in range(n - 1):
        pivot = np.argmax(np.abs(U[k:, k])) + k

        U[[k, pivot], k:] = U[[pivot, k], k:]
        P[[k, pivot], :] = P[[pivot, k], :]

        if k > 0:
            L[[k, pivot], :k] = L[[pivot, k], :k]

        multipliers = U[k + 1:, k] / U[k, k]


        L[k + 1:, k] = multipliers
        U[k + 1:, k:] -= np.outer(multipliers, U[k, k:])

    return L, U, P


def solve(L: NDArray, U: NDArray, P: NDArray, b: NDArray) -> NDArray:
    Pb = P @ b
    y = np.linalg.solve(L, Pb)
    x = np.linalg.solve(U, y)
    return x


def get_A_b(a_11: float, b_1: float) -> tuple[NDArray, NDArray]:
    A = np.array([[a_11, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]])
    b = np.array([b_1, 12.0, -39.0])
    return A, b


if __name__ == "__main__":
    # Let's implement the LU decomposition with and without pivoting
    # and check its stability depending on the matrix elements
    p = 14  # modify from 7 to 16 to check instability
    a_11 = 3 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    b_1 = -16 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    A, b = get_A_b(a_11, b_1)
    # With pivoting
    L, U, P = lu(A, permute=True)
    x = solve(L, U, P, b)
    assert np.all(np.isclose(x, [1, -7, 4])), f"The anwser {x} is not accurate enough"
    # Without pivoting
    L, U, P = lu(A, permute=False)
    x_ = solve(L, U, P, b)
    assert np.all(np.isclose(x_, [1, -7, 4])), f"The anwser {x_} is not accurate enough"
