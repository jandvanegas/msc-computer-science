import numpy as np
import scipy.optimize
import sklearn.datasets

import src.prml.prml as prml


def main():
    D, L = load_iris_binary()
    (DTR, LTR), (DTE, LTE) = prml.split_data(D, L, 2.0 / 3.0)
    K = 1
    C = 1
    error = run_svm_linear(DTR, DTE, LTE, LTR, C, K)
    print(error)
    error = run_svm_kernel(DTR, DTE, LTE, LTR, C, K)
    print(error)


def run_svm_linear(DTR, DTE, LTE, LTR, C, K):
    DTR_linear = np.append(DTR, K * np.ones((1, DTR.shape[1])), axis=0)
    DTE_linear = np.append(DTE, K * np.ones((1, DTE.shape[1])), axis=0)
    alpha = train_svm(DTR_linear, LTR, C)
    zTR = prml.vcol(2 * LTR - 1)
    W = DTR_linear @ (prml.vcol(alpha) * zTR)

    prediction_test = (W.T @ DTE_linear > 0).reshape(
        DTE_linear.shape[1]).astype(int)
    error = get_error(DTE_linear, LTE, prediction_test)
    return error


def run_svm_kernel(DTR, DTE, LTE, LTR, C, K):
    c = 0
    d = 2
    kernel = polynomial_kernel_factory(c=c, d=d, K=K)
    alpha = train_svm(DTR, LTR, C, kernel=kernel)
    zTR = prml.vcol(2 * LTR - 1)
    eval_kernel = polynomial_kernel_factory(c, d, K, eval=True)

    score = (prml.vcol(alpha).T * zTR.T) @ eval_kernel(DTR, DTE)
    prediction = (score > 0).astype(int)
    # print(f"Score: {np.sum(score, axis=0)}")
    error = get_error(DTE, LTE, prediction)
    return error


def linear_kernel(DTR):
    return DTR.T @ DTR


def polynomial_kernel_factory(c, d, K, eval=False):
    if eval:
        def polynomial(DTR, DTE):
            return np.power(DTR.T @ DTE + c, d) + np.sqrt(K)
    else:
        def polynomial(DTR):
            return np.power(DTR.T @ DTR + c, d) + np.sqrt(K)

    return polynomial


def train_svm(DTR, LTR, C=1.0, kernel=linear_kernel):
    zTR = prml.vcol(2 * LTR - 1)
    HTR = ((kernel(DTR)) * zTR) * zTR.T
    L = L_factory(HTR)
    N = DTR.shape[1]
    init = np.zeros(N)
    C_list = list(zip(np.zeros(N), np.ones(N) * C))
    alpha, f, d = scipy.optimize.fmin_l_bfgs_b(
        L, init, bounds=C_list, factr=1.0)
    return alpha


def get_error(DTR, LTR, prediction):
    return 1 - np.sum((prediction == LTR).astype(int)) / DTR.shape[1]


def L_factory(H):
    def L_and_its_gradient(alpha):
        Alpha = prml.vcol(alpha)
        L = ((1 / 2 * Alpha.T) @ H) @ Alpha - Alpha.T @ np.ones(alpha.shape[0])
        DL = H @ Alpha - 1
        return np.reshape(L, L.shape), np.reshape(DL, alpha.shape)

    return L_and_its_gradient


def load_iris_binary():
    iris = sklearn.datasets.load_iris()
    D, L = iris['data'].T, iris['target']
    D = D[:, L != 0]  # We remove setosa from D
    L = L[L != 0]  # We remove setosa from L
    L[L == 2] = 0  # We assign label 0 to virginica (was label 2)
    return D, L


if __name__ == '__main__':
    main()
