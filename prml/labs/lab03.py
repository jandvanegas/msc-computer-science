import prml
import matplotlib.pyplot as plt


def main():
    D, targets = prml.load('iris.csv')
    DP_pca = prml.compute_pca(D, m=2)
    DP_lda = prml.compute_lda(D, targets, m=2)
    scatter_2_classes(DP_pca, targets)
    scatter_2_classes(DP_lda, targets)


def scatter_2_classes(DP, targets):
    plt.figure()
    unique_targets = set(targets)
    for target in unique_targets:
        plt.scatter(DP[0, targets == target], DP[1, targets == target])
    plt.show()


if __name__ == '__main__':
    main()
