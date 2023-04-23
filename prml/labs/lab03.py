"""Lab 03: Principal Component Analysis and Linear Discriminant Analysis."""
from prml import prml
import matplotlib.pyplot as plt
import os


def main():
    """Run main function."""
    data_path = os.environ["DATA_PATH"]
    X, Y = prml.load(os.path.join(data_path, "lab03/iris.csv"))
    DP_pca = prml.compute_pca(X, m=2)
    DP_lda = prml.compute_lda(X, Y, m=2)
    scatter_2_classes(DP_pca, Y)
    scatter_2_classes(DP_lda, Y)


def scatter_2_classes(DP, targets):
    """Scatter plot of 2 classes of data points."""
    plt.figure()
    unique_targets = set(targets)
    for target in unique_targets:
        plt.scatter(DP[0, targets == target], DP[1, targets == target])
    plt.show()


if __name__ == "__main__":
    main()
