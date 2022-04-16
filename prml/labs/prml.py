import numpy as np


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
    Return two np.ndarray objects with data and targe values
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


def eigh(matrix_d):
    """
    Return eigen values and vectors using np. linalg.eigh but in desc order
    :param matrix_d: symmetric matrix
    :return: np.ndarray with eigen values, np.ndarray with eigen vectors
    """
    eig_values, eig_vectors = np.linalg.eigh(matrix_d)
    return eig_values[::-1], eig_vectors[:, ::-1]
