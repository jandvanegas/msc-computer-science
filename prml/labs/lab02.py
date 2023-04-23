"""Lab 2."""
import os

import matplotlib.pyplot as plt
import numpy as np

from prml.prml import load, vcol, vrow


def load_iris():
    """Load the iris dataset and plot it."""
    data_dir = os.environ["DATA_PATH"]
    X, Y = load( os.path.join(data_dir, "lab02/iris.csv"),)
    X_bar = center_matrix(X, axis=1)
    plot(
        X_bar,
        Y,
        ["Sepal length", "Sepal width", "Petal length", "Petal width"],
    )
    plot(X, Y, ["Sepal length", "Sepal width", "Petal length", "Petal width"])


def simple_plot(
    values: np.ndarray,
    classes: list,
    feature_names: list | None = None,
):
    """Plot the data in a simple way."""
    unique_classes = set(classes)
    fig = plt.figure()
    for feature in range(values.shape[0]):
        feature_data = values[feature]
        fig1 = fig.add_subplot(1, values.shape[0], feature + 1)
        for specific_class in unique_classes:
            class_rows = classes == specific_class
            class_values = feature_data[class_rows]
            fig1.hist(class_values, label=specific_class, density=True)
            if feature_names:
                fig1.set_title(feature_names[feature])
            fig1.legend(loc="best")
    plt.show()


def plot(
    X: np.ndarray,
    Y: np.ndarray,
    feature_names: list | None = None,
):
    """Plot data distribution.

    In the diagonal, plot the histogram of each feature.
    In the other cells, plot the scatter plot of each pair of features.
    """
    classes = set(Y)
    fig = plt.figure()
    number_of_features = X.shape[0]
    for feature_i in range(number_of_features):
        feature_i_column = X[feature_i]
        for feature_j in range(number_of_features):
            feature_j_column = X[feature_j]
            fig1 = fig.add_subplot(
                number_of_features,
                number_of_features,
                feature_i * number_of_features + feature_j + 1,
            )
            for class_ in classes:
                class_rows = Y == class_
                if feature_i == feature_j:
                    class_values = feature_i_column[class_rows]
                    fig1.hist(class_values, label=class_, density=True)
                    if feature_names:
                        fig1.set_title(feature_names[feature_i])
                else:
                    feature_class_values = feature_i_column[class_rows]
                    second_class_values = feature_j_column[class_rows]
                    fig1.scatter(
                        feature_class_values, second_class_values, label=class_
                    )
                    if feature_names:
                        fig1.set_xlabel(feature_names[feature_i])
                        fig1.set_ylabel(feature_names[feature_j])
                fig1.legend(loc="best")
    plt.subplots_adjust(
        left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.6, hspace=0.6
    )
    plt.show()


def center_matrix(matrix: np.ndarray, axis: int):
    """Center samples around features mean.

    matrix: (f, n) matrix where
        f: number of features
        n: number of features
    """
    if axis == 0:
        return matrix - vrow(matrix.mean(axis=0))
    elif axis == 1:
        return matrix - vcol(matrix.mean(axis=1))
    raise ValueError("Axis must be 0 or 1")


if __name__ == "__main__":
    load_iris()
