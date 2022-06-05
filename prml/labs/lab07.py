import numpy as np
import sklearn.datasets
from scipy.optimize import fmin_l_bfgs_b
import numpy.linalg

import prml


def main():
    train_multiclass_regression()


def train_multiclass_regression():
    Data, Layers = load_iris()
    (DTR, LTR), (DTE, LTE) = prml.split_data(Data, Layers, 2.0 / 3.0)
    log_reg_func = log_reg_multi_func_factory(DTR, LTR, lambda_param=0.001)
    K = np.unique(LTR).size
    D = DTR.shape[0]
    W_vector, f, d = fmin_l_bfgs_b(log_reg_func,
                                   x0=np.zeros((D + 1, K)),
                                   approx_grad=True,
                                   iprint=1)
    print(f"f: {f}")
    print(f"d: {d}")
    W_raw = W_vector.reshape((D + 1, K))
    b = (W_raw[D: D + 1, :]).T
    W = W_raw[0:D, :]
    print(f"W and b: {W_raw}")

    prediction = W.T @ DTE + b
    print(f"Prediction {prediction}")
    scores = np.argmax(prediction, axis=0)
    print(f"scores: {1 - np.sum(scores == LTE) / DTE.shape[1]}")


def train_binary_regression():
    D, L = load_iris_binary()
    (DTR, LTR), (DTE, LTE) = prml.split_data(D, L, 2.0 / 3.0)
    log_reg_func = log_reg_func_factory(DTR, LTR, lambda_param=0.01)
    omegas, f, d = fmin_l_bfgs_b(log_reg_func,
                                 x0=np.zeros(DTR.shape[0] + 1),
                                 approx_grad=True,
                                 iprint=1)
    print(f"omegas: {omegas}")
    print(f"f: {f}")
    print(f"d: {d}")
    w = omegas[0:-1]
    b = omegas[-1]
    prediction = prml.vcol(w).T @ DTE + b
    score = (np.ones((1, DTE.shape[1])) * prediction > 0).astype(int)
    print(f"scores: {1 - np.sum(score == prml.vrow(LTE)) / DTE.shape[1]}")


def load_iris():
    iris = sklearn.datasets.load_iris()
    D, L = iris['data'].T, iris['target']
    return D, L


def load_iris_binary():
    iris = sklearn.datasets.load_iris()
    D, L = iris['data'].T, iris['target']
    D = D[:, L != 0]  # We remove setosa from D
    L = L[L != 0]  # We remove setosa from L
    L[L == 2] = 0  # We assign label 0 to virginica (was label 2)
    return D, L


def log_reg_func_factory(DTR: np.ndarray,
                         LTR: np.ndarray,
                         lambda_param: float):
    Z = 2 * LTR - 1
    n = DTR.shape[1]

    def log_reg_func(x):
        w = prml.vcol(x[0:-1])
        b = x[-1]
        regularization = np.power(np.linalg.norm(w), 2) * lambda_param / 2.0
        loss = np.sum(np.logaddexp(0, - Z * (w.T @ DTR + b))) / n
        return regularization + loss

    return log_reg_func


def log_reg_multi_func_factory(DTR: np.ndarray,
                               LTR: np.ndarray,
                               lambda_param: float):
    D = DTR.shape[0]
    n = DTR.shape[1]
    K = np.unique(LTR).size
    T = np.zeros((K, n))
    for index in range(n):
        T[LTR[index], index] = 1

    def log_reg_multi_func(W_vector):
        W_raw = W_vector.reshape((D + 1, K))
        b = prml.vcol(W_raw[D: D + 1, :])
        W = W_raw[0:D, :]

        regularization = np.power(np.linalg.norm(W), 2) * lambda_param / 2.0
        term1 = T * (W.T @ DTR + b -
                     np.log(np.sum(np.exp(W.T @ DTR + b), axis=0)))
        total = np.sum(term1) / n
        return regularization - total

    return log_reg_multi_func


def optimize_function_yz():
    x, f, d = fmin_l_bfgs_b(function_yz,
                            x0=np.array([0, 0]),
                            approx_grad=False,
                            iprint=1)
    print(f"x: {x}")
    print(f"f: {f}")
    print(f"d: {d}")


def function_yz(x: np.ndarray):
    y = x[0]
    z = x[1]
    f = np.power(y + 3, 2) + np.sin(y) + np.power(z + 1, 2)
    gradient = np.array([
        2 * (y + 3) + np.cos(y),
        2 * (z + 1)
    ])
    return f, gradient


if __name__ == '__main__':
    main()
