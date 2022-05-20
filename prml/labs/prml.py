import math

import numpy as np
import scipy
import scipy.linalg


def vcol(vector: np.ndarray):
    """
    Converts vector into column vector
    :param vector: one dimensional vector np.ndarray (size,)
    :return: vector: two dimensional vector (size, 1)
    """
    return vector.reshape((vector.size, 1))


def vrow(vector: np.ndarray):
    """
    Converts vector into row vector
    :param vector: one dimensional vector np.ndarray (size,)
    :return: vector: two dimensional vector (1, size)
    """
    return vector.reshape((1, vector.size))


def load(file_name: str):
    """
    Return two np.ndarray objects with data and target values
    File must be in the format
    float, float, float, ..., str
    Having first values as integers/float for the features and last value as
    the target class
    :param file_name: name of a csv file
    :return: np.ndarray features x N , np.ndarray features,
    """
    array = []
    targets = []
    with open(file_name, 'r') as file:
        for raw_line in file:
            if raw_line:
                line = raw_line.split(',')
                raw_values, target = line[:-1], line[-1]
                values = [float(value) for value in raw_values]
                array.append(values)
                targets.append(target.strip())
    return np.array(array).T, np.array(targets)


def mean(matrix_d):
    """
    Compute mean of a matrix_d
    :param matrix_d: features x N data matrix
    :return: features x 1 column vector
    """
    return vcol(matrix_d.mean(1))


def covariance(matrix_d):
    """
    Compute covariance of a np.ndarray features x N
    :param matrix_d: features x N
    :return: covariance matrix : features x features
    """
    N = matrix_d.shape[1]
    mu = mean(matrix_d)
    data_centered = (matrix_d - mu)
    return data_centered @ data_centered.T / N


def covariance_between(matrix_d, matrix_l):
    """
    Return covariance between classes
    :param matrix_d: features x N
    :param matrix_l: classes vector
    :return: covariance matrix features x features
    """
    classes = set(matrix_l)
    features = matrix_d.shape[0]
    N = matrix_d.shape[1]
    s_b = np.zeros((features, features))
    mu = mean(matrix_d)
    for class_l in classes:
        d_class = matrix_d[:, matrix_l == class_l]
        nc = d_class.shape[1]
        mu_c = mean(d_class)
        classes_distance = mu_c - mu
        summation = np.multiply(nc, classes_distance) @ classes_distance.T
        s_b = s_b + summation
    return s_b / N


def covariance_within(matrix_d, matrix_l):
    classes = set(matrix_l)
    N = matrix_d.shape[1]
    features = matrix_d.shape[0]
    s_w = np.zeros((features, features))
    for class_l in classes:
        d_class = matrix_d[:, matrix_l == class_l]
        mu_c = mean(d_class)
        central_data = d_class - mu_c
        class_summation = central_data @ central_data.T
        s_w = s_w + class_summation
    return s_w / N


def compute_w(s_b, s_w, m):
    s, U = scipy.linalg.eigh(s_b, s_w)
    W = U[:, ::-1][:, 0:m]
    return W


def eigh(matrix_d):
    """
    Return eigen values and vectors using np. linalg.eigh but in desc order
    :param matrix_d: symmetric matrix
    :return: np.ndarray with eigen values, np.ndarray with eigen vectors
    """
    eig_values, eig_vectors = np.linalg.eigh(matrix_d)
    return eig_values[::-1], eig_vectors[:, ::-1]


def compute_pca(matrix_d, m):
    """
    Computes the Principal component Analysis of a Matrix
    :param matrix_d: (np.ndarray features, N) matrix
    :param m: number of components
    :return: Data projected over the m principal components
    """
    d_covariance = covariance(matrix_d)
    eig_values, eig_vectors = eigh(d_covariance)
    P = eig_vectors[:, 0:m]  # Eigen vectors to project
    DP = P.T @ matrix_d  # Matrix D projected on P
    return DP


def compute_w_2(s_b, s_w, m):
    U, s, _ = np.linalg.svd(s_w)
    P1 = np.dot(U * vrow(1.0 / (s ** 0.5)), U.T)
    Sbt = P1 @ s_b @ P1.T
    _, P2 = eigh(Sbt)
    P2 = P2[:, 0:m]
    W = P1.T @ P2
    return W


def compute_lda(matrix_d, targets, m):
    S_b = covariance_between(matrix_d, targets)
    S_w = covariance_within(matrix_d, targets)
    W = compute_w_2(S_b, S_w, m)
    DP = W.T @ matrix_d
    return DP


def logpdf_GAU_ND(X, mu, C):
    """
    Computes the Multivariate Gaussian Density

    :param X: matrix features x samples
    :param mu: mean
    :param C: empirical covariance
    :return:
    """
    M = X.shape[0]
    first_term = - 0.5 * M * np.log(2 * math.pi)
    centered_x = X - mu
    second_term = - 0.5 * np.linalg.slogdet(C)[1]
    third_term = - 0.5 * np.sum(
        (centered_x.T @ np.linalg.inv(C)) * centered_x.T,
        axis=1)
    return first_term + second_term + third_term


def loglikelihood(X, m, C):
    return logpdf_GAU_ND(X, m, C).sum(axis=0)
