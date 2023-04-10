"""Machine Leraning and Pattern Recognition Library."""
import math

import numpy as np
import scipy
import scipy.linalg


def vcol(vector: np.ndarray):
    """Convert vector into column vector.

    :param vector: one dimensional vector np.ndarray (size,)
    :return: vector: two dimensional vector (size, 1)
    """
    return vector.reshape((vector.size, 1))


def vrow(vector: np.ndarray):
    """Convert vector into row vector.

    :param vector: one dimensional vector np.ndarray (size,)
    :return: vector: two dimensional vector (1, size)
    """
    return vector.reshape((1, vector.size))


def load(file_name: str):
    """Return two np.ndarray objects with data and target values.

    File must be in the format
    float, float, float, ..., str
    Having first values as integers/float for the features and last value as
    the target class
    :param file_name: name of a csv file
    :return: np.ndarray features x N , np.ndarray features,
    """
    array = []
    targets = []
    with open(file_name, "r") as file:
        for raw_line in file:
            if raw_line:
                line = raw_line.split(",")
                raw_values, target = line[:-1], line[-1]
                values = [float(value) for value in raw_values]
                array.append(values)
                targets.append(target.strip())
    return np.array(array).T, np.array(targets)


def mean(matrix_d):
    """Compute mean of a matrix_d.

    :param matrix_d: features x N data matrix
    :return: features x 1 column vector
    """
    return vcol(matrix_d.mean(1))


def covariance(D):
    """Compute covariance of a np.ndarray features x N.

    :param matrix_d: features x N
    :return: covariance matrix : features x features
    """
    N = D.shape[1]
    mu = mean(D)
    D_centered = D - mu
    return D_centered @ D_centered.T / N


def covariance_between(D, L):
    """Return covariance between classes.

    :param D: features x N
    :param L: classes vector
    :return: covariance matrix features x features
    """
    classes = set(L)
    features = D.shape[0]
    N = D.shape[1]
    S_b = np.zeros((features, features))
    mu = mean(D)
    n_test = 0
    for class_k in classes:
        D_k = D[:, L == class_k]
        n_k = D_k.shape[1]
        mu_k = mean(D_k)
        classes_distance = mu_k - mu
        S_b = S_b + n_k * (classes_distance @ classes_distance.T)
        n_test = n_test + n_k
    assert n_test == N
    return S_b / N


def covariance_within(D, L):
    """Return covariance within classes.

    :param D: features x N
    :param L: classes vector
    :return: covariance matrix features x features
    """
    classes = set(L)
    N = D.shape[1]
    features = D.shape[0]
    s_w = np.zeros((features, features))
    for class_k in classes:
        d_k = D[:, L == class_k]
        mu_k = mean(d_k)
        D_k_centered = d_k - mu_k
        s_w = s_w + D_k_centered @ D_k_centered.T
    return s_w / N


def W_for_hermitian_matrixes(S_b, S_w, m):
    """Compute the W matrix for LDA using the Hermitian method.

    :param S_b: between class covariance matrix
    :param S_w: within class covariance matrix
    :param m: number of components
    :return: W matrix
    """
    s, U = scipy.linalg.eigh(S_b, S_w)
    W = U[:, ::-1][:, 0:m]
    return W


def eigh(matrix_d):
    """Return eigen values and vectors using np. linalg.eigh but in desc order
    :param matrix_d: symmetric matrix
    :return: np.ndarray with eigen values, np.ndarray with eigen vectors
    """
    eig_values, eig_vectors = np.linalg.eigh(matrix_d)
    return eig_values[::-1], eig_vectors[:, ::-1]


def compute_pca(D, m):
    """Compute the Principal component Analysis of a Matrix.

    :param D: (np.ndarray features, N) matrix
    :param m: number of components
    :return: Data projected over the m principal components
    """
    d_covariance = covariance(D)
    eig_values, eig_vectors = eigh(d_covariance)
    P = eig_vectors[:, 0:m]  # Eigen vectors to project
    DP = P.T @ D  # Matrix D projected on P
    return DP


def W_by_singular_value_decomposition(S_b, S_w, m):
    """Compute W for general case.

    :param S_b: between class covariance matrix
    :param S_w: within class covariance matrix
    :param m: number of components
    :return: W matrix
    """
    U, s, _ = np.linalg.svd(S_w)
    P1 = np.dot(U * vrow(1.0 / (s**0.5)), U.T)
    Sbt = P1 @ S_b @ P1.T
    _, P2 = eigh(Sbt)
    P2 = P2[:, 0:m]
    W = P1.T @ P2
    return W


def compute_lda(D, Y, m):
    """Compute the Linear Discriminant Analysis of a Matrix.

    :param D: (np.ndarray features, N) matrix_d
    :param Y: (np.ndarray N) vector with the targets
    :param m: number of components
    :return: Data projected over the m principal components
    """
    S_b = covariance_between(D, Y)
    S_w = covariance_within(D, Y)
    W = W_for_hermitian_matrixes(S_b, S_w, m)
    # W = W_by_singular_value_decomposition(S_b, S_w, m)
    DP = W.T @ D
    return DP


def logpdf_GAU_ND(X, mu, C):
    """Compute the Multivariate Gaussian Density.

    :param X: matrix features x samples
    :param mu: mean
    :param C: empirical covariance
    :return:
    """
    M = X.shape[0]
    first_term = -0.5 * M * np.log(2 * math.pi)
    centered_x = X - mu
    second_term = -0.5 * np.linalg.slogdet(C)[1]
    third_term = -0.5 * np.sum((centered_x.T @ np.linalg.inv(C)) * centered_x.T, axis=1)
    return first_term + second_term + third_term


def loglikelihood(X, m, C):
    return logpdf_GAU_ND(X, m, C).sum(axis=0)


def split_data(D: np.ndarray, L: np.ndarray, proportion, seed=0):
    nTrain = int(D.shape[1] * proportion)
    np.random.seed(seed)
    idx = np.random.permutation(D.shape[1])
    idxTrain = idx[0:nTrain]
    idxTest = idx[nTrain:]

    DTR = D[:, idxTrain]
    DTE = D[:, idxTest]
    LTR = L[idxTrain]
    LTE = L[idxTest]
    return (DTR, LTR), (DTE, LTE)


def optimal_bayes(ll_ratio, L, prior, Cfn, Cfp, threshold=None):
    """
    Computes optimal bayes decision
    :param ll_ratio: loglikelihood ratio
    :param L: real labels
    :param prior: pi value of prior probability
    :param Cfn: cost of false negatives
    :param Cfp: cost of false positives
    :param threshold: [optional] decision bayes threshold
    :return:
    """
    if threshold is None:
        threshold = -np.log((prior * Cfn) / ((1 - prior) * Cfp))
    prediction = ll_ratio > threshold
    confusion = compute_confusion_matrix(np.unique(L), L, prediction)
    TP = confusion[1, 1]
    TN = confusion[0, 0]
    FN = confusion[0, 1]
    FP = confusion[1, 0]
    FPR = FP / (FP + TN)
    FNR = FN / (FN + TP)
    return prediction, FPR, FNR, confusion


def compute_confusion_matrix(labels, L_real, L_predicted):
    confusion = np.zeros((len(labels), len(labels)))
    for column in labels:
        current = L_predicted[L_real == column]
        for row in labels:
            confusion[row, column] = np.count_nonzero(current == row)
    return confusion
