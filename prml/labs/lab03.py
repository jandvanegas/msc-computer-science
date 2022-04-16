import prml
import matplotlib.pyplot as plt


def main():
    D, targets = prml.load('iris.csv')
    covariance = prml.covariance(D)
    eig_values, eig_vectors = prml.eigh(covariance)
    m = 2
    P = eig_vectors[:, 0:m]  # Eigen vectors to project
    DP = P.T @ D  # Matrix D projected on P
    unique_targets = set(targets)
    for target in unique_targets:
        plt.scatter(DP[0, targets == target], DP[1, targets == target])
    plt.show()


if __name__ == '__main__':
    main()