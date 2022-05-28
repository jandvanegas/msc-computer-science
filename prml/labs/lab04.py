import math
import numpy as np

import prml


def main():
    import matplotlib.pyplot as plt
    plt.figure()
    XPlot = np.linspace(-8, 12, 1000)
    m = np.ones((1, 1)) * 1.0
    C = np.ones((1, 1)) * 2.0
    result = prml.logpdf_GAU_ND(prml.vrow(XPlot), m, C)
    plt.plot(XPlot.ravel(), np.exp(result))
    plt.show()

    XND1 = np.load('./lab04/X1D.npy')
    m = prml.mean(XND1)
    C = prml.covariance(XND1)

    plt.figure()
    plt.hist(XND1.ravel(), bins=50, density=True)
    XPlot = np.linspace(-8, 12, 1000)
    plt.plot(XPlot.ravel(), np.exp(prml.logpdf_GAU_ND(prml.vrow(XPlot), m, C)))
    plt.show()


if __name__ == '__main__':
    main()
